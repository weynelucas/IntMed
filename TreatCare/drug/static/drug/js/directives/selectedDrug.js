app.directive('selectedDrug', function () {
    return {
        templateUrl: '/static/drug/js/views/selectedDrug.html',
        replace: true,
        restrict: 'E',
        scope: {
            model: '=',
            remove: '=',
            index:'=',
        }
    }
});
