var callback = null;

function initFormBehaviour (formId, url, successCallback=null, target='#mainModal') {
    preventSubmitBehaviour(formId, url, target);
    removeInputErrosOnKeyup(formId);
    callback = successCallback;
}

function removeInputErrosOnKeyup(formId) {
    $(formId).find('input').on('keyup', function (event) {
        $(this).parent().removeClass('has-error').find('.help-block').remove();
    });
}

function preventSubmitBehaviour(formId, url, target) {
    console.log(target);
    $(formId).on('submit', function (event) {
        var form = this;
        event.preventDefault();


        $.ajax({
            url: url,
            type: "POST",
            async: true,
            data: $(form).serializeArray(),
            success: function (response) {
                $(target).modal('hide');
                displayToast('success', response.message);

                if(callback && typeof(callback === 'function')) {
                    callback(response.instance);
                }
            },
            error: function (request, status, error) {
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
