app.controller('SavedCheckerCtrl', function SavedCheckerCtrl ($scope, $http) {
    var urlPrefix = "/" + language + "/";
    var savedCheckersUrl = urlPrefix + "checker/list"

    $scope.init = function () {
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

    $scope.init();
});
