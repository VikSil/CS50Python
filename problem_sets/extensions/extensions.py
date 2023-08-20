def main():
    filename = input("What is the file name (with extension)?\n").strip().lower()
    ext = filename.rpartition(".")[2]
    match ext:
        case "gif" |  "png":
            print ("image/"+ext)
        case "pdf" | "zip" :
            print("application/"+ext)
        case "jpeg" | "jpg":
            print("image/jpeg")
        case "txt":
            print("text/plain")
        case _:
            print ("application/octet-stream")

main()

"""
.gif
.jpg
.jpeg
.png
.pdf
.txt
.zip

"""