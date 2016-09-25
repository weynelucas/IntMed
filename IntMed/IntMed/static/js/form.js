var formOptions = {}

function initFormBehaviour (options) {
    formOptions = options;
    formOptions.url = formOptions.url || $(formOptions.formId).attr('action');
    preventSubmitBehaviour(formOptions.formId, formOptions.url);
    removeInputErrosOnKeypress(formOptions.formId);
    removeInputErrosOnCheckboxClick(formOptions.formId);
}

function removeInputErrosOnKeypress(formId) {
    $(formId).find('input').on('keypress', function (event) {
        $(this).parent().removeClass('has-error').find('.help-block').remove();
        $(this).parent().removeClass('has-error').find('.form-control-feedback').remove();
    });
}

function removeInputErrosOnCheckboxClick(formId) {
    $(formId).find("input[type='checkbox']").on('click', function (event) {
        $(this).parent().removeClass('has-error');
    });
}

function removeAllErrors(formId) {
    $(formId).find('input').each(function () {
        $(this).parent().removeClass('has-error').find('.help-block').remove();
        $(this).parent().removeClass('has-error').find('.form-control-feedback').remove();
    });
}

function preventSubmitBehaviour(formId, url) {
    $(formId).on('submit', function (event) {
        var form = this;
        event.preventDefault();

        removeAllErrors(formId);

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
        var type = $(input).attr('type');
        var formGroup = $(input).parent();
        var helpBlock = null;
        var errorIcon = null;

        if(!$(formGroup).find(".help-block").length) {
            if(type !== 'checkbox') {
                helpBlock = $('<span>').addClass("help-block").html(response[field]);
                errorIcon = $('<span>').addClass("glyphicon form-control-feedback glyphicon-exclamation-sign");
            }
        }
        if(first) {
            $(input).focus();
            first = false;
        }
        $(formGroup).addClass("has-error").append(helpBlock).append(errorIcon);
    }
}
