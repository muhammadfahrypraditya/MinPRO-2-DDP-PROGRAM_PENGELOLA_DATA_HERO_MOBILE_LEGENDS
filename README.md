<h1 align="center">PROGRAM PENGELOLA DATA HERO MOBILE LEGENDS</h1>

<p align="left">
  <b>Nama:</b> Muhammad Fahry Praditya<br>
  <b>NIM:</b> 2609116104<br>
  <b>Kelas:</b> C
</p>

<!-- FLOWCHART LOGIN -->
<table>
  <tr>
    <th width="50%">Flowchart</th>
    <th width="50%">Penjelasan</th>
  </tr>
  <tr>
    <td>
      <img src="https://github.com/user-attachments/assets/cffac4e0-8107-477c-beee-92a56ae6504a" width="100%" />
    </td>
    <td valign="top">
      <b>FLOWCHART LOGIN</b><br><br>
      <p>
        Flowchart ini merupakan proses permulaan program. Jika memilih pilihan
        1, program akan meminta username dan password. Jika username dan
        password valid, maka akan lanjut ke proses login. Jika tidak valid,
        akan muncul pesan <b>"Username & Password Salah"</b> dan kembali ke
        menu input. Jika memilih pilihan 2, maka program akan logout dan selesai.
      </p>
    </td>
  </tr>
</table>

<br>

<!-- FLOWCHART ADMIN -->
<table>
  <tr>
    <th width="50%">Flowchart</th>
    <th width="50%">Penjelasan</th>
  </tr>
  <tr>
    <td>
      <img src="https://github.com/user-attachments/assets/53822035-feea-4ba9-bcf5-eaff0e8e7085" width="100%" />
    </td>
    <td valign="top">
      <b>FLOWCHART MENU ADMIN</b><br><br>
      <p>
        Flowchart ini merupakan menu admin yang memiliki pilihan 1 sampai 5.
        Pilihan 1 digunakan untuk menambahkan hero dengan menginput nama hero,
        role, dan lane. Jika data tidak valid, akan muncul pesan
        <b>"Data Tidak Valid"</b> dan kembali ke pilihan menu. Jika data valid,
        hero akan ditambahkan ke dalam daftar hero.
      </p>
      <p>
        Pilihan 2 digunakan untuk menampilkan seluruh data hero, kemudian
        kembali ke menu utama. Pilihan 3 digunakan untuk mengubah data hero
        berdasarkan nomor hero. Jika nomor tidak ditemukan, akan muncul pesan
        <b>"Nomor Tidak Ditemukan"</b>. Jika nomor valid, pengguna dapat
        memasukkan data baru. Jika input kosong, data lama akan tetap digunakan.
      </p>
      <p>
        Pilihan 4 digunakan untuk menghapus data hero berdasarkan nomor.
        Jika nomor valid, data hero akan dihapus. Jika nomor tidak valid,
        akan muncul pesan <b>"Nomor Tidak Ditemukan"</b>. Pilihan 5 digunakan
        untuk mengakhiri program.
      </p>
    </td>
  </tr>
</table>

<br>

<!-- FLOWCHART USER -->
<table>
  <tr>
    <th width="50%">Flowchart</th>
    <th width="50%">Penjelasan</th>
  </tr>
  <tr>
    <td>
      <img src="https://github.com/user-attachments/assets/01cd3c89-31a2-4b07-8235-9198ba4131a1" width="100%" />
    </td>
    <td valign="top">
      <b>FLOWCHART MENU USER</b><br><br>
      <p>
        Flowchart ini merupakan menu user yang hanya memiliki dua pilihan.
        Pilihan 1 digunakan untuk menampilkan list data hero, kemudian kembali
        ke menu pilihan. Jika memilih pilihan 2, maka user akan logout dan
        program selesai.
      </p>
    </td>
  </tr>
</table>

<br>

