from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import *
import os
os.system('cls')
import sys
#___________________________________________________________________________
import sqlite3 
connect=sqlite3.connect('DB.db')
myCursor=connect.cursor()
  
app= QApplication(sys.argv)

class MyClass(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(850,650)
        self.setWindowTitle('سیستم مدیریت اطلاعات دانش جویان')
    #________________________ افزودن و ویرایش _____________________________    
 
        self.Lbl1= QLabel('شماره پرسنلی:',self)
        self.Lbl1.move(230,40)
        self.Lbl1.setFont(QFont('B Mitra',17))
        self.Lbl2= QLabel('نام:',self)
        self.Lbl2.move(230,80)
        self.Lbl2.setFont(QFont('B Mitra',17))
        self.Lbl3= QLabel('نام خانوادگی:',self)
        self.Lbl3.move(230,120)
        self.Lbl3.setFont(QFont('B Mitra',17))
        self.Lbl4= QLabel('جنسیت:',self)
        self.Lbl4.move(230,160)
        self.Lbl4.setFont(QFont('B Mitra',17))
        
        self.In1=QLineEdit(self)
        self.In1.setGeometry(20,44,190,30)
        self.In1.setPlaceholderText('شماره پرسنلی 4 رقمی')
        self.In1.setFont(QFont('B Mitra',14))
        self.In2=QLineEdit(self)
        self.In2.setGeometry(20,84,190,30)
        self.In2.setPlaceholderText('نام')
        self.In2.setFont(QFont('B Mitra',14))
        self.In3=QLineEdit(self)
        self.In3.setGeometry(20,124,190,30)
        self.In3.setPlaceholderText('نام خانوادگی')
        self.In3.setFont(QFont('B Mitra',14))

        self.RadioBtn1=QRadioButton('خانم',self)
        self.RadioBtn1.setGeometry(20,160,190,30)
        self.RadioBtn1.setFont(QFont('B Mitra',17))
        self.RadioBtn1.clicked.connect(self.radio_selected)
        self.RadioBtn2=QRadioButton('آقا',self)
        self.RadioBtn2.setGeometry(100,160,190,30)
        self.RadioBtn2.setFont(QFont('B Mitra',17))
        self.RadioBtn2.clicked.connect(self.radio_selected)
        
        self.PushBtn1= QPushButton('افزودن',self)
        self.PushBtn1.setGeometry(30,210,120,55)
        self.PushBtn1.setFont(QFont('B Mitra',15,QFont.Weight.ExtraBold))
        self.PushBtn1.setIcon(QIcon('Pics/insert.png'))
        self.PushBtn1.setIconSize(QSize(38,38))
        self.PushBtn1.clicked.connect(self.Insert) 
           
        self.PushBtn2= QPushButton('ویرایش',self)
        self.PushBtn2.setGeometry(180,210,120,55)
        self.PushBtn2.setFont(QFont('B Mitra',15,QFont.Weight.ExtraBold))
        self.PushBtn2.setIcon(QIcon('Pics/Update.png'))
        self.PushBtn2.setIconSize(QSize(38,38))  
        self.PushBtn2.clicked.connect(self.Update)
    #____________________________________ حذف _________________________________
        self.Lbl5= QLabel('شماره پرسنلی:',self)
        self.Lbl5.move(230,385)
        self.Lbl5.setFont(QFont('B Mitra',17))

        self.In5=QLineEdit(self)
        self.In5.setGeometry(20,390,190,30)
        self.In5.setPlaceholderText('شماره پرسنلی 4 رقمی')
        self.In5.setFont(QFont('B Mitra',14))
        
        self.PushBtn5= QPushButton('حذف',self)
        self.PushBtn5.setGeometry(30,440,120,55)
        self.PushBtn5.setFont(QFont('B Mitra',15,QFont.Weight.ExtraBold))
        self.PushBtn5.setIcon(QIcon('Pics/delete.png'))
        self.PushBtn5.setIconSize(QSize(38,38))
        self.PushBtn5.clicked.connect(self.Delete)
    #_____________________________نمایش اطلاعات در جدول__________________________________  
        self.Tbl1=QTableWidget(self)
        self.Tbl1.setColumnCount(3)
        self.Tbl1.setGeometry(380,20,450,600)
        self.Tbl1.setColumnCount(4)
        self.Tbl1.setColumnWidth(0, 110)
        self.Tbl1.setColumnWidth(1, 85)
        self.Tbl1.setColumnWidth(2, 115)
        self.Tbl1.setColumnWidth(3, 75)
        self.Tbl1.setHorizontalHeaderLabels(['شماره پرسنلی', 'نام', 'نام خانوادگی','جنسیت'])
        self.Tbl1.setRowCount(30)
        self.Tbl1.setFont(QFont('B Mitra',12))
        self.Tbl1.setStyleSheet('text-align: center;vertical-align: middle;font-weight: bold;border:0.5px solid ;text-align:center;font-family:B Mitra;')   
        
        self.PushBtn5= QPushButton('بروز رسانی جدول',self)
        self.PushBtn5.setGeometry(30,550,210,55)
        self.PushBtn5.setFont(QFont('B Mitra',15,QFont.Weight.ExtraBold))
        self.PushBtn5.setIcon(QIcon('Pics/refresh.png'))
        self.PushBtn5.setIconSize(QSize(38,38))
        self.PushBtn5.clicked.connect(self.View)
#-------------------------------------------------    
    def radio_selected(self):
        self.RadioBtn= self.sender()
        if self.RadioBtn.isChecked():
            print(self.RadioBtn.text())
            print(type(self.RadioBtn))
        print(type(str(self.RadioBtn)))
#-------------------------------------------------         
    def Create(self):
        sql='''
        create table if not exists Student
        (
        id integer primary key,
        name varchar(20),
        family varchar(30),
        sex varchar(5)
        ) 
        '''
        myCursor.execute(sql)
        connect.commit()            
#------------------------------------------------- 
    def View(self):
        self.x=myCursor.execute('select * from Student')
        self.TblRow=0
        self.y=str(self.Tbl1.rowCount())
        for i in self.y:
            self.Tbl1.clear()
        self.Tbl1.setHorizontalHeaderLabels(['شماره پرسنلی', 'نام', 'نام خانوادگی','جنسیت'])
        for i in self.x:
            self.Tbl1.setItem(self.TblRow,0,QTableWidgetItem(str(i[0])))
            self.Tbl1.setItem(self.TblRow,1,QTableWidgetItem(i[1]))
            self.Tbl1.setItem(self.TblRow,2,QTableWidgetItem(i[2]))
            self.Tbl1.setItem(self.TblRow,3,QTableWidgetItem((i[3])))
            self.TblRow=self.TblRow+1
        connect.commit()
        print('Refresh Successfuly.')
#-------------------------------------------------            
    def ShowPopUpInsert(self):
        self.MsgBox1=QMessageBox()
        self.MsgBox1.setWindowTitle('ارور')
        self.MsgBox1.setText('شماره پرسنلی 4 رقمی نمی باشد یا تکراری است \n مطمئن شوید همه خانه ها تکمیل شده باشند')
        self.MsgBox1.setFont(QFont('B Mitra',12,QFont.Weight.ExtraBold))
        self.MsgBox1.setIcon(QMessageBox.Icon.Warning)
        self.MsgBox1.exec() 
#-------------------------------------------------        
    def Insert(self):
        self.textboxValue =self.In1.text()
        self.textboxValue2 =self.In2.text()
        self.textboxValue3 =self.In3.text()
        self.textboxValue4 =self.RadioBtn.text()
        try:
            if len(self.textboxValue) == 4 and len(self.textboxValue2)>1 and len(self.textboxValue3)>1 and self.textboxValue4 :
                myCursor.execute("insert into Student(id,name,family,sex)"
                         "values('%s','%s','%s','%s')" 
                                             % (''.join(self.In1.text()),
                                                ''.join(self.In2.text()),
                                                ''.join(self.In3.text()),
                                                ''.join(str(self.RadioBtn.text())))) 
                connect.commit() 
                print('Inserted Successfuly.')
            else:
                self.vBox1=QVBoxLayout()
                self.vBox1.addWidget(self.PushBtn1)
                self.setLayout(self.vBox1)
                self.ShowPopUpInsert()
        except:
            self.vBox1=QVBoxLayout()
            self.vBox1.addWidget(self.PushBtn1)
            self.setLayout(self.vBox1)
            self.ShowPopUpInsert()
#---------------------------------------------------
    def ShowPopUpDel(self):
        self.MsgBox1=QMessageBox()
        self.MsgBox1.setWindowTitle('ارور')
        self.MsgBox1.setText('شماره پرسنلی 4 رقمی نیست یا اشتباه است.')
        self.MsgBox1.setFont(QFont('B Mitra',12,QFont.Weight.ExtraBold))
        self.MsgBox1.setIcon(QMessageBox.Icon.Warning)
        self.MsgBox1.exec()
#----------------------------------------------------
    def Delete(self):
        self.L1=[]
        self.Num=0
        self.textboxValue6 =self.In5.text()
        
        self.x=myCursor.execute('select id from Student')
        for i in self.x:
            self.L1.extend(i)
        print(self.L1)
        
        if self.textboxValue6 in str(self.L1):
            self.Num+=1
        print(self.Num)
        if len(self.textboxValue6) == 4 and self.Num == 1:
            myCursor.execute("delete from Student where id=('%s')" % (''.join(self.In5.text())))
            connect.commit()
            print('Deleted Succesfuly') 
        else:
            self.ShowPopUpDel()
#-----------------------------------------------
    def ShowPopUpUp(self):
        self.MsgBox1=QMessageBox()
        self.MsgBox1.setWindowTitle('ارور')
        self.MsgBox1.setText('همه خانه ها تکمیل نیست\nیا شماره پرسنلی اشتباه وارد شده است')
        self.MsgBox1.setFont(QFont('B Mitra',12,QFont.Weight.ExtraBold))
        self.MsgBox1.setIcon(QMessageBox.Icon.Warning)
        self.MsgBox1.exec()  
#-------------------------------------------------         
    def Update(self):
        self.L1=[]
        self.Num=0
        self.textboxValue =self.In1.text()
        self.textboxValue2 =self.In2.text()
        self.textboxValue3 =self.In3.text()
        self.textboxValue4 =self.RadioBtn.text()
        self.x=myCursor.execute('select id from Student')
        for i in self.x:
            self.L1.extend(i)
        print(self.L1)
        
        if self.textboxValue in str(self.L1):
            self.Num+=1
        print(self.Num)
        if len(self.textboxValue) == 4 and len(self.textboxValue2)>1 and len(self.textboxValue3)>0 and self.Num == 1 and self.textboxValue4 :
            myCursor.execute("update Student set name=('%s'),family=('%s'),sex=('%s') where id=('%s')"
                         % (''.join(self.In2.text()),
                            ''.join(self.In3.text()),
                            ''.join(str(self.RadioBtn.text())),
                            ''.join(self.In1.text())))
            connect.commit() 
            print('updated Succesfuly') 
        else:
            self.vBox1=QVBoxLayout()
            self.vBox1.addWidget(self.PushBtn1)
            self.setLayout(self.vBox1)
            self.ShowPopUpUp()
#------------------------------------------------- 

window=MyClass()
window.Create()
window.show()
sys.exit(app.exec_())