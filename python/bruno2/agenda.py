from PyQt5 import uic, QtWidgets
import mysql.connector
from reportlab.pdfgen import canvas

db = mysql.connector.connect(
    host = "localhost",
    user = "root", 
    password = "",
    database= "agenda"
)
def main():
    print("etec")



def cadastro():
    nome = agenda.le_nome.text()
    email = agenda.le_email.text()
    telefone = agenda.le_telefone.text()
    
    if agenda.le_residencial.isChecked():
        tipoTelefone = "R"
    else: 
        tipoTelefone= "C"

    cursor = db.cursor()
    query_sql= "insert into contatos(nome,email,telefone,tipoTelefone) values (%s, %s,%s, %s)"
    data = (str(nome), str(email), str(telefone), tipoTelefone)
    cursor.execute(query_sql, data)
    db.commit()
    
app= QtWidgets.QApplication([])
agenda=uic.loadUi("agenda.ui")
agenda.btnCadastro.clicked.connect(cadastro)
agenda.show()
app.exec()
