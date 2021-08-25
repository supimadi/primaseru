$(function () {
  $('.dateinput').daterangepicker({
    singleDatePicker: true,
    showDropdowns: true,
    autoUpdateInput: false,
    minYear: 1930,
    maxYear: parseInt(moment().format('YYYY'),10) + 5,
    locale: {
      'format': "DD/MM/YYYY",
      'daysOfWeek': [
        "Min",
        "Sen",
        "Sel",
        "Rab",
        "Kam",
        "Jum",
        "Sab",
      ]
    }
  });

  $('.dateinput').on('apply.daterangepicker', function(ev, picker) {
    $(this).val(picker.startDate.format('DD/MM/YYYY'));
  });

  $('.dateinput').on('cancel.daterangepicker', function(ev, picker) {
    $(this).val('');
  });


});
