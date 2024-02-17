import openai
from decouple import config


class AIOConfig:

    def __init__(self, api_key=None, gpt_model=None, dall_e_model=None, audio_speech_model=None):
        self.api_key = api_key or config("OPENAI_API_KEY")
        self.gpt_model = gpt_model or config("GPT_MODEL")
        self.dall_e_model = dall_e_model or config("DALL_E_MODEL")
        self.audio_speech_model = audio_speech_model or config("AUDIO_SPEECH_MODEL")
        openai.api_key = self.api_key

    @property
    def get_api_key(self):
        return self.api_key

    @property
    def get_gpt_model(self):
        return self.gpt_model

    @property
    def get_dall_e_model(self):
        return self.dall_e_model

    @property
    def get_audio_speech_model(self):
        return self.audio_speech_model
