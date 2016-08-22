window.Parsley.addValidator('uniqueUsername', {
    requiementType: 'boolean',
    validateString: function (value, requirement) {
        var response = isUniqueField('username', value);
        return response == requirement;
    }
});

window.Parsley.addValidator('uniqueEmail', {
    requiementType: 'boolean',
    validateString: function (value, requirement) {
        var response = isUniqueField('email', value);
        return response == requirement;
    }
});

window.Parsley.addValidator('passwordCheck', {
    requiementType: 'boolean',
    validateString: function (value, requirement) {
        var response = check_password(value);
        return response == requirement;
    }
});

function validateForm() {
    $("form").parsley({
        excluded: 'input:hidden',
        errorClass: 'has-error',
        classHandler: function (el) {
            return el.$element.closest('.form-group');
        },
        errorsContainer: function(el) {
            return el.$element.closest('.form-group');
        },
        errorsWrapper: "<span class='help-block'></span>",
        errorTemplate: "<span></span>",
    });
}


function isUniqueField(field, value) {
    var response = true;
    $.ajax({
        url: "/accounts/lookup/" + field + "/" + value,
        dataType: 'json',
        type: 'get',
        async: false,
        success: function(data) {
            response = !(data.totalResults > 0)
        },
        error: function() {
            response = true;
        }
    });
    return response;
}

function check_password(password) {
    var response = false;
    $.ajax({
        url: "/accounts/check_password/" + password,
        dataType: 'json',
        type: 'get',
        async: false,
        success: function(data) {
            response = data.check
        },
        error: function() {
            response = false;
        }
    });
    return response;
}
