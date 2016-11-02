Array.prototype.contains = function(obj) {
    var i = this.length;
    while (i--) {
        if (this[i] === obj) {
            return true;
        }
    }
    return false;
}

$(window).on('resize', function () {
    changePaginationWhenMobile();
})

$(function () {
    $('#loading').fadeOut('slow');
    changePaginationWhenMobile();
});


function changePaginationWhenMobile () {
    $('.pagination').toggleClass('pagination-sm', $(window).width() < 400);
}
