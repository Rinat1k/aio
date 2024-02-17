import json
import logging

from json import JSONDecodeError

from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_POST

from aio.dtos.cv_data_dto import CVDataDTO
from aio.service.aio_config import AIOConfig
from aio.service.aio_chat import AIOChat
from aio.service.aio_image import AIOImage
from aio.service.aio_voice import AIOVoice

logger = logging.getLogger(__name__)


def index(request):
    return render(request, "index.html")


@require_POST
def chat(request):
    aio_chat = AIOChat(AIOConfig())
    try:
        json_data = json.loads(request.body)
        user_message = json_data.get("user_message", "")
    except JSONDecodeError as exception:
        return JsonResponse({"error": f"Invalid JSON data: {str(exception)}"}, status=400)
    except KeyError as exception:
        return JsonResponse({"error": f"Key error: {str(exception)}"}, status=400)

    aio_chat_response = aio_chat.get_response(user_message)
    return JsonResponse({"chat_response": aio_chat_response})


@require_POST
def image(request):
    aio_image = AIOImage(AIOConfig())
    try:
        json_data = json.loads(request.body)
        user_prompt = json_data.get("user_prompt", "")
    except JSONDecodeError as exception:
        return JsonResponse({"error": f"Invalid JSON data: {str(exception)}"}, status=400)
    except KeyError as exception:
        return JsonResponse({"error": f"Key error: {str(exception)}"}, status=400)

    aio_image_response = aio_image.get_response(user_prompt)
    return JsonResponse({"image_response": aio_image_response})


@require_POST
def voice(request):  # todo [Доработать]
    aio_voice = AIOVoice(AIOConfig())
    try:
        json_data = json.loads(request.body)
        user_text = json_data.get("user_text", "")
    except JSONDecodeError as exception:
        return JsonResponse({"error": f"Invalid JSON data: {str(exception)}"}, status=400)
    except KeyError as exception:
        return JsonResponse({"error": f"Key error: {str(exception)}"}, status=400)

    aio_voice_response = aio_voice.get_response(user_text)
    return JsonResponse({"voice_response": str(aio_voice_response)})


@require_POST
def create_cv(request):
    aio_chat = AIOChat(AIOConfig())
    user_cv_request_data = json.loads(request.body)
    cv_data_dto = CVDataDTO(user_cv_request_data["user_name"],
                            user_cv_request_data["user_experience"],
                            user_cv_request_data["user_education"],
                            user_cv_request_data["user_languages"])
    return JsonResponse({"generated_cv": aio_chat.get_generated_cv(cv_data_dto)})
