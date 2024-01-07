import sys


from PyQt5.QtWidgets import QApplication
from girisEkrani import GirisEkrani

app=QApplication(sys.argv)
girisEkrani=GirisEkrani()
girisEkrani.show()


sys.exit(app.exec_())
"""
kullanıcı adı : user
şifre : admin

"""