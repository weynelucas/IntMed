app.directive('interaction', function () {
    return {
        templateUrl: '/static/drug/js/views/interactionItem.html',
        replace: true,
        restrict: 'E',
        scope: {
            model: '=',
        }
    }
});
