app.controller('MultipleDrugsCheckerCtrl', function MultipleDrugsCheckerCtrl($scope, $http, $cookies) {

    var dataFromCookies = false;
    var urlPrefix = "/" + language + "/";
    var saveCheckerUrl = urlPrefix + "drug/save_result/";
    var exportCheckerUrl = urlPrefix + "drug/export/";
    var processInteractionsUrl = urlPrefix + "interactions/multiple/"

    $scope.init = function () {
        var selectedDrugsFromCookies = $cookies.getObject("selectedDrugs");
        var interactionsFromCookies = $cookies.getObject("interactions");

        if(selectedDrugsFromCookies && interactionsFromCookies) {
            dataFromCookies = true;
        }
        $scope.checker = {
            selectedDrugs: selectedDrugsFromCookies || [],
            interactions: interactionsFromCookies || [],
        }
        $scope.loading = false;
    }


    $scope.clearSelectedDrugs = function () {
        $scope.checker.selectedDrugs = [];
    }

    $scope.removeSelectedDrug = function (index) {
        $scope.checker.selectedDrugs.splice(index, 1);
    }

    $scope.insertSelectedDrug = function (drug) {
        $scope.checker.selectedDrugs.push(angular.copy(drug))
        delete drug;
    }

    $scope.selectedIds = function () {
        return $scope.checker.selectedDrugs.map(function (drug) {
            return drug.id;
        });
    }

    $scope.selectedNames = function () {
        return $scope.checker.selectedDrugs.map(function (drug) {
            return drug.name;
        });
    }

    $scope.processInteractions = function () {
        $http({
            method: 'GET',
            url: '/interactions/multiple/',
            params: {
                drug: $scope.selectedNames(),
            },
            headers: {
                'X-Requested-With': 'XMLHttpRequest'
            },
        }).success(function (data, status) {
            $scope.checker.interactions = data;
        }).error(function (data) {
            $scope.checker.interactions = [];
        }).then(function (data) {
            $scope.loading = false;
            $cookies.putObject("interactions", $scope.checker.interactions);
        });
    }

    $scope.openSaveModal = function (elem) {
        remoteFunction(saveCheckerUrl, elem.target, function (response) {
            var html_response = $.parseHTML(response, document, true)
            var drugsContainer = $(html_response).find('.form-group:last')[0];

            var drugsInputs = $scope.checker.selectedDrugs.map(function (drug) {
                return $('<input>').attr({
                    type: 'hidden',
                    name: 'drugs',
                    value: drug.id,
                    id: 'id_drugs_' + drug.id,
                });
            });

            $(drugsContainer).html(drugsInputs);

            return html_response;
        });
    }

    $scope.exportChecker = function () {
        window.location.href = exportCheckerUrl + "?pdfModel=" + JSON.stringify($scope.checker);
    }

    $scope.$watch(function (scope) {
        return scope.checker.selectedDrugs.length;
    }, function (value) {
        $cookies.putObject("selectedDrugs", $scope.checker.selectedDrugs);
        $cookies.putObject("interactions", $scope.checker.interactions);

        if(!dataFromCookies) {
            if (value > 1) {
                $scope.loading = true;
                $scope.processInteractions();
            } else {
                $scope.checker.interactions = [];
                $scope.loading = false;
            }
        } else {
            dataFromCookies = false;
        }
    });

    $scope.init();
});
