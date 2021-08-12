$("#generate-registration").one("click", function() {
  $.ajax({
    url: `/d/reg-num/`,
    method: "GET",
    async: true,
    success: (data) => {
      $("#id_registration_number").val(data.reg_num)
    },
  });
});
