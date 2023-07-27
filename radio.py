import threading
import time
import vlc

channels = []


def thread(my_func):
    def wrapper(*args, **kwargs):
        my_thread = threading.Thread(target=my_func, args=args, kwargs=kwargs)
        my_thread.start()
    return wrapper


@thread
def play_radio(url):
    global channels
    play_station = vlc.MediaPlayer(url)
    play_station.play()
    while True:
        command = input("Для остановки введите команду (stop) или для смены волны введите ее номер\nПоле для ввода: ")
        if command == 'stop':
            play_station.stop()
            break
        elif command.isdigit():
            play_station.stop()
            play_music(channels[int(command)-1])
        else: continue


def play_music(radio_station):
    time.sleep(1)
    mass = radio_station.split(' | ')
    station_url = mass[1]
    name_station = mass[0]
    print(name_station)
    play_radio(station_url)


def main():
    global channels
    stations_txt = open("stations.txt", "r")
    # считываем все строки
    lines = stations_txt.readlines()
    # итерация по строкам
    for line in lines:
        channels.append(line.strip())

    counter = 1
    for channel in channels:
        mass_channel = channel.split(' | ')
        print(f'{counter} -> {mass_channel[0]}')
        counter += 1

if __name__ == '__main__':
    main()
    st_number = 1
    play_music(channels[st_number-1])
