function remoteFunction(url, elem) {
    $.ajax({
        url: url,
        type: 'get',
        success: function (response) {
            var target = $(elem).data('target');
            $(target).html(response);
        }
    })
}
