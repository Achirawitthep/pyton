import sys, os
import sqlite3
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QTableWidgetItem

DB_PATH = os.path.join(os.path.dirname(__file__), 'asset.db')

def init_db():
    conn = sqlite3.connect(DB_PATH)
    try:
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS asset(
                id TEXT PRIMARY KEY NOT NULL,
                asset_code TEXT,
                asset_name TEXT,
                major TEXT,
                room TEXT,
                coordinate TEXT
            )
        """)
        conn.commit()
    finally:
        conn.close()

class AssetForm(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('asset_form.ui', self)  # โหลดไฟล์ UI ที่คุณสร้างไว้

        init_db()

        self.pushButton.clicked.connect(self.saveData)
        self.btn_edit.clicked.connect(self.update_record)
        self.btn_delete.clicked.connect(self.delete_record)
        self.tableWidget.cellClicked.connect(self.on_row_clicked)

        self.loadData()

    def saveData(self):
        id_ = self.lineEdit.text().strip()
        asset_code = self.lineEdit_2.text().strip()
        asset_name = self.lineEdit_3.text().strip()
        major = self.lineEdit_4.text().strip()
        room = self.lineEdit_5.text().strip()
        coordinate = self.lineEdit_6.text().strip()

        if not all([id_, asset_code, asset_name, major, room, coordinate]):
            QMessageBox.warning(self, "ข้อมูลไม่ครบถ้วน", "กรุณากรอกข้อมูลให้ครบทุกช่อง")
            return

        try:
            conn = sqlite3.connect(DB_PATH)
            cur = conn.cursor()
            cur.execute("""
                INSERT INTO asset (id, asset_code, asset_name, major, room, coordinate)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (id_, asset_code, asset_name, major, room, coordinate))
            conn.commit()
            QMessageBox.information(self, "สำเร็จ", "บันทึกข้อมูลสำเร็จ")
        except Exception as e:
            QMessageBox.critical(self, "บันทึกข้อมูลล้มเหลว", f"เกิดข้อผิดพลาด\n{e}")
        finally:
            conn.close()

        self.loadData()

    def loadData(self):
        try:
            conn = sqlite3.connect(DB_PATH)
            cur = conn.cursor()
            cur.execute("SELECT * FROM asset")
            rows = cur.fetchall()
        except Exception as e:
            QMessageBox.critical(self, "โหลดข้อมูลล้มเหลว", f"เกิดข้อผิดพลาด\n{e}")
            return
        finally:
            conn.close()

        self.tableWidget.setRowCount(len(rows))
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setHorizontalHeaderLabels(['รหัส', 'รหัสครุภัณฑ์', 'ชื่อครุภัณฑ์', 'สาขาวิชา', 'ห้อง/อาคาร', 'พิกัด'])

        for r, row in enumerate(rows):
            for c, val in enumerate(row):
                self.tableWidget.setItem(r, c, QTableWidgetItem(str(val)))

        self.tableWidget.resizeColumnsToContents()

    def on_row_clicked(self, row, column):
        self.lineEdit.setText(self.tableWidget.item(row, 0).text())
        self.lineEdit_2.setText(self.tableWidget.item(row, 1).text())
        self.lineEdit_3.setText(self.tableWidget.item(row, 2).text())
        self.lineEdit_4.setText(self.tableWidget.item(row, 3).text())
        self.lineEdit_5.setText(self.tableWidget.item(row, 4).text())
        self.lineEdit_6.setText(self.tableWidget.item(row, 5).text())

    def update_record(self):
        id_ = self.lineEdit.text().strip()
        asset_code = self.lineEdit_2.text().strip()
        asset_name = self.lineEdit_3.text().strip()
        major = self.lineEdit_4.text().strip()
        room = self.lineEdit_5.text().strip()
        coordinate = self.lineEdit_6.text().strip()

        if not id_:
            QMessageBox.warning(self, "ไม่พบรหัส", "กรุณาเลือกข้อมูลจากตารางก่อน")
            return

        if not all([asset_code, asset_name, major, room, coordinate]):
            QMessageBox.warning(self, "ข้อมูลไม่ครบถ้วน", "กรุณากรอกข้อมูลให้ครบทุกช่อง")
            return

        try:
            conn = sqlite3.connect(DB_PATH)
            cur = conn.cursor()
            cur.execute("""
                UPDATE asset
                SET asset_code=?, asset_name=?, major=?, room=?, coordinate=?
                WHERE id=?
            """, (asset_code, asset_name, major, room, coordinate, id_))
            conn.commit()
            QMessageBox.information(self, "สำเร็จ", "แก้ไขข้อมูลเรียบร้อย")
        except Exception as e:
            QMessageBox.critical(self, "แก้ไขข้อมูลล้มเหลว", f"เกิดข้อผิดพลาด\n{e}")
        finally:
            conn.close()

        self.loadData()

    def delete_record(self):
        id_ = self.lineEdit.text().strip()
        if not id_:
            QMessageBox.warning(self, "ไม่พบรหัส", "กรุณาเลือกข้อมูลจากตารางก่อน")
            return

        confirm = QMessageBox.question(self, "ยืนยันการลบ", f"ต้องการลบข้อมูล รหัส '{id_}' หรือไม่?",
                                       QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if confirm != QMessageBox.Yes:
            return

        try:
            conn = sqlite3.connect(DB_PATH)
            cur = conn.cursor()
            cur.execute("DELETE FROM asset WHERE id=?", (id_,))
            conn.commit()
            QMessageBox.information(self, "สำเร็จ", "ลบข้อมูลเรียบร้อย")
        except Exception as e:
            QMessageBox.critical(self, "ลบข้อมูลล้มเหลว", f"เกิดข้อผิดพลาด\n{e}")
        finally:
            conn.close()

        self.loadData()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = AssetForm()
    window.show()
    sys.exit(app.exec_())
