app.controller('MultipleDrugsCheckerCtrl', function MultipleDrugsCheckerCtrl($scope, $http, $cookies) {

    $scope.init = function () {
        $scope.selectedDrugs = $cookies.getObject("selectedDrugs") || [];
        $scope.interactions = [];
        $scope.loading = false;
    }

    $scope.openSaveModal = function (url, elem) {
        remoteFunction(url, elem.target, function (response) {
            var html_response = $.parseHTML(response, document, true)
            var drugsContainer = $(html_response).find('.form-group:last')[0];

            var drugsInputs = $scope.selectedDrugs.map(function (drug) {
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

    $scope.clearSelectedDrugs = function () {
        $scope.selectedDrugs = [];
    }

    $scope.removeSelectedDrug = function (index) {
        $scope.selectedDrugs.splice(index, 1);
    }

    $scope.insertSelectedDrug = function (drug) {
        $scope.selectedDrugs.push(angular.copy(drug))
        delete drug;
    }

    $scope.selectedIds = function () {
        return $scope.selectedDrugs.map(function (drug) {
            return drug.id;
        });
    }

    $scope.selectedNames = function () {
        return $scope.selectedDrugs.map(function (drug) {
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
            $scope.interactions = data;
            $scope.loading = false;
        }).error(function (data) {
            $scope.interactions = [];
            $scope.loading = false;
        });
    }

    $scope.$watch(function (scope) {
        return scope.selectedDrugs.length;
    }, function (value) {
        $cookies.putObject("selectedDrugs", $scope.selectedDrugs);
        $scope.loading = true;

        if (value > 1) {
            $scope.processInteractions();
        } else {
            $scope.interactions = [];
            $scope.loading = false;
        }
    });

    $scope.init();
});
