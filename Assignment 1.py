#listing songs
def list_song(songlist):
    i = 1
    not_learned = 0
    learned = 0

    #loop through the list
    for row in songlist:
        #check and count number of songs learned (n) and not learned(y)
        #unlearned songs are marked with "*"
        if row[3] == "n":
            learned = learned + 1
            mark = " "
        else:
            not_learned = not_learned + 1
            mark = "*"

        #format the list of items with equal gaps
        print("{}. {} {:35}- {:30}({})".format(i, mark, row[0], row[1], row[2]))
        i = i + 1
    print("\n{} songs learned, {} songs still to learn".format(learned, not_learned))


#adding song in list
def add_song(songlist):
    #get song title
    title = input("Title: ").title()
    while title == "":
        print("Input cannot be blank\nPlease enter a title")
        title = input("Title: ").title()

    #get song artist
    artist = input("Artist: ").title()
    while artist == "":
        print("Input cannot be blank\nPlease enter an artist name")
        artist = input("Artist: ").title()

    #get song year
    check = 0
    while check == 0:
        try:
            year = int(input("Year: "))
            #Error checking, ensure year is not < 0
            if year <= 0:
                print("Number must be > 0")
            #if no error, create new song as a list
            else:
                new_song = [title, artist, year, "y"]
                check = 1
                songlist.append(new_song)
                return sorted(songlist, key = lambda element: (element[1], element[0]))

        except ValueError:
            print("Invalid input!\nPlease enter a valid number")
    #add the new song into the song list


#completing songs
def complete_song(songlist):
    not_learned = 0
    learned = 0
    for row in songlist:
        #check and count number of songs learned and not learned
        if row[3] == "n":
            learned = learned + 1
        else:
            not_learned = not_learned + 1
    #if there are no more unlearned songs, stop the function and return to main()
    if not_learned == 0:
        print("No more songs to learn!")
        return sorted(songlist, key = lambda element: (element[1], element[0]))

    print("Enter the number of a song to mark as learned")
    #the -1 is so that the it'll access the correct list as count starts from 0
    number = int(input(">>>")) - 1

    #ensure that the number song is not over or below songlist
    while number < 0 or number > len(songlist) - 1:
        print("Invalid song number")
        number = int(input(">>>")) - 1

    if songlist[number][3] == "n":
        print("You have already learned {}".format(songlist[number][0]))
    else:
        songlist[number][3] = "n"
        print("{} by {} learned".format(songlist[number][0], songlist[number][1]))

    return sorted(songlist, key = lambda element: (element[1], element[0]))


def main():
    #importing file
    import csv

    #storing it into a list so there is no need for repeated reading of file
    songlist = []
    num_of_songs = 0
    with open('songs.csv') as file:
        reader = csv.reader(file)
        for row in reader:
            songlist.append(row)
            num_of_songs = num_of_songs + 1
    #sorting list by artist then song name
    songlist = sorted(songlist, key = lambda element: (element[1], element[0]))
    print("Welcome Zhen Hui\n{} songs loaded".format(num_of_songs))

    #Menu of choices for user
    menu = """Menu:
    L - List songs
    A - Add new song
    C - Complete a song
    Q - Quit"""
    print(menu)
    choice = str(input(">>>")).upper()

    #loop for user to continue until quit
    while choice != "Q":
        if choice == "L":
            list_song(songlist)

        elif choice == "A":
            songlist = add_song(songlist)

        elif choice == "C":
            songlist = complete_song(songlist)

        #Error checking to ensure user do not input choice out of menu
        else:
            print("Invalid choice")
        print(menu)

        choice = str(input(">>>")).upper()

    with open('songs.csv', 'w') as file:
        writer = csv.writer(file, lineterminator='\n')
        writer.writerows(songlist)
    print("{} songs saved to songs.csv\nHave a nice day!".format(len(songlist)))
main()