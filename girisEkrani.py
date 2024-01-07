from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QPushButton,QVBoxLayout,QHBoxLayout,QLineEdit,QMessageBox,QMessageBox,QLabel,QShortcut
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QKeySequence,QIcon
from girisYapildi import GirisYapildi

kullaniciAdi="user"
sifre="admin"
class GirisEkrani(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("To Do List")
        self.setFixedSize(400,150)
        self.setWindowIcon(QIcon("toDoList.png"))

        vbox=QVBoxLayout()

        hboxKullaniciAdi=QHBoxLayout()
        self.kullaniciAdiLabel=QLabel("Kullanici Adı: ")
        self.kullaniciAdiLineEdit=QLineEdit()
        self.kullaniciAdiLineEdit.setFixedSize(QSize(200,20))


        hboxKullaniciAdi.addWidget(self.kullaniciAdiLabel)
        hboxKullaniciAdi.addWidget(self.kullaniciAdiLineEdit)

        hboxSifre=QHBoxLayout()
        self.SifreLabel=QLabel("Şifre: ")
        self.SifreLineEdit=QLineEdit()
        self.SifreLineEdit.setFixedSize(QSize(200,20))
        self.SifreLineEdit.setEchoMode(QLineEdit.Password)

        hboxSifre.addWidget(self.SifreLabel)
        hboxSifre.addWidget(self.SifreLineEdit)

        self.buton=QPushButton()
        self.buton.setText("Giriş Yap")
        self.buton.setFixedSize(QSize(100,30))
        self.buton.clicked.connect(self.giris_yap_tusu)

        vbox.addLayout(hboxKullaniciAdi)
        vbox.addLayout(hboxSifre)
        vbox.addWidget(self.buton,alignment=Qt.AlignmentFlag.AlignCenter)
        self.setLayout(vbox)  # ana layout'muzu vbox olarak belirliyoruz.

        enter_shortcut = QShortcut(QKeySequence(Qt.Key_Return), self)
        enter_shortcut.activated.connect(self.giris_yap_tusu)

        asagi_yon_shortcut = QShortcut(QKeySequence(Qt.Key_Down), self)
        asagi_yon_shortcut.activated.connect(self.asagi_yon_tusu)

        yukari_yon_shortcut = QShortcut(QKeySequence(Qt.Key_Up), self)
        yukari_yon_shortcut.activated.connect(self.yukari_yon_tusu)

        esc_shortcut = QShortcut(QKeySequence(Qt.Key.Key_Escape),self)
        esc_shortcut.activated.connect(self.close)
        

    def giris_yap_tusu(self):
        if self.kullaniciAdiLineEdit.text()==kullaniciAdi and self.SifreLineEdit.text()==sifre:
            self.hide()  # closeEvent metodu çalışmasın diye sakladım zaten girisYapildi ekraninda pencereyi kapatınca buradaki gizlenmiş olan pencere de kapanacak
            self.giris=GirisYapildi()
            self.giris.show()
            """ self ile tanimlamazsam fonksiyon bittikten sonra bu nesne yok
            oluyor yani local bir değişken gibi oluyor. açtiginiz ekran direk kapaniyor yani"""


        else:
            QMessageBox.warning(self,"HATA","Kullanici adı veya şifre yanlış")
            
    def asagi_yon_tusu(self):
        self.SifreLineEdit.setFocus()
    def yukari_yon_tusu(self):
        self.kullaniciAdiLineEdit.setFocus()
    
    def closeEvent(self,event):
        
        yanit=QMessageBox()
        yanit.setWindowTitle("Çıkış")
        yanit.setText("Programı sonlandırmak istediğinizden emin misiniz?")
        evet_butonu = yanit.addButton('Evet', QMessageBox.YesRole)

        yanit.exec_()
        if yanit.clickedButton() == evet_butonu:
            event.accept()
        else:
            event.ignore()