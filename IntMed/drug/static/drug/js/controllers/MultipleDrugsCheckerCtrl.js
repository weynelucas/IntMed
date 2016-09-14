app.controller('MultipleDrugsCheckerCtrl', function MultipleDrugsCheckerCtrl($scope, $rootScope, $http, $cookies) {

    var dataFromCookies = false;
    var urlPrefix = "/" + language + "/";
    var saveCheckerUrl = urlPrefix + "checker/create/";
    var exportCheckerUrl = urlPrefix + "checker/export/";
    var processInteractionsUrl = urlPrefix + "interactions/multiple/";

    $scope.init = function () {
        var selectedDrugsFromCookies = $cookies.getObject("selectedDrugs");
        var interactionsFromCookies = $cookies.getObject("interactions");

        if(selectedDrugsFromCookies && interactionsFromCookies) {
            dataFromCookies = true;
        }
        $scope.checker = {
            selectedDrugs: selectedDrugsFromCookies || [],
            interactions: interactionsFromCookies || [],
        }
        $scope.loading = false;
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
        $http({
            method: 'GET',
            url: processInteractionsUrl,
            params: {
                drug: $scope.selectedIds(),
            },
            headers: {
                'X-Requested-With': 'XMLHttpRequest'
            },
        }).success(function (data, status) {
            $scope.checker.interactions = data;
        }).error(function (data) {
            $scope.checker.interactions = [];
        }).then(function (data) {
            $scope.loading = false;
            $cookies.putObject("interactions", $scope.checker.interactions);
        });
    }

    $scope.openSaveModal = function (elem) {
        $http({
            method: 'GET',
            url: saveCheckerUrl,
            headers: {
                'X-Requested-With': 'XMLHttpRequest'
            },
        }).success(function (response){
            response = appendDrugsIdsOnHtmlResponse(response);

            var target = $(elem.target).data('target');
            $(target).html(response);

            initFormBehaviour('#modal_form', saveCheckerUrl, function (checker) {
                // Called outside AngularJS
                $scope.$apply($scope.checkerSaved(checker));
            }, target);
        });
    }

    $scope.exportChecker = function () {
        window.location.href = exportCheckerUrl + "?checker=" + JSON.stringify($scope.checker);
    }

    $scope.checkerSaved = function (checker) {
        $rootScope.$broadcast('checkerSaved', checker)
    }

    $rootScope.$on('verifyInteraction', function (evt, drugs) {
        $scope.checker.selectedDrugs = angular.copy(drugs);
    });

    $scope.$watch('checker.selectedDrugs', function (selectedDrugs) {
        $cookies.putObject("selectedDrugs", $scope.checker.selectedDrugs);
        $cookies.putObject("interactions", $scope.checker.interactions);

        if(!dataFromCookies) {
            if (selectedDrugs.length > 1) {
                $scope.loading = true;
                $scope.processInteractions();
            } else {
                $scope.checker.interactions = [];
                $scope.loading = false;
            }
        } else {
            dataFromCookies = false;
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
