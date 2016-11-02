app.directive('interactionRow', function () {
    return {
        templateUrl: '/static/interactions/js/views/interactionRow.html',
        replace: false,
        restrict: 'EA',
        scope: {
            model: '=',
        }
    }
});
