from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QPushButton,QVBoxLayout,QHBoxLayout,QLabel,QLineEdit,QCalendarWidget, QTimeEdit,QDialog,QMessageBox
from PyQt5.QtCore import QSize,QDateTime
from PyQt5.QtGui import QIcon
import json
class GorevEkleme(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Görev Ekleme")
        self.setFixedSize(600,400)
        self.setWindowIcon(QIcon("toDoList.png"))

        anaLayout=QVBoxLayout()

        self.tarih_bilgisi_qdatetime = QDateTime()
        self.tarih_bilgisi_str = str

        self.baslangic_tarihi_qdatetime = QDateTime()
        self.baslangic_tarihi_str = str

        self.bitis_tarihi_qdatetime = QDateTime()
        self.bitis_tarihi_str = str

        
        hboxGorevAdi=QHBoxLayout()
        gorevAdi=QLabel("Görev Adı: ")
        gorevAdi.setStyleSheet("font-weight: 600; font-size: 16px;")
        self.gorevAdiLineEdit=QLineEdit()
        self.gorevAdiLineEdit.setFixedSize(QSize(360,60))

        hboxGorevAdi.addWidget(gorevAdi)
        hboxGorevAdi.addWidget(self.gorevAdiLineEdit)


        hboxGorevIcerigi=QHBoxLayout()
        gorevIcerigi=QLabel("Görev İçeriği: ")
        gorevIcerigi.setStyleSheet("font-weight: 600; font-size: 16px;")

        self.gorevIcerigiLineEdit=QLineEdit()
        self.gorevIcerigiLineEdit.setFixedSize(QSize(360,60))

        hboxGorevIcerigi.addWidget(gorevIcerigi)
        hboxGorevIcerigi.addWidget(self.gorevIcerigiLineEdit)


        hboxGorevBaslangicTarihi=QHBoxLayout()
        gorevBaslangicTarihi=QLabel("Görev Başlangıç Tarihi: ")
        gorevBaslangicTarihi.setStyleSheet("font-weight: 600; font-size: 16px;")

        hboxGorevBaslangicTarihi.addWidget(gorevBaslangicTarihi)
        self.GorevBaslangicTarihiButon=QPushButton("Takvim")
        self.GorevBaslangicTarihiButon.setIcon(QIcon("takvim.png"))
        self.GorevBaslangicTarihiButon.setFixedSize(QSize(360,60))
        self.GorevBaslangicTarihiButon.setIconSize(QSize(150,40))

        self.GorevBaslangicTarihiButon.clicked.connect(self.baslangicTarihiBelirleme)
        hboxGorevBaslangicTarihi.addWidget(self.GorevBaslangicTarihiButon)

        hboxGorevBitisTarihi=QHBoxLayout()
        gorevBitisTarihi=QLabel("Görev Bitiş Tarihi: ")
        gorevBitisTarihi.setStyleSheet("font-weight: 600; font-size: 16px;")
        hboxGorevBitisTarihi.addWidget(gorevBitisTarihi)

        self.GorevBitisTarihiButon=QPushButton("Takvim")
        self.GorevBitisTarihiButon.setIcon(QIcon("takvim.png"))
        self.GorevBitisTarihiButon.setFixedSize(QSize(360,60))
        self.GorevBitisTarihiButon.setIconSize(QSize(150,40))
        hboxGorevBitisTarihi.addWidget(self.GorevBitisTarihiButon)
        

        gorevEklemeOnaylaButton=QPushButton("ONAYLA")

        self.GorevBitisTarihiButon.clicked.connect(self.bitisTarihiBelirleme)

        gorevEklemeOnaylaButton.clicked.connect(self.gorevOnayla)

        anaLayout.addLayout(hboxGorevAdi)
        anaLayout.addLayout(hboxGorevIcerigi)
        anaLayout.addLayout(hboxGorevBaslangicTarihi)
        anaLayout.addLayout(hboxGorevBitisTarihi)
        anaLayout.addWidget(gorevEklemeOnaylaButton,alignment=Qt.AlignmentFlag.AlignCenter)

        self.setLayout(anaLayout)
    def takvimGoruntule(self):
        takvimPenceresi = QDialog(self)
        takvimPenceresi.setWindowTitle("Takvim")
        takvimPenceresi.setFixedSize(600, 400)
        takvimPenceresi.takvim = QCalendarWidget()
        takvimPenceresi.saat = QTimeEdit()
        takvimPenceresi.saat.setDisplayFormat("HH:mm")
        takvimOnaylaButon = QPushButton("ONAYLA")

        takvimLayout = QVBoxLayout()
        takvimLayout.addWidget(takvimPenceresi.takvim)
        takvimLayout.addWidget(takvimPenceresi.saat)
        takvimLayout.addWidget(takvimOnaylaButon)
        takvimPenceresi.setLayout(takvimLayout)

        def onaylaTiklandi():
            takvim_bilgisi = takvimPenceresi.takvim.selectedDate()
            takvim_bilgisi = takvim_bilgisi.toString('dd.MM.yyyy')
            saat_bilgisi = takvimPenceresi.saat.time()
            saat_bilgisi = saat_bilgisi.toString('HH:mm')
            self.tarih_bilgisi_str = takvim_bilgisi + ' ' + saat_bilgisi
            self.tarih_bilgisi_qdatetime = QDateTime.fromString(self.tarih_bilgisi_str, 'dd.MM.yyyy HH:mm')
            takvimPenceresi.accept()

        takvimOnaylaButon.clicked.connect(onaylaTiklandi)
        takvimPenceresi.exec_()
        return self.tarih_bilgisi_qdatetime
    
    def baslangicTarihiBelirleme(self):
        self.baslangic_tarihi_qdatetime = self.takvimGoruntule()
        self.baslangic_tarihi_str = self.baslangic_tarihi_qdatetime.toString('dd.MM.yyyy HH:mm')
        self.GorevBaslangicTarihiButon.setText(self.baslangic_tarihi_str)


    def bitisTarihiBelirleme(self):
        self.bitis_tarihi_qdatetime = self.takvimGoruntule()
        self.bitis_tarihi_str = self.bitis_tarihi_qdatetime.toString('dd.MM.yyyy HH:mm')
        self.GorevBitisTarihiButon.setText(self.bitis_tarihi_str)


    def gorevOnayla(self):
        
        gorev_aktifliği = str
        suanki_zaman_qdatetime = QDateTime.currentDateTime()
        
        if suanki_zaman_qdatetime < self.baslangic_tarihi_qdatetime:
            gorev_tamamlama_durumu = "Görev Henüz Başlamadı"
        elif suanki_zaman_qdatetime < self.bitis_tarihi_qdatetime:
            gorev_tamamlama_durumu = "Görev Henüz Tamamlanmadı"
        else:
            gorev_tamamlama_durumu = "Görev Teslim süresi geçti"
        if gorev_tamamlama_durumu == "Görev Teslim süresi geçti" or gorev_tamamlama_durumu == "Görev Henüz Başlamadı":
            gorev_aktifliği = "Aktif değil"
        else:
            gorev_aktifliği = "Aktif"
        if self.baslangic_tarihi_qdatetime < self.bitis_tarihi_qdatetime:

            degerlerSozlugu= { self.gorevAdiLineEdit.text() : {
            "gorev_aktifligi": f"{gorev_aktifliği}",
            "gorev_durumu": f"{gorev_tamamlama_durumu}",
            "gorev_icerigi": self.gorevIcerigiLineEdit.text(),
            "gorev_baslangic_tarihi":  self.baslangic_tarihi_str,
            "gorev_bitis_tarihi": self.bitis_tarihi_str } }

            with open("data.json", "r", encoding="utf-8") as dosya:
                try:
                    mevcut_veri = json.load(dosya)
                except json.JSONDecodeError:
                    mevcut_veri = []
            mevcut_veri.append(degerlerSozlugu)
            with open("data.json", "w", encoding="utf-8") as dosya:  # with open kullandığımızda dosyayı ayriyetten kapatmamıza gerek yok kendi kendine kapanıyor zaten.
                json.dump(mevcut_veri, dosya, ensure_ascii=False, indent=2)
            QMessageBox.information(self,"Görev Ekle","Görev başarıyla eklendi")
            self.close()
        else:
            QMessageBox.warning(self,"HATA","Başlangıç Tarihi, bitiş Tarihinden sonra olamaz!")
        