from PyQt5 import uic, QtWidgets
import mysql.connector
from reportlab.pdfgen import canvas

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "db_agenda"
)

    
def cadastro():
    nome = agenda.leNome.text()
    email = agenda.leEmail.text()
    telefone = agenda.leTelefone.text()
    
    if agenda.rbRecidencial.isChecked():
        tipoTelefone = "R"
    else: tipoTelefone = "C"
    
    cursor = db.cursor()
    comandoSQL = "insert into contatos (nome, email, telefone, tipoTelefone) values (%s, %s, %s, %s)"
    dados = (str(nome), str(email), str(telefone), tipoTelefone)
    cursor.execute(comandoSQL, dados)
    db.commit()

def consultar():
    listarContatos.show()
    
    cursor = db.cursor()
    comandoSQL = "select * from tb_contatos"
    cursor.execute(comandoSQL)
    contatosLidos = cursor.fetchall()
    
    listarContatos.tabelaContatos.setRowCount(len(contatosLidos))
    listarContatos.tabelaContatos.setColumnCount(5)
    
    for i in range (0, len(contatosLidos)):
        for f in range(0,5):
            listarContatos.tabelaContatos.setItem(i, f, QtWidgets.QTableWidgetItem(str(contatosLidos[i][f])))

app=QtWidgets.QApplication([])
agenda=uic.loadUi('agenda.ui')
listarContatos=uic.loadUi('contatos.ui')

agenda.btnCadastro.clicked.connect(cadastro)
agenda.btnConsultar.clicked.connect(consultar)

# listarContatos.btnGerarPdf.cliked.connect(gerarPdf)
# listarContatos.btnExcluirContato.cliked.connect(excluirContato)

agenda.show()
app.exec()
