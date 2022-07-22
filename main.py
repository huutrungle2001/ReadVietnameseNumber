import re
from Regex import Regex


def main():
    fileIn = "input.txt"
    fileOut = "output.txt"
    # fileIn = input("Nhập tên file input: ")
    # fileOut = input("Nhập tên file output: ")
    regex = Regex(fileIn, fileOut)
    regex.process()
    print(f"Dữ liệu đã được xử lý và ghi vào file {fileOut}")


if __name__ == "__main__":
    main()
