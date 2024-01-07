from PyQt5.QtWidgets import QWidget,QLabel,QMessageBox ,QComboBox,QVBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize, Qt
import json

class GorevSilme(QWidget):
    def __init__(self):
        super().__init__()
        with open("data.json", "r", encoding="utf-8") as dosya:
            try:
                json_verisi = json.load(dosya)
            except json.JSONDecodeError:
                json_verisi = []
        sozluk_sayisi = len(json_verisi)
        print(f"JSON dosyasındaki sözlük sayısı: {sozluk_sayisi}")
        if sozluk_sayisi==0:
            QMessageBox.warning(self, "Uyarı", "Silinecek görev bulunamadı. Lütfen görev ekleyin.")
            self.close()
        
        else:
            vbox=QVBoxLayout()
            self.setWindowTitle("Görev Silme")
            self.setWindowIcon(QIcon("toDoList.png"))
            self.setFixedSize(400,150)
            self.setStyleSheet("background-color:  #FF3D3D;")
            label = QLabel("Hangi görevi silmek istiyorsunuz?")
            label.setFixedSize(QSize(350,30))
            label.setStyleSheet("font-size: 17px; font-weight: 600;")
            self.combobox=QComboBox(self)
            self.combobox.setFixedSize(QSize(350,30))
            for sozluk in json_verisi: 
                for gorev_adi in sozluk.keys():
                        self.combobox.addItem(gorev_adi)

            self.combobox.activated.connect(lambda _, json_verisi=json_verisi: self.silinecek_gorev(json_verisi))
            """
            self.combobox.currentIndexChanged.connect( lambda _, json_verisi=json_verisi : self.silinecek_gorev(json_verisi))
            activated olayı, bir QComboBox öğesinde bir öğe seçildiğinde tetiklenen bir olaydır. Diğer yandan currentIndexChanged olayı, seçilen öğe değiştiğinde her defasında tetiklenir, yani bir öğe seçildiğinde veya öğenin durumu değiştiğinde çağrılır.
            Dolayısıyla, activated olayı, sadece bir öğe seçildiğinde işlem yapmak istediğinizde kullanışlıdır. currentIndexChanged olayı ise öğenin durumu her değiştiğinde, yani seçim yapılıp yapılmadığına bakılmaksızın her değiştiğinde tetiklenir.
            Kodunuzda activated kullanılması durumunda, sadece bir öğe seçildiğinde silinecek_gorev metodunun çağrılmasını sağlamış olduk. Bu sayede, bir görevi sildikten sonra bir sonraki görevi sormak için tekrar çağrılmayacak ve sorun giderilmiş olacaktır.
            """
            vbox.addWidget(label,alignment=Qt.AlignmentFlag.AlignCenter)
            vbox.addWidget(self.combobox,alignment=Qt.AlignmentFlag.AlignCenter)
            self.setLayout(vbox)  

    def silinecek_gorev(self,json_verisi):
        silinecek_gorev_adi=self.combobox.currentText()
        for veri in json_verisi: 
            for gorev_adi , gorev_bilgileri in veri.items():
                if silinecek_gorev_adi==gorev_adi:
                    yanit = QMessageBox.question(self,"Görev Silme",f"{gorev_adi} silinicektir. Onaylıyor musunuz?",QMessageBox.Yes, QMessageBox.No)
                    if yanit == QMessageBox.Yes:
                        QMessageBox.information(self,"Görev Silme","Görev Başarıyla Silindi")
                        silinecek_sozluk = veri
                        self.combobox.removeItem(self.combobox.findText(gorev_adi))
                        json_verisi.remove(silinecek_sozluk)
                        with open("data.json", "w", encoding="utf-8") as dosya:
                            json.dump(json_verisi, dosya, ensure_ascii=False, indent=2)
                    else:
                        QMessageBox.information(self,"Görev Silinmedi","Görev Silinmedi")   

                    self.close()