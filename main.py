from pyfiglet import Figlet
import sys

#create an instance of figlet
f = Figlet()
#print(f.getFonts())

if len(sys.argv) == 1:

    phrase = input("Input your text")
    print(f.renderText(phrase))
elif sys.argv[1] != '-f' or sys.argv[1] != '--font' or sys.argv[2] not in f.getFonts():
        sys.exit("Error try a diffrent font or put -f at the beginning of your font!!")
else:
    phrase = input("Input your text")
    f.setFont(font = sys.argv[2])


print(f.renderText(phrase))






