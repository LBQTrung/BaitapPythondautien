dtb = float(input("Nhap diem trung binh: "))
if (dtb >= 0):
    if (dtb >= 9):
        print("Xuat sac")
    elif (dtb >= 8):
        print("Gioi")
    elif (dtb >= 7):
        print("Kha")
    elif (dtb >= 5):
        print("Trung binh")
    else:
        print("Yeu")
else:
    print("Nhap diem khong hop le")

