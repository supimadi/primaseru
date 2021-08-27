from django.db import models

class FilesPool(models.Model):
    name = models.CharField('Nama File', max_length=100)
    files = models.FileField('File', upload_to="files_pool/", help_text="Silahkan Upload File yang Diinginkan.")

    def __str__(self):
        return self.name
