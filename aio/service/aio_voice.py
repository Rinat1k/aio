from pathlib import Path

import openai
from aio.service.aio_config import AIOConfig


class AIOVoice:
    def __init__(self, config: AIOConfig):
        self.config = config

    def get_response(self, message): #todo доработать [все захардкожено!!!]
        speech_file_path = "/home/rinat/Projects/django_project/aio/static/speech.mp3"
        response = openai.audio.speech.create(
            model=self.config.get_audio_speech_model,
            voice="alloy",
            input=message
        )
        response.stream_to_file(speech_file_path)
        return "/home/rinat/Projects/django_project/aio/static/speech.mp3"
