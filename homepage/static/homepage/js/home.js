const navbar = document.querySelector('.navbar');
const navToggler = document.querySelector('.navbar-toggler');

document.addEventListener('scroll', ()=> {
    const scrollTop = this.pageYOffset;
    if(scrollTop >= 50){
        navbar.classList.add('scrolled');
    } else {
        navbar.classList.remove('scrolled');
    }
});

navToggler.addEventListener('click', ()=> {
    navToggler.classList.toggle('active')
})
