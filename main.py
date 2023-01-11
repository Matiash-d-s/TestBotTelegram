import random

import telebot
from telebot import types
from random import shuffle

bot = telebot.TeleBot('5886265811:AAFyIIGaJzICuITu426SRu_9Az0nSP6cgmk')
bot.set_webhook()

agents = {
'Brimestone' : ['Пассивный','Командный игрок','Много общаюсь','Саппорт','Легкий','Скиллы'],
'Viper' : ['Пассивный','Командный игрок/Полагаюсь на себя','Много общаюсь/Молча концентрируюсь','Люркер','Сложный','Скиллы'],
'Omen' : ['Активный/Пассивный','Командный игрок/Полагаюсь на себя','Много общаюсь','Саппорт','Легкий','Скиллы'],
'Killjoy' : ['Пассивный','Командный игрок/Полагаюсь на себя','Много общаюсь/Молча концентрируюсь','Люркер','Легкий','Скиллы'],
'Cypher' : ['Пассивный','Полагаюсь на себя','Много общаюсь/Молча концентрируюсь','Люркер','Сложный','Скиллы'],
'Sova' : ['Пассивный','Командный игрок','Много общаюсь','Саппорт','Сложный','Скиллы'],
'Sage' : ['Пассивный/Активный','Полагаюсь на себя/Командный игрок','Много общаюсь','Саппорт/Керри','Легкий','Аим'],
'Phoenix' : ['Активный','Полагаюсь на себя','Много общаюсь/Молча концентрируюсь','Керри','Легкий','Скиллы'],
'Jett' : ['Активный','Полагаюсь на себя','Много общаюсь/Молча концентрируюсь','Керри','Сложный','Аим'],
'Reyna' : ['Активный','Полагаюсь на себя','Много общаюсь/Молча концентрируюсь','Керри','Легкий','Аим'],
'Raze' : ['Активный','Полагаюсь на себя/Командный игрок','Много общаюсь/Молча концентрируюсь','Керри','Сложный','Аим'],
'Breach' : ['Активный','Командный игрок','Много общаюсь','Саппорт','Легкий','Скиллы'],
'Skye' : ['Активный','Командный игрок','Много общаюсь','Саппорт','Легкий','Скиллы'],
'Yoru' : ['Активный','Командный игрок/Полагаюсь на себя','Много общаюсь/Молча концентрируюсь','Люркер/Керри','Сложный','Скиллы'],
'Astra' : ['Пассивный','Командный игрок','Много общаюсь','Саппорт','Сложный','Скиллы'],
'KAY/O' : ['Активный','Полагаюсь на себя/Командный игрок','Много общаюсь/Молча концентрируюсь','Саппорт/Керри','Легкий','Скиллы'],
'Chamber' : ['Пассивный/Активный','Полагаюсь на себя','Много общаюсь/Молча концентрируюсь','Люркер','Легкий','Аим'],
'Neon' : ['Активный','Полагаюсь на себя','Много общаюсь/Молча концентрируюсь','Керри','Сложный','Аим'],
'Fade' : ['Пассивный/Активный','Командный игрок/Полагаюсь на себя','Много общаюсь/Молча концентрируюсь','Саппорт','Сложный','Скиллы'],
'Harbor' : ['Пассивный','Командный игрок','Много общаюсь','Саппорт','Сложный','Скиллы']
}

id = 0


def make_pair(x,y):
    return lambda n: x if n==0 else y
def first_element(p):
    return p(0)

def second_element(p):
    return p(1)

first_question = "Имеется ли у вас опыт в шутерах? (н-р: CS:GO,Warface,Warzone и проч.)"
second_qeustion = "Где бы вы предпочли находиться? В гуще событий или координировать действия команды из тыла?"
third_qeustion = "Полагаетесь ли вы на своих сокомандников или чаще надеетесь только на себя?"
forth_question = "Много ли вы говорите во время игры или стараетесь оставаться немногословным?"
fifth_question = "Какой стиль ведения игры вам ближе?"
six_question = "При возникновении опастной ситуации на что вы будете полагаться: стрельба(аим) или способнойсти персонажа(скиллы)?"


first_answers = (make_pair('Да, я давно играю', 'Сложный'),
                 make_pair('Нет, я новичок в этом жанре игр', 'Легкий'),)

second_answers = (make_pair('Я люблю быть в гуще событий', 'Активный'),
                  make_pair('Нет, я координирую действия, оставаясь далеко', 'Пассивный'),
                  make_pair('И то и другое', 'Пассивный/Активный'),)

third_answers =  (make_pair('Я люблю играть в команде', 'Командный игрок'),
                  make_pair('Нет, я чаще играю один', 'Полагаюсь на себя'),
                  make_pair('Зависит от ситуации', 'Командный игрок/Полагаюсь на себя'),)

