import openai
from decouple import config


class AIOConfig:

    def __init__(self, api_key=None, gpt_model=None):
        self.api_key = api_key or config("OPENAI_API_KEY")
        self.gpt_model = gpt_model or config("GPT_MODEL")
        openai.api_key = self.api_key

    @property
    def get_api_key(self):
        return self.api_key

    @property
    def get_gpt_model(self):
        return self.gpt_model
