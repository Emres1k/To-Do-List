from PyQt5.QtWidgets import QWidget,QLabel,QMessageBox,QComboBox,QVBoxLayout,QHBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize, Qt
import json

class GorevTamamlama(QWidget):
    def __init__(self):
        super().__init__()
        with open("data.json", "r", encoding="utf-8") as dosya:
            try:
                json_verisi = json.load(dosya)
            except json.JSONDecodeError:
                json_verisi = []
        sozluk_sayisi = len(json_verisi)
        if sozluk_sayisi==0:
            QMessageBox.warning(self, "Uyarı", "Tamamlanacak görev bulunamadı. Lütfen görev ekleyin.")
            self.close()

        else:
            vbox=QVBoxLayout()
            self.setWindowTitle("Görev Tamamlama")
            self.setWindowIcon(QIcon("toDoList.png"))
            self.setFixedSize(400,150)
            self.setStyleSheet("background-color:  #FF3D3D;")
            label = QLabel("Hangi görevi tamamlamak istiyorsunuz?")
            label.setFixedSize(QSize(350,30))
            label.setStyleSheet("font-size: 17px; font-weight: 600;")
            
            self.combobox=QComboBox(self)
            self.combobox.setFixedSize(QSize(350,30))
            for sozluk in json_verisi: 
                for gorev_adi , gorev_bilgileri in sozluk.items():
                    if gorev_bilgileri["gorev_aktifligi"] == "Aktif":
                        print("aaaaaaaa")
                        self.combobox.addItem(gorev_adi)
            if self.combobox.count()==0:
                QMessageBox.warning(self, "Uyarı", "Tamamlanacak görev bulunamadı. Lütfen görev ekleyin.")
                self.close()
            else:
                self.combobox.activated.connect( lambda _, json_verisi=json_verisi : self.tamamlanacak_gorev(json_verisi))
                hbox=QHBoxLayout()
                hbox.addWidget(label,alignment=Qt.AlignmentFlag.AlignCenter)
                vbox.addLayout(hbox)
                vbox.addWidget(self.combobox,alignment=Qt.AlignmentFlag.AlignCenter)
                self.setLayout(vbox)  


    
    def tamamlanacak_gorev(self,json_verisi):
        tamamlanacak_gorev_adi=self.combobox.currentText()
        for veri  in json_verisi: 
            for gorev_adi , gorev_bilgileri in veri.items():
                if tamamlanacak_gorev_adi==gorev_adi:
                    yanit = QMessageBox.question(self,"Görev Tamamlama",f"{gorev_adi} tamamlanacaktır. Onaylıyor musunuz?",QMessageBox.Yes, QMessageBox.No)
                    if yanit == QMessageBox.Yes:
                        gorev_bilgileri["gorev_durumu"] = "Görev Tamamlandı"
                        gorev_bilgileri["gorev_aktifligi"] = "Tamamlandı"
                        QMessageBox.information(self,"Görev Tamamlama","Görev Başarıyla Tamamlandı")
                        with open("data.json", "w", encoding="utf-8") as dosya:
                            json.dump(json_verisi, dosya, ensure_ascii=False, indent=2)
                        self.combobox.removeItem(self.combobox.findText(gorev_adi))
                        
                    else:
                        QMessageBox.information(self,"Görev Tamamlama","Görev Tamamlanmadı")

                    self.close()