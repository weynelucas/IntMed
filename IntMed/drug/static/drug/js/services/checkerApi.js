app.factory('checkerApi', function ($http) {
    var url = "/api/checker/";

    var request = function (method, pk, data) {
        var requestData = {
            method: method,
            headers: {
                'X-Requested-With': 'XMLHttpRequest'
            },
        }
        requestData.url = url + (pk ? pk + "/" : "");
        if(data) {
            requestData.data = data;
        }
        return $http(requestData);
    }

    return {
        get: function (pk) {
            return request("GET", pk);
        },
        put: function (pk, data) {
            return request("PUT", pk, data);
        },
        delete: function (pk) {
            return request("DELETE", pk);
        }
    }
})
