from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QPushButton,QVBoxLayout,QHBoxLayout,QMessageBox,QShortcut,QLabel
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QIcon,QKeySequence,QPixmap
from gorevEkleme import GorevEkleme
from gorevGoruntuleme import GorevGoruntuleme
from gorevTamamlama import GorevTamamlama
from gorevSilme import GorevSilme
class GirisYapildi(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Giriş Yapıldı")
        self.setFixedSize(800,400)
        self.setWindowIcon(QIcon("toDoList.png"))
        self.setStyleSheet("background-color: #DDDDDD;")

        vbox=QVBoxLayout()

        label_arka_plan = QLabel()
        pixmap=QPixmap("hosgeldiniz.png")
        label_arka_plan.setPixmap(pixmap)
        label_arka_plan.setScaledContents(True)

        vbox.addWidget(label_arka_plan)
        
        self.butonGorevEkle=QPushButton("Görev Ekle")
        self.butonGorevEkle.setFixedSize(QSize(200,60))
        self.butonGorevEkle.setStyleSheet("background-color: red; border-style: outset;border-width: 2px; border-radius: 10px;border-color: black;font-size: 16px; font-weight: bold; ")
        self.butonGorevEkle.clicked.connect(self.gorevEkle)

        self.butonGorevGoruntule=QPushButton("Görev Görüntüleme")
        self.butonGorevGoruntule.setFixedSize(QSize(200,60))
        self.butonGorevGoruntule.setStyleSheet("background-color: red; border-style: outset;border-width: 2px; border-radius: 10px;border-color: black;font-size: 16px; font-weight: bold; ")
        self.butonGorevGoruntule.clicked.connect(self.gorevGoruntule)

        self.butonGorevTamamlama=QPushButton("Görev Tamamlama")
        self.butonGorevTamamlama.setFixedSize(QSize(200,60))
        self.butonGorevTamamlama.setStyleSheet("background-color: red; border-style: outset;border-width: 2px; border-radius: 10px;border-color: black;font-size: 16px; font-weight: bold; ")
        self.butonGorevTamamlama.clicked.connect(self.gorevTamamla)


        self.butonGorevSilme=QPushButton("Görev Silme")
        self.butonGorevSilme.setFixedSize(QSize(200,60))
        self.butonGorevSilme.setStyleSheet("background-color: red; border-style: outset;border-width: 2px; border-radius: 10px;border-color: black; font-size: 16px; font-weight: bold; ")
        self.butonGorevSilme.clicked.connect(self.gorevSil)

        hbox1=QHBoxLayout()
        hbox1.addWidget(self.butonGorevEkle)
        hbox1.addWidget(self.butonGorevGoruntule)

        hbox2=QHBoxLayout()
        hbox2.addWidget(self.butonGorevTamamlama)
        hbox2.addWidget(self.butonGorevSilme)
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)

        self.setLayout(vbox)  


        esc_shortcut = QShortcut(QKeySequence(Qt.Key.Key_Escape),self)
        esc_shortcut.activated.connect(self.close)

    def gorevEkle(self):
        self.gorevEkleme=GorevEkleme()
        self.gorevEkleme.show()
    def gorevGoruntule(self):
        self.gorevGoruntu = GorevGoruntuleme() 
        self.gorevGoruntu.show()
    def gorevTamamla(self):
        self.gorevTamamlama = GorevTamamlama()
        self.gorevTamamlama.show()
    def gorevSil(self):
        self.gorevSilme = GorevSilme()
        self.gorevSilme.show()
    def closeEvent(self,event):
        
        yanit=QMessageBox()
        yanit.setWindowTitle("Çıkış")
        yanit.setText("Programı sonlandırmak istediğinizden emin misiniz?")
        evet_butonu = yanit.addButton('Evet', QMessageBox.YesRole)
        hayir_butonu = yanit.addButton('Hayır', QMessageBox.NoRole)

        yanit.exec_()
        if yanit.clickedButton() == evet_butonu:
            event.accept()
        else:
            event.ignore()