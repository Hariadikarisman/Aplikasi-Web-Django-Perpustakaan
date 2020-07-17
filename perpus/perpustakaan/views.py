from django.shortcuts import render, redirect, HttpResponse
from perpustakaan.models import Buku
from perpustakaan.forms import FormBuku
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm
from perpustakaan.resource import BukuResource


# judul = ['satusatu', 'duadua', 'tigatiga'] #biasa disini dan dipakai oleh method lain
def coba1(request):
    judul = ['satusatu', 'duadua', 'tigatiga'] # atau disini hanya di method ini saja bisa digunakan
    kontek = {
        'title':judul
    }
    return render(request, 'index.html', kontek)

def export_xls(request):
    buku = BukuResource()
    dataset = buku.export()
    response = HttpResponse(dataset.xls, content_type = 'application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="Laporan buku.xls"'
    return response

@login_required(login_url = settings.LOGIN_URL)
def signup(request):
    if request.POST:
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "User Berhasil Dibuat")
            return redirect('signup')
        else:
            messages.error(request, "Terjadi Kesalahan!")
            return redirect('signup')
    else:
        form = UserCreationForm
        context = {
            'form': form,
        }
    return render(request, 'signup.html', context)

@login_required(login_url = settings.LOGIN_URL)
def buku(request):
    # kalau mau ambil data dari tabel berbeda tidak perlu menggunakan inner join, cukup tambahkan __nama
    # jika hanya ingin menampilkan 3 buah data saja cukup tuliskan di akhir all()[:jumlah data yang diinginkan] atau disebut dengan LIMIT
    book = Buku.objects.all() #[:2] # kalau mau ambil sebuah isi dalam bukku gunakan all()
    context = {
        'book':book,
    }
    return render(request, "buku.html", context)

@login_required(login_url = settings.LOGIN_URL)
def penerbit(request):
    penulis = Buku.objects.all()
    context = {
        'penulis':penulis,
    }
    return render(request, "penerbit.html", context)

@login_required(login_url = settings.LOGIN_URL)
def tambahBuku(request):
    if request.POST:
        form = FormBuku(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form = FormBuku()
            pesan = 'Data Berhasil Di Simpan'
            context = {
                'form': form,
                'pesan': pesan,
            }
            return render(request, 'tambahBuku.html', context)
    else:
        form = FormBuku()

        context = {
            'form': form,
        }
    return render(request, "tambahBuku.html", context)

@login_required(login_url = settings.LOGIN_URL)
def ubahBuku(request, id_buku):
    buku = Buku.objects.get(id = id_buku)
    template = 'ubahBuku.html'
    if request.POST:
        form = FormBuku(request.POST, request.FILES, instance = buku)
        if form.is_valid():
            form.save()
            messages.success(request, "Data Berhasil Diubah")
            return redirect('ubahBuku', id_buku = id_buku)
    else:
        form = FormBuku(instance = buku)
        context = {
            'form': form,
            'buku': buku,
        }
    return render(request, "ubahBuku.html", context)

@login_required(login_url = settings.LOGIN_URL)
def hapusBuku(request, id_buku):
    buku = Buku.objects.filter(id = id_buku)
    buku.delete()
    messages.success(request, "Data Buku Berhasil Dihapus")

    return redirect('buku')







