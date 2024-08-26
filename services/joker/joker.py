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
    
    # init model and config once
    app.state.model = GeminiModel(GEMINI_API_KEY, model=model_config.model)
    app.state.model_config = model_config
    
    logging.info(f"model config:\n{pformat(dict(model_config))}")

    yield
    # shutdown
    del app.state.model
    del app.state.model_config
    

# init app
app = FastAPI(lifespan=lifespan)
    
    
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
        joke = app.state.model(prompt=prompt, generation_config=app.state.model_config.generation_config)
    except Exception:
        logging.info(traceback.format_exc())
        joke = "Error occurred, try again"
        
    return {"response": joke}