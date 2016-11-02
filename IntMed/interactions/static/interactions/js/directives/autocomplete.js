app.directive('autocomplete', ['$http', function ($http) {
    return function (scope, elem, attrs) {
        elem.autocomplete({
            minLength:3,
            source: function (request, response) {
                $http({
                    method: 'GET',
                    url: '/api/drug/',
                    params: {
                        q: request.term,
                        exclude_property: 'id',
                        exclude_value: scope.selectedIds(),
                    },
                    headers: {
                        'X-Requested-With': 'XMLHttpRequest'
                    },
                }).success(function (data, status) {
                    response( data.length === 1 && data[ 0 ].length === 0 ? [] : data );
                });
            },
            focus: function (event, ui) {
                return false;
            },
            select: function (event, ui) {
                scope.$apply(scope.insertSelectedDrug(ui.item));
                $(event.target).val('');
                return false;
            },
        }).autocomplete( "instance" )._renderItem = function(ul, item) {
            var uiItemTitle = $('<span>').addClass('ui-autocomplete-item-title').html(item.name + '<br/>');
            var uiItemSubtitle = $('<span>').addClass('ui-autocomplete-item-subtitle').html(item.action);
            var uiItemContainer = $('<div>').addClass('ui-autocomplete-item-container').append(uiItemTitle).append(uiItemSubtitle);

            return $("<li>").append(uiItemContainer).appendTo(ul);
        };
    }
}]);
