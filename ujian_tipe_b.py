import os

def show_menu():
    print("""
==========================
SELAMAT DATANG DI EASYBANK 
==========================
1. Pengelolaan Rekening Saldo
2. Transaksi Perbankan
3. Riwayat Transaksi
4. Sistem Manajemen Rekening
5. Exit
""")

def input_account():
    print('\n Pengelolaan Rekening dan Saldo')
    print('1. Bikin Tabungan baru')
    print('2. Lihat Saldo Terkini')
    pilihan = input('Pilih Menu : ')
    if pilihan == '1':        
        nama = input('Masukan Nama Anda : ')
        nik = input('Masukan NIK KTP : ')
        password = input('Masukan Password Baru : ')
        with open('tabungan.txt','w') as tabungan:
            tabungan.write(f'Nama : {nama} \n')
            tabungan.write(f'Nik : {nik} \n')
            tabungan.write(f'Password : {password} \n')
            print('Berhasil Membuat Tabungan Baru')
    elif pilihan == '2':
        try:
            with open('saldo.txt','r') as lihat:
                baca = lihat.read()
                print(f'Rp.{baca}')
                print('Saldo Kosong silahkan isi') 
        except Exception as e:
            print(e)
    else:
        print('Inputan harus berupa angka!')
        main()

        
def transaksi():
    password = 'adm123'
    print('\n Transaksi Perbankan')
    print('1. Transfer antar Rekening')
    print('2. Bayar Tagihan')
    pilihan = input('Silahkan pilih menu diatas : ')
    if pilihan == '1':  
        nama = input('Masukan nama pengirim : ')              
        bank = input('Pilih Rekening Tujuan : ')
        tanggal = input('Masukan Tanggal Transaksi')
        nominal = input('Masukan Jumlah saldo : Rp. ')
        validasi = input(f'Anda yakin ingin mentransfer ke akun bank {bank} dengan nominal Rp.{nominal} (y/n) ')
        if validasi == 'y':
            password_validasi = input('Masukan Password : ')
            if password_validasi == password :
                print('Transaksi berhasil')
                with open('account.txt','w') as file:
                    file.write(f'================= \n')
                    file.write(f'RIWAYAT TRANSAKSI \n')
                    file.write(f'================= \n')
                    file.write(f'Nama Pengirim     : {nama} \n')
                    file.write(f'Tanggal transaksi : {tanggal} \n')
                    file.write(f'Nominal Transaksi : {nominal} \n')
                    file.write(f'Rekening Tujuan   : {bank} \n')
            else:
                print('password anda salah.')
                transaksi()
        elif validasi == 'n':
            print('Transaksi Gagal')
            main()

    elif pilihan == '2':  
        nama_tagihan = input('Masukan nama tagihan : ')              
        bank = input('Pilih Rekening Tujuan : ')
        tanggal = input('Masukan Tanggal Transaksi')
        nominal = input('Masukan Jumlah saldo : Rp. ')
        validasi = input(f'Anda yakin ingin mentransfer ke akun bank {bank} dengan nominal Rp.{nominal} (y/n) ')
        if validasi == 'y':
            password_validasi = input('Masukan Password : ')
            if password_validasi == password :
                print('Transaksi berhasil')
                with open('account.txt','a') as file:
                    file.write(f'================= \n')
                    file.write(f'RIWAYAT TRANSAKSI \n')
                    file.write(f'================= \n')
                    file.write(f'Nama Tagihan     : {nama_tagihan} \n')
                    file.write(f'Tanggal transaksi : {tanggal} \n')
                    file.write(f'Nominal Transaksi : {nominal} \n')
                    file.write(f'Rekening Tujuan   : {bank} \n')
            else:
                print('password anda salah.')
                transaksi()
        elif validasi == 'n':
            print('Transaksi Gagal')
            main()

    else:
        print('Inputan tidak sesuai!')
        main()

def riwayat():
    try:
        with open('account.txt','r') as riwayat:
            baca = riwayat.read()
            print(baca)
    except Exception as e:
        print(e)


def sistem():
    print('\n Sistem Manajemen Rekening')
    print('1. Buka Akun')
    print('2. Hapus Akun')
    print('3. Isi Saldo')
    inputan = input('Pilih menu diatas : ')
    if inputan == '1':
        try:
            with open('tabungan.txt','r') as buka:
                akun = buka.read()
                print(akun)
        except Exception as e:
            print(e)
    elif inputan == '2':
        try:
            validation = input('Apakah anda yakin ingin menghapus akun (y/n) : ')
            if validation == 'y':
                os.remove('tabungan.txt')
                print('Hapus Berhasil')
            elif validation == 'n':
                print('Gagal Hapus Akun')
                main()
        except Exception as e:
            print(e)
        
    elif inputan == '3':
        saldo = input('Masukan Nominal Saldo : Rp.')
        with open('saldo.txt','w') as baru:
            baru.write(saldo)
    else:
        print('Inputan Tidak Sesuai.')
        main()
def main():    
    while True:
        show_menu()
        pilihan = input('Pilih menu diatas (1-5) : ')
        if pilihan == '1':
            input_account()
        elif pilihan == '2':
            transaksi()
        elif pilihan == '3':
            riwayat()
        elif pilihan == '4':
            sistem()
        elif pilihan == '5':
            print('terimakasih, selamat datang kembali.')
            break
        else:
            print('Maaf Inputan tidak tersedia.')

if __name__ == '__main__':
    main()
        
