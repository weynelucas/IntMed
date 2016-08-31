function initFormBehaviour (formId) {
    preventSubmitBehaviour(formId);
    removeInputErrosOnKeyup(formId);
}

function removeInputErrosOnKeyup(formId) {
    $(formId).find('input').on('keyup', function (event) {
        $(this).parent().removeClass('has-error').find('.help-block').remove();
    });
}

function preventSubmitBehaviour(formId) {
    $(formId).on('submit', function (event) {
        var form = this;
        event.preventDefault();

        $.ajax({
            url: "create/",
            method: "POST",
            async: true,
            data: encapsulateData(form),
            success: function (response) {
                console.log(response)
            },
            error: function (request, status, error) {
                displayErrors(form, request.responseJSON);
            }
        });
    });
}

function encapsulateData(form) {
    var inputs = $(form).find("input");
    data = {};
    $(inputs).each(function (index, elem) {
        data[elem.name] = elem.value;
    });
    return data;
}

function displayErrors(form, response) {
    var first = true;
    for (field in response) {
        var input = $(form).find("input[name='" + field + "']");
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
