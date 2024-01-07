from PyQt5.QtWidgets import QPushButton,QLabel,QMessageBox ,QTableWidget,QTableWidgetItem,QMainWindow,QWidget
from PyQt5.QtGui import QIcon,QColor
from PyQt5.QtCore import QDateTime
from PyQt5.QtCore import Qt
import json
class GorevGoruntuleme(QMainWindow):
    def __init__(self):
        super().__init__()

        with open("data.json", "r", encoding="utf-8") as dosya:
            try:
                json_verisi = json.load(dosya)
            except json.JSONDecodeError:
                json_verisi = []
        sozluk_sayisi = len(json_verisi)
        if sozluk_sayisi==0:
            QMessageBox.warning(self, "Uyarı", "Gösterilecek görev bulunamadı. Lütfen görev ekleyin.")
            self.close()
        else:
            self.table_widget = QTableWidget()
            self.table_widget.setRowCount(sozluk_sayisi+1)
            self.table_widget.setColumnCount(6)
            self.table_widget.setItem(0,0,QTableWidgetItem("Görev Adı"))
            self.table_widget.setItem(0,1,QTableWidgetItem("Görev Aktifliği"))
            self.table_widget.setItem(0,2,QTableWidgetItem("Görev Durumu"))
            self.table_widget.setItem(0,3,QTableWidgetItem("Görev İçeriği"))
            self.table_widget.setItem(0,4,QTableWidgetItem("Görev Başlangıç Tarihi"))
            self.table_widget.setItem(0,5,QTableWidgetItem("Görev Bitiş Tarihi"))
            for col in range(6):
                item = self.table_widget.item(0,col)
                item.setTextAlignment(0x0004 | 0x0080) 
                # 0x0004: Bu, Qt.AlignCenter'ı temsil eder ve içeriği yatayda ortalar.
                # 0x0080: Bu, Qt.AlignVCenter'ı temsil eder ve içeriği dikeyde ortalar.

            for gorev_numarasi, veri  in enumerate(json_verisi): 
                for gorev_adi , gorev_bilgileri in veri.items():

                    self.gorev_degisiklkleri(json_verisi,gorev_numarasi,gorev_adi,gorev_bilgileri)

                    self.table_widget_hucre_renkleri(gorev_numarasi,gorev_bilgileri)


                    # her hücre için ayrı ayrı buton oluşturmamız gerekiyor yoksa 1 tane butonumuz olur sadece
                    self.table_widget.setCellWidget(gorev_numarasi + 1, 3, self.gorev_icerigi_buton)
                    self.gorev_icerigi_buton.clicked.connect(lambda _ ,gorev_ad=gorev_adi, gorev_icerigi=gorev_bilgileri["gorev_icerigi"]: self.gorev_icerigi_buton_tiklandi(gorev_ad,gorev_icerigi))
                    # _ ifadesi self parametresini işaret eder
                    # lambda döngülerde son değeri kullanıl o yüzden defult değer atamak zorunda kaldık

                                    
                    self.table_widget.setItem(gorev_numarasi + 1, 4, QTableWidgetItem(gorev_bilgileri["gorev_baslangic_tarihi"]))
                    self.table_widget.setItem(gorev_numarasi + 1, 5, QTableWidgetItem(gorev_bilgileri["gorev_bitis_tarihi"]))

            self.table_widget.resizeRowsToContents()
            self.table_widget.resizeColumnsToContents()
            
            self.setWindowTitle("Gorev Goruntuleme")
            self.setWindowIcon(QIcon("toDoList.png"))


            self.setCentralWidget(self.table_widget)
            
            self.table_widget.setSizeAdjustPolicy(QTableWidget.AdjustToContents)
            self.setFixedSize(self.sizeHint())  
            
            
    def gorev_icerigi_buton_tiklandi(self,gorev_adi,gorev_icerigi):
        self.gorev_icerigi_penceresi=QWidget()
        self.gorev_icerigi_penceresi.setWindowTitle(f"{gorev_adi} İçeriği")
        self.gorev_icerigi_penceresi.setWindowIcon(QIcon("gorev_icerigi.jpg"))
        self.gorev_icerigi_penceresi.setStyleSheet("background-color:  #FF3D3D; font-size: 15px; font-weight: 600;")
        gorev_icerigi=QLabel(gorev_icerigi,self.gorev_icerigi_penceresi)
        gorev_icerigi.setAlignment(Qt.AlignTop | Qt.AlignLeft)  # QLabel'ı sola üste hizala
        gorev_icerigi.setWordWrap(True)  # QLabel içeriği pencere boyutunu aştığında otomatik satır başı yap

        gorev_icerigi_uzunluk = gorev_icerigi.sizeHint().width()
        content_heigh_yukseklik = gorev_icerigi.sizeHint().height()
        self.gorev_icerigi_penceresi.resize(max(gorev_icerigi_uzunluk+10, 200), max(content_heigh_yukseklik+10, 150))
        self.gorev_icerigi_penceresi.show()

    def gorev_degisiklkleri(self,json_verisi,gorev_numarasi,gorev_adi,gorev_bilgileri):

        
        self.table_widget.setItem(gorev_numarasi + 1, 0, QTableWidgetItem(gorev_adi))
        self.table_widget.setItem(gorev_numarasi + 1, 1, QTableWidgetItem(gorev_bilgileri["gorev_aktifligi"]))

        suanki_zaman_qdatetime = QDateTime.currentDateTime()
        baslangic_tarihi_qdatetime = QDateTime.fromString(gorev_bilgileri["gorev_baslangic_tarihi"], 'dd.MM.yyyy HH:mm')
        bitis_tarihi_qdatetime = QDateTime.fromString(gorev_bilgileri["gorev_bitis_tarihi"], 'dd.MM.yyyy HH:mm')
        if gorev_bilgileri["gorev_aktifligi"] == "Tamamlandı":
            gorev_bilgileri["gorev_durumu"] = "Görev Tamamlandı"
        elif suanki_zaman_qdatetime > baslangic_tarihi_qdatetime:
            gorev_bilgileri["gorev_durumu"] = "Görev Henüz Tamamlanmadı"

        if suanki_zaman_qdatetime > bitis_tarihi_qdatetime:
            gorev_bilgileri["gorev_durumu"] = "Görev Teslim süresi geçti"

        if gorev_bilgileri["gorev_durumu"] == "Görev Teslim süresi geçti":
            gorev_bilgileri["gorev_aktifligi"] = "Aktif değil"
        with open("data.json", "w", encoding="utf-8") as dosya:
            json.dump(json_verisi, dosya, ensure_ascii=False, indent=2)
    

    def table_widget_hucre_renkleri(self,gorev_numarasi,gorev_bilgileri):
        # gorev_aktifligi
        durum_item = QTableWidgetItem(gorev_bilgileri["gorev_aktifligi"])
        if gorev_bilgileri["gorev_aktifligi"] == "Aktif değil":
            durum_item.setBackground(QColor(128, 128, 128))
        elif gorev_bilgileri["gorev_aktifligi"] == "Tamamlandı":
            durum_item.setBackground(QColor(0, 0, 255))
        elif gorev_bilgileri["gorev_aktifligi"] == "Aktif":
            durum_item.setBackground(QColor(0, 255, 0))
                    
        else:
            QMessageBox.warning(self,"HATA","Sistemsel hata")
        self.table_widget.setItem(gorev_numarasi + 1, 1, durum_item)

        # gorev_durumu
        durum_item = QTableWidgetItem(gorev_bilgileri["gorev_durumu"])
        if gorev_bilgileri["gorev_durumu"] == "Görev Henüz Başlamadı":
            durum_item.setBackground(QColor(255, 255, 0))               # sarı
        elif gorev_bilgileri["gorev_durumu"] == "Görev Teslim süresi geçti":
            durum_item.setBackground(QColor(255, 0, 0))                 # kırmızı
        elif gorev_bilgileri["gorev_durumu"] == "Görev Henüz Tamamlanmadı":
            durum_item.setBackground(QColor(255, 180, 0))               # turuncu
        elif gorev_bilgileri["gorev_durumu"] == "Görev Tamamlandı":
            durum_item.setBackground(QColor(0, 255, 0))                 # yeşil
        else:
            QMessageBox.warning(self,"HATA","Sistemsel Hata")
        self.table_widget.setItem(gorev_numarasi + 1, 2, durum_item)

        self.gorev_icerigi_buton=QPushButton("İÇERİK")
        self.gorev_icerigi_buton.setStyleSheet("background-color: gray ; ")
