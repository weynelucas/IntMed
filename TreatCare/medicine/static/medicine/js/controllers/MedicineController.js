app.controller('MedicineController', function MedicineController($scope) {
    $scope.selectedMedicines = [];

    $scope.removeSelectedMedicine = function (index) {
        $scope.selectedMedicines.splice(index, 1);
    }

    $scope.insertSelectedMedicine = function (medicine) {
        $scope.selectedMedicines.push(angular.copy(medicine))
        delete medicine;
    }

    $scope.$watch(function (scope) {
        return scope.selectedMedicines.length;
    }, function (value) {
        if (value > 1) {
            // Process medicine interactions
        }
    });
});
