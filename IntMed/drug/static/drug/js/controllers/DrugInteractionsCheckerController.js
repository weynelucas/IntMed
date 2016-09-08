app.controller('DrugInteractionsCheckerController', function  DrugInteractionsCheckerController ($scope, $http) {
    $scope.interactions = [];
    $scope.selectedDrug = null;
    $scope.loading = false;
    $scope.insertSelectedDrug = function (drug) {
        $scope.selectedDrug = drug;

    }
    $scope.selectedIds = function () {
        return $scope.selectedDrug ? $scope.selectedDrug.id : null;
    }
    $scope.findInteractions = function () {
        $http({
            method: 'GET',
            url: '/interactions/single/',
            params: {
                drug: $scope.selectedDrug.name,
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
        return scope.selectedDrug;
    }, function (value){
        if(value) {
            $scope.loading = true;
            $scope.findInteractions()
        }
    });
});
