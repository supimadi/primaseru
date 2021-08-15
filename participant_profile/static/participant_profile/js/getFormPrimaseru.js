$(document).ready(() => {
    let container = [
        [$("#participant-form"), "#v-pills-participant-tab", "participant"],
        [$("#father-form"), "#v-pills-father-tab", "father"],
        [$("#mother-form"), "#v-pills-mother-tab", "mother"],
        [$("#guardian-form"), "#v-pills-guardian-tab", "guardian"],
        [$("#major-form"), "#v-pills-major-tab", "major"],
        [$("#kk-form"), "#v-pills-kk-tab", "kk"],
        [$("#lms-form"), "#v-pills-lms-tab", "lms"],
        [$("#graduation-form"), "#v-pills-graduation-tab", "graduation"],
        [$("#re-payment-form"), "#v-pills-re-payment-tab", "re-payment"],
    ];
    for (let a = 0; a < container.length; a++){
        $("#v-pills-tab").one("click", container[a][1], () => {
            $.ajax({
                url: `/p/${container[a][2]}/`,
                headers: { 'X-Button-Clicked': container[a][2] },
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
