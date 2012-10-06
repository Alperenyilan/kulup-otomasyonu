#!/usr/bin/python
#-*- coding:utf-8 -*-

#'____________________ Import Library's ___________________________________
import sys
import os
import cv
import Image
import shutil
import time
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import MySQLdb

#'____________________ Variables and connections __________________________
PRODUCT = True#False
mysql = MySQLdb.connect("localhost","root","sckn","kutuphane")
lstClubList = ["İletişim Kulübü","Genç Yöneticiler Kulübü"]

#'____________________ New Member Window __________________________________
class AddNewMember(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.cwMouseLeft  = 0 # Capture Window Click Mouse Left
        self.cwMouseRight = 0 # Capture Windows Click Mouse Right

        self.lblTurkeyIDNumber = QLabel(u"T.C Kimlik No:",self)
        self.lblTurkeyIDNumber.move(10,30)
        self.lblSchoolNumber = QLabel(u"Okul Numarası:",self)
        self.lblSchoolNumber.move(10,60)
        self.lblName = QLabel(u"İsmi:",self)
        self.lblName.move(10,90)
        self.lblSurname = QLabel(u"Soyismi:",self)
        self.lblSurname.move(10,120)
        self.lblFatherName = QLabel(u"Baba Adı:",self)
        self.lblFatherName.move(10,150)
        self.lblMotherName = QLabel(u"Anne Adı:",self)
        self.lblMotherName.move(10,180)
        self.lblBirthofPlace = QLabel(u"Doğum Yeri:",self)
        self.lblBirthofPlace.move(10,210)
        self.lblDateOfBirth = QLabel(u"Doğum Tarihi:",self)
        self.lblDateOfBirth.move(10,240)
        self.lblBloodGroup = QLabel(u"Kan Grubu:",self)
        self.lblBloodGroup.move(10,270)
        self.lblProvince = QLabel(u"İl",self)
        self.lblProvince.move(10,300)
        self.lblCounty = QLabel(u"İlçe:",self)
        self.lblCounty.move(10,330)
        self.lblAddress = QLabel(u"Adres:",self)
        self.lblAddress.move(10,360)
        self.lblpic = QLabel(self)
        self.lblpic.setGeometry(150, 440, 200,250)
        self.lblpic.setPixmap(QPixmap("img/nopic.png"))
        self.lblpic.setScaledContents(True);
        self.lblSex = QLabel(u"Cinsiyet:",self)
        self.lblSex.move(400,30)
        self.lblSchoolName=QLabel(u"Fakülte/MYO/YO:",self)
        self.lblSchoolName.move(400,60)
        self.lblSection = QLabel(u"Bölüm:",self)
        self.lblSection.move(400,90)
        self.lblMobileNumber = QLabel(u"Cep Telefonu:",self)
        self.lblMobileNumber.move(400,120)
        self.lbleMail = QLabel(u"E-Posta",self)
        self.lbleMail.move(400,150)
        self.lblOtherClubs = QLabel(u"Diğer Kulüpler:",self)
        self.lblOtherClubs.move(400,180)
        self.lblAllowsendSMS = QLabel("SMS:",self)
        self.lblAllowsendSMS.move(400,300)
        self.lblAllowsendMail = QLabel(u"E-Posta:",self)
        self.lblAllowsendMail.move(400,330)
        self.lblDues = QLabel(u"Aidat'ı Yatırdı",self)
        self.lblDues.move(400,360)
        self.lblWanttoActiveRole = QLabel(u"Aktif rol istiyor:",self)
        self.lblWanttoActiveRole.move(400,390)
        self.lblOtherThings = QLabel(u"Diğer Şeyler:",self)
        self.lblOtherThings.move(400,420)

        self.txtTurkeyIDNumber = QLineEdit(self)
        self.txtTurkeyIDNumber.move(125,30)
        self.txtTurkeyIDNumber.resize(250,27)
        self.txtTurkeyIDNumber.setInputMask('99999999999;_')
        self.txtSchoolNumber = QLineEdit(self)
        self.txtSchoolNumber.move(125,60)
        self.txtSchoolNumber.resize(170,27)
        self.txtSchoolNumber.setInputMask('9999999999;_')
        self.txtName = QLineEdit(self)
        self.txtName.move(125,90)
        self.txtName.resize(250,27)
        self.txtSurname = QLineEdit(self)
        self.txtSurname.move(125,120)
        self.txtSurname.resize(250,27)
        self.txtFatherName = QLineEdit(self)
        self.txtFatherName.move(125,150)
        self.txtFatherName.resize(250,27)
        self.txtMotherName = QLineEdit(self)
        self.txtMotherName.move(125,180)
        self.txtMotherName.resize(250,27)
        self.txtBirthOfPlace = QLineEdit(self)
        self.txtBirthOfPlace.move(125,210)
        self.txtBirthOfPlace.resize(250,27)
        self.txtBirthOfDate = QLineEdit(self)
        self.txtBirthOfDate.move(125,240)
        self.txtBirthOfDate.resize(125,27)
        self.txtBirthOfDate.setInputMask('99/99/9999;_')
        self.txtCounty = QLineEdit(self)
        self.txtCounty.move(125,330)
        self.txtCounty.resize(250,27)
        self.txtAddress = QTextEdit(self)
        self.txtAddress.move(125,360)
        self.txtAddress.resize(250,75)
        self.txtSchoolName = QLineEdit(self)
        self.txtSchoolName.move(520,60)
        self.txtSchoolName.resize(250,27)
        self.txtSection = QLineEdit(self)
        self.txtSection.move(520,90)
        self.txtSection.resize(250,27)
        self.txtMobileNumber = QLineEdit(self)
        self.txtMobileNumber.move(520,120)
        self.txtMobileNumber.resize(250,27)
        self.txtMobileNumber.setInputMask('999 999 99 99;_')
        self.txteMail = QLineEdit(self)
        self.txteMail.move(520,150)
        self.txteMail.resize(250,27)
        self.txtOtherThings = QTextEdit(self)
        self.txtOtherThings.move(520,420)
        self.txtOtherThings.resize(250,200)

        #lstClubList = ["İletişim Kulübü","Genç Yöneticiler Kulübü"]
        self.listWidget = QListWidget(self)
        for i in lstClubList:
            item = QListWidgetItem(u"%s" % i)
            self.listWidget.addItem(item)
        self.listWidget.move(522,180)
        self.listWidget.resize(248,118)
        self.listWidget.setSelectionMode(QAbstractItemView.ExtendedSelection)

        self.rbtnAllowSMSyes = QRadioButton(u"&Gönderilsin", self)
        self.rbtnAllowSMSyes.move(520,300)
        self.rbtnAllowSMSno = QRadioButton(u"Gönderilmesin", self)
        self.rbtnAllowSMSno.move(630,300)
        self.rbtnAllowSMSno.resize(115,27)
        self.grpAllowSMS = QButtonGroup()
        self.grpAllowSMS.addButton(self.rbtnAllowSMSyes)
        self.grpAllowSMS.addButton(self.rbtnAllowSMSno)
        self.rbtnAllowEMailyes = QRadioButton(u"&Gönderilsin", self)
        self.rbtnAllowEMailyes.move(520,330)
        self.rbtnAllowEMailno = QRadioButton(u"Gönderilmesin", self)
        self.rbtnAllowEMailno.move(630,330)
        self.rbtnAllowEMailno.resize(115,27)
        self.grpAllowEmail = QButtonGroup()
        self.grpAllowEmail.addButton(self.rbtnAllowEMailyes)
        self.grpAllowEmail.addButton(self.rbtnAllowEMailno)
        self.rbtnDuesyes = QRadioButton(u"&Yatırdı", self)
        self.rbtnDuesyes.move(520,360)
        self.rbtnDuesno = QRadioButton(u"Yatırmadı", self)
        self.rbtnDuesno.move(630,360)
        self.grpDues = QButtonGroup()
        self.grpDues.addButton(self.rbtnDuesyes)
        self.grpDues.addButton(self.rbtnDuesno)
        self.rbtnWantActiveRoleyes = QRadioButton(u"&İstiyor", self)
        self.rbtnWantActiveRoleyes.move(520,390)
        self.rbtnWantActiveRoleno = QRadioButton(u"İstemiyor", self)
        self.rbtnWantActiveRoleno.move(630,390)
        self.grpWantActiveRole = QButtonGroup()
        self.grpWantActiveRole.addButton(self.rbtnWantActiveRoleyes)
        self.grpWantActiveRole.addButton(self.rbtnWantActiveRoleno)

        self.cmbBloodGroup = QComboBox(self)
        self.cmbBloodGroup.addItem("0 RH(+)")
        self.cmbBloodGroup.addItem("0 RH(-)")
        self.cmbBloodGroup.move(125,270)
        self.cmbBloodGroup.resize(250,27)
        self.cmbProvince = QComboBox(self)
        self.cmbProvince.addItem("Adana")
        self.cmbProvince.move(125,300)
        self.cmbProvince.resize(250,27)
        self.cmbSex = QComboBox(self)
        self.cmbSex.addItem("Bayan")
        self.cmbSex.addItem("Bay")
        self.cmbSex.move(520,30)
        self.cmbSex.resize(250,27)

        self.btntakeaphoto  = QPushButton(u"Fotoğraf Çek", self)
        self.btntakeaphoto.move(10,440)
        self.btnRemovePhoto = QPushButton(u"Fotoğrafı Sil",self)
        self.btnRemovePhoto.move(10,475)
        self.btnAddPhotofromFile = QPushButton(u"Dosyadan Ekle",self)
        self.btnAddPhotofromFile.move(10,510)
        self.btnAddPhotofromURL = QPushButton(u"URL'den ekle",self)
        self.btnAddPhotofromURL.move(10,545)
        self.btnControlSchoolNumber = QPushButton(u"Kontrol Et",self)
        self.btnControlSchoolNumber.resize(75,27)
        self.btnControlSchoolNumber.move(300,60)
        self.btnSaveMember = QPushButton(u"&Kayıt Et",self)
        self.btnSaveMember.move(520,625)
        self.btnSaveMember.resize(150,50)
        self.btnResetForm = QPushButton(u"Temizle",self)
        self.btnResetForm.move(680,625)
        self.btnResetForm.resize(90,50)
        self.btnShowCalendar = QPushButton(u"Takvimi Göster",self)
        self.btnShowCalendar.move(273,238)
        self.btnShowCalendar.setCheckable(True)

        QObject.connect(self.btntakeaphoto,SIGNAL('clicked()'),self.takeaphoto)
        QObject.connect(self.btnRemovePhoto,SIGNAL("clicked()"),self.removephoto)
        QObject.connect(self.btnShowCalendar,SIGNAL("clicked()"),self.calendarshowhide)
        QObject.connect(self.btnAddPhotofromFile,SIGNAL("clicked()"),self.addphotofromfile)
        QObject.connect(self.btnAddPhotofromURL,SIGNAL("clicked()"),self.addphotofromurl)
        QObject.connect(self.btnSaveMember,SIGNAL("clicked()"),self.selecteditemsoc)

        exitAction = QAction(QIcon('exit.png'), '&Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(qApp.quit)
        menubar  = self.menuBar()
        fileMenu = menubar.addMenu("&Menu")
        fileMenu.addAction(exitAction)

        self.wdgCalendar = QWidget(self)
        cal = QCalendarWidget(self.wdgCalendar)
        cal.setGridVisible(True)
        self.wdgCalendar.resize(500,500)
        self.wdgCalendar.move(370,250)
        self.wdgCalendar.hide()

        self.statusBar().showMessage('')
        resolution = QDesktopWidget().screenGeometry()
        self.setGeometry(400, 400, resolution.width(), resolution.height())
        self.setWindowTitle(u"Kulüp Otomasyonu Giriş Ekranı")
        self.move((resolution.width() / 2) - (self.frameSize().width() / 2),(resolution.height() / 2) - (self.frameSize().height() / 2))

    #'________________ Take A Photo Function from camera __________________
    def takeaphoto(self):
        camcapture = cv.CaptureFromCAM(-1)
        cv.NamedWindow("FotografCek",1)
        cv.SetMouseCallback("FotografCek",self.mouseEventp)
        while True:
            frame = cv.QueryFrame(camcapture)
            cv.ShowImage("FotografCek",frame) 
            k = cv.WaitKey(5)
            if k % 256 == 10 or self.cwMouseLeft==1:
                if frame:
                    cv.SaveImage("uye.jpeg",frame)
                    self.statusBar().showMessage(u"Fotoğraf Çekildi")
                    self.cropandresizephoto()
                    break
            if k % 256 == 27 or self.cwMouseRight==1:
                break
        cv.DestroyWindow("FotografCek")
        self.cwMouseLeft = 0
        self.cwMouseRight = 0

    #'________________ Crop for passport photo ____________________________
    def cropandresizephoto(self):
        #'________ Crop ___________________________________________________
        im = Image.open("uye.jpeg")
        left = 200
        top = 60
        width = 333
        height =420
        box = (left, top, left+width, top+height)
        region = im.crop(box)
        region.save("uye.jpeg")
        #'________ Resize _____________________________________________
            # No need resize because I use "setScaledContent" method
        #'________ Show Image Label ___________________________________
        self.lblpic.setPixmap(QPixmap("uye.jpeg"))
    def removephoto(self):
        self.lblpic.setPixmap(QPixmap("img/nopic.png"))
        os.system("rm uye.jpeg")
        self.statusBar().showMessage(u"Fotoğraf Silindi")
        #self.lblCounty.setText("Merhba")
    #'____________ MouseEvent from cv. window
    def mouseEventp(self,event,x,y,flags,param):
        if event == cv.CV_EVENT_LBUTTONUP:
            self.cwMouseLeft = 1
        if event == cv.CV_EVENT_RBUTTONUP:
            self.cwMouseRight = 1
    #'____________ BirthDate Calendar Show Hide ______________________
    def calendarshowhide(self):
        if self.btnShowCalendar.isChecked():
            self.wdgCalendar.show()
        else:
            self.wdgCalendar.hide()
    #'____________ Add Photo From File _______________________________
    def addphotofromfile(self):
        fname = QFileDialog.getOpenFileName(self, u'Fotoğraf Seç','/home',u"Resim Dosyaları (*.png *.jpg *.bmp)")
        shutil.copy2(fname, '/mnt/yedek/projects/python/kulup-otomasyon/uye.jpeg')
        self.lblpic.setPixmap(QPixmap("uye.jpeg"))
    #'____________ Add Photo From URL ________________________________
    def addphotofromurl(self):
        vpfromurl,iswritten= QInputDialog.getText(self, u'Fotoğraf Ekle', u'Fotoğraf &url yazın:')
        if iswritten and vpfromurl!="":
            os.system("wget --no-check-certificate -O /mnt/yedek/projects/python/kulup-otomasyon/uye.jpeg "+str(vpfromurl))
            self.lblpic.setPixmap(QPixmap("uye.jpeg"))
            self.statusBar().showMessage(u"Fotoğraf URL'den eklendi")
    #'____________ selected item
    def selecteditemsoc(self):
        for item in self.listWidget.selectedItems():
            print item.text()

#'____________________ Main Window (Login Window) _________________________
class LoginScreen(QMainWindow):
    def __init__(self,clubname):
        QMainWindow.__init__(self)

        fntClubName = QFont('Ubuntu')
        fntClubName.setPointSize(12)
        fntClubName.setBold(True)
        lblClubName = QLabel("<font color='#b22222'>"+clubname+"</font>",self)
        lblClubName.setFont(fntClubName)
        lblClubName.move(15,3)
        lblClubName.resize(180,29)
        lblUserName = QLabel(u"Kullanıcı Adı:", self)
        lblUserName.move(15, 30)
        lblPassword = QLabel(u"Şifre:", self)
        lblPassword.move(15, 60)
        self.txtUserName = QLineEdit(self)
        self.txtUserName.move(100,25)
        self.txtUserName.resize(182,27)
        self.txtPassword = QLineEdit(self)
        self.txtPassword.move(100,55)
        self.txtPassword.setEchoMode (QLineEdit.Password)
        self.txtPassword.resize(182,27)
        self.btnLogin  = QPushButton(u"Giriş Yap", self)
        self.btnLogin.resize(270,27)
        self.btnLogin.move(15,90)
        QObject.connect (self.txtPassword, SIGNAL ('returnPressed()'), self.logincheck)
        QObject.connect (self.btnLogin, SIGNAL ('clicked()'), self.logincheck)
        QObject.connect (self.txtUserName, SIGNAL ('returnPressed()'), self.logincheck)
        #self.setAttribute(Qt.WA_TranslucentBackground) 
        #self.setWindowFlags(Qt.Tool | Qt.FramelessWindowHint)
        #self.setWindowFlags(self.windowFlags() | Qt.WindowStaysOnTopHint)
        self.setGeometry(400, 400, 300, 120)
        self.setWindowTitle(u"Kulüp Otomasyonu Giriş Ekranı")
        resolution = QDesktopWidget().screenGeometry()
        self.move((resolution.width() / 2) - (self.frameSize().width() / 2),(resolution.height() / 2) - (self.frameSize().height() / 2))
        self.show()
    #'_____________ Login Check Control ___________________________________
    def logincheck(self):
        self.password = self.txtPassword.text()
        self.username = self.txtUserName.text()
        if self.username == "" or self.password == "":
            QMessageBox.critical(self,u"Hata",u"Boş alan bırakılamaz!", QMessageBox.Ok, QMessageBox.Ok)
        else:
            with mysql:
                cur = mysql.cursor()
                cur.execute("select count(*)from users where username='%s' and password = '%s';" % (self.username,self.password))
                rows = cur.fetchall()
                if rows[0][0] == 1:
                    self.hide()
                    self.addnewmember = AddNewMember()
                    self.addnewmember.show()
                else:
                    QMessageBox.critical(self,u"Hata",u"Kullanıcı Bulunamadı!", QMessageBox.Ok, QMessageBox.Ok)

def main():
    app = QApplication(sys.argv)
    if PRODUCT :
        ex = LoginScreen(u"İletişim Kulübü")
    else:
        ex = AddNewMember()
        ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
