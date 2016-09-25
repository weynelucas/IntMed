app.directive('savedChecker', function () {
    return {
        templateUrl: '/static/drug/js/views/savedChecker.html',
        replace: true,
        restrict: 'E',
        scope: true,
        link: function (scope, elem, attrs) {
            scope.drugsLabel = attrs.drugsLabel;
            scope.defaultTitle = attrs.defaultTitle;
        }
    }
});
