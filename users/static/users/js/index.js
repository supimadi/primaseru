$(() => {
    $(document).scroll(() => {
        let nav = $(".navbar");
        nav.toggleClass('scrolled', $(this).scrollTop() > nav.height());
        nav.toggleClass('shadow-sm', $(this).scrollTop() > nav.height());
        nav.toggleClass('grad-dark', $(this).scrollTop() < nav.height());
    });
});
