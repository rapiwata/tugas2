# Templat Proyek Django untuk Railway

Repositori ini berisi sebuah templat untuk membuat proyek Django yang siap di-*deploy* ke [Railway](https://railway.app/).

## Daftar Isi

- [Daftar Isi](#daftar-isi)
- [Instruksi Penggunaan](#instruksi-penggunaan)
- [Lisensi](#lisensi)
- [Referensi](#referensi)

## Instruksi Penggunaan

### Pengembangan Lokal

Apabila kamu ingin menggunakan repositori ini sebagai repositori awalan yang nantinya akan kamu modifikasi, ikuti langkah-langkah berikut.

1. Buka laman GitHub repositori templat kode, lalu klik tombol "**Use this template**"
   untuk membuat salinan repositori ke dalam akun GitHub milikmu.

2. Buka laman GitHub repositori yang dibuat dari templat, lalu gunakan perintah
   `git clone` untuk menyalin repositorinya ke suatu lokasi di dalam sistem
   berkas (*filesystem*) komputermu.

   ```shell
   git clone <URL ke repositori di GitHub> <path ke suatu lokasi di filesystem>
   ```

3. Masuk ke dalam repositori yang sudah di-*clone* dan jalankan perintah berikut
   untuk menyalakan *virtual environment*.

   ```shell
   python -m venv env
   ```

4. Nyalakan *virtual environment* dengan perintah berikut.

   ```shell
   # Windows
   .\env\Scripts\activate
   # Linux/Unix, e.g. Ubuntu, MacOS
   source env/bin/activate
   ```

5. Instal *dependencies* yang dibutuhkan untuk menjalankan aplikasi dengan perintah berikut.

   ```shell
   pip install -r requirements.txt
   ```

6. Jalankan aplikasi Django menggunakan server pengembangan yang berjalan secara lokal.

   ```shell
   python manage.py runserver
   ```

7. Bukalah `http://localhost:8000` pada browser favoritmu untuk melihat apakah aplikasi sudah berjalan dengan benar.

### Pengembangan di Railway

1. Buka situs web [Railway](https://railway.app/) dan klik tombol `Start a New Project`.

2. Klik pilihan `Deploy from GitHub repo`.

3. Klik tombol `Login With GitHub` dan masuklah ke dalam akun GitHub kamu.

4. Kamu akan kembali ke halaman pembuatan proyek baru. Klik pilihan `Deploy from GitHub repo` dan klik `Configure GitHub App`.

5. Pilih tempat kamu menyimpan repositori program ini dan klik `Install & Authorize`.

6. Kamu akan kembali ke halaman pembuatan proyek baru. Klik pilihan `Deploy from GitHub repo` dan pilih repositori program ini.

7. Klik `Add variables` dan buat variabel baru dengan nama `APP_NAME` dan isikan nama aplikasi kamu yang akan dibuat menjadi URL aplikasi.

8. Klik menu `Settings` dan ubahlah URL yang ada pada bagian `Domains` sesuai dengan `APP_NAME` yang telah dispesifikasikan sebelumnya.

9. Tekan Control + K atau Command + K dan pilih `New Service -> Database -> Add PostgreSQL` untuk menginisiasi basis data PostgreSQL sebagai basis data yang digunakan.

## Lisensi

Templat ini didistribusikan dengan lisensi [MIT](LICENSE).

## Referensi

- [django-template-heroku](https://github.com/laymonage/django-template-heroku)
- [Templat Proyek Django PBP](https://github.com/pbp-fasilkom-ui/django-pbp-template)
- [Pindah dari Heroku ke Railway](https://determinedguy.github.io/cecoret/heroku-to-railway/)

[link railway menuju tugas https://tugas-2-studytracker-mraffi.up.railway.app/ ]

Menjawab Soal nomer 8

1.Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.

Jawab : 

bagan/grafik berada di link berikut
|  |   |   |   |   
V  V   V   V   V
https://www.canva.com/design/DAFbfxG2HKM/2IIJ7W_nUIFAg0190I97Kw/view?utm_content=DAFbfxG2HKM&utm_campaign=share_your_design&utm_medium=link&utm_source=shareyourdesignpanel

2.Jelaskan kenapa menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?

Jawab :

-Menginstal virtualenv dan menggunakannya sebelum menginstal Django adalah praktik yang disarankan, meskipun tidak penting saat memulai dengan versi terbaru. Dianjurkan untuk membuat virtual environment terdedikasi untuk setiap proyek Django, dan venv, yang dibangun ke dalam Python, adalah salah satu cara untuk mengelola virtual environment. tools ini digunakan secara luas, dan yang terbaik adalah membuat virtual environment setiap kali kita mengerjakan proyek Python yang menggunakan dependensi eksternal yang dipasang dengan pip, apa pun sistem operasinya. Ini berlaku untuk Windows, Linux, dan macOS.

-Ya, secara teknis dimungkinkan untuk membuat aplikasi web berbasis Django tanpa menggunakan virtual environment. Namun, sangat disarankan untuk menggunakan virtual environment karena membantu mengisolasi dependensi dan konfigurasi proyek kita dari global sistem kita. Ini memastikan bahwa proyek kita berjalan secara konsisten di berbagai sistem dan menghindari konflik dengan proyek Python lain di sistem kita.
Tanpa menggunakan virtual environment, kita mungkin mengalami masalah dengan versi paket yang bertentangan, dan dependensi proyek kita mungkin bertentangan dengan proyek Python lain atau paket tingkat sistem. Selain itu, mungkin sulit untuk mereproduksi dan berbagi proyek kita dengan orang lain.
Singkatnya, meskipun memungkinkan untuk membuat aplikasi web berbasis Django tanpa menggunakan virtual environment, sangat disarankan untuk menggunakannya untuk memastikan pengembangan yang konsisten dan terisolasi.

3.Penjelasan bagaimana cara mengimplementasikan poin 1 sampai dengan 4 di atas.

jawab:

(step 1)tarik template menggunakan git pull pada link https://github.com/determinedguy/django-railway-template

(step 2)lakukan perintah pip install -r requirement.txt pada command promp
[isi nya adalah sebagai berikut]
|
V
asgiref==3.6.0
certifi==2022.12.7
charset-normalizer==3.0.1
dj-database-url==1.2.0
Django==4.1.7
gunicorn==20.1.0
idna==3.4
psycopg2-binary==2.9.5
pytz==2022.7.1
requests==2.28.2
six==1.16.0
sqlparse==0.4.3
typed-ast==1.5.4
tzdata==2022.7
urllib3==1.26.14
whitenoise==6.3.0
wrapt==1.14.1

(step 3)membuat projek aplikasi baru bernama study_tracker di folder 

(step 4)pada django_project tambahkan aplikasi study tracker ke setting, masukkan ke dalam variabel INSTALLED_APPS(dengan nama study_tracker)ini dapat dilakukan dengan menjalankan perintah django-admin startproject django_tutorial .

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'main',
    'study_tracker'
]

(step 5) buat berkas model pada app study tracker bernama assignment dan tambahkan atribut atribut baru seperti
name untuk nama tugas dengan tipe CharField,
subject untuk mata kuliah tugas dengan tipe CharField,
date untuk tenggat waktu tugas dengan tipe DateTimeField,
progress untuk indikator progress tugas dengan tipe IntegerField,
description untuk deskripsi tugas dengan tipe TextField.

(step 6)jalankan perintah python manage.py makemigrations dan python manage.py migrate pada command promp

(step 7)pada views.py buat lah fungsi untuk mengambil data dari model yang nantinya akan di return ke html(seperti yang dibawah ini)

from django.shortcuts import render
from .models import Assignment

def assignment_list(request):
    assignments = Assignment.objects.all()
    context = {
        'list_of_study': assignment_list,
        'name': 'M.Raffi'
    }

    return render(request, "assignment.html", context)





(step 8)buat kerangka pada assignment.html(seperti berikut)

{% extends 'base.html' %}

{% block content %}
<h5>Nama: </h5>
<b>{{name}}</b>

<table>
    <tr>
        <th>Name</th>
        <th>Jenis</th>
        <th>subjek</th>
        <th>progress</th>
        <th>description</th>
    </tr>
    {% comment %} Tambahkan data di bawah baris ini {% endcomment %}
    {% for transaction in list_of_transactions %}
    <tr>
        <td>{{assignment.name}}</td>
        <td>{{assignment.type}}</td>
        <td>{{assignment.amount}}</td>
        <td>{{assignment.date}}</td>
        <td>{{assignment.description}}</td>
    </tr>
{% endfor %}
</table>

{% endblock content %}

(step 9)pada urls tambahkan path
from django.urls import path
from study_tracker.views import assignment_list 

app_name = 'study_tracker'

urlpatterns = [
    path('', assignment_list, name='assignment_list'),
]

(step akhir) untuk memastikan server nya berjalan lakukan perintah python manage.py runserver pada command promp [http://localhost:8000/study_tracker/] //klik ctrl-c untuk mengakhiri server

Soal Latihan Baru(Latihan 4)

1.Apa kegunaan {% csrf_token %} pada elemen <form>? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen <form>?

Jawab:


{% csrf_token %} adalah tag template Django yang digunakan untuk menambahkan token CSRF (Cross-site request forgery) pada elemen <form>. CSRF token adalah tanda digital yang digunakan untuk mengidentifikasi apakah permintaan POST yang dibuat oleh pengguna benar-benar berasal dari situs web yang sah.

Jika tidak ada potongan kode {% csrf_token %} pada elemen <form>, maka Django akan mengembalikan pesan kesalahan "CSRF verification failed". Hal ini karena Django secara default memerlukan token CSRF untuk setiap permintaan POST yang diterima untuk menghindari serangan CSRF.

Oleh karena itu, penting untuk selalu menambahkan {% csrf_token %} pada setiap elemen <form> yang mengandung permintaan POST dalam aplikasi.

2.Apakah kita dapat membuat elemen <form> secara manual (tanpa menggunakan generator seperti {{ form.as_table }})? Jelaskan secara gambaran besar bagaimana cara membuat <form> secara manual.

Jawab:
Ya, kita dapat membuat elemen <form> secara manual tanpa menggunakan generator seperti {{ form.as_table }}. Dalam hal ini, kita perlu menulis kode HTML secara manual untuk menentukan elemen <form>, seperti <input>, <label>, dan lain-lain.

Berikut adalah gambaran besar cara membuat <form> secara manual:

Tentukan aksi dan metode formulir
Kita perlu menentukan aksi dan metode formulir. Aksi formulir menunjukkan URL ke mana data formulir dikirimkan dan metode formulir menunjukkan cara data dikirimkan (POST atau GET).

Contoh:

php
Copy code
<form action="/submit-form/" method="post">
Tambahkan input dan label
Kita perlu menambahkan input dan label ke dalam elemen <form>. Input dapat berupa jenis-jenis seperti teks, kata sandi, kotak centang, radio button, dan sebagainya. Setiap input membutuhkan label yang terkait.

Contoh:

ruby
Copy code
<label for="username">Username:</label>
<input type="text" id="username" name="username" required>
Tambahkan tombol submit
Kita perlu menambahkan tombol submit agar pengguna dapat mengirimkan data formulir ke server.

Contoh:

bash
Copy code
<button type="submit">Submit</button>
Tambahkan token CSRF
Kita perlu menambahkan token CSRF untuk melindungi formulir dari serangan CSRF.

Contoh:

Copy code
{% csrf_token %}
Setelah formulir selesai dibuat, kita dapat menempatkannya pada halaman web dengan menambahkan elemen <form> pada HTML. Dalam contoh di atas, formulir akan muncul pada halaman web di URL "/submit-form/" dengan metode POST.

3.Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.

Jawab:
Proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML dapat dijelaskan sebagai berikut:

Submisi formulir oleh pengguna
Pengguna mengisi formulir pada halaman web dan menekan tombol "submit".

Data formulir dikirim ke server
Data formulir yang diisi oleh pengguna dikirim ke server melalui protokol HTTP.

Validasi data
Server melakukan validasi data yang dikirim dari formulir untuk memastikan bahwa data tersebut valid dan aman.

Menyimpan data ke database
Jika data yang dikirimkan valid dan aman, server akan menyimpan data ke database.

Menampilkan data pada halaman web
Data yang disimpan di database akan ditampilkan pada halaman web melalui template HTML. Untuk mengambil data dari database, server menggunakan bahasa pemrograman seperti Python atau PHP untuk mengambil data dari database dan mengirimkannya ke template HTML.

Menerapkan template HTML
Server akan menerapkan template HTML yang telah dibuat sebelumnya untuk menampilkan data yang disimpan di database. Dalam proses ini, server akan menggabungkan data dari database dengan elemen HTML yang telah ditentukan di dalam template HTML.

Pengguna melihat hasilnya
Pengguna akan melihat halaman web yang menampilkan data yang telah disimpan pada database. Data dapat ditampilkan dalam bentuk tabel, grafik, atau elemen lainnya tergantung pada desain template HTML.

Dengan demikian, proses alur data dari submisi formulir, penyimpanan data di database, dan tampilan data pada halaman web membutuhkan beberapa tahapan yang melibatkan validasi, pengambilan, penyimpanan, dan penggabungan data menggunakan bahasa pemrograman dan template HTML.

4.Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.

Jawab:
1.Buka file views.py di dalam aplikasi study_tracker.
2.Tambahkan baris kode berikut: import redirect, UserCreationForm, dan messages.
3.Buatlah fungsi baru bernama register yang menerima parameter request dan berisi kode untuk menghasilkan formulir registrasi secara otomatis menggunakan UserCreationForm(request.POST). Kemudian, hasilkan akun pengguna ketika data di-submit dari form dengan menggunakan form.save().
4.Buatlah file baru bernama register.html pada folder study_tracker/templates untuk membuat halaman registrasi.
5.Buatlah formulir dengan menggunakan generator {{ form.as_table }}.
6.Buka file urls.py di dalam aplikasi study_tracker.
7.Impor fungsi register dan tambahkan path-nya pada urls.py.
8.Buka file views.py di dalam aplikasi study_tracker.
9.Tambahkan baris kode berikut: import authenticate dan login.
10.Buatlah fungsi baru bernama login_user yang menerima parameter request dan berisi kode untuk mengautentikasi pengguna yang ingin login.
11.Buatlah file baru bernama login.html pada folder study_tracker/templates untuk membuat halaman login.
12.Buka file urls.py di dalam aplikasi study_tracker.
13.Impor fungsi login_user dan tambahkan path-nya pada urls.py.
14.Modifikasi variabel name pada context dalam fungsi show_tracker yang berada pada views.py menjadi {{'name': request.user.username}} agar dapat menampilkan nama pengguna yang telah login.
15Buka file views.py di dalam aplikasi study_tracker.
16.Tambahkan baris kode berikut: import logout.
17.Buatlah fungsi baru bernama logout_user yang menerima parameter request dan berisi kode untuk melakukan mekanisme logout.
18.Buka file assignment_list.html pada folder study_tracker/templates.
19.Tambahkan kode untuk menambahkan tombol logout.
20.Buka file urls.py di dalam aplikasi study_tracker.
21.Impor fungsi logout_user dan tambahkan path-nya pada urls.py.
22.Buka file views.py di dalam aplikasi study_tracker.
23.Tambahkan baris kode berikut: import login_required.
24.Tambahkan kode {{ @login_required(login_url='/money_tracker/login/') }} di atas fungsi show_tracker agar halaman study tracker hanya dapat diakses oleh pengguna yang telah login (terautentikasi).