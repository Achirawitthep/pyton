def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "ไม่สามารถหารด้วยศูนย์ได้"
    return x / y

def power(x, y):
    return x ** y

def main():
    while True:
        print("\n=== เครื่องคิดเลข ===")
        print("เลือกประเภทการคำนวณ:")
        print("1. บวก")
        print("2. ลบ")
        print("3. คูณ")
        print("4. หาร")
        print("5. ยกกำลัง")
        print("0. ออกจากโปรแกรม")

        choice = input("กรุณาเลือก (0-5): ")

        if choice == '0':
            print("ลาก่อน!")
            break

        if choice in ['1', '2', '3', '4', '5']:
            try:
                num1 = float(input("ป้อนตัวเลขที่ 1: "))
                num2 = float(input("ป้อนตัวเลขที่ 2: "))

                if choice == '1':
                    print("ผลลัพธ์:", add(num1, num2))
                elif choice == '2':
                    print("ผลลัพธ์:", subtract(num1, num2))
                elif choice == '3':
                    print("ผลลัพธ์:", multiply(num1, num2))
                elif choice == '4':
                    print("ผลลัพธ์:", divide(num1, num2))
                elif choice == '5':
                    print("ผลลัพธ์:", power(num1, num2))
            except ValueError:
                print("กรุณาป้อนตัวเลขให้ถูกต้อง")
        else:
            print("กรุณาเลือกหมายเลขที่ถูกต้อง (0-5)")

if __name__ == "__main__":
    main()