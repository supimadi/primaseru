$(document).ready(() => {
    $.ajax({
        url: `/p/major/`,
        method: "GET",
        async: true,
        beforeSend: () => {
            $("#jurusan-form").html(`<div class="m-auto"><span class="spinner-border spinner-border-lg text-danger" role="status" aria-hidden="true"></span></div>`)
        },
        success: (data) => {
            $("#jurusan-form").empty().html(data);
        },
    });

    let container = [
        [$("#ayah-form"), "#v-pills-id-ayah-tab", "father"],
        [$("#ibu-form"), "#v-pills-id-ibu-tab", "mother"],
        [$("#wali-form"), "#v-pills-id-wali-tab", "guardian"],
        [$("#jurusan-form"), "#v-pills-major-tab", "major"],
        [$("#berkas-form"), "#v-pills-files-tab", "files"],
        [$("#KK-form"), "#v-pills-files-tab", "kk"],
        [$("#lms-content"), "#v-pills-exam-tab", "lms"],
        [$("#graduation-content"), "#v-pills-graduation-tab", "graduation"],
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
