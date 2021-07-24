function updateCircle() {
  $('.second.circle').circleProgress({
    value: step / 8,
    fill: {
      gradient: ["red", "orange"]
    }
  }).on('circle-animation-progress', function(event, progress) {
    $(this).find('p').html(Math.round(step * progress) + '/8');
  });
}
const TITLE_TEXT = [
  'Data Pribadi',
  'Alamat Pribadi',
  'Catatan Kesehatan Pribadi',
  'Identitas Ayah',
  'Identitas Ibu',
  'Identitas Wali',
  'Memilih Program Studi',
  'Unggah Photo',
];
const DESC_TEXT = [
  'Silahkan mengisi angket Data Pribadi dengan sebenar - benarnya.',
  'Silahkan mengisi angket Alamat Pribadi dengan sebenar - benarnya.',
  'Silahkan mengisi angket Catatan Kesehatan dengan sebenar - benarnya.',
  'Silahkan mengisi angket Profile Ayah dengan sebenar - benarnya.',
  'Silahkan mengisi angket Profile Ibu dengan sebenar - benarnya.',
  'Silahkan mengisi angket Profile Wali dengan sebenar - benarnya, jika memiliki wali.',
  'Silahkan memilih program studi sesuai dengan minat dan bakat.',
  'Silahkan mengunggah pas photo, pastikan berpakaian rapih dan jelas..',
];

function changeText() {
  $('#title-text').empty().html(TITLE_TEXT[step-1])
  $('#desc-text').text(DESC_TEXT[step-1])
}

updateCircle();
changeText();
