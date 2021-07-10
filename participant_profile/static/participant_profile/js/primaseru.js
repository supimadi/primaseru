$(document).ready( () => {
    let textbox = [
        $('#id_address_kk'),
        $('#id_real_address'),
        $('#id_medic_record')
    ];
    for (let x = 0; x < textbox.length; x++) {
        textbox[x].autoresize(1, 5);
    }
    $("#photo-profile-form").change(() => {
        document.forms["photo-profile-form"].submit();
    });

    $("#v-pills-exam-tab").on("click", () => {
        $.ajax({
            url: `/exam/`,
            method: "GET",
            async: true,
            beforeSend: () => {
                $("#exam-content").html(`<div class="m-auto"><span class="spinner-border spinner-border-lg text-danger" role="status" aria-hidden="true"></span></div>`)
            },
            success: (data) => {
                $("#exam-content").empty().html(data);
            },
        });
    });

    // TODO Add more name to :
    // full name (done), city_born, education, salary, email, phone
    let tabs = $(".tab-profile");
    for (let i = 0; i < tabs.length; i++) {
        $(tabs[i]).click(() => {
            let text = tabs[i].innerHTML.split(" ")[1]; // Get name of the parent from side bar
            let full_name = `Nama Lengkap ${text} <span class="asteriskField">*</span>`;
            setTimeout(() => {
                $("#div_id_full_name label").html(full_name);
            }, 200);
        });
    }

});
