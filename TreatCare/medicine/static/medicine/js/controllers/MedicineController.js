app.controller('MedicineController', function MedicineController($scope) {
    $scope.selectedMedicines = [];

    $scope.clearSelectedMedicines = function () {
        $scope.selectedMedicines = [];
    }

    $scope.removeSelectedMedicine = function (index) {
        $scope.selectedMedicines.splice(index, 1);
    }

    $scope.insertSelectedMedicine = function (medicine) {
        $scope.selectedMedicines.push(angular.copy(medicine))
        delete medicine;
    }

    $scope.selectedIds = function () {
        return $scope.selectedMedicines.map(function (medicine) {
            return medicine.id;
        });
    }

    $scope.$watch(function (scope) {
        return scope.selectedMedicines.length;
    }, function (value) {
        if (value > 1) {
            // Process medicine interactions

        }
    });
});
