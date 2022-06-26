import os

def show_cities(list_cities):
    print('Daftar kota yang berhasil diextract dari database...')
    city_number = 1
    for element in list_cities[1:]:
        print(f'{city_number}. {element}')
        city_number = city_number + 1

def show_plot_mode():
    print('\nPilih mode plot:')
    print('A. Plot 1 kota')
    print('B. Plot 3 kota')
    print('C. Plot semua')
    print('D. Selesai dan keluar ')

def clear_screen():
    if(os.name == 'posix'):
        os.system('clear')
    # else screen will be cleared for windows
    else:
        os.system('cls')

def show_welcome_message():
    print("Welcome to the Weather Report App v.1.0.0")