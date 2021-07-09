$(document).ready(() => {

  $('#screenshoot').click(() => {
    html2canvas($('#kartu-peserta')[0], {
      allowTaint: true,
      useCORS: true,
    })
    .then(function (canvas) {
      // It will return a canvas element
      let image = canvas.toDataURL("image/png", 0.5);
      window.open(image);
    })
    .catch((e) => {
      // Handle errors
      console.log(e);
    });
  });

});
