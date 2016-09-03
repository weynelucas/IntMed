app.directive('autocomplete', ['$http', function ($http) {
    return function (scope, elem, attrs) {
        elem.autocomplete({
            minLength:3,
            source: function (request, response) {
                $http({
                    method: 'GET',
                    url: '/medicine/',
                    params: {
                        q: request.term,
                    },
                    headers: {
                        'X-Requested-With': 'XMLHttpRequest'
                    },
                }).success(function (data, status) {
                    response( data.length === 1 && data[ 0 ].length === 0 ? [] : data );
                });
            },
            select: function (event, ui) {
                scope.$apply(scope.insertSelectedMedicine(ui.item));
                return false;
            },
        }).autocomplete( "instance" )._renderItem = function(ul, item) {
            return $("<li>")
            .append("<div>" + item.name + "<br>" + "<span class='presentation'>" + item.active_principle + "<span>" + "</div>" )
            .appendTo(ul);
        };
    }
}]);
