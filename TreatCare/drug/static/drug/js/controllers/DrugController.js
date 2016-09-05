app.controller('DrugController', function DrugController($scope, $http) {
    $scope.selectedDrugs = [];
    $scope.interactions = [];
    $scope.loading = false;

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
            url: '/drug/perform_interactions/',
            params: {
                drug: $scope.selectedNames(),
            },
            headers: {
                'X-Requested-With': 'XMLHttpRequest'
            },
        }).success(function (data, status) {
            $scope.interactions = data;
            $scope.loading = false;
        });
    }

    $scope.$watch(function (scope) {
        return scope.selectedDrugs.length;
    }, function (value) {
        $scope.loading = true;
        if (value > 1) {
            // Process drug interactions
            $scope.processInteractions();
        } else {
            $scope.interactions = [];
            $scope.loading = false;
        }
    });
});