<!-- IMPORT LIBRARY -->
<table>
  <tr>
    <th width="50%">Tampilan Kode</th>
    <th width="50%">Penjelasan</th>
  </tr>
  <tr>
    <td>
      <img src="https://github.com/user-attachments/assets/327e17db-4485-4a8c-8cbe-d4b95f6011c3" width="100%" />
    </td>
    <td valign="top">
      <b>IMPORT LIBRARY</b><br><br>
      <p>
        Program menggunakan library <b>time</b> untuk mengatur waktu atau jeda
        dalam program, <b>pwinput</b> digunakan untuk memasukkan
        password dengan karakter yang tidak terlihat, dan <b>prettytable</b>
        digunakan untuk menambahkan tabel agar output rapi.
      </p>
    </td>
  </tr>
</table>

<br>

<!-- DATA AKUN DAN DATA HERO -->
<table>
  <tr>
    <th width="50%">Tampilan Kode</th>
    <th width="50%">Penjelasan</th>
  </tr>
  <tr>
    <td>
      <img src="https://github.com/user-attachments/assets/1184f8f2-bcd4-471b-9cb8-a5f7002ebb17" width="100%" />
    </td>
    <td valign="top">
      <b>DATA AKUN DAN DATA HERO</b><br><br>
      <p>
        Pada bagian ini terdapat data akun yang disimpan dalam bentuk
        <b>dictionary</b>, yaitu akun admin dan user yang masing-masing
        memiliki password dan role.
      </p>
      <p>
        Selain itu, terdapat <b>data hero</b> yang disimpan dalam bentuk
        list berisi dictionary. Setiap hero memiliki nama, role, dan lane.
        Program juga memiliki <b>daftar role dan lane yang valid</b> untuk
        digunakan sebagai validasi saat pengguna memasukkan data.
      </p>
    </td>
  </tr>
</table>

<br>

<!-- LOGIN -->
<table>
  <tr>
    <th width="50%">Tampilan Kode</th>
    <th width="50%">Penjelasan</th>
  </tr>
  <tr>
    <td>
      <img src="https://github.com/user-attachments/assets/12e3fa72-bc2e-485e-9ccb-ceb976b36c9a" width="100%" />
    </td>
    <td valign="top">
      <b>LOGIN</b><br><br>
      <p>
        Fungsi <b>login()</b> digunakan untuk memproses login pengguna dengan
        memasukkan username dan password. Password menggunakan <b>pwinput</b>
        agar karakter password tidak terlihat.
      </p>
      <p>
        Program mengecek username dan password dengan data akun yang tersedia.
        Jika benar, akan muncul pesan <b>"Login berhasil!"</b> dan username
        dikembalikan. Jika salah, program menampilkan pesan
        <b>"Username atau password salah"</b>.
      </p>
    </td>
  </tr>
</table>

<br>

<!-- MENAMBAH DATA HERO -->
<table>
  <tr>
    <th width="50%">Tampilan Kode</th>
    <th width="50%">Penjelasan</th>
  </tr>
  <tr>
    <td>
      <img src="https://github.com/user-attachments/assets/3695872d-e5ff-4ea5-a1d8-8be348b7b3b8" width="100%" />
    </td>
    <td valign="top">
      <b>MENAMBAH DATA HERO</b><br><br>
      <p>
        Fungsi <b>tambah_data()</b> digunakan untuk menambahkan hero baru
        ke dalam daftar data hero. Pengguna diminta memasukkan
        <b>nama hero, role, dan lane</b>.
      </p>
      <p>
        Program melakukan validasi untuk memastikan data tidak boleh kosong,
        role harus sesuai dengan daftar role yang tersedia, dan lane harus
        sesuai dengan daftar lane yang valid. Program juga mengecek apakah
        nama hero sudah ada.
      </p>
      <p>
        Jika semua data valid dan hero belum ada, data akan ditambahkan
        menggunakan <b>append()</b> dan program menampilkan pesan
        <b>"Data hero berhasil ditambahkan"</b>.
      </p>
    </td>
  </tr>
</table>

<br>

