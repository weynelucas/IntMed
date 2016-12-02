app.filter('paginationSlice', function() {
    return function(input, currentPage, pageSize) {
        return input.slice((currentPage-1)*pageSize, currentPage*pageSize);
    }
});
