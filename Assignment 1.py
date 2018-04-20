"""
Ong Zhen Hui
This program reads a song list from the CSV, which allows a user to keep track of which song they wish to learn and
which songs they have completed. Each song contains the "title", "artist", and "year". The user can choose to add
a song in the list, and which songs to complete.
The song list is sorted by the artist then by the title.
Completed songs cannot be changed from learned to required.

https://github.com/OngZhenHui/CP1404_A1_Ong_Zhen_Hui
"""

"""
def list_song(songlist):
    count number of learned songs and not learned songs
    print sorted list of songs
    print number of learned songs and not learned songs
"""
#list songs
def list_song(songlist):
    i = 1
    not_learned = 0
    learned = 0

    #loop through the list
    for row in songlist:
        #check and count number of songs learned (n) and not learned(y)
        #mark unlearned songs with "*"
        if row[3] == "n":
            learned = learned + 1
            mark = " "
        else:
            not_learned = not_learned + 1
            mark = "*"

        #format and print the list of items with equal gaps
        print("{}. {} {:35}- {:30}({})".format(i, mark, row[0], row[1], row[2]))
        i = i + 1
    print("\n{} songs learned, {} songs still to learn".format(learned, not_learned))

"""
def add_song():
    get title from user
    error check user input
    
    get artist from user
    error check user input

    get year from user
    error check user input
    
    add new song to the list
    return new list
"""
#create function to add song in list
def add_song(songlist):
    #get song title from user
    title = input("Title: ").title()
    import string
    #error check that title is not blank
    while title == "":
        print("Input cannot be blank\nPlease enter a title")
        title = input("Title: ").title()

    #get song artist
    artist = input("Artist: ").title()
    #error check that title is not blank
    while artist == "":
        print("Input cannot be blank\nPlease enter an artist name")
        artist = input("Artist: ").title()

    #get song year
    check = 0
    while check == 0:
        try:
            year = int(input("Year (YYYY): "))
            #Error checking, ensure year is not too low or over current year
            if year <= 1500 or year >2018:
                print("Year must be between 1500 and current year (2018)")
            #if no error, create new song as a list
            else:
                new_song = [title, artist, year, "y"]
                check = 1
                songlist.append(new_song)
                return sorted(songlist, key = lambda element: (element[1], element[0]))

        #Error check for value error
        except ValueError:
            print("Invalid input!\nPlease enter a valid number")
    #add the new song into the song list

"""
def complete_song():
    count number of learned and unlearned songs
    if all songs are learned
        print "No more songs to learn!"
    
    get song number from user
    error check song numnber is within songlist range
    if song number is learned
        print "you have already learned that song"
    if song number is unlearned
        change song from unlearned to learned
    update and return songlist
"""
#create function for completing songs
def complete_song(songlist):
    not_learned = 0
    learned = 0
    for row in songlist:
        #check and count number of songs learned and not learned
        if row[3] == "n":
            learned = learned + 1
        else:
            not_learned = not_learned + 1
    #if there are no more unlearned songs, stop the function and return
    if not_learned == 0:
        print("No more songs to learn!")
        return sorted(songlist, key = lambda element: (element[1], element[0]))

    print("Enter the number of a song to mark as learned")

    check = 0
    while check == 0:
        try:
            number = int(input(">>>")) - 1
            #Error check that number song is not over or below songlist
            if number < 0 or number > len(songlist) - 1:
                print("Invalid song number")

            #Error check to see if song was already completed
            elif songlist[number][3] == "n":
                print("You have already learned {}".format(songlist[number][0]))
                return songlist

            #Change song from unlearned to complete
            else:
                songlist[number][3] = "n"
                print("{} by {} learned".format(songlist[number][0], songlist[number][1]))

                return sorted(songlist, key=lambda element: (element[1], element[0]))
        #Error check for value error
        except ValueError:
            print("Invalid input")


"""
open and read csv file
sort the list by artist then title
print menu
get user choice
error check user input
call function according to user input
overwrite csv file when user quits
"""

#import file
import csv

#store it into a list so there is no need for repeated reading of file
songlist = []
num_of_songs = 0
with open('songs.csv') as file:
    reader = csv.reader(file)
    for row in reader:
        songlist.append(row)
        num_of_songs = num_of_songs + 1
#sort list by artist then song name
songlist = sorted(songlist, key = lambda element: (element[1], element[0]))
print("Welcome Zhen Hui\n{} songs loaded".format(num_of_songs))

#Print menu
menu = """Menu:
L - List songs
A - Add new song
C - Complete a song
Q - Quit"""
print(menu)
choice = str(input(">>>")).upper()

#loop for user to continue until quit
while choice != "Q":
    #call list function
    if choice == "L":
        list_song(songlist)

    #call add song function
    elif choice == "A":
        songlist = add_song(songlist)

    #call complete song function
    elif choice == "C":
        songlist = complete_song(songlist)

    #Error checking to ensure user do not input choice out of menu
    else:
        print("Invalid choice")
    print(menu)
    choice = str(input(">>>")).upper()

#overwrite current csv file
with open('songs.csv', 'w') as file:
    writer = csv.writer(file, lineterminator='\n')
    writer.writerows(songlist)
print("{} songs saved to songs.csv\nHave a nice day!".format(len(songlist)))
