app.filter('slice', function() {
    return function(input, begin, end) {
        return input.slice(begin, end);
    }
});
