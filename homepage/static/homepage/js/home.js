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

setInterval(() => {
    let now = new Date().getTime();
    let distance = date - now;

    let days = Math.floor(distance / (1000 * 60 * 60 * 24));
    let hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    let minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
    let seconds = Math.floor((distance % (1000 * 60)) / 1000);

    document.getElementById('day').innerHTML = days;
    document.getElementById('hour').innerHTML = hours;
    document.getElementById('minute').innerHTML = minutes;
    document.getElementById('second').innerHTML = seconds;
}, 1000)
