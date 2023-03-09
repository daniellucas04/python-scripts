# Aula 7 - Trabalhando com janelas gráficas

# Importando classe uic
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMessageBox


# Funções

def exit_program():
    exit()


def action_new():
    screen.rotulo.setText("Ação 'Novo' acionado")


def help_message():
    message = QMessageBox(window)
    message.setWindowTitle("Ajuda!")
    message.setText(
        "Os botões existem para efetuar uma ação. Descubra o que cada um faz clicando neles ou leia a lista de funções neste site: https://website.com.br/btnFunctions!")
    message.setIcon(QMessageBox.Question)
    message.addButton(QMessageBox.Ok).setText("De nada!")
    message.exec()  # Mostra caixa de diálogo


# Criando o objeto da aplicação
app = QApplication([])

# Carregando o arquivo .ui
Form, Window = uic.loadUiType("janela.ui")

# Variável (objeto) que armazena o formulário
screen = Form()
# Variável (objeto) que representa a janela
window = Window()

# Vinculando o formulário à janela
screen.setupUi(window)

# Adicionar eventos
screen.btnFechar.clicked.connect(exit_program)
screen.actionButtonHelp.triggered.connect(help_message)
# Alterar texto do rótulo
screen.rotulo.setText("Aperte um dos botões")

screen.actionNovo.triggered.connect(action_new)

window.show()
# Executando a aplicação
app.exec()
