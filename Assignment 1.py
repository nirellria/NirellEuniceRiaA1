"""
Assignment 1 CP1404 Programming 2
Nirell Eunice Ria
"""
from operator import itemgetter
data_list=[]
songs_file = "songs.csv"
def main():
    read_file()#reads songs.csv file
    print("Songs To Learn 1.0 - by Nirell Eunice Ria")
    number_songs = count_songs()  # counts how many songs in the csv file
    print("{} songs loaded".format(number_songs))
    while True:
        print("Menu :")
        print("L - List songs\nA - Add new song\nC - Complete a song\nQ - Quit")
        answer = input(">>>")
        answer = answer.upper()#transform all letters to be uppercase so the menu can handle uppercase and lowercase
        answer = valid_answer(answer)#checks the validity of the input
        if answer == "L":
            list_song()
        if answer == "C":
            complete_song()
        if answer == "A":
            add_song()
        elif answer == "Q":
            quit_program()
            break
    print("Thank you, bye !")