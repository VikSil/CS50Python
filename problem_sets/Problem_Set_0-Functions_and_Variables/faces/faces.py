def convert(emoji):
    #do something to convert emoji to a pictogram
    output = emoji.replace(":)", "\U0001F642").replace(":(","\U0001F641")
    return(output)

def main():

    mood = input("Talk to me in emoji!\n")
    print(convert(mood))


main()