<!-- MENAMPILKAN DATA HERO -->
<table>
  <tr>
    <th width="50%">Tampilan Kode</th>
    <th width="50%">Penjelasan</th>
  </tr>
  <tr>
    <td>
      <img src="https://github.com/user-attachments/assets/f976b70d-5037-4d9b-8b88-ea79cbbd5b70" width="100%" />
    </td>
    <td valign="top">
      <b>MENAMPILKAN DATA HERO</b><br><br>
      <p>
        Fungsi <b>tampilkan_data()</b> digunakan untuk menampilkan seluruh
        data hero Mobile Legends dalam bentuk tabel di terminal.
      </p>
      <p>
        Program mengecek apakah <b>data_hero</b> kosong. Jika kosong, akan
        muncul pesan <b>"Belum ada data hero."</b> lalu keluar dari fungsi
        menggunakan <b>return</b>.
      </p>
      <p>
        Jika ada data, program membuat tabel menggunakan <b>PrettyTable</b>
        dengan kolom <b>No, Nama Hero, Role, dan Lane</b>. Setiap hero pada
        <b>data_hero</b> ditambahkan ke tabel beserta nomor urut otomatis,
        kemudian tabel dicetak ke layar.
      </p>
    </td>
  </tr>
</table>

<br>

<!-- MENGUBAH DATA HERO -->
<table>
  <tr>
    <th width="50%">Tampilan Kode</th>
    <th width="50%">Penjelasan</th>
  </tr>
  <tr>
    <td>
      <img src="https://github.com/user-attachments/assets/7decf1a7-e071-45f3-ba06-044fd83dd7de" width="100%" />
    </td>
    <td valign="top">
      <b>MENGUBAH DATA HERO</b><br><br>
      <p>
        Fungsi <b>ubah_data()</b> digunakan untuk mengubah data hero yang
        sudah tersimpan berdasarkan nomor urutnya. Program terlebih dahulu
        menampilkan daftar hero menggunakan <b>tampilkan_data()</b>, kemudian
        pengguna diminta memasukkan nomor hero yang ingin diubah.
      </p>
      <p>
        Input nomor diubah ke angka dengan <b>int()</b> di dalam
        <b>try</b>. Jika yang dimasukkan bukan angka, <b>except ValueError</b>
        menampilkan pesan <b>"Masukkan angka saja"</b> lalu keluar dari fungsi.
      </p>
      <p>
        Setelah itu, pengguna memasukkan nama, role, dan lane yang baru.
        Program memvalidasi bahwa nama tidak boleh kosong, role harus ada di
        <b>daftar_role</b>, dan lane harus ada di <b>daftar_lane</b>. Jika
        valid, data hero pada indeks <b>nomor - 1</b> diperbarui dan program
        menampilkan pesan <b>"Data hero berhasil diubah!"</b>.
      </p>
    </td>
  </tr>
</table>

<br>

<!-- MENGHAPUS DATA HERO -->
<table>
  <tr>
    <th width="50%">Tampilan Kode</th>
    <th width="50%">Penjelasan</th>
  </tr>
  <tr>
    <td>
      <img src="https://github.com/user-attachments/assets/79782ec2-8084-4cf0-923b-b7d6a70622c6" width="100%" />
    </td>
    <td valign="top">
      <b>MENGHAPUS DATA HERO</b><br><br>
      <p>
        Fungsi <b>hapus_data()</b> digunakan untuk menghapus data hero
        yang tersimpan. Program terlebih dahulu menampilkan daftar hero,
        kemudian pengguna diminta memasukkan nomor hero yang ingin dihapus.
      </p>
      <p>
        Program mengecek apakah input yang dimasukkan berupa angka. Jika
        bukan angka, akan muncul pesan <b>"Masukkan angka saja"</b>.
        Setelah itu, nomor hero diperiksa untuk memastikan nomor tersebut
        tersedia. Jika tidak ditemukan, program menampilkan pesan
        <b>"Nomor hero tidak ditemukan"</b>.
      </p>
      <p>
        Jika nomor valid, data hero akan dihapus menggunakan fungsi
        <b>pop()</b>. Setelah berhasil dihapus, program menampilkan nama
        hero beserta pesan <b>"berhasil dihapus"</b>.
      </p>
    </td>
  </tr>
