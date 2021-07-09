$('#id_start_date').daterangepicker({
  singleDatePicker: true,
  showDropdowns: true,
  minYear: 2015,
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
$('#id_end_date').daterangepicker({
  singleDatePicker: true,
  showDropdowns: true,
  minYear: 2015,
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
