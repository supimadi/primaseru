const navbar = document.querySelector('.navbar');
const navToggler = document.querySelector('.navbar-toggler');

// AOS Initzilation
AOS.init({
    startEvent: 'DOMContentLoaded',
    duration: 1000,
});

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

async function quota_chart() {
    const ctx = document.getElementById('myChart').getContext('2d');

    const cap = await fetch(`${URL}`)
      .then(response => response.json())
        .then(data => {
            return data;
        });

    const labels = [
        'Siswa yang sudah terdaftar',
        'Kuota tersisa jurusan TJAT',
        'Kuota tersisa jurusan TKJ',
        'Kuota tersisa jurusan MM',
    ];

    const data = {
        labels: labels,
        datasets: [{
          label: 'Presentasi Kuota Tersisa',
          data: cap.data,
          backgroundColor: ['#FF3131','#38B0EA', '#6F318B', '#6FCF97'],
        }],
    };
    
    const config = {
        type: 'doughnut',
        plugins: [ChartDataLabels],
        data: data,
        options: {
            aspectRatio: 1,
            responsive : true,
            plugins: {
                title: {
                    display: true,
                    text: 'Presentasi Kuota Tersisa',
                    font: {size: 18}
                },
                legend: {
                    position: 'bottom',
                    labels: {
                        font: {size: 24},
                    }
                },
                datalabels: {
                    color: '#FFFFFF',
                    font: {
                        size: 32
                    },
                    formatter: (value, ctx) => {
                        let percentage = (value * 100 / cap.totalCap ).toFixed(2)+"%";
                        return percentage;
                      },
                },
            }
        }
    };
    update_chart_onresize(config);
    const myChart = new Chart(ctx, config);

}

function update_chart_onresize(config){

    const smallDevice = window.matchMedia("(min-width: 767.98px)");
    smallDevice.addListener(handle_device_change);

    function handle_device_change(e) {
        if (e.matches){
            // config.options.plugins.legend.position='right';
            config.options.plugins.datalabels.font.size=24;
            config.options.plugins.legend.labels.font.size=20;
        }
        else {
            // config.options.plugins.legend.position='bottom';
            config.options.plugins.datalabels.font.size=14;
            config.options.plugins.legend.labels.font.size=16;
        }
    }
    handle_device_change(smallDevice);
}

function update_countdown() {
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

        // If the count down is finished, write some text
        if (distance <= 0) {
            clearInterval(update_countdown);
            document.getElementById("countdown").innerHTML = "Primaseru Telah Ditutup.";
            document.getElementById("schedule-headline").innerHTML = "Sampai Jumpa Dilain Waktu.";
        }

    }, 1000)

}
update_countdown();
quota_chart()
