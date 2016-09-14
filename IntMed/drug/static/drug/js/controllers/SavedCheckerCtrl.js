app.controller('SavedCheckerCtrl', function SavedCheckerCtrl ($scope, $rootScope, $http) {
    var urlPrefix = "/" + language + "/";
    var savedCheckersUrl = urlPrefix + "checker/list"

    $scope.init = function () {
        $scope.savedCheckers = [];
        $scope.currentPage = 1;
        $scope.maxSize = 3;
        $scope.pageSize = 3;

        $http({
            method: 'GET',
            url: savedCheckersUrl,
            headers: {
                'X-Requested-With': 'XMLHttpRequest'
            },
        }).success(function (data, status) {
            $scope.savedCheckers = data;
        }).error(function (data) {
            $scope.savedCheckers = [];
        })
    }

    $scope.insertChecker = function (checker) {
        $scope.savedCheckers.push(checker);
    }

    $scope.verifyInteraction = function (checker) {
        $rootScope.$broadcast('verifyInteraction', checker.selected_drugs);
    }

    $rootScope.$on('checkerSaved', function (evt, checker) {
        $scope.insertChecker(checker);
    });

    $scope.init();
});
