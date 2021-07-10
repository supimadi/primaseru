$(document).ready(() => {
    $.ajax({
        url: `/p/participant/`,
        method: "GET",
        async: true,
        beforeSend: () => {
            $("#peserta-form").html(`<div class="m-auto"><span class="spinner-border spinner-border-lg text-danger" role="status" aria-hidden="true"></span></div>`)
        },
        success: (data) => {
            $("#peserta-form").empty().html(data);
        },
    });

    let container = [
        [$("#ayah-form"), "#v-pills-id-ayah-tab", "father"],
        [$("#ibu-form"), "#v-pills-id-ibu-tab", "mother"],
        [$("#wali-form"), "#v-pills-id-wali-tab", "guardian"],
        [$("#jurusan-form"), "#v-pills-major-tab", "major"],
        [$("#files-form"), "#v-pills-files-tab", "berkas"],
    ];
    for (let a = 0; a < container.length; a++){
        $("#v-pills-tab").one("click", container[a][1], () => {
            $.ajax({
                url: `/p/${container[a][2]}/`,
                method: "GET",
                async: true,
                beforeSend: () => {
                    $(container[a][0]).html(`<div class="m-auto"><span class="spinner-border spinner-border-lg text-danger" role="status" aria-hidden="true"></span></div>`)
                },
                success: (data) => {
                    $(container[a][0]).empty().html(data);
                },
            });
        });
    }
});
