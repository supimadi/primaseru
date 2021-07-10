$('.dateinput').daterangepicker({
  singleDatePicker: true,
  showDropdowns: true,
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
