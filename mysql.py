from PyQt5 import uic, QtWidgets
import mysql.connector
from reportlab.pdfgen import canvas


banco = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database = 'db_agenda'
)

def Cadastro():
    campoNome = agenda.textEdit_4
    campoEmail= agenda.textEdit_5
    campoTelefone= agenda.textEdit_2

    if agenda.checkBox.isChecked():
        tipoTelefone = 'celular'
    elif agenda.checkBox_2.isChecked():
        tipoTelefone = 'residencial'
    else:
        tipoTelefone = 'nao selecionado'
        
    bdCursor = banco.cursor()

    comando_SQL = 'INSERT INTO tb_contatos (nome, email, telefone, tipoTelefone) values (%s, %s, %s, %s)'
    dados = (str(campoNome), str(campoEmail), str(campoTelefone) , tipoTelefone)
    bdCursor.execute(comando_SQL, dados)
    banco.commit()

def main():
    Cadastro()

app = QtWidgets.QApplication([])
agenda = uic.loadUi('design.ui')
agenda.pushButton.clicked.connect(main)

agenda.show()
app.exec()



def consultarContatos():
    listarContatos.show

    cursor = banco.cursor()
    comando_SQL = 'SELECT * FROM contatos'
    cursor.execute(comando_SQL)
    contatosLidos = cursor.fetchall()
    
    listarContatos.tabelaContatos.setRowCount(len(contatosLidos))
    listarContatos.tabelaContatos.setColumnCount(5)

    for i in range (0, len(contatosLidos)):
        for f in range (0 , 5):
            listarContatos.tabelaContatos.setItem(i, f, QtWidgets.QTableWidgetItem(str(contatosLidos[i][f])))



app = QtWidgets.QApplication([])
listaContato = uic.loadUi('contatos.ui')

agenda.btnCadastro.clicked.connect(cadastrarContato)
agenda.btnConsultar.clicked.connect(consultarContatos)

listarContatos.btnGerarPdf.clicked.connect(gerarPdf)
listarContatos.btnExcluirContato.clicked.connect(excluirContato)

agenda.show()
app.exec()