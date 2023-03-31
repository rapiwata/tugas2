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

Soal Latihan 5(Latihan Baru)

1.Apa perbedaan dari inline, internal, dan external CSS? Apa saja kelebihan dan kekurangan dari masing-masing style?

jawab:CSS adalah singkatan dari Cascading Style Sheets, yang digunakan untuk mengontrol tampilan dan format pada halaman web. Ada tiga cara untuk menambahkan CSS ke halaman web: inline CSS, internal CSS, dan external CSS. Berikut adalah perbedaan dan kelebihan/kekurangan dari masing-masing jenis CSS:

Inline CSS
Inline CSS adalah CSS yang ditulis langsung pada elemen HTML yang ingin diubah tampilannya, dengan menggunakan atribut "style". Contohnya seperti ini:
html
Copy code
<h1 style="color: red;">Ini adalah judul dengan warna merah</h1>
Kelebihan:

Sangat mudah digunakan dan diterapkan, karena hanya membutuhkan penambahan atribut "style" pada elemen HTML.
Dapat mengatasi kebutuhan yang spesifik pada satu elemen HTML tertentu.
Kekurangan:

Tidak efisien dan tidak praktis untuk digunakan pada halaman web dengan jumlah elemen HTML yang banyak.
Mengulangi penulisan CSS pada setiap elemen HTML yang sama membutuhkan banyak waktu dan usaha.
Internal CSS
Internal CSS ditulis pada tag <style> dalam bagian <head> dari halaman web. Contohnya seperti ini:
html
Copy code
<head>
  <style>
    h1 {
      color: red;
    }
  </style>
</head>
<body>
  <h1>Ini adalah judul dengan warna merah</h1>
</body>
Kelebihan:

Mudah diterapkan pada seluruh elemen HTML pada halaman web yang sama.
Tidak membutuhkan waktu dan usaha yang banyak seperti inline CSS.
Kekurangan:

Tidak praktis digunakan pada halaman web yang berbeda-beda, karena harus menuliskan CSS pada setiap halaman web.
External CSS
External CSS adalah CSS yang ditulis pada file terpisah dengan ekstensi ".css", dan kemudian ditautkan ke halaman web menggunakan tag <link>. Contohnya seperti ini:
html
Copy code
<head>
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <h1>Ini adalah judul dengan warna merah</h1>
</body>
Kelebihan:

Sangat efisien dan praktis digunakan pada halaman web yang berbeda-beda, karena dapat digunakan pada setiap halaman web dengan hanya menautkan file CSS yang sama.
Memudahkan perubahan tampilan pada halaman web, karena hanya perlu mengubah file CSS yang terpisah.
Kekurangan:

Membutuhkan waktu dan usaha tambahan untuk membuat file CSS yang terpisah dan menautkannya ke halaman web.
Dalam kesimpulannya, keputusan untuk menggunakan jenis CSS yang mana bergantung pada kebutuhan dan kompleksitas halaman web. Inline CSS cocok digunakan untuk mengubah tampilan elemen HTML secara spesifik. Internal CSS dapat digunakan pada halaman web yang kompleks, tetapi tidak ingin menghadapi kerumitan dalam penulisan CSS pada setiap elemen HTML. External CSS sangat cocok digunakan pada halaman web yang kompleks dan ingin efisien dalam perubahan tampilan.


5.Jelaskan tag HTML5 yang kamu ketahui.

jawab:CSS selector adalah cara untuk memilih elemen HTML yang ingin diubah tampilannya menggunakan CSS. Ada beberapa tipe CSS selector yang dapat digunakan, yaitu:

