function remoteFunction(url, elementId) {
    $.ajax({
        url: url,
        type: 'get',
        success: function (response) {
            $('#' + elementId).html(response)
        }
    })
}
