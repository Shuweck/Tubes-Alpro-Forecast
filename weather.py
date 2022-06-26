import os
import csv
import time
import matplotlib.pyplot as plt
from fungsi import show_cities, show_plot_mode, clear_screen, show_welcome_message

# database location
curr_dir = os.path.dirname(__file__)
db_dir = os.path.join(curr_dir, 'database')

# show welcome message
# print("Welcome to Weather Report")
clear_screen()
show_welcome_message()

# list all available database
print('\nDaftar database yang tersedia...')
print('1. db1.csv')
print('2. db2.csv')
print('3. db3.csv')

# getting user input for which database to use
try:
    pilihan_db = int(input("\nPilih database yang akan dimuat (1/2/3): "))

    if pilihan_db == 1:
        db_name = os.path.join(db_dir, 'db1.csv')
        print('database (db1.csv) telah dipilih...')

    if pilihan_db == 2:
        db_name = os.path.join(db_dir, 'db2.csv')
        print('saat ini db2.csv belum tersedia')

    if pilihan_db == 3:
        db_name = os.path.join(db_dir, 'db3.csv')
        print('saat ini db3.csv belum tersedia')

except ValueError:  # exception raised if wrong input is chosen
    print('[error] pilih antara (1), (2) atau (3)')
    raise
except:             # exception for others
    print('[error] program error saat memilih database. Keluar dari program...')
    raise


# if the application reaches this line, meaning pilihan_db == 1
# that means, now load db1.csv
print('mencoba loading database...')
try:
    file = open(db_name,'r')
except FileNotFoundError:
    print('[error] file tidak tersedia...')
    raise
else:
    print(f'Database {db_name} berhasil dimuat...')
    time.sleep(3)

# mencoba read csv dan cek apakah file benar
csvreader = None
try:
    csvreader = csv.reader(file)
except:
    print('[error] gagal dalam import csv, kemungkinan format data tidak benar')
    raise

# Extracting field names
header = []
try:
    header = next(csvreader)
except EOFError:
    print('[error] file sudah dibaca habis, tidak ada data lagi...')
    raise

# Extracting row
rows = []
for row in csvreader:
    rows.append(row)

file.close()

# create list for each column
temp_chugwater = []
temp_jeddah = []
temp_gothenburg = []
temp_tokyo = []
temp_bandung = []
waktu = []

for row in rows:
    waktu.append(int(row[0]))
    temp_chugwater.append(int(row[1]))
    temp_jeddah.append(int(row[2]))
    temp_gothenburg.append(int(row[3]))
    temp_tokyo.append(int(row[4]))
    temp_bandung.append(int(row[5]))

# now that the data is loaded into header and rows, update the users
# on what are inside the headers and rows
print('Data has been successfully loaded')
print('\nHere are the cities that are available to plot: ')
# city_number = 1
# for element in header[1:]:
#     print(f'{city_number}. {element}')
#     city_number = city_number + 1



# print('\nPilih mode plot:')
# print('A. Plot 1 kota')
# print('B. Plot 3 kota')
# print('C. Plot semua')



# plotting
plot = True
while plot: 
    # clear screen first
    clear_screen()

    # show welcome message
    show_welcome_message()

    # daripada print banyak baris, kita masukin fungsi show_cities
    show_cities(header)

    # daripada print banyak line, masukin fungsi show_plot_mode
    show_plot_mode()

    try:
        mode = input('\nPilihan anda (A/B/C/D): ')
    except ValueError:
        print('[error] pastikan pilihan anda antara A/B/C/D')
        continue

    if mode.upper() == 'A':
        # selalu gunakan try-except untuk user input
        try:
            pilihan_single = int(input('Pilih satu kota (1/2/3/dst): '))
        except ValueError:
            print('[error] pastikan pilihan anda berupa angka index yang tertera...')
            raise

        # try-except untuk plotting mode-A bisa digabung
        try:
            if pilihan_single == 1:
                plt.plot(waktu, temp_chugwater)
                plt.xlabel('Waktu')
                plt.ylabel('Suhu')
                plt.title('Suhu Cuaca di Chugwater')
                plt.show()
                print('\nSuhu Cuaca di Chugwater berhasil ditampilkan...kembali ke menu plot...')
                time.sleep(3)
            elif pilihan_single == 2:
                plt.plot(waktu, temp_jeddah)
                plt.xlabel('Waktu')
                plt.ylabel('Suhu')
                plt.title('Suhu Cuaca di jeddah')
                plt.show()
                print('\nSuhu Cuaca di jeddah berhasil ditampilkan...kembali ke menu plot...')
                time.sleep(3)
            elif pilihan_single == 3:
                plt.plot(waktu, temp_gothenburg)
                plt.xlabel('Waktu')
                plt.ylabel('Suhu')
                plt.title('Suhu Cuaca di Gothenburg')
                plt.show()
                print('\nSuhu Cuaca di Gothenburg berhasil ditampilkan...kembali ke menu plot...')
                time.sleep(3)
            elif pilihan_single == 4:
                plt.plot(waktu, temp_tokyo)
                plt.xlabel('Waktu')
                plt.ylabel('Suhu')
                plt.title('Suhu Cuaca di Tokyo')
                plt.show()
                print('\nSuhu Cuaca di Tokyo berhasil ditampilkan...kembali ke menu plot...')
                time.sleep(3)
            elif pilihan_single == 5:
                plt.plot(waktu, temp_bandung)
                plt.xlabel('Waktu')
                plt.ylabel('Suhu')
                plt.title('Suhu Cuaca di Bandung')
                plt.show()
                print('\nSuhu Cuaca di Bandung berhasil ditampilkan...kembali ke menu plot...')
                time.sleep(3)
            else:
                print('\nKota nomor ini tidak tersedia...kembali ke menu plot...')
                time.sleep(3)
                continue
        except:
            print('[error] gagal visualisasi data...coba ulangi')
            continue

    elif mode.upper() == 'B':
        print('Saat ini belum bisa menampilkan 3 kota')
        pass
    elif mode.upper() == 'C':
        # try-except untuk plot mode-C jg bisa digabung
        try:
            plt.plot(waktu,temp_chugwater, label = 'Chugwater') 
            plt.plot(waktu,temp_jeddah, label = 'Jeddah')
            plt.plot(waktu,temp_gothenburg, label = 'Gothenburg')
            plt.plot(waktu,temp_tokyo, label = 'Tokyo')
            plt.plot(waktu,temp_bandung, label = 'Bandung')
            plt.legend()
            plt.xticks(waktu)
            plt.xlabel('Jam')
            plt.ylabel('Suhu (C)')
            plt.show()
            print('Suhu cuaca berhasil ditampilkan...kembali ke menu plot...')  
            time.sleep(3) 
        except:
            print('[error] gagal visualisasi data...coba ulangi...')
            continue  
    elif mode.upper() == 'D':
        plot = False
    else:
        print('Pilihan tidak tersedia') 

# program ends
clear_screen()
print('Terima kasih telah menggunakan aplikasi kami')
print('Tertanda: Ahmad Rafiano Software Company')
