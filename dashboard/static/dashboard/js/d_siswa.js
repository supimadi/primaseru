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
});
