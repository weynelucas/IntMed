app.controller('SingleDrugCheckerCtrl', function SingleDrugCheckerCtrl($scope, $timeout,  interactionsApi, filterFilter, multipleSelectFilterFilter) {

    $scope.init = function () {
        $scope.currentPage = 1;
        $scope.maxSize = 5;
        $scope.pageSize = 50;
        $scope.options = {
            pageSize: [10, 25, 50, 100],
            action: ["No action", "Informative", "Adjust", "Avoid"],
            evidence: ["Case", "Study", "Theoretical", "Extensive"],
            type: [
                {code: "MILD_INTERACTION", text:"Leve"},
                {code: "MODERATE_INTERACTION", text:"Moderada"},
                {code: "NOTHING_EXPECTED", text:"Nada esperado"},
                {code: "SEVERE_INTERACTION", text:"Grave"},
                {code: "UNKNOWN_SEVERITY_INTERACTION", text:"Gravidade desconhecida"}
            ]
        };
        $scope.loading = false;
        $scope.checker = {
            selectedDrug: {},
            interactions: [],
        };
    }

    $scope.selectedIds = function () {
        return  $scope.checker.selectedDrug ? $scope.checker.selectedDrug.id : [];
    }

    $scope.insertSelectedDrug = function (drug) {
        $scope.checker.selectedDrug = angular.copy(drug);
        delete drug;
    }

    $scope.processInteractions = function () {
        $scope.loading = true;

        interactionsApi.processSingleInteractions($scope.selectedIds()).success(function (data, status) {
            $scope.checker.interactions = data;
            $scope.totalItems = data.length;
        }).error(function (data) {
            $scope.checker.interactions = [];
        }).then(function (data) {
            $scope.loading = false;
        });
    }

    $scope.sortBy = function (propertyName) {
        $scope.reverse = ($scope.propertyName === propertyName) ? !$scope.reverse : false;
        $scope.propertyName = propertyName;
    }

    $scope.getSortingClass = function (propertyName) {
        var sortingClass = "sorting";

        if ($scope.propertyName == propertyName) {
            if($scope.reverse) {
                sortingClass += "_desc";
            } else {
                sortingClass += "_asc";
            }
        }

        return sortingClass;
    }

    $scope.resetFilters = function () {
        $scope.search = {};
        clearAllSelect2Inputs();
    }

    $scope.$watch("checker.selectedDrug", function (newSelectedDrug, oldSelectedDrug) {
        if (!$.isEmptyObject($scope.checker.selectedDrug)) {
            $timeout(function () {
                $scope.resetFilters();
            });
            $scope.processInteractions();
        }
    }, true);

    $scope.$watch('search', function (newVal, oldVal) {
        if (newVal != undefined) {
            $scope.filtered = filterFilter($scope.checker.interactions, newVal.text);
            $scope.filtered = multipleSelectFilterFilter($scope.filtered, newVal.select);
            $scope.totalItems = $scope.filtered.length;
            $scope.currentPage = 1;
        }
    }, true);

    $scope.init();

});
