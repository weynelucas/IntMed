app.directive('selectedMedicine', function () {
    return {
        templateUrl: '/static/medicine/js/views/selectedMedicine.html',
        replace: true,
        restrict: 'E',
        scope: {
            medicine: '=',
            remove: '=',
            index:'=',
        }
    }
});
