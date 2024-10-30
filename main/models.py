from django.db import models


class CV(models.Model):
    ad = models.CharField(max_length=100)
    soyad = models.CharField(max_length=100)
    biyografi = models.TextField()
    deneyim = models.TextField()
    eğitim_durumu = models.TextField()
    fotoğraf = models.ImageField(upload_to='photos/')  # Profil fotoğrafınızı yüklemek için

