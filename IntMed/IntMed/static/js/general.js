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

function stopPropagation (event) {
    if (event && event.stopPropagation) {
        event.stopPropagation();
    } else if (window.event) {
        window.event.cancelBubble = true;
    } else if (window.$.Event.prototype) {
        window.$.Event.prototype.stopPropagation();
    }
}