Selector Elemen
Selector elemen memilih elemen HTML berdasarkan jenis elemennya, seperti <h1>, <p>, atau <div>. Contohnya:
css
Copy code
h1 {
  color: red;
}
Selector ID
Selector ID memilih elemen HTML berdasarkan atribut id yang diberikan. Setiap ID pada halaman web harus unik. Contohnya:
css
Copy code
#header {
  background-color: grey;
}
Selector Kelas
Selector kelas memilih elemen HTML berdasarkan atribut class yang diberikan. Banyak elemen HTML dapat memiliki kelas yang sama. Contohnya:
css
Copy code
.menu {
  font-size: 16px;
}
Selector Universal
Selector universal memilih semua elemen HTML pada halaman web. Contohnya:
css
Copy code
* {
  margin: 0;
  padding: 0;
}
Selector Keturunan
Selector keturunan memilih elemen HTML yang menjadi keturunan dari elemen lainnya. Contohnya:
css
Copy code
div p {
  font-weight: bold;
}
Selector Adjacent Sibling
Selector adjacent sibling memilih elemen HTML yang menjadi saudara seketurunan dari elemen lainnya dan langsung bersebelahan. Contohnya:
css
Copy code
h1 + p {
  font-size: 18px;
}
Selector General Sibling
Selector general sibling memilih elemen HTML yang menjadi saudara seketurunan dari elemen lainnya. Contohnya:
css
Copy code
h1 ~ p {
  font-size: 16px;
}
Selector Elemen Anak Langsung
Selector elemen anak langsung memilih elemen HTML yang menjadi anak langsung dari elemen lainnya. Contohnya:
css
Copy code
div > p {
  color: blue;
}
Selector Attribute
Selector attribute memilih elemen HTML berdasarkan atribut tertentu. Contohnya:
css
Copy code
input[type="text"] {
  border: 1px solid grey;
}
Itulah beberapa tipe CSS selector yang dapat digunakan untuk memilih elemen HTML pada halaman web. Pemilihan selector yang tepat akan memudahkan dalam mengubah tampilan elemen HTML.


jelaskan step by step:
-pertama saya mengimport Import JsonResponse dari django.httpdan csrf_exempt dari django.views.decorators.csrf ke dalam file views.py
-Buatlah fungsi baru dengan nama create_study_ajax yang menerima parameter request pada file study_tracker/views.py.
-kita salin kode tersebut pada def create_study_ajax(request):  
-Import function yang telah kamu buat sebelumnya pada study_tracker/urls.py.
-Tambahkan path baru untuk membuat objek transaksi baru dengan baris kode berikut ini pada urlpatterns. yaitu pada
path('create-ajax/', create_study_ajax, name='create_study_ajax'),
-Modifikasi file study_tracker/assginment.html
{% extends 'base.html' %}

