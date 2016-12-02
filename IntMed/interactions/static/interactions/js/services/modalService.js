app.factory('modalService', function ($http) {
    var openModal = function (url, target, interceptResponseCallback, modalLoadedCallback) {
        $http({
            method: 'GET',
            url: url,
            headers: {
                'X-Requested-With': 'XMLHttpRequest'
            },
        }).success(function (response) {
            if(interceptResponseCallback && typeof(interceptResponseCallback) === 'function') {
                response = interceptResponseCallback(response);
            }

            if(typeof(target) === 'object') target = $(target).data('target');
            $(target).html(response);

            if(modalLoadedCallback && typeof(modalLoadedCallback) === 'function') {
                modalLoadedCallback();
            }
        });
    }

    return {
        openModal: openModal,
    }
});
