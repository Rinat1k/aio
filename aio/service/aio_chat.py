import openai
from aio.service.aio_config import AIOConfig


class AIOChat:

    def __init__(self, config: AIOConfig):
        self.config = config

    def get_response(self, message):
        return openai.chat.completions.create(
            model=self.config.get_gpt_model,
            messages=[
                {"role": "user", "content": f"{message}"}
            ],
            temperature=0,
        ).choices[0].message.content
