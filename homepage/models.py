from urllib.parse import urlparse, parse_qs

from django.db import models

class FilesPool(models.Model):
    name = models.CharField('Nama File', max_length=100)
    files = models.FileField('File', upload_to="files_pool/", help_text="Silahkan Upload File yang Diinginkan.")

    def __str__(self):
        return self.name

class ProsTelkomBandung(models.Model):
    image = models.FileField("Gambar (Icon)", upload_to='homepage_icon/')
    desc = models.TextField(verbose_name="Deskripsi")

    def __str__(self):
        return self.desc

class TestimonialModel(models.Model):
    link_video = models.CharField('Link video', max_length=100)
    video_id = models.CharField('Video ID', max_length=50, null=True)
    full_name = models.CharField('Nama lengkap', max_length=100)
    photo = models.ImageField('Photo', upload_to="testimoni/", null=True)
    title = models.CharField('Title pemberi testimoni', max_length=100, help_text="Contoh: Alumni TKJ Angkatan 7.")
    testimonial = models.TextField('Testimoni')

    def _trim_yoututbe_id(self):
        video_url = self.link_video
         
        try:
            url_parsed = urlparse(video_url)
            url_parsed = parse_qs(url_parsed.query)
            return url_parsed["v"][0]
        except KeyError:
            url = video_url.split("/")
            return url[len(url) - 1]

    def __str__(self):
        return f'Testimoni: {self.full_name}'

    def save(self, *args, **kwargs):

        if self.link_video:
            self.video_id = self._trim_yoututbe_id()

        super(TestimonialModel, self).save(*args, **kwargs)



