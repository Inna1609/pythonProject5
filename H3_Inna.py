note = []
def final():
    answer = input()
    if answer == 'add':
        while True:
            answer = str(input("Write your note. When you finish press 'enter'"))
            if answer == '6':
                exit()
    elif answer == 'earliest':
        print(note)
        quit()
    elif answer == 'latest':
        note.reverse()
        print(note)
        quit()
    elif answer == 'longest':
        print(sorted(note, key=len)[::-1])
        quit()
    elif answer == 'shortest':
        print(sorted(note, key=len)[0::])
        quit()
    elif answer == '6':
        exit()
    else:
        print("Ooops...try again!)")
        return final()
print("This is program for writing notes. You could choose command."
          "\nYou could write note using command 'add'. \nFor reveiwing from earliest - 'earliest'. "
          "\nFor reveiwing from latest - 'latest'. \nFor reveiwing from longest - 'longest'. "
          "\nFor reveiwing from shortest - 'shortest'. For exit : '6'")