</table>

<br>

<!-- MENU ADMIN CRUD -->
<table>
  <tr>
    <th width="50%">Tampilan Kode</th>
    <th width="50%">Penjelasan</th>
  </tr>
  <tr>
    <td>
      <img src="https://github.com/user-attachments/assets/51e1158c-34f3-4097-a5f1-22f3f6dcac64" width="100%" />
    </td>
    <td valign="top">
      <b>MENU ADMIN CRUD</b><br><br>
      <p>
        Fungsi <b>menu_admin()</b> digunakan sebagai menu utama admin untuk
        mengelola data hero. Menu berjalan menggunakan perulangan
        <b>while True</b> sehingga admin dapat melakukan beberapa proses
        secara berulang.
      </p>
      <p>
        Admin memiliki lima pilihan, yaitu <b>Tambah Data Hero</b>,
        <b>Tampilkan Data Hero</b>, <b>Ubah Data Hero</b>,
        <b>Hapus Data Hero</b>, dan <b>Logout</b>. Setiap pilihan akan
        menjalankan fungsi yang sesuai.
      </p>
      <p>
        Jika admin memilih pilihan 5, program menampilkan pesan
        <b>"Logout berhasil"</b> dan menggunakan <b>break</b> untuk
        menghentikan perulangan. Jika pilihan yang dimasukkan tidak tersedia,
        program menampilkan pesan <b>"Pilihan tidak valid"</b> dan kembali
        ke menu admin.
      </p>
    </td>
  </tr>
</table>

<br>

<!-- MENU USER -->
<table>
  <tr>
    <th width="50%">Tampilan Kode</th>
    <th width="50%">Penjelasan</th>
  </tr>
  <tr>
    <td>
      <img src="https://github.com/user-attachments/assets/1b63a632-d03f-4220-b41a-731eea9c122e" width="100%" />
    </td>
    <td valign="top">
      <b>MENU USER</b><br><br>
      <p>
        Fungsi <b>menu_user()</b> digunakan sebagai menu untuk user yang
        hanya dapat melihat data hero. Menu menggunakan perulangan
        <b>while True</b> agar user dapat memilih menu berulang kali.
      </p>
      <p>
        User memiliki dua pilihan, yaitu <b>1. Tampilkan Data Hero</b>
        dan <b>2. Logout</b>. Jika memilih pilihan 1, program akan
        menjalankan fungsi <b>tampilkan_data()</b> untuk menampilkan
        seluruh data hero.
      </p>
      <p>
        Jika memilih pilihan 2, program menampilkan pesan
        <b>"Logout berhasil!"</b> kemudian menggunakan <b>break</b>
        untuk keluar dari perulangan. Jika pilihan tidak tersedia,
        program akan menampilkan pesan <b>"Pilihan tidak valid!"</b>.
      </p>
    </td>
  </tr>
</table>

<br>

<!-- MAIN PROGRAM -->
<table>
  <tr>
    <th width="50%">Tampilan Kode</th>
    <th width="50%">Penjelasan</th>
  </tr>
  <tr>
    <td>
      <img src="https://github.com/user-attachments/assets/4bfd906c-dce3-4ee0-8c7b-c8e8697806b6" width="100%" />
    </td>
    <td valign="top">
      <b>MAIN PROGRAM</b><br><br>
      <p>
        Fungsi <b>main()</b> merupakan bagian utama yang menjalankan program.
        Program menggunakan <b>while True</b> agar menu utama dapat ditampilkan
        secara berulang sampai pengguna memilih untuk keluar.
      </p>
      <p>
        Pada menu utama terdapat pilihan <b>Login</b> dan <b>Keluar</b>.
        Jika memilih Login, program akan menjalankan fungsi <b>login()</b>.
        Jika login berhasil, program akan mengecek role akun. Jika role adalah
        <b>admin</b>, maka diarahkan ke <b>menu_admin()</b>, sedangkan user
        biasa diarahkan ke <b>menu_user()</b>.
      </p>
      <p>
        Jika pengguna memilih pilihan 2, program menampilkan pesan
        <b>"Terima kasih"</b> dan menggunakan <b>break</b> untuk mengakhiri
        program. Jika pilihan tidak tersedia, akan muncul pesan
        <b>"Pilihan tidak valid"</b>.
      </p>
    </td>
  </tr>
