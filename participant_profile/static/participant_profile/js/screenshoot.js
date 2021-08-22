let button = document.getElementById("unduh");

function screenshoot() {
  domtoimage.toJpeg(document.getElementById('main'), {quality: 1, bgcolor: '#fff'})
            .then(function (blob) {
              window.saveAs(blob, `${name}.jpg`);
            })
            .catch(function (error) {
              console.error('oops, something went wrong!', error);
            });
}

button.addEventListener('click', function() {
  screenshoot();
});
screenshoot();
