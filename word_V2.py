import random
from select import select

print("---------------------------------------------------------------")
print("JOM TEKA PERKATAAN: PERKAKASAN KOMPUTER & BAHASA PENGATURCARAAN")
print("---------------------------------------------------------------")

#Input nama
nama=str(input("Masukkan nama anda: "))
umur=int(input("Masukkan umur anda: "))

#Wujudkan perkataan yang perlu diteka
words_computer = ['cpu', 'tetikus', 'papan kekunci', 'ram', 'monitor', 'kabel vga', 'speaker', 'headphone', 'cdrom', 'disket', 'pencetak']
words_languages = ['cobol', 'java', 'ruby', 'python', 'c#', 'c++', 'c', 'assembly', 'perl', 'php', 'javascript', 'pascal']

wordsChoices = {
    1: words_computer,
    2: words_languages,
}

#Perkataan yang dipilih secara random
word = " "



#Untuk memaparkan ruang kosong(mengikut bilangan perkataan)
spaces = ['_']* len(word)

def get_letter_position(guess, word, spaces):
    index = -2
    while index != -1:
        if guess in word:
            index = word.find(guess) #Finds index with the first occurance of the letter
            removed_character ='*'
            word = word[:index] + removed_character + word[index+1:] #If 'i' is inputted, Dish -> D*sh
            spaces[index] = guess #Reveals the the correct guess
        else:
            index = -1
     
    return (word, spaces) #returns the new word and spaces


def win_check():
    #Semak ruang kosong dalam perkataan
    for i in range(0, len(spaces)):
        if spaces[i] == '_':
            return -1
     
    return 1

def game_loop(word):
    global spaces

    num_turns = len(word)
    for i in range(-1, num_turns): #tries = length of word
        guess = input('\nMasukkan huruf anda:').lower()
        if guess == '':
            print('Maaf, abjad pilihan tiada dalam senarai.')

        elif guess in word:
            word, spaces = get_letter_position(guess, word, spaces)
            for x in spaces:
                print(x, end=" ")
            print()
        else:
            print('Maaf, abjad pilihan tiada dalam senarai.')
     
        if win_check() == 1:
            print('Tahniah ' +nama+'....Anda Telah Berjaya.  :-)\n')
            #break
            return 1
     
        print(nama,',anda mempunyai '+str(num_turns - i)+' peluang lagi.')
        print()

    #Output sekiranya peluang habis
    print(nama, ", anda telah menggunakan semua peluang. D:\nCuba lagi pada lain kali!\n")
    return 1

#Main loop
rungame = True
selection = None
while True:
    if rungame:
        #Pilihan menu
        while True:
            print("\nSila pilih menu:\n1.Perkakasan Komputer\n2.Bahasa Pengaturcaraan")
            themeChoice = input(">")
            themeChoice.strip()
            if themeChoice.isnumeric():
                themeChoice = int(themeChoice)
                if themeChoice in wordsChoices.keys():
                    selection = wordsChoices[themeChoice]
                    break
                else: 
                    print("Pilihan tersebut tidak wujud, sila pilih tema lain.") #Paparan mesej input tidak wujud
            else:
                print("Input tidak sah, hanya input jenis nombor diterima.") # Paparan mesej jika masukkan input selain nombor
            print("")

        #Perkataan yang dipilih secara random
        word = random.choice(selection)
        #print(word)

        #Untuk memaparkan ruang kosong(mengikut bilangan perkataan)
        spaces = ['_']* len(word)
        game_loop(word)

    else:
        print("Baiklah, terima kasih kerana cuba bermain! (Tekan butang ENTER untuk keluar)")
        input("")
        break

    #Pilihan Teruskan atau keluar program
    repeatCheck = input("Adakah kamu ingin main sekali lagi? (Y/N)> ")
    repeatCheck = repeatCheck.lower()
    if repeatCheck == 'y' or repeatCheck == 'Y':
        rungame = True

    elif repeatCheck == 'n' or repeatCheck == 'N':
        rungame = False

    else:
        rungame = False