</table>

<br>

<!-- OUTPUT TAMBAH DATA -->
<table>
  <tr>
    <th width="50%">Output</th>
    <th width="50%">Penjelasan</th>
  </tr>
  <tr>
    <td>
      <img src="https://github.com/user-attachments/assets/5053cbad-f964-40eb-8aba-a303433aea14" width="100%" />
    </td>
    <td valign="top">
      <b>HASIL OUTPUT PROGRAM</b><br><br>
      <p>
        Output ini menunjukkan proses program saat pengguna melakukan
        <b>login sebagai admin</b>. Setelah username dan password yang
        dimasukkan benar, program menampilkan pesan
        <b>"Login berhasil!"</b> dan masuk ke menu admin.
      </p>
      <p>
        Pada menu admin, pengguna memilih pilihan <b>1</b> untuk menambahkan
        data hero. Pengguna kemudian memasukkan nama hero <b>Azzam</b>,
        role <b>Tank</b>, dan lane <b>Roam</b>.
      </p>
      <p>
        Karena semua data yang dimasukkan valid, program berhasil menambahkan
        hero ke dalam daftar dan menampilkan pesan
        <b>"Data hero berhasil ditambahkan"</b>.
      </p>
    </td>
  </tr>
</table>

<br>

<!-- OUTPUT TAMPILKAN DATA -->
<table>
  <tr>
    <th width="50%">Output</th>
    <th width="50%">Penjelasan</th>
  </tr>
  <tr>
    <td>
      <img src="https://github.com/user-attachments/assets/c1dc4f22-5b84-4eb3-9406-c545bee5fe1e" width="100%" />
    </td>
    <td valign="top">
      <b>OUTPUT MENAMPILKAN DATA HERO</b><br><br>
      <p>
        Output ini menunjukkan proses ketika admin memilih menu
        <b>2. Tampilkan data hero</b>. Program kemudian menampilkan seluruh
        data hero yang tersimpan dalam daftar.
      </p>
      <p>
        Data ditampilkan dalam bentuk tabel sederhana yang berisi
        <b>nomor, nama hero, role, dan lane</b>. Pada output ini terdapat
        7 data hero, termasuk hero baru yaitu <b>Azzam</b> dengan role
        <b>Tank</b> dan lane <b>Roam</b>.
      </p>
      <p>
        Data yang ditampilkan menunjukkan bahwa proses penambahan data
        sebelumnya berhasil tersimpan dan dapat ditampilkan kembali
        melalui menu admin.
      </p>
    </td>
  </tr>
</table>

<br>

<!-- OUTPUT UBAH DATA -->
<table>
  <tr>
    <th width="50%">Output</th>
    <th width="50%">Penjelasan</th>
  </tr>
  <tr>
    <td>
      <img src="https://github.com/user-attachments/assets/045466c1-418d-45df-91e9-a1ec8b2be508" width="100%" />
    </td>
    <td valign="top">
      <b>OUTPUT MENGUBAH DATA HERO</b><br><br>
      <p>
        Output ini menunjukkan proses ketika admin memilih menu
        <b>3. Ubah data hero</b>. Program menampilkan daftar hero terlebih
        dahulu, kemudian admin memasukkan nomor hero yang ingin diubah.
      </p>
      <p>
        Pada contoh ini, admin memilih hero nomor <b>7</b> yang sebelumnya
        bernama <b>Azzam</b>. Kemudian data tersebut diubah menjadi nama
        <b>Jayu</b>, dengan role <b>Assassin</b> dan lane <b>Jungle</b>.
      </p>
      <p>
        Setelah data baru dimasukkan dan valid, program berhasil memperbarui
        data hero dan menampilkan pesan
        <b>"Data hero berhasil diubah"</b>.
      </p>
    </td>
  </tr>
</table>

<br>

