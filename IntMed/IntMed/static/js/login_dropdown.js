function loginDropdownInit(language) {
    $('#login-dropdown').on({
        'show.bs.dropdown': function () {
            remoteFunction('/' + language + '/accounts/login', '#login-dp');
        },
        'hide.bs.dropdown': function () {
            $('#login-dp').html(
                $('<div>').addClass('loading-icon loading-icon-sm row talign-center')
                .append($('<i>').addClass('fa fa-spinner fa-spin fa-4x fast-spin'))
                .append($('<span>').addClass('sr-only').html('Loading...')))
            }
        });
}
