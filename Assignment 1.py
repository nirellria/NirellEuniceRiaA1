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
        if answer == "Q":
            quit_program()
            break
    print("Thank you, bye !")

def read_file():
    file = open(songs_file, "r")
    for data in file.readlines():
        data = data.strip()#delete the white spaces within the csv file
        data = data.split(",")
        data_list.sort(key=itemgetter(1, 2))#list the songs by their Artist name then by their released year
        data_list.append(data)#adds the edited version of the csv file (data) to the data_list
    file.close()

def count_songs():
    songs = 0
    for song in range(len(data_list)):
        songs += 1
    return songs

def valid_answer(choice):
    while choice !="L" and choice !="A" and choice !="C" and choice!="Q" : #program will keep on asking for other input until the user give the right input
        print("Invalid menu choice")
        print("Menu :")
        print("L - List songs\nA - Add new song\nC - Complete a song\nQ - Quit")
        choice = input(">>>")
        choice = choice.upper()
    return choice

def list_song():
    learned = 0 #start the variable learned as 0
    notlearned = 0 #start the variable notlearned as 0
    for index, data in enumerate(data_list):
        if data[3] == "y":
            print(index,"* {:40s} - {:30s} ({})".format(data[0], data[1], data[2]))
            notlearned += 1
        else:
            print(index, "{:42s} - {:30s} ({})".format(data[0], data[1], data[2]))
            learned += 1
    print("{} songs learned, {} songs still need to learn".format(learned,notlearned))

def complete_song():
    songs_amount=int(count_songs())#counts the amount of song at the moment
    print("Enter a number of a song to mark as learned")
    while True:
        try:
            respond = int(input(">>>"))
            if respond >= songs_amount :
                print ("Invalid song number")
            elif respond < 0 :
                print ("Number must be >= 0")
            else:
                break
        except ValueError:
            print("Invlaid input; enter a valid number")

    for index, data in enumerate(data_list):
        if index == respond:
            if data[3] == "y":
                data[3] = "n"
                print("{} by {} learned".format(data[0], data[1]))
            else :
                print("You have already learned {}".format(data[0]))

main()