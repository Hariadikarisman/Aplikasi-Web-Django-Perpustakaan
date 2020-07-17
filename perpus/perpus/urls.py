# from django.http import HttpResponse

# def buku(request):
#     return HttpResponse("Ini Lagi Buat Buku")  # INI SEMUA BAGIAN CONTOH
# buku, penerbit, tambahBuku
# def profil(request):
#     return HttpResponse("Ini Lagi Buat Profil")
from django.contrib import admin
from django.urls import path
from perpustakaan.views import * # adalah memangil semua method yang ada di views perpustakaan
from django.contrib.auth.views import LoginView, LogoutView
from django.conf.urls.static import static

urlpatterns = [
    path('coba1/', coba1),
    path('admin/', admin.site.urls),
    path('buku/', buku, name = 'buku'),
    path('penerbit/', penerbit, name = 'penerbit'),
    path('buku/tambah/', tambahBuku, name = 'tambahBuku'),
    path('buku/ubah/<int:id_buku>',ubahBuku, name = 'ubahBuku'),
    path('buku/hapus/<int:id_buku>', hapusBuku, name = 'hapusBuku'),
    path('masuk/', LoginView.as_view(), name = 'masuk'),
    path('keluar/', LogoutView.as_view(next_page = 'masuk'), name = 'keluar'),
    path('signup/', signup, name = 'signup'),
    path('export/xls/', export_xls, name = 'export_xls'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
