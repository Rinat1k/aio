$("#sendUserMessage").click(function () {
    const message = {
        "user_message": $("#userMessage").val(),
    };

    $.ajax({
        url: '/chat/',
        type: 'POST',
        contentType: 'application/json',
        data: JSON.stringify(message),
        headers: {
            'X-CSRFToken': getCSRF('csrftoken')
        },
        success: function (response) {
            console.log('Success:', response);
            $("#chatResponse").text(response.chat_response);
        },
        error: function (error) {
            console.error('Error:', error);
        }
    });
});

$("#sendUserPrompt").click(function () {
    const userPrompt = {
        "user_prompt": $("#userPrompt").val(),
    };

    $.ajax({
        url: '/image/',
        type: 'POST',
        contentType: 'application/json',
        data: JSON.stringify(userPrompt),
        headers: {
            'X-CSRFToken': getCSRF('csrftoken')
        },
        success: function (response) {
            console.log('Success:', response);
            $("#imageResponse").attr("src", response.image_response);
        },
        error: function (error) {
            console.error('Error:', error);
        }
    });
});

$("#sendUserText").click(function () {
    const userText = {
        "user_text": $("#userText").val(),
    };
    console.log(userText)
    $.ajax({
        url: '/voice/',
        type: 'POST',
        contentType: 'application/json',
        data: JSON.stringify(userText),
        headers: {
            'X-CSRFToken': getCSRF('csrftoken')
        },
        success: function (response) {
            console.log('Success:', response);
            $("#audioVoice").attr("src", response.voice_response);
        },
        error: function (error) {
            console.error('Error:', error);
        }
    });
});

$("#createCV").click(function () {
    const userData = {
        "user_name": $("#userName").val(),
        "user_experience": $("#userExperience").val(),
        "user_education": $("#userEducation").val(),
        "user_languages": $("#userLanguages").val()
    };

    $.ajax({
        url: '/create_cv/',
        type: 'POST',
        contentType: 'application/json',
        data: JSON.stringify(userData),
        headers: {
            'X-CSRFToken': getCSRF('csrftoken')
        },
        success: function (response) {
            console.log('Success:', response);
            $("#CVOutput").text(response.generated_cv)
        },
        error: function (error) {
            console.error('Error:', error);
        }
    });
});


function getCSRF(name) {
    const value = "; " + document.cookie;
    const parts = value.split("; " + name + "=");
    if (parts.length === 2) return parts.pop().split(";").shift();
}