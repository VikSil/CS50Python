from pyfiglet import Figlet
import sys
import random

def main():
    figlet = Figlet()
    fontlist = figlet.getFonts()


    usrfont = 'temp'

    #user did not provide a font
    if len(sys.argv) == 1:
        usrfont = fontlist[random.randint(1,424)]
    elif len(sys.argv) == 3:
        if (sys.argv[1] == "-f" or sys.argv[1] == "-font") and sys.argv[2] in fontlist:
            usrfont = sys.argv[2]
        else:
            sys.exit("Incorect arguments, will halt")
    else:
        sys.exit("Too many argument, will halt.")


    #print(fontlist)
    #print(len(fontlist))
    usrtext = input("Input: ")

    try:
        if usrfont in fontlist:
            figlet.setFont(font=usrfont)
            print(figlet.renderText(usrtext))
    except:
        sys.exit("Something unexpected happened")



if __name__ == "__main__":
    main()