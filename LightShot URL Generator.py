import random, time, webbrowser, os

os.system('mode con: cols=45 lines=10')

def urlGenerator():
    siteExt = ""

    lower = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    number = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    for i in range (2):
        siteExt += random.choice(lower)
    for x in range (4):
        siteExt += random.choice(number)

    return siteExt


def siteDirector():
    print ("Generating and opening bullshit images...\n\n")

    for i in range(15):

        url = "https://prnt.sc/" + urlGenerator()
        time.sleep(.3)
        webbrowser.open(url)
    finishProgram()


def finishProgram():
    print ("Finished opening random bullshit images\nGo again? (Y/N)\n")
    if input().lower() == "y" or input().lower() == "yes":
        siteDirector()
    else:
        print ("Alright, go fuck yourself.")

if __name__ == "__main__":
    siteDirector()