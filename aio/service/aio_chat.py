import os

import openai

from aio.dtos.cv_data_dto import CVDataDTO
from aio.service.aio_config import AIOConfig
from aio.config.json_handler import JsonHandler


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

    def get_generated_cv(self, cv_data_dto: CVDataDTO):
        chat_templates_json_handler = JsonHandler("aio/config/chat_templates.json")
        chat_templates_json_handler.load_from_file()
        template_request_cv = chat_templates_json_handler.get_value("template_request_cv")
        user_data = template_request_cv.format(cv_data_dto.full_name,
                                               cv_data_dto.experience,
                                               cv_data_dto.education,
                                               cv_data_dto.languages)
        return openai.chat.completions.create(
            model=self.config.get_gpt_model,
            messages=[
                {"role": "user", "content": f"{user_data}"}
            ],
            temperature=0,
        ).choices[0].message.content
