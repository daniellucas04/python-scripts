# Aula 8

# Importando classe uic
import random

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication


# Funções

def challenge():
    global result
    random_number1 = random.randint(1, 10)
    random_number2 = random.randint(1, 10)
    challenge_label = "{}x{}".format(random_number1, random_number2)
    screen.challengeLabel.setText(challenge_label)

    result = random_number1 * random_number2
    responses = [result, result + random_number1, result - random_number2]
    random.shuffle(responses)

    screen.btnResponse1.setText(str(responses[0]))
    screen.btnResponse2.setText(str(responses[1]))
    screen.btnResponse3.setText(str(responses[2]))


def verify_response(button):
    global result
    global score
    user_response = button.text()

    if int(user_response) == result:
        screen.resultLabel.setStyleSheet("color: green")
        screen.resultLabel.setText("Acertou!")
        score += 1
        screen.scoreDigit.setText(str(score))
    else:
        screen.resultLabel.setStyleSheet("color: red")
        screen.resultLabel.setText("Errou!")

    challenge()


def verify1():
    verify_response(screen.btnResponse1)


def verify2():
    verify_response(screen.btnResponse2)


def verify3():
    verify_response(screen.btnResponse3)


# Criando o objeto da aplicação
app = QApplication([])

# Carregando o arquivo .ui
Form, Window = uic.loadUiType("multiply_game.ui")

# Variável (objeto) que armazena o formulário
screen = Form()
# Variável (objeto) que representa a janela
window = Window()

# Vinculando o formulário à janela
screen.setupUi(window)

# Eventos
screen.btnResponse1.clicked.connect(verify1)  # Verifica resposta do usuário
screen.btnResponse2.clicked.connect(verify2)  # Verifica resposta do usuário
screen.btnResponse3.clicked.connect(verify3)  # Verifica resposta do usuário

# Variáveis global
result = 0
score = 0

challenge()

# Executando a aplicação
window.show()
app.exec()
