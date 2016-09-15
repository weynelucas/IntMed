app.controller('SavedCheckerCtrl', function SavedCheckerCtrl ($scope, $rootScope, $http, modalService) {
    var urlPrefix = "/" + language + "/";
    var savedCheckersUrl = urlPrefix + "api/checker/"

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

    $scope.deleteConfirmation = function (checker) {
        preventInsideClick();
        $scope.toDeleteIndex = $scope.savedCheckers.indexOf(checker);
        $('#savedCheckerModal').modal();
    }

    $scope.insertChecker = function (checker) {
        $scope.savedCheckers.push(checker);
    }

    $scope.removeChecker = function (index) {
        $scope.savedCheckers.splice(index,1);
    }

    $scope.verifyInteraction = function (checker) {
        $rootScope.$broadcast('verifyInteraction', checker.selected_drugs);
    }

    $rootScope.$on('checkerSaved', function (evt, checker) {
        $scope.insertChecker(checker);
    });

    function preventInsideClick(e) {
        if (!e) var e = window.event;
        e.cancelBubble = true;
        if (e.stopPropagation) e.stopPropagation();
    }

    $scope.init();
});
