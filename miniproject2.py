#mini project 2 
from prettytable import PrettyTable
import time
import pwinput

# Data akun (dictionary)
akun = {
    "admin": {"password": "admin123", "role": "admin"},
    "user": {"password": "user123", "role": "user"}
}

# Data hero (list berisi dictionary)
data_hero = [
    {"nama": "Miya", "role": "Marksman", "lane": "Gold"},
    {"nama": "Tigreal", "role": "Tank", "lane": "Roam"},
    {"nama": "Alucard", "role": "Fighter", "lane": "Jungle"},
    {"nama": "Gord", "role": "Mage", "lane": "Mid"},
    {"nama": "Karina", "role": "Assassin", "lane": "Jungle"},
    {"nama": "Estes", "role": "Support", "lane": "Roam"}
]
# daftar role dan lane yang valid 
daftar_role = ["Tank", "Fighter", "Assassin", "Mage", "Marksman", "Support"]
daftar_lane = ["Gold", "Exp", "Mid", "Jungle", "Roam"]


# Login 
def login():
    print("\n=== LOGIN ===")
    username = input("Username : ")
    password = pwinput.pwinput("Password : ")

    if username in akun and akun[username]["password"] == password:
        print("Login berhasil")
        time.sleep(1)
        return username

    print("Username atau password salah!")
    return ""

# menambah data
def tambah_data():
    print("\n=== TAMBAH DATA HERO ===")
    nama = input("Nama Hero : ")
    role = input("Role      : ")
    lane = input("Lane      : ")

    if nama == "" or role == "" or lane == "":
        print("Data tidak boleh kosong")
        return
    if role not in daftar_role:
        print("Role tidak valid")
        return
    if lane not in daftar_lane:
        print("Lane tidak valid")
        return
    for hero in data_hero:
        if hero["nama"] == nama:
            print("Hero sudah ada")
            return

    data_hero.append({"nama": nama, "role": role, "lane": lane})
    print("Data hero berhasil ditambahkan!")

# menampilkan data
def tampilkan_data():
    print("\n=== DAFTAR DATA HERO ===")
    if data_hero == []:
        print("Belum ada data hero.")
        return

    tabel = PrettyTable()
    tabel.field_names = ["No", "Nama Hero", "Role", "Lane"]

    nomor = 1
    for hero in data_hero:
        tabel.add_row([nomor, hero["nama"], hero["role"], hero["lane"]])
        nomor = nomor + 1

    print(tabel)

# mengubah data
def ubah_data():
    print("\n=== UBAH DATA HERO ===")
    tampilkan_data()
    try:
        nomor = int(input("Masukkan nomor hero yang ingin diubah: "))
    except ValueError:
        print("Masukkan angka saja")
        return

    nama = input("Nama Hero baru : ")
    role = input("Role baru      : ")
    lane = input("Lane baru      : ")

    if nama == "":
        print("Nama tidak boleh kosong!")
        return
    if role not in daftar_role:
        print("Role tidak valid!")
        return
    if lane not in daftar_lane:
        print("Lane tidak valid!")
        return

    data_hero[nomor - 1]["nama"] = nama
    data_hero[nomor - 1]["role"] = role
    data_hero[nomor - 1]["lane"] = lane
    print("Data hero berhasil diubah!")

# menghapus data
def hapus_data():
    print("\n=== HAPUS DATA HERO ===")
    tampilkan_data()
    try:
        nomor = int(input("Masukkan nomor hero yang ingin dihapus: "))
    except ValueError:
        print("Masukkan angka saja")
        return

    hero = data_hero.pop(nomor - 1)
    print("Hero", hero["nama"], "berhasil dihapus!")


# Menu admin CRUD
def menu_admin(username):
    while True:
        print("\n=== MENU ADMIN -", username, "===")
        print("1. Tambah data hero")
        print("2. Tampilkan data hero")
        print("3. Ubah data hero")
        print("4. Hapus data hero")
        print("5. Logout")
        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            tambah_data()
        elif pilihan == "2":
            tampilkan_data()
        elif pilihan == "3":
            ubah_data()
        elif pilihan == "4":
            hapus_data()
        elif pilihan == "5":
            print("Logout berhasil")
            break
        else:
            print("Pilihan tidak valid")


# Menu user (hanya melihat data)
def menu_user(username):
    while True:
        print("\n=== MENU USER -", username, "===")
        print("1. Tampilkan data hero")
        print("2. Logout")
        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            tampilkan_data()
        elif pilihan == "2":
            print("Logout berhasil!")
            break
        else:
            print("Pilihan tidak valid")

def main():
    while True:
        print("\n=== DATA HERO MOBILE LEGENDS ===")
        print("1. Login")
        print("2. Keluar")
        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            username = login()
            if username == "":
                print("Login gagal")
            else:
                if akun[username]["role"] == "admin":
                    menu_admin(username)
                else:
                    menu_user(username)
        elif pilihan == "2":
            print("Terima kasih")
            break
        else:
            print("Pilihan tidak valid")

main()
