from django.db import models

# Create your models here.
class Kelompok(models.Model):
    nama = models.IntegerField()
    keterangan = models.CharField(max_length=200)

    def __str__(self):
        return self.keterangan

class Dosen(models.Model):
    NIP = models.CharField(max_length=200)
    nama = models.CharField(max_length=200)
    tanggallahir = models.DateTimeField(max_length=200)
    photo = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    fakultas = models.ForeignKey(Kelompok,on_delete=models.CASCADE,null=True)
    prodi = models.CharField(max_length=200)
    alamat = models.TextField(max_length=200)

    def __str__(self):
        return self.nama

class Staf(models.Model):
    NIP = models.CharField(max_length=200)
    nama = models.CharField(max_length=200)
    tanggallahir = models.CharField(max_length=200)
    photo = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    unit = models.CharField(max_length=200)
    alamat = models.TextField(max_length=200)

    def __str__(self):
        return self.NIP

class Mahasiswa(models.Model):
    NIM = models.CharField(max_length=200)
    nama = models.CharField(max_length=200)
    tanggallahir = models.CharField(max_length=200)
    photo = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    fakultas = models.CharField(max_length=200)
    prodi = models.CharField(max_length=200)

    def __str__(self):
        return self.NIM