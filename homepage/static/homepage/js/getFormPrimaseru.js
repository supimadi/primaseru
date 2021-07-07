$(document).ready(() => {
    $.ajax({
        url: `/profile/siswa/`,
        method: "GET",
        async: true,
        beforeSend: () => {
            $("#student-content").html(`<div class="m-auto"><span class="spinner-border spinner-border-lg text-danger" role="status" aria-hidden="true"></span></div>`)
        },
        success: (data) => {
            $("#student-content").empty().html(data);
        },
    });

    let container = [
        [$("#father-content"), "#v-pills-id-ayah-tab", "ayah"],
        [$("#mother-content"), "#v-pills-id-ibu-tab", "ibu"],
        [$("#guardian-content"), "#v-pills-id-wali-tab", "wali"],
        [$("#major-content"), "#v-pills-major-tab", "jurusan"],
        [$("#files-content"), "#v-pills-files-tab", "berkas"],
    ];
    for (let a = 0; a < container.length; a++){
        $("#v-pills-tab").one("click", container[a][1], () => {
            $.ajax({
                url: `/profile/${container[a][2]}/`,
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
