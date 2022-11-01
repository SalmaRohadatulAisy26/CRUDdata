from django.shortcuts import render, redirect
from fakultas.models import Dosen, Staf, Mahasiswa
from fakultas.forms import FormDosen, FormStaf, FormMahasiswa
from django.contrib import messages


# Create your views here.
def hapus_Dosen(request, id_Dosen):
    dosen = Dosen.objects.filter(id=id_Dosen)
    dosen.delete()

    return redirect('/untirta/#datadosen')

def ubah_Dosen(request, id_Dosen):
    dosen = Dosen.objects.get(id=id_Dosen)
    template = 'ubah-dosen.html'
    if request.POST:
        form = FormDosen(request.POST, instance=dosen)
        if form.is_valid():
            form.save()
            messages.success(request, "Data berhasil diperbaharui!")
            return redirect('ubah_Dosen', id_Dosen=id_Dosen)
    else:
        form = FormDosen(instance=dosen)
        konteks = {
            'form':form,
            'dosen':dosen,
        }
    return render(request, template, konteks)

def ubah_Staf(request, id_Staf):
    staf = Staf.objects.get(id=id_Staf)
    template = 'ubah-staf.html'
    if request.POST:
        form = FormStaf(request.POST, instance=staf)
        if form.is_valid():
            form.save()
            messages.success(request, "Data berhasil diperbaharui!")
            return redirect('ubah_Staf', id_Mahasiswa=id_Staf)
    else:
        form = FormStaf(instance=staf)
        konteks = {
            'form':form,
            'staf':staf,
        }
    return render(request, template, konteks)

def ubah_Mahasiswa(request, id_Mahasiswa):
    mahasiswa = Mahasiswa.objects.get(id=id_Mahasiswa)
    template = 'ubah-mahasiswa.html'
    if request.POST:
        form = FormMahasiswa(request.POST, instance=mahasiswa)
        if form.is_valid():
            form.save()
            messages.success(request, "Data berhasil diperbaharui!")
            return redirect('ubah_Mahasiswa', id_Mahasiswa=id_Mahasiswa)
    else:
        form = FormMahasiswa(instance=mahasiswa)
        konteks = {
            'form':form,
            'mahasiswa':mahasiswa,
        }
    return render(request, template, konteks)

def index(request):
    books = Dosen.objects.all()
    stafs = Staf.objects.all()
    students = Mahasiswa.objects.all()

    konteks = {
        'books': books,
        'stafs': stafs,
        'students': students,
    }
    return render(request, 'seputar.html', konteks)


def tambah_Dosen(request):
    if request.POST:
        form = FormDosen(request.POST)
        if form.is_valid():
            form.save()
            form = FormDosen()
            pesan = "Data berhasil disimpan"

            contents = {
                'form': form,
                'pesan': pesan,
            }
            return render(request, 'tambah-dosen.html', contents)
    else:
        form = FormDosen()

        konteks = {
            'form': form,
        }

    return render(request, 'tambah-dosen.html', konteks)

def tambah_Staf(request):
    if request.POST:
        form = FormStaf(request.POST)
        if form.is_valid():
            form.save()
            form = FormStaf()
            pesan = "Data berhasil disimpan"

            konteks = {
                'form': form,
                'pesan': pesan,
            }
            return render(request, 'tambah-staf.html', konteks)
    else:
        form = FormStaf()

        konteks = {
            'form': form,
        }

    return render(request, 'tambah-staf.html', konteks)

def tambah_Mahasiswa(request):
    if request.POST:
        form = FormMahasiswa(request.POST)
        if form.is_valid():
            form.save()
            form = FormMahasiswa()
            pesan = "Data berhasil disimpan"

            konteks = {
                'form': form,
                'pesan': pesan,
            }
            return render(request, 'tambah-mahasiswa.html', konteks)
    else:
        form = FormMahasiswa()

        konteks = {
            'form': form,
        }

    return render(request, 'tambah-mahasiswa.html', konteks)