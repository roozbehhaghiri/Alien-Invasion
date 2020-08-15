import os
hs = open("Highscore.txt", "r+")
inputss = int(input())
lhs = int(hs.read())
if inputss > lhs:
    hs.close()
    os.remove("Highscore.txt")
    hs = open("Highscore.txt", "w")
    hs.write(str(inputss))
    hs.close()


