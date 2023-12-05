from msilib.schema import Property

import openai
from decouple import config


class OpenAIService:

    def __init__(self):
        self.api_key = config("OPENAI_API_KEY")
        self.gpt_model = config("GPT_MODEL")

    @property
    def get_api_key(self):
        return self.api_key

    @property
    def get_model(self):
        return self.gpt_model

    def get_chat_response(self, message):
        return openai.chat.completions.create(
            model=self.gpt_model,
            messages=[
                {"role": "user", "message": message}
            ]
        )
