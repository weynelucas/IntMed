var app = angular.module('drugInteractions', ['ngCookies', 'ui.bootstrap']);

app.config(function($interpolateProvider) {
  $interpolateProvider.startSymbol('{[{');
  $interpolateProvider.endSymbol('}]}');
});
