app.controller('MultipleDrugsCheckerCtrl', function MultipleDrugsCheckerCtrl($scope, $rootScope, $http, $cookies, modalService, interactionsApi) {

    var urlPrefix = "/" + language + "/";
    var saveCheckerUrl = urlPrefix + "checker/create/";
    var exportCheckerUrl = urlPrefix + "checker/export/";
    var processInteractionsUrl = urlPrefix + "interactions/multiple/";

    $scope.init = function () {
        $scope.checker = {
            selectedDrugs: [],
            interactions:  [],
        }
        $scope.loading = false;
        interactionsApi.loadToken();
    }

    $scope.clearSelectedDrugs = function () {
        $scope.checker.selectedDrugs = [];
    }

    $scope.removeSelectedDrug = function (index) {
        $scope.checker.selectedDrugs.splice(index, 1);
    }

    $scope.insertSelectedDrug = function (drug) {
        $scope.checker.selectedDrugs.push(angular.copy(drug))
        delete drug;
    }

    $scope.selectedIds = function () {
        return $scope.checker.selectedDrugs.map(function (drug) {
            return drug.id;
        });
    }

    $scope.selectedNames = function () {
        return $scope.checker.selectedDrugs.map(function (drug) {
            return drug.name;
        });
    }

    $scope.processInteractions = function () {
        interactionsApi.proccessMultipleInteractions($scope.selectedIds()).success(function (data, status) {
            $scope.checker.interactions = data;
        }).error(function (data) {
            $scope.checker.interactions = [];
        }).then(function (data) {
            $scope.loading = false;
        });
    }

    $scope.openSaveModal = function (elem) {
        modalService.openModal(saveCheckerUrl, elem.target, appendDrugsIdsOnHtmlResponse, function () {
            initFormBehaviour({
                formId: '#modal_form',
                url: saveCheckerUrl,
                success: function (response) {
                    $scope.$apply($scope.checkerSaved(response.data));

                    var target = $(elem.target).data('target');
                    $(target).modal('hide');

                    displayToast('success', response.message);
                }
            });
        });
    }

    $scope.exportChecker = function () {
        // Encode semicolons to send by url
        var jsonString = JSON.stringify($scope.checker).split(';').join('%3B');
        window.location.href = exportCheckerUrl + "?checker=" + jsonString;
    }

    $scope.checkerSaved = function (checker) {
        $rootScope.$broadcast('checkerSaved', checker)
    }

    $rootScope.$on('verifyInteraction', function (evt, drugs) {
        $scope.checker.selectedDrugs = angular.copy(drugs);
    });

    $scope.$watchCollection('checker.selectedDrugs', function (selectedDrugs) {
        if (selectedDrugs.length > 1) {
            $scope.loading = true;
            $scope.processInteractions();
        } else {
            $scope.checker.interactions = [];
            $scope.loading = false;
        }
    }, true);

    function appendDrugsIdsOnHtmlResponse (response) {
        var html_response = $.parseHTML(response, document, true)
        var drugsContainer = $(html_response).find('.form-group:last')[0];

        var drugsInputs = $scope.checker.selectedDrugs.map(function (drug) {
            return $('<input>').attr({
                type: 'hidden',
                name: 'selected_drugs',
                value: drug.id,
                id: 'id_drugs_' + drug.id,
            });
        });

        $(drugsContainer).html(drugsInputs);

        return html_response;
    }

    $scope.init();
});
