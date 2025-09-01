import os
class TXT:
    def Created():
        text_data = """ Hello ! Achirawit Thepburi ...... """

        with open("student.txt", "w", encoding="utf-8") as file:
            try:
                file.write(text_data)
                print("บันทึกไฟล์เรียบร้อยแล้ว")
            except:
                print("บันทึกไม่ได้")

    def Reader():
        with open("student.txt", "r", encoding="utf-8") as file:
            try:
                print(file.read())
                
            except:
                print("อ่านไฟล์ไม่ได้")

    def Update(data_update):
        with open("student.txt", "r+", encoding="utf-8") as file:
            try:
                file.write(data_update)
                print("อัปเดตข้อมูลเรียบร้อยแล้ว")
            except:
                print("ไม่สามารถอัปเดตข้อมูลได้")

    def Del(fileName):
        file = fileName
        if(os.path.exists(file)):
            os.remove(file)
            print("ลบไฟล์เรียบร้อยแล้ว")
        else:
            print("ไม่พบไฟล์ที่จะลบ", file)


create = TXT.Created() 
read = TXT.Reader()

up_to_dated = TXT.Update("Test")
read = TXT.Reader()


delete = TXT.Del("student.txt")

