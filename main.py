import telebot

MyBot = telebot.TeleBot('5871741517:AAHcl44pBUy0s5lX_74U0-JkBHksLb1CL2w')

@MyBot.message_handler(content_types=['text'])
def replyer(message):
    MyBot.send_message(message.chat.id, WriteRecipe(message.text))
    print(message.chat.id)

def WriteRecipe(call):
    NotFound = True
    if ((call == "1") or (call == "Понедельник") or (call == "понедельник")):
        NotFound = False
        schedule = "Расписание на понедельник:\n"
        schedule = schedule + "2. Теория автоматов (10:15 - 11:45)\n"
        schedule = schedule + "3. Организация ЭВМ (12:00 - 13:30)\n"
        schedule = schedule + "4. Прикладная физическая культура (14:15 - 15:45)\n"
        schedule = schedule + "5. НИРС (16:00 - 17:30)\n"
        return schedule

    if ((call == "2") or (call == "Вторник") or (call == "вторник")):
        NotFound = False
        schedule = "Расписание на вторник:\n"
        schedule = schedule + "3. Теория автоматов (12:00 - 13:30)\n"
        schedule = schedule + "4. Организация эвм (14:15 - 15:45)\n"
        schedule = schedule + "5. Базы данных (16:00 - 17:30)\n"
        schedule = schedule + "6. Интеллектуальные системы и технологии (17:40 - 19:05)\n"
        return schedule

    if ((call == "3") or (call == "Среда") or (call == "среда")):
        NotFound = False
        schedule = "Расписание на среду:\n"
        schedule = schedule + "2. Системотехника и системология (10:15 - 11:45)\n"
        schedule = schedule + "3. Базы данных (12:00 - 13:30)\n"
        schedule = schedule + "4. Базы данных (14:15 - 15:45)\n"
        return schedule

    if ((call == "4") or (call == "Четверг") or (call == "четверг")):
        NotFound = False
        schedule = "Расписание на четверг:\n"
        schedule = schedule + "3. Технологии разработки программного обеспечения (12:00 - 13:30)\n"
        schedule = schedule + "4. Технологии разработки программного обеспечения (14:15 - 15:45)\n"
        return schedule

    if ((call == "5") or (call == "Пятница") or (call == "пятница")):
        NotFound = False
        schedule = "Расписание на пятницу:\n"
        schedule = schedule + "Пар нет!\n"
        return schedule

    if ((call == "6") or (call == "Суббота") or (call == "суббота")):
        NotFound = False
        schedule = "Расписание на субботу:\n"
        schedule = schedule + "1. Интеллектуальные системы и технологии (8:30 - 10:00)\n"
        return schedule

    if ((call == "7") or (call == "Воскресенье") or (call == "воскресенье")):
        NotFound = False
        schedule = "Расписание на воскресенье:\n"
        schedule = schedule + "Пар нет!\n"
        return schedule

    if (NotFound):
        return "Нет такого дня недели!"

MyBot.polling()