forth_answers =  (make_pair('Я люблю много общаться', 'Много общаюсь'),
                  make_pair('Нет, я предпочитаю молча концетрироваться', 'Молча концентрируюсь'),
                  make_pair('По настроению', 'Много общаюсь/Молча концентрируюсь'),)

fifth_answers =  (make_pair('Я люблю расчитывать на свои собственные силы', 'Керри'),
                  make_pair('Я предпочту реализовать проработанную тактику', 'Саппорт'),
                  make_pair('Могу пойти на риск, если это того стоит', 'Саппорт/Керри'),
                  make_pair('Я люблю принимать важные стратегические решения', 'Люркер'),)

six_answers =  (make_pair('Аим', 'Аим'),
                make_pair('Скиллы', 'Скиллы'))


question_one = make_pair(first_question,first_answers)
question_two = make_pair(second_qeustion,second_answers)
question_three = make_pair(third_qeustion,third_answers)
question_four = make_pair(forth_question,forth_answers)
question_five = make_pair(fifth_question,fifth_answers)
question_six = make_pair(six_question,six_answers)


list_of_questions = [question_one,question_two,question_three,question_four,question_five,question_six]

print(first_element(second_element(list_of_questions[id])[0]))
print(len(second_element(list_of_questions[1])))
#first_element(second_element(list_of_questions[id])[0])
keywords = []

def get_question_by_id(id):
    return list_of_questions[id]


@bot.message_handler(commands=["start"])
def get_start(message):
    global id
    global keywords
    id = 0
    #bot.clear_step_handler(message)
    keywords.clear()
    markup = types.InlineKeyboardMarkup(row_width=1)
    i = 0
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    for i in range(0,len(second_element(list_of_questions[id]))):
        keyboard.row(telebot.types.InlineKeyboardButton(first_element(second_element(list_of_questions[id])[i]),
                                                        callback_data = f"{i}"))
        #markup.add(keyboard)
        i+=1

    #keywords.append(second_element(second_element(list_of_questions[id])[i]))
    bot.send_message(message.chat.id,first_element(list_of_questions[id]), reply_markup=keyboard)

def get_next_question():
    print('a')

@bot.callback_query_handler(func = lambda call:True)
def call(call):
    global id
    global keywords
    print(id,len(list_of_questions))
    if call.data == 'restart':
        print("call.data == restart")
        id = 0
        keywords.clear()
        get_start(call.message)
        return

    if call.message:
        list_of_current_keys = []
        i = 0
        for i in range(0, len(second_element(list_of_questions[id]))):
            list_of_current_keys.append(i)
            i += 1

        print(list_of_current_keys)
        print(call.data)
        if int(call.data) in list_of_current_keys:
            print(second_element(second_element(list_of_questions[id])[int(call.data)]))
            keywords.append(second_element(second_element(list_of_questions[id])[int(call.data)]))
            id+=1
            if id == len(list_of_questions):
                print(keywords)
                best_agent = get_analize(keywords)
                print(best_agent)
                markup = types.InlineKeyboardMarkup(row_width=1)
                btn1 = types.InlineKeyboardButton("Пройти заново",
                                                      callback_data='restart')
                markup.add(btn1)
                bot.send_message(call.message.chat.id, f"Вам лучше играть на {best_agent}",
                                     reply_markup=markup)
            else:
                i = 0
                keyboard = types.InlineKeyboardMarkup(row_width=1)
                for i in range(0, len(second_element(list_of_questions[id]))):
                    keyboard.row(
                        telebot.types.InlineKeyboardButton(first_element(second_element(list_of_questions[id])[i]),
                                                               callback_data = f"{i}"))
                    i += 1
                bot.send_message(call.message.chat.id, first_element(list_of_questions[id]), reply_markup=keyboard)



@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    print("a")


def get_list_of_questions():
    shuffled_list = shuffle(list_of_questions)
    return shuffled_list

@bot.message_handler(commands=['start'])
def button(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    btn1 = types.InlineKeyboardButton(first_element(first_element(second_element(list_of_questions[id]))))
    btn2 = types.InlineKeyboardButton(first_element(second_element(second_element(list_of_questions[id]))))


def get_certain_question():
    list = get_list_of_questions()
    keyboard = telebot.types.InlineKeyboardMarkup()

    item = types.InlineKeyboardButton

def get_analize(keywords):
    global agents
    agents_score = {agent: 0 for agent in agents}
    max_score = 0
    #print(keywords)
    for key in keywords:
        for agent,features in agents.items():
            #print(agents.items())
            if key in features:
                print(agent)
                agents_score[agent] +=1
                max_score = max(agents_score[agent],max_score)
    best_agents = []
    print(agents_score)
    for agent, score in agents_score.items():
        if score == max_score:
            best_agents.append(agent)
    idx = 0
    if len(best_agents)>1:
        idx = random.randint(0,len(best_agents)-1)
    return best_agents[idx]


if __name__ == '__main__':
     bot.polling()
