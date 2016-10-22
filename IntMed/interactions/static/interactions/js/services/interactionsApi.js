app.factory('interactionsApi', function ($http) {
    var url = "http://api.startupfactor.com.br";
    var token = "f2360d4b17b259c0b15d0b1f57025a9580feb127";
    var uri = {
        multiple: '/api/interactions/multiple/',
        single: '/api/interactions/single/',
    };

    var request = function (url, uri, arg) {
        var requestData = {};
        requestData.method = 'GET';
        requestData.url = url + uri;
        requestData.headers = {
            'Authorization': 'Token ' + token,
        }
        requestData.params = {
            drug: arg,
        }

        return $http(requestData);
    };

    return {
        proccessMultipleInteractions: function (drugId) {
            return request(url, uri.multiple, drugId);
        },
        processSingleInteractions: function (drugsIds) {
            return request(url, uri.multiple, drugsIds);
        }
    };
});
