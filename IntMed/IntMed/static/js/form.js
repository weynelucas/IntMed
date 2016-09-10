function initFormBehaviour (formId, url) {
    preventSubmitBehaviour(formId, url);
    removeInputErrosOnKeyup(formId);
}

function removeInputErrosOnKeyup(formId) {
    $(formId).find('input').on('keyup', function (event) {
        $(this).parent().removeClass('has-error').find('.help-block').remove();
    });
}

function preventSubmitBehaviour(formId, url) {
    $(formId).on('submit', function (event) {
        var form = this;
        event.preventDefault();

        $.ajax({
            url: url,
            type: "POST",
            async: true,
            data: $(form).serializeArray(),
            success: function (response) {
                $('#mainModal').modal('hide');
                displayToast('success', response.message);
            },
            error: function (request, status, error) {
                console.log(request.responseJSON);
                displayErrors(form, request.responseJSON);
            }
        });
    });
}

function displayErrors(form, response) {
    var first = true;
    for (field in response) {
        var input = $(form).find("[name='" + field + "']");
        var formGroup = $(input).parent();
        var helpBlock = null;

        if(!$(formGroup).find(".help-block").length) {
            helpBlock = $('<span>').addClass("help-block").html(response[field]);
        }
        if(first) {
            $(input).focus();
            first = false;
        }
        $(formGroup).addClass("has-error").append(helpBlock);
    }
}
