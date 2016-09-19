app.factory('checkerApi', function ($http) {
    var url = "/api/checker/";
    var languageCode = "";

    var request = function (method, pk, data) {
        var requestData = {
            method: method,
        }
        requestData.url = (languageCode ? "/" + languageCode : "") + url + (pk ? pk + "/" : "");
        if(data) {
            requestData.data = data;
        }
        return $http(requestData);
    }

    return {
        setLanguageCode: function (language) {
            languageCode = language;
        },
        get: function (pk) {
            return request("GET", pk);
        },
        put: function (pk, data) {
            return request("PUT", pk, data);
        },
        delete: function (pk) {
            return request("DELETE", pk);
        },
    }
})
