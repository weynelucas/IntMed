app.directive('interaction', function () {
    return {
        templateUrl: '/static/interactions/js/views/interaction.html',
        replace: false,
        restrict: 'E',
        scope: {
            model: '=',
            evidenceLabel: '@',
            actionLabel: '@',
            explanationLabel: '@',
        }
    }
});
