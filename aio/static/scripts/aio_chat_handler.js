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
            'X-CSRFToken': getCookie('csrftoken')
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

function getCookie(name) {
    const value = "; " + document.cookie;
    const parts = value.split("; " + name + "=");
    if (parts.length === 2) return parts.pop().split(";").shift();
}