<h1 align="center">PROGRAM PENGELOLA DATA HERO MOBILE LEGENDS</h1>

<p align="left">
  <b>Nama:</b> Muhammad Fahry Praditya<br>
  <b>NIM:</b> 2609116104<br>
  <b>Kelas:</b> C
</p>

<!-- FLOWCHART LOGIN -->
<table>
  <tr>
    <td width="50%" align="center">
      <img 
        src="https://github.com/user-attachments/assets/cffac4e0-8107-477c-beee-92a56ae6504a"
        width="100%"
      />
    </td>
    <td width="50%" valign="top">
      <h3>FLOWCHART LOGIN</h3>
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
    <td width="50%" align="center">
      <img 
        src="https://github.com/user-attachments/assets/53822035-feea-4ba9-bcf5-eaff0e8e7085"
        width="100%"
      />
    </td>
    <td width="50%" valign="top">
      <h3>FLOWCHART MENU ADMIN</h3>
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
    <td width="50%" align="center">
      <img 
        src="https://github.com/user-attachments/assets/01cd3c89-31a2-4b07-8235-9198ba4131a1"
        width="100%"
      />
    </td>
    <td width="50%" valign="top">
      <h3>FLOWCHART MENU USER</h3>
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
    <td width="50%" align="center">
      <img 
        src="https://github.com/user-attachments/assets/8ee0ad00-23b0-4a74-a1d6-90458a4138bd"
        width="100%"
      />
    </td>
    <td width="50%" valign="top">
      <h3>IMPORT LIBRARY</h3>
      <p>
        Program menggunakan library <b>time</b> untuk mengatur waktu atau jeda
        dalam program, sedangkan <b>pwinput</b> digunakan untuk memasukkan
        password dengan karakter yang tidak terlihat.
      </p>
    </td>
  </tr>
</table>
<br>

<!-- DATA AKUN DAN DATA HERO -->
<table>
  <tr>
    <td width="50%" align="center">
      <img 
        src="https://github.com/user-attachments/assets/1184f8f2-bcd4-471b-9cb8-a5f7002ebb17"
        width="100%"
      />
    </td>
    <td width="50%" valign="top">
      <h3>DATA AKUN DAN DATA HERO</h3>
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



<table>
  <tr>
    <td width="50%" align="center">
      <img 
        src="https://github.com/user-attachments/assets/12e3fa72-bc2e-485e-9ccb-ceb976b36c9a"
        width="100%"
      />
    </td>
    <td width="50%" valign="top">
      <h3>LOGIN</h3>
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



<table>
  <tr>
    <td width="50%" align="center">
      <img 
        src="https://github.com/user-attachments/assets/2181ab66-c096-4674-b6a2-0b6f93790dd8"
        width="100%"
      />
    </td>
    <td width="50%" valign="top">
      <h3>MENAMBAH DATA HERO</h3>
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


<table>
  <tr>
    <td width="50%" align="center">
      <img 
        src="https://github.com/user-attachments/assets/cbb5c1b3-d55e-4e86-8a73-87729bc96a00" />
    </td>
    <td width="50%" valign="top">
      <h3>MENAMBAH DATA HERO</h3>
      <p>
        Fungsi <b>tambah_data()</b> digunakan untuk menambahkan data hero baru.
        Pengguna diminta mengisi <b>nama hero, role, dan lane</b>.
      </p>
      <p>
        Program melakukan pengecekan agar data tidak boleh kosong. Role dan
        lane juga harus sesuai dengan daftar yang sudah ditentukan.
        Selain itu, program mengecek apakah nama hero sudah ada untuk
        menghindari data yang sama.
      </p>
      <p>
        Jika semua data valid, data hero akan ditambahkan ke dalam
        <b>data_hero</b> menggunakan <b>append()</b>. Setelah berhasil,
        program menampilkan pesan <b>"Data hero berhasil ditambahkan"</b>.
      </p>
    </td>
  </tr>
</table>


<table>
  <tr>
    <td width="50%" align="center">
      <img 
        src="https://github.com/user-attachments/assets/fc12ae8d-58e6-49f5-9207-17588de6280e"
        width="100%"
      />
    </td>
    <td width="50%" valign="top">
      <h3>MENAMPILKAN DATA HERO</h3>
      <p>
        Fungsi <b>tampilkan_data()</b> digunakan untuk menampilkan seluruh
        data hero yang tersimpan di dalam <b>data_hero</b>.
      </p>
      <p>
        Program terlebih dahulu mengecek apakah data hero masih kosong.
        Jika belum ada data, program akan menampilkan pesan
        <b>"Belum ada data hero."</b> dan proses dihentikan.
      </p>
      <p>
        Jika data tersedia, program menampilkan nomor, nama hero, role,
        dan lane. Variabel <b>nomor</b> digunakan sebagai nomor urut dan
        akan bertambah setiap kali program melakukan perulangan pada
        setiap data hero.
      </p>
    </td>
  </tr>
</table>

<table>
  <tr>
    <td width="50%" align="center">
      <img 
        src="https://github.com/user-attachments/assets/8c387f5c-e12b-4507-9d42-4d576dcfe60b"
        width="100%"
      />
    </td>
    <td width="50%" valign="top">
      <h3>MENAMPILKAN DATA HERO</h3>
      <p>
        Fungsi <b>tampilkan_data()</b> digunakan untuk menampilkan seluruh
        data hero yang tersimpan di dalam <b>data_hero</b>.
      </p>
      <p>
        Program terlebih dahulu mengecek apakah data hero masih kosong.
        Jika belum ada data, program akan menampilkan pesan
        <b>"Belum ada data hero."</b> dan proses dihentikan.
      </p>
      <p>
        Jika data tersedia, program menampilkan nomor, nama hero, role,
        dan lane. Variabel <b>nomor</b> digunakan sebagai nomor urut dan
        akan bertambah setiap kali program melakukan perulangan pada
        setiap data hero.
      </p>
    </td>
  </tr>
