function update_countdown(today, day, hour, minute, second, container) {
    setInterval(() => {
        let now = new Date().getTime();
        let distance = today - now;

        let days = Math.floor(distance / (1000 * 60 * 60 * 24));
        let hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        let minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
        let seconds = Math.floor((distance % (1000 * 60)) / 1000);

        document.getElementById(day).innerHTML = days;
        document.getElementById(hour).innerHTML = hours;
        document.getElementById(minute).innerHTML = minutes;
        document.getElementById(second).innerHTML = seconds;

        // If the count down is finished, write some text
        if (distance <= 0) {
            clearInterval(update_countdown);
            document.getElementById(container).innerHTML = "<h5 class='mt-3 font-weight-bold'>Jalur Pendaftar Telah Ditutup.</h5>";
        }

    }, 1000)

}


