app.directive('selectedDrug', function () {
    return {
        templateUrl: '/static/interactions/js/views/selectedDrug.html',
        replace: true,
        restrict: 'E',
        scope: {
            model: '=',
            remove: '=',
            single: '=',
            message: '@',
            index:'=',
        }
    }
});
