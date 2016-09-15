app.controller('SavedCheckerCtrl', function SavedCheckerCtrl ($scope, $rootScope, modalService, checkerApi) {
    var urlPrefix = "/" + language + "/";
    var savedCheckersUrl = urlPrefix + "api/checker/"

    $scope.init = function () {
        $scope.savedCheckers = [];
        $scope.currentPage = 1;
        $scope.maxSize = 3;
        $scope.pageSize = 3;

        checkerApi.get().success(function (data, status) {
            $scope.savedCheckers = data;
        }).error(function (data) {
            $scope.savedCheckers = [];
        })
    }

    $scope.deleteConfirmation = function (checker) {
        preventInsideClick();
        $scope.toDelete = checker
        $('#savedCheckerModal').modal();
    }

    $scope.insertChecker = function (checker) {
        $scope.savedCheckers.push(checker);
    }

    $scope.removeChecker = function (checker) {
        var toDeleteIndex = $scope.savedCheckers.indexOf(checker);
        checkerApi.delete(checker.id).success(function (data, status) {
            $scope.savedCheckers.splice(toDeleteIndex, 1);
            $('#savedCheckerModal').modal('hide');
            displayToast('success', data.feedbackMessage);
        });
    }

    $scope.verifyInteraction = function (checker) {
        checker.uses = checker.uses + 1;

        checkerApi.put(checker.id, {
            uses: checker.uses
        }).success(function (data, status) {
            $rootScope.$broadcast('verifyInteraction', checker.selected_drugs);
        });
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
