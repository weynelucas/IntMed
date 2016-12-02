function clearAllSelect2Inputs () {
    $('select.select2').select2('val', 'All');
}

function setSelect2ContainerWidth() {
    $( ".select2-container" ).each( function() {
        var $this = $( this ),
        inputGroup = $this.parents( ".input-group" ),
        inputGroupContainerWidth,
        inputGroupAddonWidth = 0;

        if ( inputGroup.length ) {
            inputGroupContainerWidth = inputGroup.parents( "[class^='col-']" ).width() || inputGroup.parents( ".form-group" ).width();

            $this.parents( ".input-group" ).find( ".input-group-addon, .input-group-btn" ).each( function() {
                inputGroupAddonWidth += $( this ).outerWidth();
            });

            $this.css({ width: inputGroupContainerWidth - inputGroupAddonWidth });
        }
    });
}

window.onresize = function( event ) {
    setSelect2ContainerWidth();
}

$(function () {
    $('.select2').select2();
    setSelect2ContainerWidth();
});
