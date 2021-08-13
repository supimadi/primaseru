$("#generate-registration").on("click", function() {
  if ($("#id_registration_number").val()) {
    alert("Data tidak kosong");
  } else {
    $.ajax({
      url: `/d/reg-num/`,
      method: "GET",
      async: true,
      success: (data) => {
        $("#id_registration_number").val(data.reg_num);
        $("#generate-registration").prop('disabled', true);
        document.getElementById("participantForm").submit.click()
      },
    });
  }
  return true;
});
