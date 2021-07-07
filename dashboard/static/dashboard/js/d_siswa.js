$(document).ready(() => {

    $(".form-control").prop('disabled', true);

    $(".verified-form").on('click', '.save-verify', () => {
        $(".form-control").prop('disabled', false);
    });

    $("#activate-form").on('click', () => {
        if ($(".form-control").is(':disabled')) {
            $(".form-control").prop('disabled', false);
        } else {
            $(".form-control").prop('disabled', true);
        }
    });


    $("#updateNameUser").one('click', (e) => {
        let elem = $("#changeNameModal .modal-body");
        $.ajax({
            url: `/dashboard/users/${calon_pk}/`,
            method: "GET",
            async: true,
            beforeSend: () => {
                elem.html(`<div class="m-auto"><span class="spinner-border spinner-border-lg text-danger" role="status" aria-hidden="true"></span></div>`)
            },
            success: (data) => {
                elem.empty().html(data);
                $("#changeNameModal .modal-body form").prop('action',`/dashboard/users/${calon_pk}/` );
            },
        });
    });

});
