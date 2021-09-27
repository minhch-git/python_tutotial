# Câu 1 (2.0 điểm). Viết hàm in các số nguyên tố trong khoảng từ 30 đến 200
# import math


# def showPrime():
#     temp = 0
#     for number in range(30, 100, 1):
#         if number % 2 == 0:
#             continue
#         count = 0
#         for i in range(2, int(math.sqrt(number)) + 1, 1):
#             if number % i == 0:
#                 count = count + 1
#         if count == 0:
#             print(number)
#             temp = temp + 1

#     print(temp)


# def main():
#     showPrime()


# if __name__ == "__main__":
#     main()


# Câu 2 (6.0 điểm). Để thực hiện quản lý mặt hàng của một kho hàng,
# người ta xây dựng một class có tên là MatHang với các thông tin như sau:
# Các thuộc tính: mã mặt hàng, tên mặt hàng, số lượng, đơn giá

# Các phương thức chính: khởi tạo, sử dụng chỉ thị @properties cho phương thức có tên là thành tiền.
# Với: thành tiền = số  lượng * đơn giá
#      Câu 2.1 (1.0 điểm): Tạo một class với các thông tin được miêu tả như trên;

import os


class MatHang:
    def __init__(self, code, name, amount, price):
        self.code = code
        self.name = name
        self.amount = int(amount)
        self.price = int(price)

    def __str__(self):
        return f"code: {self.code}, name: {self.name}, amount: {self.amount}, price: {self.price}"

    @property
    def totalPrice(self):
        return self.amount * self.price


data = []


def storeData(MatHang):
    data.append(MatHang)


def showInfo(item):
    print(f"{item}, Total price: {item.totalPrice}")


# Câu 2.3 (1.5 điểm): Nhập dữ liệu vào chương trình
#    Các dữ liệu của class được lưu trong file văn bản đầu vào, có cấu trúc như sau:
#                   Mã mặt hàng|Tên mặt hàng|Số lượng|Đơn giá
#    Ví dụ một dòng thông tin cho một mặt hàng:
#                   MH01|Gạo Lài sữa|3|17000
#    Anh (chị) tự cho các thông tin của các mặt hàng với ít nhất 5 dòng thông tin cho 5 mặt hàng.
def inputValue():
    cwd = os.getcwd()
    inFileName = input("Enter file name: ")
    inFile = cwd + "/" + inFileName

    if os.path.exists(inFile) == False:
        print("Not found file name!")
        return

    f = open(inFile, "r")
    for line in f.readlines():
        items = line.split("|")
        if len(items) == 4:
            storeData(MatHang(items[0], items[1], items[2], items[3]))
    f.close()


# Câu 2.4 (1.0 điểm): Hiển thị tất cả các thông tin của các mặt hàng ra màn hình (bao gồm cả thông tin về Thành tiền).
#     Trong trường hợp chưa có thông tin của mặt hàng nào thì thông báo
#         “Bạn cần nhập thông tin về mặt hàng”.
def option2():
    if len(data) == 0:
        print("Bạn cần nhập thông tin về mặt hàng!")
        return
    for item in data:
        showInfo(item)


# Câu 2.5 (1.0 điểm): Hiển thị thông tin của mặt hàng có
#    Đơn giá cao nhất ra màn hình (bao gồm cả thông tin về Thành tiền)
def option3():
    if len(data) == 0:
        print("Bạn chưa có mặt hàng nào cả!")
        return
    maxPrice = data[0].price
    for i in range(1, len(data)):
        if data[i].price > maxPrice:
            maxPrice = data[i].price

    for item in data:
        if item.price == maxPrice:
            showInfo(item)


# Câu 2.6 (1.0 điểm): Từ các thông tin của các mặt hàng,
#     anh (chị) hãy ghi tất cả các thông tin của các mặt hàng có Số lượng từ 5 trở lên
#     (bao gồm cả thông tin về Thành tiền) ra file văn bản với
#     mỗi mặt hàng là một dòng thông tin
#     (cấu trúc tương tự file văn bản đầu vào).
def option4():
    if len(data) == 0:
        print("Bạn chưa có mặt hàng nào cả!")
        return
    cwd = os.getcwd()
    outFileName = input("Enter name output file: ")
    outFile = cwd + "/" + outFileName
    if os.path.exists(outFile) == False:
        print("Not found output file.")
        return
    f = open(outFile, "w")
    for item in data:
        f.write(
            f"{item.code}|{item.name}|{item.amount}|{item.price}|{item.totalPrice}\n"
        )


# Câu 2.2 (0.5 điểm): Tạo một menu để lựa chọn thực hiện công việc cho các câu sau:
#                    Câu 2.3, Câu 2.4, Câu 2.5 và Câu 2.6
def print_menu():
    menu_options = {
        1: "Câu 2.3: Nhập dữ liệu vào chương trình.",
        2: "Câu 2.4: Hiển thị tất cả các thông tin của các mặt hàng (bao gồm cả thông tin về Thành tiền).",
        3: "Câu 2.5: Hiển thị thông tin của mặt hàng có Đơn giá cao nhất.",
        4: "Câu 2.6: Ghi tất cả các thông tin của các mặt hàng có Số lượng từ 5 trở lên ra file",
        5: "Thoát chương trình.",
    }

    for key in menu_options.keys():
        print(key, "--", menu_options[key])


def main():
    while True:
        print_menu()
        option = int(input("Enter your choice: "))
        if option == 1:
            inputValue()
        elif option == 2:
            option2()
        elif option == 3:
            option3()
        elif option == 4:
            option4()
        elif option == 5:
            print("Thanks message before exiting")
            exit()
        else:
            print("Invalid option. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()