{% block content %}
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>
-lalu tambahkan kode seperti berikut
<script>
$(document).ready(function(){
    $.get("/register/json/", function(data) {
        for (i=0; i<data.length; i++){
            $('#tracker').append(`
            <div id="${data[i].id}--task" class="col-md-6 col-lg-3 mb-3">
                <div class="card d-flex">
                    <div class="card-body d-flex flex-column">
                        <h5 class="card-title">${data[i].fields.name}</h5>
                        <p class="card-text date">${data[i].fields.date}</p>
                        <p class="card-text">${data[i].fields.lesson}</p>
                        <p class="card-text">${data[i].fields.subject}</p>
                        <p class="card-text">${data[i].fields.progress}</p>
                        <div class="mt-auto">
                            <a href="/register/delete/${data[i].pk}" class="btn btn-primary delete mb-2">Hapus</a>
                            <a href="/register/modify/${data[i].pk}" class="btn btn-secondary mb-2">Ubah</a>
                        </div>
                    </div>
                </div>
            </div>
            `)
        }
    });
</script>

-lalu kemudian kita tambahin kode kode seperti berikut pada assignment

<body>
    <h5>Nama: </h5>
    <p>{{name}}</p>
    <button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#createModal">
        Tambah studi
    </button>

    <!-- Modal -->
    <div class="modal" id="createModal" tabindex="-1" aria-labelledby="createModalLabel" aria-hidden="true">
        <div class="modal-dialog">
        <div class="modal-content">
            <div class="modal-header">
            <h1 class="modal-title fs-5" id="createModalLabel">Tambah Studi</h1>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Cancel"></button>
            </div>
            <div class="modal-body">
            {% csrf_token %}
            <label for="name" class="form-label">Judul studi:</label><br>
            <input type="text" id="name" class="form-control" name="name" placeholder="Kalkulus"><br>
            <label for="subject" class="form-label">jenis studi:</label>
            <select name="subject" id="subject" class="form-select" aria-label="Default select example">
                <option selected value="Tugas Harian">Tugas Harian</option>
                <option value="Tugas Akhir">Tugas Akhir</option>
                <option value="Ujian">Ujian</option>
            </select><br>
            <label for="lesson" class="form-label">Matakuliah:</label><br>
            <input type="text" id="lesson" class="form-control" name="lesson" placeholder="Kalkulus"><br>
            <label for="progress" class="form-label">progress:</label><br>
            <input type="number" id="progress" class="form-control" name="progress" placeholder=""><br>
            <label for="description" class="form-label">Deskripsi studi:</label><br>
            <input type="text" id="description" class="form-control" name="description" placeholder="Mengikuti sesuai jadwal"><br>
            </div>
            <div class="modal-footer">
            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Cancel</button>
            <button id="submit_btn" type="button" class="btn btn-primary create" id="add-task" data-bs-dismiss="modal">Add</button>
            </div>
        </div>
        </div>
    </div>
</body>

<div class="row m-2" id="study_tracker"></div>



<h5>Sesi terakhir login: {{ last_login }}</h5>
{% endblock content %}


-kemudian pada assigbment.html tambahin
<script>
  $(document).ready(function(){
      $.get("/study_tracker/json/", function(data) {
          for (i=0; i<data.length; i++){
              $('#study_tracker').append(`
              <div id="${data[i].id}--task" class="col-md-6 col-lg-3 mb-3">
                  <div class="card d-flex">
                      <div class="card-body d-flex flex-column">
                          <h5 class="card-title">${data[i].fields.name}</h5>
                          <p class="card-text date">${data[i].fields.date}</p>
                          <p class="card-text">${data[i].fields.lesson}</p>
                          <p class="card-text">${data[i].fields.subject}</p>
                          <p class="card-text">${data[i].fields.progress}</p>
                          <p class="card-text">${data[i].fields.description}</p>
                          <div class="mt-auto">
                              <a href="/study_tracker/delete/${result.id}" class="btn btn-primary delete mb-2">Hapus</a>
                              <a href="/study_tracker/modify/${result.id}" class="btn btn-secondary mb-2">Ubah</a>
                          </div>
                      </div>
                  </div>
              </div>
              `)
          }
      });

      $("#submit_btn").click(function(){
            $.post("/study_tracker/create-ajax/", {
                name: $("#name").val(),
                lesson: $("#lesson").val(),
                subject: $("#subject").val(),
                progress: $("#progress").val(),
                description: $("#description").val()

            },
            function(result, status){
                if (status == 'success'){
                    $("#study_tracker").append(`
                    <div id="${result.id}--task" class="col-md-6 col-lg-3 mb-3">
                        <div class="card d-flex">
                            <div class="card-body d-flex flex-column">
                                <h5 class="card-title">${result.name}</h5>
                                <p class="card-text date">${result.date}</p>
                                <p class="card-text">${result.lesson}</p>
                                <p class="card-text">${result.subject}</p>
                                <p class="card-text">${result.progress}</p>
                                <p class="card-text">${result.description}</p>
                                <div class="mt-auto">
                                    <a href="/study_tracker/delete/${result.id}" class="btn btn-primary delete mb-2">Hapus</a>
                                    <a href="/study_tracker/modify/${result.id}" class="btn btn-secondary mb-2">Ubah</a>
                                </div>
                            </div>
                        </div>
                    </div>
                    `);
                $('#name').val('')
                $('#date').val('')
                $('#lesson').val('')
                $('#subject').val('')
                $('#progress').val('')
                $('#description').val('')
                }
            })
        })
    })
</script>




Tugas 6

Jelaskan perbedaan antara asynchronous programming dengan synchronous programming.

jawab :Synchronous programming dan asynchronous programming adalah dua pendekatan yang berbeda dalam mengatur bagaimana sebuah program berjalan. Perbedaan antara keduanya adalah sebagai berikut:

Synchronous Programming
Synchronous programming (sinkron) adalah pendekatan dimana sebuah program berjalan secara linear atau sekuensial. Artinya, kode dieksekusi baris per baris secara berurutan. Pada synchronous programming, sebuah task harus menyelesaikan eksekusinya sebelum task berikutnya dapat dimulai.

Asynchronous Programming
Asynchronous programming (asinkron) adalah pendekatan dimana sebuah program tidak perlu menunggu task yang sedang berjalan untuk menyelesaikan eksekusinya sebelum menjalankan task berikutnya. Pada asynchronous programming, program bisa melanjutkan eksekusinya meskipun task yang sedang berjalan belum selesai.

Perbedaan utama antara synchronous programming dan asynchronous programming adalah cara program berjalan. Synchronous programming dijalankan secara sekuensial dan memerlukan waktu untuk menyelesaikan satu task sebelum mengeksekusi task berikutnya. Sementara itu, asynchronous programming dijalankan secara paralel atau simultan, sehingga memungkinkan beberapa task berjalan secara bersamaan tanpa harus menunggu satu sama lain.


Jelaskan penerapan asynchronous programming pada AJAX.

jawab:Asynchronous JavaScript and XML (AJAX) adalah teknik yang memungkinkan sebuah halaman web untuk memperbarui data secara dinamis tanpa harus memuat ulang seluruh halaman web. Pada dasarnya, AJAX memanfaatkan teknik asynchronous programming untuk mengirim request dan menerima response dari server tanpa harus menunggu halaman web untuk dimuat ulang.

Berikut adalah penerapan asynchronous programming pada AJAX:

Menggunakan XMLHttpRequest (XHR)
XMLHttpRequest (XHR) adalah objek pada JavaScript yang memungkinkan sebuah halaman web untuk mengirim request HTTP asynchronous ke server dan menerima response dari server. Pada AJAX, XHR digunakan untuk mengirimkan request ke server tanpa harus menunggu halaman web untuk dimuat ulang. Setelah server memberikan response, XHR akan menangani data tersebut dan memperbarui halaman web sesuai dengan responsenya.

Callback Function
Pada AJAX, biasanya digunakan callback function untuk menangani respons dari server setelah request telah dikirimkan. Callback function akan dieksekusi setelah respons dari server diterima, dan akan memperbarui halaman web sesuai dengan responsenya. Callback function sangat berguna pada asynchronous programming karena memungkinkan program untuk menjalankan task secara bersamaan tanpa harus menunggu task sebelumnya selesai terlebih dahulu.

Promise
Promise adalah cara lain untuk menangani respons dari server pada AJAX. Promise pada AJAX mirip dengan callback function, namun menggunakan sintaks yang berbeda. Promise pada AJAX digunakan untuk menangani respons dari server dan melakukan aksi sesuai dengan responsenya.

Jelaskan penerapan asynchronous programming pada AJAX.
jawab:
Dalam penerapan asynchronous programming pada AJAX, penting untuk memperhatikan keterkaitan antara request dan responsenya. Setiap request harus memiliki responsenya yang sesuai, dan halaman web harus diperbarui sesuai dengan responsenya. Dalam melakukan debugging pada AJAX, sangat disarankan untuk menggunakan tools developer pada browser seperti Chrome DevTools atau Firebug untuk memantau request dan responsenya.

Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma event-driven programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.

jawab:
Event-driven programming adalah sebuah metode pemrograman dimana jalur eksekusi program ditentukan oleh kejadian atau peristiwa tertentu, seperti masukan dari pengguna atau perubahan data. Berbeda dengan pendekatan pemrograman lainnya, pada event-driven programming, kode tidak dieksekusi secara berurutan dari atas ke bawah, melainkan dipicu oleh event yang terjadi. Pada penggunaan JavaScript dan AJAX, event-driven programming memungkinkan aplikasi web untuk merespons secara dinamis terhadap interaksi pengguna dan perubahan data tanpa perlu memuat ulang halaman secara keseluruhan. Dengan begitu, aplikasi web dapat memberikan pengalaman pengguna yang lebih baik dan responsif. Sumber referensi untuk topik ini dapat ditemukan di "Introduction to events" yang tersedia pada Mozilla Developer Network (MDN), "Ajax - Developer guides" pada MDN, dan "Event-driven application design with JavaScript" dari O'Reilly.

