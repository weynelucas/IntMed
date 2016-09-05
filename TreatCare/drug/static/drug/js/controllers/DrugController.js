app.controller('DrugController', function DrugController($scope, $http) {
    $scope.selectedDrugs = [];
    $scope.interactions = [];

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

    $scope.$watch(function (scope) {
        return scope.selectedDrugs.length;
    }, function (value) {
        if (value > 1) {
            // Process drug interactions
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
            });
        } else {
            $scope.interactions = [];
        }
    });
});
