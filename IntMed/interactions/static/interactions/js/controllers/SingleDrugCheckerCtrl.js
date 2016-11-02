Array.prototype.contains = function(obj) {
    var i = this.length;
    while (i--) {
        if (this[i] === obj) {
            return true;
        }
    }
    return false;
}
app.filter('customFilter', function () {
    return function (items, filterData) {
        if(filterData == undefined)
            return items;
        var keys = Object.keys(filterData);
        var filtered = [];
        var populate = true;
        for (var i = 0; i < items.length; i++) {
            var item = items[i];
            populate = true;
            for(var j = 0; j < keys.length ; j++){
                if(filterData[keys[j]] != undefined){
                    if(filterData[keys[j]].length == 0 || filterData[keys[j]].contains(item[keys[j]])){
                        populate = true;
                    }else{
                        populate = false;
                        break;
                    }
                }
            }
            if(populate){
                filtered.push(item);
            }
        }
        return filtered;
    };
});

app.controller('SingleDrugCheckerCtrl', function SingleDrugCheckerCtrl($scope, interactionsApi, filterFilter, customFilterFilter) {

    $scope.init = function () {
        $scope.currentPage = 1;
        $scope.maxSize = 5;
        $scope.pageSize = 50;
        $scope.options = {
            pageSize: [10, 25, 50, 100],
            action: ["No action", "Informative", "Adjust", "Avoid"],
            evidence: ["Case", "Study", "Theoretical", "Extensive"],
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
    }

    $scope.$watch("checker.selectedDrug", function (newSelectedDrug, oldSelectedDrug) {
        if (!$.isEmptyObject($scope.checker.selectedDrug)) {
            $scope.processInteractions();
        }
    });

    $scope.$watch('search', function (newVal, oldVal) {
        if (newVal != undefined) {
            $scope.filtered = filterFilter($scope.checker.interactions, newVal.text);
            $scope.filtered = customFilterFilter($scope.filtered, newVal.select);
            $scope.totalItems = $scope.filtered.length;
            $scope.currentPage = 1;
        }
    }, true);

    $scope.init();

});
