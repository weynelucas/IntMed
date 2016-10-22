app.directive('interaction', function () {
    return {
        templateUrl: '/static/interactions/js/views/interaction.html',
        replace: true,
        restrict: 'E',
        scope: {
            model: '=',
            evidenceLabel: '@',
            actionLabel: '@',
        }
    }
});
