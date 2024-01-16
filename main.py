import tkinter
import customtkinter
import pygame
from PIL import Image, ImageTk
from threading import *
import time
import math

# Modes: system (default), light, dark
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")


root = customtkinter.CTk()  # create CTk window like you do with the Tk window
root.title('Music Player')
root.geometry('400x480')
pygame.mixer.init()

list_of_songs = [
    'music/test.wav',
    'music/1980.wav',
    'music/test.wav',
    'music/test.wav',
]
list_of_covers = [
    'img/screensaver.png',
    'img/screensaver.png',
    'img/screensaver.png',
    'img/screensaver.png',
]

n = 0


def get_album_cover(song_name, n):
    image1 = Image.open(list_of_covers[n])
    image2 = image1.resize((250, 250))
    load = ImageTk.PhotoImage(image2)
    label1 = tkinter.Label(root, image=load)
    label1.image = load
    label1.place(relx=.19, rely=.06)

    stripped_string = song_name[6:-4]
    song_name_label = tkinter.Label(
        text=stripped_string, bg='#222222', fg='white')
    song_name_label.place(relx=.4, rely=.6)


def progress():
    a = pygame.mixer.Sound(f'{list_of_songs[n]}')
    song_len = a.get_length() * 3
    for i in range(0, math.ceil(song_len)):
        time.sleep(.3)
        progressbar.set(pygame.mixer.music.get_pos() / 1000000)


def threading():
    t1 = Thread(target=progress)
    t1.start()


def play_music():
    threading()
    global n
    current_song = n
    if n > 2:
        n = 0
    song_name = list_of_songs[n]
    pygame.mixer.music.load(song_name)
    pygame.mixer.music.play(loops=0)
    pygame.mixer.music.set_volume(.5)
    get_album_cover(song_name, n)
    n += 1


def skip_foward_button():
    play_music()


def skip_back_button():
    global n
    n -= 2
    play_music()


def volume(value):
    pygame.mixer.music.set_volume(value)


# buttons
play_button = customtkinter.CTkButton(
    master=root, text="Play", command=play_music)
play_button.place(relx=0.5, rely=0.7, anchor=customtkinter.CENTER)

skip_foward = customtkinter.CTkButton(
    master=root, text=">", command=skip_foward_button, width=2)
skip_foward.place(relx=0.75, rely=0.7, anchor=customtkinter.CENTER)

skip_back = customtkinter.CTkButton(
    master=root, text="<", command=skip_back_button, width=2)
skip_back.place(relx=0.25, rely=0.7, anchor=customtkinter.CENTER)

slider = customtkinter.CTkSlider(
    master=root, from_=0, to=1, command=volume, width=210)
slider.place(relx=0.5, rely=0.78, anchor=customtkinter.CENTER)

progressbar = customtkinter.CTkProgressBar(
    master=root, progress_color='#03fc9d', width=250)
progressbar.place(relx=0.5, rely=0.85, anchor=tkinter.CENTER)


root.mainloop()
