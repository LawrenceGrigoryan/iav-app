import logging
import os
import traceback
from pprint import pformat
from contextlib import asynccontextmanager
from pathlib import Path

from fastapi import FastAPI, status
from omegaconf import OmegaConf

from utils.model import GeminiModel
from utils.data_classes import HealthCheck, JokerRequest

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(message)s", datefmt="%m/%d/%Y %I:%M:%S %p")


@asynccontextmanager
async def lifespan(app: FastAPI):
    # startup events
    GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")
    
    # load model config
    config_path = Path(Path(__file__).resolve().parents[0], "model_config.yaml")
    model_config = OmegaConf.load(config_path)
    
    # init model and config once for an app
    app.state.model = GeminiModel(GEMINI_API_KEY, model=model_config.model)
    app.state.model_config = model_config
    
    logging.info(f"model config:\n{pformat(dict(model_config))}")

    yield
    # shutdown
    del app.state.model
    del app.state.model_config
    

# init app
app = FastAPI(
    title="LLM Joke Generator",
    lifespan=lifespan
)
    
    
@app.get("/health",
         tags=["healthcheck"],
         summary="Perform a Health Check",
         response_description="Return HTTP Status Code 200 (OK)",
         status_code=status.HTTP_200_OK,
         response_model=HealthCheck,)
def healthcheck() -> HealthCheck:
    return HealthCheck(status="OK")


@app.post("/generate_joke")
def generate_joke(joker_request: JokerRequest) -> dict:
    logging.info(f"generating a joke, input:\n{pformat(joker_request.model_dump())}")
    try:
        prompt = joker_request.prompt
        generation_config = app.state.model_config.generation_config.copy()
        # incoming params from ui have a priority over the default config
        if joker_request.generation_config:
            for param, value in joker_request.generation_config.items():
                generation_config[param] = value

        logging.info(f"final generation params:\n{pformat(generation_config)}")

        joke = app.state.model(prompt=prompt, generation_config=generation_config)
    except Exception:
        logging.info(traceback.format_exc())
        joke = "Error occurred, try again"
        
    return {"response": joke}