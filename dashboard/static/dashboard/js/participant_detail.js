$("#generate-registration").on("click", function() {
  if ($("#id_registration_number").val()) {
    alert("Data tidak kosong");
  } else {
    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
    $.ajax({
      url: `/d/reg-num/`,
      method: "POST",
      headers: {'X-CSRFToken': csrftoken},
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
