$(document).ready(() => {

    $(document).on('click', '#openNav', () => {
        $("#mySidenav").toggleClass("sidenavOpen")
        $("#main").toggleClass("mainMargin")
    });

});
