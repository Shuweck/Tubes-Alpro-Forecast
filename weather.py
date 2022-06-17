import csv
import matplotlib.pyplot as plt

# show welcome message
print("Welcome to Weather Report")
# this is to show that application is running
# the message should contain the name of the application, creator name & email


# interact with the user

# ask user to select one database (csv) to load, for now only one csv -- "Sample cuaca.csv"


# give them options on what to choose, it's good to show what the application actually does

# list all available database
print('1. db1.csv')
print('2. db2.csv')
print('3. db3.csv')

pilihan_db = int(input("\nSelect the database to load: "))

if pilihan_db == 2:
    print('saat ini db2.csv belum tersedia')
    exit()

if pilihan_db == 3:
    print('saat ini db3.csv belum tersedia')
    exit()

# if the application reaches this line, meaning pilihan_db == 1
# that means, now load db1.csv

file = open('C:\Workspace\Alpro\Tugas matkul alpro\Tubes\database\db1.csv','r')

csvreader = csv.reader(file)

# Extracting field names
header = []
header = next(csvreader)


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
city_number = 1
for element in header[1:]:
    print(f'{city_number}. {element}')
    city_number = city_number + 1


print('\nPilih mode plot:')
print('A. Plot 1 kota')
print('B. Plot 3 kota')
print('C. Plot semua')

mode = input('\nPilihan anda (A/B/C): ')

if mode == 'A':
    pilihan_single = int(input('Pilih satu kota: '))
    if pilihan_single == 1:
        plt.plot(waktu, temp_chugwater)
        plt.xlabel('Waktu')
        plt.ylabel('Suhu')
        plt.title('Suhu Cuaca di Chugwater')
        plt.show()
        print('\nSuhu Cuaca di Chugwater berhasil ditampilkan')
    elif pilihan_single == 2:
        plt.plot(waktu, temp_jeddah)
        plt.xlabel('Waktu')
        plt.ylabel('Suhu')
        plt.title('Suhu Cuaca di jeddah')
        plt.show()
        print('\nSuhu Cuaca di jeddah berhasil ditampilkan')
    elif pilihan_single == 3:
        plt.plot(waktu, temp_gothenburg)
        plt.xlabel('Waktu')
        plt.ylabel('Suhu')
        plt.title('Suhu Cuaca di Gothenburg')
        plt.show()
        print('\nSuhu Cuaca di Gothenburg berhasil ditampilkan')
    elif pilihan_single == 4:
        plt.plot(waktu, temp_tokyo)
        plt.xlabel('Waktu')
        plt.ylabel('Suhu')
        plt.title('Suhu Cuaca di Tokyo')
        plt.show()
        print('\nSuhu Cuaca di Tokyo berhasil ditampilkan')
    elif pilihan_single == 5:
        plt.plot(waktu, temp_bandung)
        plt.xlabel('Waktu')
        plt.ylabel('Suhu')
        plt.title('Suhu Cuaca di Bandung')
        plt.show()
        print('\nSuhu Cuaca di Bandung berhasil ditampilkan')
elif mode == 'B':
    print('Saat ini belum bisa menampilkan 3 kota')
    pass
else:
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
    print('Suhu cuaca berhasil ditampilkan')