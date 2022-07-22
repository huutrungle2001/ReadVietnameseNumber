import re
from Reader import ReadNumber

class Regex:
    def __init__(self, fileIn, fileOut):
        self.fileIn = fileIn
        self.fileOut = fileOut
        try:
            self.fileIn = open(self.fileIn, "r")
        except FileNotFoundError:
            print("File not found")
            exit()

        # create file out
        self.fileOut = open(self.fileOut, "w")

    # read file in, replace all number with number in Vietnamese
    def process(self):
        for line in self.fileIn:
            # extract number from line
            numbers = re.findall(r"[-+]?\d*\.\d+|\d+", line)
            # convert number to Vietnamese
            text = []
            for number in numbers:
                if "." in number:
                    readNumber = number.split(".")
                    integer = str(ReadNumber(readNumber[0]))
                    decimal = str(ReadNumber(readNumber[1]))
                    line = line.replace(number, integer + " phẩy " + decimal)
                else:
                    line = line.replace(number, str(ReadNumber(number)), 1)
                    text.append(str(ReadNumber(number)))
            self.fileOut.write(line)
        self.fileIn.close()
        self.fileOut.close()