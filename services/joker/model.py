from abc import ABC, abstractmethod
import google.generativeai as genai
from google.generativeai.types.generation_types import BlockedPromptException


class BaseModel(ABC):
    @abstractmethod
    def __call__(self):
        pass


class GeminiModel(BaseModel):
    def __init__(self, api_key: str, model: str):
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel(
            model,
            safety_settings={
                "HATE": "BLOCK_NONE",
                "HARASSMENT": "BLOCK_NONE",
                "SEXUAL": "BLOCK_NONE",
                "DANGEROUS": "BLOCK_NONE",
            },
        )

    def __call__(self, prompt: str, generation_config: dict = {}, **kwargs) -> str:
        response = self.model.generate_content(prompt, generation_config=generation_config, **kwargs)
        # raise an exception manually because google just returns the response without exceptions
        if hasattr(response, "_error") and type(response._error) is BlockedPromptException:
            raise response._error
        json_response_str = response.candidates[0].content.parts[0].text

        return json_response_str
