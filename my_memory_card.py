from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from random import shuffle

class Question():
    def __init__(self, question, rightanswer, wronganswer1, wronganswer2, wronganswer3):
        self.question = question
        self.rightanswer = rightanswer
        self.wronganswer1 = wronganswer1
        self.wronganswer2 = wronganswer2
        self.wronganswer3 = wronganswer3

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
app = QApplication([])
window = QWidget()
window.resize(400,200)
window.setWindowTitle('Memory Card')
window.total = 0
window.score = 0

options = QGroupBox('Варианты ответов')
option1 = QRadioButton('Энцы')
option2 = QRadioButton('Смурфы')
option3 = QRadioButton('Чулымцы')
option4 = QRadioButton('Алеуты')
optionsgroup = QButtonGroup()
optionsgroup.addButton(option1)
optionsgroup.addButton(option2)
optionsgroup.addButton(option3)
optionsgroup.addButton(option4)

afteranswer = QGroupBox('Результат теста')
result = QLabel('Правильно/Неправильно')
correctanswer = QLabel('Правильный объект')

vlayout_afteranswer = QVBoxLayout()

hlayout_options = QHBoxLayout()
vlayout_options1 = QVBoxLayout()
vlayout_options2 = QVBoxLayout()

vlayout_options1.addWidget(option1)
vlayout_options1.addWidget(option2)
vlayout_options2.addWidget(option3)
vlayout_options2.addWidget(option4)
hlayout_options.addLayout(vlayout_options1)
hlayout_options.addLayout(vlayout_options2)

vlayout_afteranswer.addWidget(result)
vlayout_afteranswer.addWidget(correctanswer, alignment=Qt.AlignHCenter)


options.setLayout(hlayout_options)
afteranswer.setLayout(vlayout_afteranswer)

question = QLabel('Какой национальности не существует?')
hlayout_question = QHBoxLayout()
hlayout_question.addWidget(question, alignment=Qt.AlignHCenter)

hlayout_forgroupbox = QHBoxLayout()
hlayout_forgroupbox.addWidget(options)
hlayout_forgroupbox.addWidget(afteranswer)
afteranswer.hide()

answerbutton = QPushButton('Ответить')
hlayout_answerbutton = QHBoxLayout()
hlayout_answerbutton.addStretch(1)
hlayout_answerbutton.addWidget(answerbutton, stretch = 2)
hlayout_answerbutton.addStretch(1)

vlayout_core = QVBoxLayout()

vlayout_core.addLayout(hlayout_question)
vlayout_core.addLayout(hlayout_forgroupbox)
vlayout_core.addLayout(hlayout_answerbutton)
vlayout_core.setSpacing(20)

window.setLayout(vlayout_core)

answers = [option1, option2, option3, option4]


def show_result():
    options.hide()
    afteranswer.show()
    answerbutton.setText('Следующий вопрос')

def show_question():
    afteranswer.hide()
    options.show()
    answerbutton.setText('Ответить')
    optionsgroup.setExclusive(False)
    option1.setChecked(False) 
    option2.setChecked(False)
    option3.setChecked(False) 
    option4.setChecked(False)
    optionsgroup.setExclusive(True)

def show_correct(alo):
    result.setText(alo)
    show_result()



def ask(q):
    shuffle(answers)
    answers[0].setText(q.rightanswer)
    answers[1].setText(q.wronganswer1)
    answers[2].setText(q.wronganswer2)
    answers[3].setText(q.wronganswer3)
    question.setText(q.question)
    correctanswer.setText(q.rightanswer)
    show_question()

def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно!')
        window.score += 1
    else:
        show_correct('Неправильно!')
    print('СТАТИСТИКА')
    print('-ВСЕГО ВОПРОСОВ: ', window.total)
    print('-ПРАВИЛЬНЫХ ОТВЕТОВ: ', window.score)
    print('РЕЙТИНГ: ', window.score / window.total * 100)

questions = []
question1 = Question('1 Как зовут первого второго третьего?', 'второй третий', 'третий II', 'первый второй третий', 'нет верного ответа')
questions.append(question1)
question2 = Question('2 Как зовут первого второго третьего?', 'второй третий', 'третий II', 'первый второй третий', 'нет верного ответа')
questions.append(question2)
question3 = Question('3 Как зовут первого второго третьего?', 'второй третий', 'третий II', 'первый второй третий', 'нет верного ответа')
questions.append(question3)
question4 = Question('4 Как зовут первого второго третьего?', 'второй третий', 'третий II', 'первый второй третий', 'нет верного ответа')
questions.append(question4)
question5 = Question('5 Как зовут первого второго третьего?', 'второй третий', 'третий II', 'первый второй третий', 'нет верного ответа')
questions.append(question5)
question6 = Question('6 Как зовут первого второго третьего?', 'второй третий', 'третий II', 'первый второй третий', 'нет верного ответа')
questions.append(question6)
question7 = Question('7 Как зовут первого второго третьего?', 'второй третий', 'третий II', 'первый второй третий', 'нет верного ответа')
questions.append(question7)
shuffle(questions)


def next_question():
    window.total += 1
    if window.total == 7:
        print('вопросов нет, дружище')
    else:
        currentquestion = questions[window.total - 1]
        ask(currentquestion)
        print('-ВСЕГО ВОПРОСОВ: ', window.total)
        print('-ПРАВИЛЬНЫХ ОТВЕТОВ: ', window.score)

def click_ok():
    if 'Ответить' == answerbutton.text():
        check_answer()
    else:
        next_question()


answerbutton.clicked.connect(click_ok)
next_question()
window.show()
app.exec_()