<!-- OUTPUT HAPUS DATA -->
<table>
  <tr>
    <th width="50%">Output</th>
    <th width="50%">Penjelasan</th>
  </tr>
  <tr>
    <td>
      <img src="https://github.com/user-attachments/assets/f7617533-9314-46f6-9a8e-81aaff8d4593" />
    </td>
    <td valign="top">
      <b>OUTPUT MENGHAPUS DATA HERO</b><br><br>
      <p>
        Output ini menunjukkan proses ketika admin memilih menu
        <b>4. Hapus data hero</b>. Program menampilkan judul
        <b>HAPUS DATA HERO</b> lalu menampilkan daftar hero dalam bentuk
        tabel yang berisi nomor, nama hero, role, dan lane. Pada output ini
        terdapat 6 data hero, yaitu Miya, Tigreal, Alucard, Gord, Karina,
        dan Estes.
      </p>
      <p>
        Setelah itu, admin diminta memasukkan nomor hero yang ingin dihapus.
        Pada contoh ini, admin memasukkan nomor <b>5</b>, yaitu hero
        <b>Karina</b> dengan role <b>Assassin</b> dan lane <b>Jungle</b>.
      </p>
      <p>
        Karena nomor yang dimasukkan valid, data hero berhasil dihapus dan
        program menampilkan pesan <b>"Hero Karina berhasil dihapus!"</b>.
      </p>
    </td>
  </tr>
</table>

<br>

<!-- OUTPUT LOGOUT ADMIN -->
<table>
  <tr>
    <th width="50%">Output</th>
    <th width="50%">Penjelasan</th>
  </tr>
  <tr>
    <td>
      <img <img width="612" height="434" alt="Cuplikan layar 2026-10-06 135156" src="https://github.com/user-attachments/assets/fd60aa5f-1410-4fc1-951f-f1c0febe3cbc" />
    </td>
    <td valign="top">
      <b>OUTPUT LOGOUT ADMIN</b><br><br>
      <p>
        Output ini menunjukkan proses ketika admin berada pada
        <b>Menu Admin</b>. Program menampilkan beberapa pilihan menu,
        seperti tambah data hero, tampilkan data hero, ubah data hero,
        hapus data hero, dan logout.
      </p>
      <p>
        Pada contoh ini, admin memilih menu <b>5. Logout</b>
        dengan memasukkan angka <b>5</b>. Pilihan tersebut digunakan
        untuk keluar dari sesi admin.
      </p>
      <p>
        Setelah pilihan diproses, program menampilkan pesan
        <b>"Logout berhasil"</b>. Hal ini menunjukkan bahwa admin
        telah berhasil keluar dari sistem.
      </p>
    </td>
  </tr>
</table>

<br>

<!-- OUTPUT USER -->
<table>
  <tr>
    <th width="50%">Output</th>
    <th width="50%">Penjelasan</th>
  </tr>
  <tr>
    <td>
      <img src="https://github.com/user-attachments/assets/f89a9586-afc1-4b7c-a8e4-a13cfe58b3f5" width="100%" />
    </td>
    <td valign="top">
      <b>OUTPUT LOGIN & MENAMPILKAN DATA HERO (USER)</b><br><br>
      <p>
        Output ini menunjukkan alur kerja pengguna biasa (<b>user</b>).
        Pertama, pengguna memilih menu <b>1. Login</b> pada menu utama,
        kemudian memasukkan username dan password hingga muncul pesan
        <b>"Login berhasil!"</b>.
      </p>
      <p>
        Setelah masuk ke <b>MENU USER</b>, pengguna memilih menu
        <b>1. Tampilkan data hero</b>. Program kemudian menampilkan tabel
        berisi daftar hero yang mencakup kolom nomor, nama hero, role, dan
        lane (contoh: Miya, Tigreal, Alucard, dll).
      </p>
      <p>
        Terakhir, pengguna memilih menu <b>2. Logout</b> dari Menu User,
        dan program memberikan konfirmasi berupa pesan
        <b>"Logout berhasil"</b>.
      </p>
    </td>
  </tr>
</table>
