/*
Init datetimepicker inputs behaviour
    Classes:
        .dp: datetimepicker input
        .dp-linked: container of linked datetimepickers
*/
function datetimePickerBehaviour () {
    $('.dp').datetimepicker({
        locale: 'pt-br',
        format: $(this).data('date-format') ? $(this).data('date-format')  : 'DD/MM/YYYY HH:mm',
        maxDate: new Date(),
    });
    // Liked pickers
    $('.dp-linked .dp:first').datetimepicker({
        locale: 'pt-br',
        format: $(this).data('date-format') ? $(this).data('date-format')  : 'DD/MM/YYYY HH:mm',
        maxDate: new Date(),
    });
    $('.dp-linked .dp:last').datetimepicker({
        locale: 'pt-br',
        format: $(this).data('date-format') ? $(this).data('date-format')  : 'DD/MM/YYYY HH:mm',
        maxDate: new Date(),
        useCurrent: false,
    });
    $(".dp-linked .dp:first").on("dp.change", function (e) {
        $(".dp-linked .dp:last").data("DateTimePicker").minDate(e.date);
    });
    $(".dp-linked:last").on("dp.change", function (e) {
        $(".dp-linked .dp:first").data("DateTimePicker").maxDate(e.date);
    });
}
