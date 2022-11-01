from django.contrib import admin
from fakultas.models import Kelompok, Dosen, Staf, Mahasiswa
# Register your models here.

class DosenAdmin(admin.ModelAdmin):
    list_display = ['NIP', 'nama', 'tanggallahir', 'photo', 'email', 'fakultas', 'prodi', 'alamat']
    search_fields = ['NIP', 'nama', 'tanggallahir', 'photo', 'email', 'fakultas', 'prodi', 'alamat']
    list_filter = ('fakultas',)
    list_per_page = 10

class StafAdmin(admin.ModelAdmin):
    list_display = ['NIP', 'nama', 'tanggallahir', 'photo', 'email', 'unit', 'alamat']
    search_fields = ['NIP', 'nama', 'tanggallahir', 'photo', 'email', 'unit', 'alamat']
    list_per_page = 10

class MahasiswaAdmin(admin.ModelAdmin):
    list_display = ['NIM', 'nama', 'tanggallahir', 'photo', 'email', 'fakultas', 'prodi']
    search_fields = ['NIM', 'nama', 'tanggallahir', 'photo', 'email', 'fakultas', 'prodi']
    list_per_page = 10
admin.site.register(Kelompok)
admin.site.register(Dosen, DosenAdmin)
admin.site.register(Staf, StafAdmin)
admin.site.register(Mahasiswa, MahasiswaAdmin)