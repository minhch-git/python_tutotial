"""
Author: chiu cam minh
Date: 30/01/2021
Program: Cau02_IT19A2B_ChiuCamMinh_50133.py
Problem:
    Anh (chị) hãy sử dụng ngôn ngữ lập trình Python để thực hiện bài thi.
    Câu 2 (6.0 điểm). Để thực hiện quản lý mặt hàng của một kho hàng, người ta xây dựng một class có tên là MatHang với các thông tin như sau:
    Các thuộc tính: mã mặt hàng, tên mặt hàng, số lượng, đơn giá
    Các phương thức chính: khởi tạo, sử dụng chỉ thị @properties cho phương thức có tên là thành tiền.
    Với: thành tiền = số  lượng * đơn giá
        Câu 2.1 (1.0 điểm): Tạo một class với các thông tin được miêu tả như trên;
        Câu 2.2 (0.5 điểm): Tạo một menu để lựa chọn thực hiện công việc cho các câu sau:
            Câu 2.3, Câu 2.4, Câu 2.5 và Câu 2.6
        Câu 2.3 (1.5 điểm): Nhập dữ liệu vào chương trình
            Các dữ liệu của class được lưu trong file văn bản đầu vào, có cấu trúc như sau:
                            Mã mặt hàng|Tên mặt hàng|Số lượng|Đơn giá
            Ví dụ một dòng thông tin cho một mặt hàng:
                            MH01|Gạo Lài sữa|3|17000
            Anh (chị) tự cho các thông tin của các mặt hàng với ít nhất 5 dòng thông tin cho 5 mặt hàng.
        Câu 2.4 (1.0 điểm): Hiển thị tất cả các thông tin của các mặt hàng ra màn hình 
            Trong trường hợp chưa có thông tin của mặt hàng nào thì thông báo
                “Bạn cần nhập thông tin về mặt hàng”.
        Câu 2.5 (1.0 điểm): Hiển thị thông tin của mặt hàng có Đơn giá cao nhất ra màn hình (bao gồm cả thông tin về Thành tiền)
        Câu 2.6 (1.0 điểm): Từ các thông tin của các mặt hàng, anh (chị) hãy ghi tất cả các thông tin của các mặt hàng có Số lượng từ 5 trở lên (bao gồm cả thông tin về Thành tiền) ra file văn bản với mỗi mặt hàng là một dòng thông tin (cấu trúc tương tự file văn bản đầu vào).
Solution:
"""


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


def option23():
    """Câu 2.3 Nhập dữ liệu vào chương trình"""
    inFile = "IT19A2B_ChiuCamMinh_50133_inp.txt"
    f = open(inFile, "r", encoding="utf-8")
    for line in f.readlines():
        items = line.split("|")
        if len(items) == 4:
            storeData(MatHang(items[0], items[1], items[2], items[3]))
    f.close()
    print("==" * 10)
    print("> Hoàn thành việc nhập dữ liệu từ file: ", inFile)
    print("==" * 10)


def option24():
    """Câu 2.4 Hiển thị tất cả các thông tin của các mặt hàng"""
    print("==" * 10)
    if len(data) == 0:
        print("Bạn cần nhập thông tin về mặt hàng!")
        print("==" * 10)
        return

    for item in data:
        showInfo(item)
    print("==" * 10)


def option25():
    """Câu 2.5: Hiển thị thông tin của mặt hàng có Đơn giá cao nhất"""
    print("==" * 10)
    if len(data) == 0:
        print("Bạn chưa có mặt hàng nào cả!")
        print("==" * 10)
        return
    maxPrice = data[0].price
    for i in range(1, len(data)):
        if data[i].price > maxPrice:
            maxPrice = data[i].price

    for item in data:
        if item.price == maxPrice:
            showInfo(item)
    print("==" * 10)


def option26():
    """Câu 2.6 Ghi tất cả các thông tin của các mặt hàng có Số lượng từ 5 trở lên vào file"""
    outFile = "IT19A2B_ChiuCamMinh_50133_out.txt"
    print("==" * 10)
    if len(data) == 0:
        print("Xuất file thất bại, Bạn chưa có mặt hàng nào!")
        print("==" * 10)
        return

    f = open(outFile, "w")
    for item in data:
        f.write(
            f"{item.code}|{item.name}|{item.amount}|{item.price}|{item.totalPrice}\n"
        )
    print("> Hoàn thành việc xuất dữ liệu ra file: ", outFile)
    print("==" * 10)


def print_menu():
    menu_options = {
        1: "Nhập dữ liệu vào chương trình từ file.",
        2: "Hiển thị tất cả các thông tin của các mặt hàng.",
        3: "Hiển thị thông tin của mặt hàng có Đơn giá cao nhất.",
        4: "Ghi tất cả các thông tin của các mặt hàng có Số lượng từ 5 trở lên ra file",
        5: "Thoát chương trình.",
    }

    for key in menu_options.keys():
        print(key, "--", menu_options[key])


def main():
    while True:
        print_menu()
        option = int(input("Bạn chọn công việc: "))
        if option == 1:
            option23()
        elif option == 2:
            option24()
        elif option == 3:
            option25()
        elif option == 4:
            option26()
        elif option == 5:
            print("Good bye!!!")
            exit()
        else:
            print("Invalid option. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()
