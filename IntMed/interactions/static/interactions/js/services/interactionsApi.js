app.factory('interactionsApi', function ($http) {
    var url = "http://api.sim.intmed.com.br";
    var token = "8507910ddca9965f915f26c1b71da93b58cd28cd";
    var uri = {
        multiple: '/api/interactions/multiple/',
        single: '/api/interactions/single/',
    };
    var interactionsProperties = {
        action: ["Nenhuma", "Informar", "Monitorar", "Ajustar", "Evitar"],
        evidence: ["Caso", "Estudo", "Teórica", "Extensa"],
        severity: ["Leve", "Moderada", "Nada esperado", "Séria", "Severidade desconhecida"]
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
        proccessMultipleInteractions: function (drugsIds) {
            return request(url, uri.multiple, drugsIds);
        },
        processSingleInteractions: function (drugId) {
            return request(url, uri.single, drugId);
        },
        getInteractionsProperties: function () {
            return interactionsProperties;
        }
    };
});
