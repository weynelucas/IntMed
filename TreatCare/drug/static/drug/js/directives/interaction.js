app.directive('interaction', function () {
    return {
        templateUrl: '/static/drug/js/views/interaction.html',
        replace: true,
        restrict: 'E',
        scope: {
            model: '=',
        }
    }
});
