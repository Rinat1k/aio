import openai
from aio.service.aio_config import AIOConfig


class AIOImage:

    def __init__(self, config: AIOConfig):
        self.config = config
        self.number_of_images = 1

    def get_response(self, prompt):
        return openai.images.generate(
            model=self.config.get_dall_e_model,
            n=self.number_of_images,
            size="1024x1024",
            prompt=prompt
        ).data[0].url
