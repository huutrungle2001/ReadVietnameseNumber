UNITS = {0: "", 1: "nghìn", 2: "triệu", 3: "tỷ"}

DIGITS = {
    "0": "không",
    "1": "một",
    "2": "hai",
    "3": "ba",
    "4": "bốn",
    "5": "năm",
    "6": "sáu",
    "7": "bảy",
    "8": "tám",
    "9": "chín",
}


class ReadNumber:
    def __init__(self, num=""):
        self.num = "".join(num.split())
        self.output = []

    def addZeros(self):
        count = len(self.num) % 3
        count = 3 - count if count % 3 != 0 else count
        self.num = "0" * count + self.num

    def readTwo(self, b, c, hasHundred):
        if b == "0":
            if hasHundred and c == "0":
                return
            if hasHundred:
                self.output.append("lẻ")
            self.output.append(DIGITS[c])
        elif b == "1":
            self.output.append("mười")
            if c != "0":
                self.output.append(DIGITS[c])
            elif c == "5":
                self.output.append("lăm")
        else:
            self.output.append(DIGITS[b])
            self.output.append("mươi")
            if c == "1":
                self.output.append("mốt")
            elif c == "4":
                self.output.append("tư")
            elif c == "5":
                self.output.append("lăm")
            elif c != "0":
                self.output.append(DIGITS[c])

    def readThree(self, a, b, c, readZeroHundred):
        if a != "0" or readZeroHundred:
            self.output.append(DIGITS[a])
            self.output.append("trăm")
        self.readTwo(b, c, a != "0" or readZeroHundred)

    def read(self):
        self.addZeros()
        for i in range(len(self.num) // 3):
            a, b, c = self.num[i * 3 : i * 3 + 3]
            isFirstGroup = i == 0
            self.readThree(a, b, c, not isFirstGroup)
            self.output.append(UNITS[len(self.num) // 3 - 1 - i])

    def __str__(self):
        self.read()
        self.output.remove("")
        return " ".join(self.output)