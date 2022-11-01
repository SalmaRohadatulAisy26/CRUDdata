from django.contrib import admin
from django.urls import path 
from fakultas.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('untirta/', index, name='untirta'),
    path('tambah-dosen/', tambah_Dosen, name='tambah_Dosen'),
    path('tambah-staf/', tambah_Staf, name='tambah_Staf'),
    path('tambah-mahasiswa/', tambah_Mahasiswa, name='tambah_Mahasiswa'),
    path('Dosen/ubah/<int:id_Dosen>', ubah_Dosen, name='ubah_Dosen'),
    path('Mahasiswa/ubah/<int:id_Mahasiswa>', ubah_Mahasiswa, name='ubah_Mahasiswa'),
    path('Staf/ubah/<int:id_Staf>', ubah_Staf, name='ubah_Staf'),
    path('Dosen/hapus/<int:id_Dosen>', hapus_Dosen, name='hapus_Dosen'),
]
