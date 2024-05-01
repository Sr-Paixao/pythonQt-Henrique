from PyQt5 import uic, QtWidgets

def main():
    print('Etec')

app = QtWidgets.QApplication([])
agenda = uic.loadUi('design.ui')
agenda.pushButton.clicked.connect(main)

agenda.show()
app.exec()



