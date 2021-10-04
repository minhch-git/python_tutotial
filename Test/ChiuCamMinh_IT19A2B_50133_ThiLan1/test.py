def Cau2():
    data = []
    n = 0

    class MatHang:
        def __init__(self, ma, ten, sl, dg):
            self.ma_mh = ma
            self.ten_mh = ten
            self.so_luong = sl
            self.don_gia = dg

        @property
        def thanh_tien(self):
            return self.so_luong * self.don_gia

    def c23():
        f = open("IT19A2B_49527_PhanThiAnh_INP.txt", mode="r", encoding="utf-8")
        n = int(f.readline())
        for i in range(n):
            row_data = f.readline().split("|")
            mat_hang = MatHang(
                row_data[0], row_data[1], int(row_data[2]), int(row_data[3])
            )
            data.append(mat_hang)
        f.close()
        print(" Hoàn thành việc nhập dữ liệu từ file IT19A2B_49527_PhanThiAnh_INP.txt")

    def c24():
        print(" = " * 10)
        if len(data) == 0:
            print("Bạn cần nhập thông tin về mặt hàng")
        else:
            print("\nIn thong tin cac mat hang:\n")
            for i in data:
                print(
                    "{:<5}"
                    "{:<15}"
                    "{:>10}"
                    "{:>10}".format(
                        i.ma_mh, i.ten_mh, i.so_luong, i.don_gia, i.thanh_tien
                    )
                )

    def c25():
        print("*" * 10)
        matHangCaoNhat = data[0]
        for i in data:
            if i.don_gia > matHangCaoNhat.don_gia:
                matHangCaoNhat = i

        matHangCaoNhat_str = (
            matHangCaoNhat.ma_mh
            + "|"
            + matHangCaoNhat.ten_mh
            + "|"
            + str(matHangCaoNhat.so_luong)
            + "|"
            + str(matHangCaoNhat.don_gia)
            + "|"
            + str(matHangCaoNhat.thanh_tien)
            + "\n"
        )
        print(matHangCaoNhat_str)

    def c26():
        outFile = "IT19A2B_49517_PhanThiAnh_OUT.txt"
        f = open(outFile, "w")
        for item in data:
            f.write(
                f"{item.ma_mh}|{item.ten_mh}|{item.so_luong}|{item.don_gia}|{item.thanh_tien}\n"
            )
        print("> Hoàn thành việc xuất dữ liệu ra file: ", outFile)
        print("==" * 10)
