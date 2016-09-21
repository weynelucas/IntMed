var formOptions = {}

function initFormBehaviour (options) {
    formOptions = options;
    formOptions.url = formOptions.url || $(formOptions.formId).attr('action');
    preventSubmitBehaviour(formOptions.formId, formOptions.url);
    removeInputErrosOnKeypress(formOptions.formId);
}

function removeInputErrosOnKeypress(formId) {
    $(formId).find('input').on('keypress', function (event) {
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
                formOptions.success(response);
            },
            error: function (request, status, error) {
                formOptions.error ? formOptions.error(request, status, error) : displayErrors(form, request.responseJSON);
            },
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