</table>


<table>
  <tr>
    <td width="50%" align="center">
      <img 
        src="https://github.com/user-attachments/assets/79782ec2-8084-4cf0-923b-b7d6a70622c6" 
        width="100%"
      />
    </td>
    <td width="50%" valign="top">
      <h3>MENGHAPUS DATA HERO</h3>
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


<table>
  <tr>
    <td width="50%" align="center">
      <img 
        src="https://github.com/user-attachments/assets/51e1158c-34f3-4097-a5f1-22f3f6dcac64"
        width="100%"
      />
    </td>
    <td width="50%" valign="top">
      <h3>MENU ADMIN CRUD</h3>
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


<table>
  <tr>
    <td width="50%" align="center">
      <img 
       src="https://github.com/user-attachments/assets/1b63a632-d03f-4220-b41a-731eea9c122e"
        width="100%"
      />
    </td>
    <td width="50%" valign="top">
      <h3>MENU USER</h3>
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


<table>
  <tr>
    <td width="50%" align="center">
      <img 
     src="https://github.com/user-attachments/assets/4bfd906c-dce3-4ee0-8c7b-c8e8697806b6"
        width="100%"
      />
    </td>
    <td width="50%" valign="top">
      <h3>MAIN PROGRAM</h3>
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


<table>
  <tr>
    <td width="50%" align="center">
      <img 
        src="https://github.com/user-attachments/assets/5053cbad-f964-40eb-8aba-a303433aea14"
        width="100%"
      />
    </td>
    <td width="50%" valign="top">
      <h3>HASIL OUTPUT PROGRAM</h3>
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

<table>
  <tr>
    <td width="50%" align="center">
      <img
        src="https://github.com/user-attachments/assets/c1dc4f22-5b84-4eb3-9406-c545bee5fe1e"
        width="100%"
      />
    </td>
    <td width="50%" valign="top">
      <h3>OUTPUT MENAMPILKAN DATA HERO</h3>
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

<table>
  <tr>
    <td width="50%" align="center">
      <img 
        src="https://github.com/user-attachments/assets/045466c1-418d-45df-91e9-a1ec8b2be508"
        width="100%"
      />
    </td>
    <td width="50%" valign="top">
      <h3>OUTPUT MENGUBAH DATA HERO</h3>
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


<table>
  <tr>
    <td width="50%" align="center">
      <img 
       src="https://github.com/user-attachments/assets/139feacd-5267-44fa-8953-49a2248e37df"
        width="100%"
      />
    </td>
    <td width="50%" valign="top">
      <h3>OUTPUT MENGHAPUS DATA HERO</h3>
      <p>
        Output ini menunjukkan proses ketika admin memilih menu
        <b>4. Hapus data hero</b>. Program menampilkan daftar data hero
        terlebih dahulu, kemudian admin diminta memasukkan nomor hero
        yang ingin dihapus.
      </p>
      <p>
        Pada contoh ini, admin memilih hero nomor <b>7</b>, yaitu hero
        <b>Jayu</b> dengan role <b>Assassin</b> dan lane <b>Jungle</b>.
        Setelah nomor hero valid, program menghapus data tersebut dari
        daftar hero.
      </p>
      <p>
        Setelah berhasil dihapus, program menampilkan pesan
        <b>"Hero Jayu berhasil dihapus"</b>. Hal ini menunjukkan bahwa
        proses penghapusan data hero berhasil dilakukan.
      </p>
    </td>
  </tr>
</table>

<table>
  <tr>
    <td width="50%" align="center">
      <img 
       src="https://github.com/user-attachments/assets/139feacd-5267-44fa-8953-49a2248e37df"
        width="100%"
      />
    </td>
    <td width="50%" valign="top">
      <h3>OUTPUT LOGOUT ADMIN</h3>
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

<table>
  <tr>
    <td width="50%" align="center">
      <img 
       src="https://github.com/user-attachments/assets/f89a9586-afc1-4b7c-a8e4-a13cfe58b3f5" 
        width="100%"
        alt="Output Menu User"
      />
    </td>
    <td width="50%" valign="top">
      <h3>OUTPUT LOGIN & MENAMPILKAN DATA HERO (USER)</h3>
      <p>
        Output ini menunjukkan alur kerja pengguna biasa (<b>user</b>). Pertama, pengguna memilih menu <b>1. Login</b> pada menu utama, kemudian memasukkan username dan password hingga muncul pesan <b>"Login berhasil!"</b>.
      </p>
      <p>
        Setelah masuk ke <b>MENU USER</b>, pengguna memilih menu <b>1. Tampilkan data hero</b>. Program kemudian menampilkan tabel berisi daftar hero yang mencakup kolom nomor, nama hero, role, dan lane (contoh: Miya, Tigreal, Alucard, dll).
      </p>
      <p>
        Terakhir, pengguna memilih menu <b>2. Logout</b> dari Menu User, dan program memberikan konfirmasi berupa pesan <b>"Logout berhasil"</b>.
      </p>
    </td>
  </tr>
</table>
