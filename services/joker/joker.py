import logging
import os
import traceback
from contextlib import asynccontextmanager
from pathlib import Path

from fastapi import FastAPI
from omegaconf import OmegaConf

from utils.model import GeminiModel
from utils.data_classes import JokerRequest

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

    yield
    # shutdown
    del app.state.model
    del app.state.model_config
    

# init app
app = FastAPI(lifespan=lifespan)


@app.post("/generate_joke")
def generate_joke(joker_request: JokerRequest) -> str:
    try:
        prompt = joker_request.prompt
        joke = app.state.model(prompt=prompt, generation_config=app.state.model_config.generation_config)
    except Exception:
        logging.info(traceback.format_exc())
        joke = "Error occurred, try again"
        
    return joke