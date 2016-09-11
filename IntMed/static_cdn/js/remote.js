function remoteFunction(url, elem, interceptResponse=null) {
    $.ajax({
        url: url,
        type: 'get',
        success: function (response) {
            if(interceptResponse && typeof(interceptResponse) === 'function') {
                response = interceptResponse(response);
            }

            var target = $(elem).data('target');
            $(target).html(response);
        }
    });
}
