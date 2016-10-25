app.controller('SavedCheckerCtrl', function SavedCheckerCtrl ($scope, $rootScope, modalService, checkerApi) {

    $scope.init = function () {
        $scope.savedCheckers = [];
        $scope.editingChecker = {};
        $scope.currentPage = 1;
        $scope.maxSize = 3;
        $scope.pageSize = 3;
        $scope.loading = true;

        checkerApi.setLanguageCode(language);

        checkerApi.get().success(function (data, status) {
            $scope.savedCheckers = data;
            $scope.loading = false;
        }).error(function (data) {
            $scope.savedCheckers = [];
        })
    }

    $scope.deleteConfirmation = function (checker) {
        $scope.preventInsideClick();
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

    $scope.editChecker = function (checker) {
        $scope.editingChecker[checker.id] = true;
        $scope.preventInsideClick();
    }

    $scope.updateChecker = function (checker) {
        checkerApi.put(checker.id, {
            title: checker.title,
        }).success(function (data, status) {
            $scope.editingChecker[checker.id] = false;
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

    $scope.preventInsideClick = function (e) {
        if (!e) var e = window.event;
        e.cancelBubble = true;
        if (e.stopPropagation) e.stopPropagation();
    }

    $scope.init();
});
