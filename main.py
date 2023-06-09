import telebot
from telebot import types
import random
from random import choice
import os
import time
import pickle

print("Бот запущен")
# start command


bot = telebot.TeleBot('5838139796:AAG8THb1NY22eb9fliLHHBsjzNAemtPSIFk')



def add_user_to_list(user_id):
    try:
        with open('user_list.pickle.txt', 'rb') as f:
            user_list = pickle.load(f)
    except FileNotFoundError:
        user_list = []
    if user_id not in user_list:
        user_list.append(user_id)
        with open('user_list.pickle.txt', 'wb') as f:
            pickle.dump(user_list, f)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_chat_action(message.chat.id, 'typing')
    time.sleep(2)
    add_user_to_list(message.from_user.id)
    bot.send_message(message.chat.id, 'Вітаю {0.first_name}! \nЩоб почати тестування відправте команлу /test'.format(
        message.from_user, bot.get_me()), parse_mode='html')


def send_message_to_all_users(text):
    with open('user_list.pickle.txt', 'rb') as f:
        user_list = pickle.load(f)
    for user_id in user_list:
        bot.send_message(user_id, text)


@bot.message_handler(commands=['send'])
def send_handler(message):
    admins = [1899500715, 796675939, 1686685747, 242694200, 799759968, 796303579, 403927852, 627754650, 977149977, 697885027]  # список разрешенных пользователей
    if message.from_user.id not in admins:
        bot.send_message(message.chat.id, 'Ви не маєте права використовувати цю команду.')
        return
    
    text = message.text[6:]  # Убираем команду "/send "
    send_message_to_all_users(text)
    bot.send_message(message.chat.id, 'Повідомлення відправлено')


@bot.message_handler(commands=['feedback'])
def start_message(message):

    bot.send_chat_action(message.chat.id, 'typing')
    time.sleep(2)
    bot.send_message(message.chat.id, text="У тебе з'явилися питання чи пропозиції? Тоді напиши команді підтримки,для цього використай цей шаблон:\n forward : *Твій текст* ",
                     disable_notification=True)  # Отвечаем на сообщение



# Функция для обработки ответа на вопрос

questions = [
    {
        'text': 'Яка тканина зображена на фото?',
        'photo': 'pic/мезотелій.jpg',
        'answers': ['Багатошаровий незроговілий плоский епітелій ', 'Мезотелій', 'Миготливий епітелій'],
        'correct_answer': 'Мезотелій',
        'incorrent': ['Багатошаровий незроговілий плоский епітелій ', 'Миготливий епітелій']
    },
    {
        'text': 'Назва тканини зображенної на фото',
        'photo': 'pic/миготливий_епітелій.jpg',
        'answers': ['Миготливий епітелій', 'Одношаровий циліндричний епітелій', 'Одношаровий багаторядний війчастий епітелій'],
        'correct_answer': 'Миготливий епітелій',
        'incorrent': ['Одношаровий циліндричний епітелій', 'Одношаровий багаторядний війчастий епітелій']
    },
    {
        'text': 'Назвіть тканину зображену на фото',
        'photo': 'pic/багатошаровий_нпе.jpg',
        'answers': ['Багатошаровий незроговілий плоский епітелій', 'Перехідний епітелій', 'Багатошаровий зроговілий плоский'],
        'correct_answer': 'Багатошаровий незроговілий плоский епітелій',
        'incorrent': ['Перехідний епітелій', 'Багатошаровий зроговілий плоский']
    },
    {
        'text': 'Яка тканина зображена на фото?',
        'photo': 'pic/одношаровий_це.jpg',
        'answers': ['Одношаровий циліндричний епітелій', 'Одношаровий багаторядний війчастий епітелій', 'Багатошаровий зроговілий плоский епітелій'],
        'correct_answer': 'Одношаровий циліндричний епітелій',
        'incorrent': ['Одношаровий багаторядний війчастий епітелій', 'Багатошаровий зроговілий плоский епітелій']
    },
    {
        'text': 'Назвіть тканину зображену на фото',
        'photo': 'pic/одношаровийбве.jpg',
        'answers': ['Одношаровий багаторядний війчастий епітелій', 'Сальна залоза шкіри людини', 'Мазок крові людини'],
        'correct_answer': 'Одношаровий багаторядний війчастий епітелій',
        'incorrent': ['Сальна залоза шкіри людини', 'Мазок крові людини']
    },
    {
        'text': 'Яка назва цієї тканини?',
        'photo': 'pic/Багатошаровийзпе.jpg',
        'answers': ['Багатошаровий зроговілий плоский епітелій', 'Перехідний епітелій', 'Щільна неоформлена сполучна тканина сітчастого шару шкіри'],
        'correct_answer': 'Багатошаровий зроговілий плоский епітелій',
        'incorrent': ['Перехідний епітелій', 'Щільна неоформлена сполучна тканина сітчастого шару шкіри']
    },
    {
        'text': 'Назвіть тканину зображену на фото',
        'photo': 'pic/Перехіднийесм.jpg',
        'answers': ['Перехідний епітелій сечового міхура', 'Еластична хрящова тканина.Зона охрястя', 'Волокниста хрящова тканина'],
        'correct_answer': 'Перехідний епітелій сечового міхура',
        'incorrent': ['Еластична хрящова тканина.Зона охрястя', 'Волокниста хрящова тканина.']
    },
    {
        'text': 'Яка назва цієї тканини?',
        'photo': 'pic/одношаровийкце.jpg',
        'answers': ['Одношаровий кубічний і циліндричний епітелій', 'Перехідний епітелій сечового міхур', 'Зелена залоза рака'],
        'correct_answer': 'Одношаровий кубічний і циліндричний епітелій',
        'incorrent': ['Перехідний епітелій сечового міхур', 'Зелена залоза рака']
    },
    {
        'text': 'Яка назва цієї тканини?',
        'photo': 'pic/простіальвеолярнібз.jpg',
        'answers': ['Прості альвеолярні білкові залози', 'Зелена залоза рака', 'Сальна залоза шкіри людини'],
        'correct_answer': 'Прості альвеолярні білкові залози',
        'incorrent': ['Зелена залоза рака', 'Сальна залоза шкіри людини']
    },
    {
        'text': 'Назвіть тканину зображену на фото',
        'photo': 'pic/щитоподібназс.jpg',
        'answers': ['Прості альвеолярні білкові залози', 'Щитовидна залоза собаки', 'Фібробласти клітини неправильної видовженої форми'],
        'correct_answer': 'Щитовидна залоза собаки',
        'incorrent': ['Прості альвеолярні білкові залози', 'Фібробласти клітини неправильної видовженої форми']
    },
    {
        'text': 'Яка назва цієї тканини?',
        'photo': 'pic/зеленазалозар.jpg',
        'answers': ['Зелена залоза рака', 'Щитовидна залоза собаки', 'Сальна залоза шкіри людини'],
        'correct_answer': 'Зелена залоза рака',
        'incorrent': ['Щитовидна залоза собаки', 'Сальна залоза шкіри людини']
    },
    {
        'text': 'Назвіть тканину зображену на фото',
        'photo': 'pic/сальназшл.jpg',
        'answers': ['Сальна залоза шкіри людини', 'Моноцити', 'Пухка сполучна тканина'],
        'correct_answer': 'Сальна залоза шкіри людини',
        'incorrent': ['Моноцити', 'Пухка сполучна тканина']
    },
    {
        'text': 'Що зображено на фото?',
        'photo': 'pic/моноцити.jpg',
        'answers': ['Сальна залоза шкіри людини', 'Моноцити', 'Базофіли'],
        'correct_answer': 'Моноцити',
        'incorrent': ['Сальна залоза шкіри людини', 'Базофіли']
    },
    {
        'text': 'Назвіть тканину зображену на фото',
        'photo': 'pic/Базофіли.jpg',
        'answers': ['Базофіли', 'Нейтрофіли', 'Моноцити'],
        'correct_answer': 'Базофіли',
        'incorrent': ['Нейтрофіли', 'Моноцити']
    },
    {
        'text': 'Назвіть тканину зображену на фото',
        'photo': 'pic/нейрофіли.jpg',
        'answers': ['Нейтрофіли', 'Моноцити', 'Базофіли'],
        'correct_answer': 'Нейтрофіли',
        'incorrent': ['Моноцити', 'Базофіли']
    },
    {
        'text': 'Назва цього препарату',
        'photo': 'pic/мазоккл.jpg',
        'answers': ['Мазок крові людини', 'Еозинофіли', 'Багатошаровий зроговілий плоский епітелій'],
        'correct_answer': 'Мазок крові людини',
        'incorrent': ['Багатошаровий зроговілий плоский епітелій', 'Еозинофіли']
    },
    {
        'text': 'Що зображено на фото?',
        'photo': 'pic/мазоккж.jpg',
        'answers': ['Мазок крові жаби', 'Щільна неоформлена сполучна тканина шкіри', 'Жирова тканина'],
        'correct_answer': 'Мазок крові жаби',
        'incorrent': ['Щільна неоформлена сполучна тканина шкіри', 'Жирова тканина']
    },
    {
        'text': 'Назвіть тканину зображену на фото',
        'photo': 'pic/мазоккровіл2.jpg',
        'answers': ['Мазок крові людини', 'Нейроглія білої речовини спинного мозку', 'Псевдоуніполярний нейрон спинномозкового ганглію'],
        'correct_answer': 'Мазок крові людини',
        'incorrent': ['Нейроглія білої речовини спинного мозку', 'Псевдоуніполярний нейрон спинномозкового ганглію']
    },
    {
        'text': 'Яка назва цього препарату?',
        'photo': 'pic/Еозинофіли.jpg',
        'answers': ['Еозинофіли', 'Лімфоцити', 'Базофіли'],
        'correct_answer': 'Еозинофіли',
        'incorrent': ['Лімфоцити', 'Базофіли']
    },
    {
        'text': 'Яка назва цього препарату?',
        'photo': 'pic/Лімфоцити.jpg',
        'answers': ['Лімфоцити', 'Еритроцити', 'Ретикулярні тканина у складі кровотворних органів'],
        'correct_answer': 'Лімфоцити',
        'incorrent': ['Еритроцити', 'Ретикулярні тканина у складі кровотворних органів']
    },
    {
        'text': 'Назвіть тканину зображену на фото',
        'photo': 'pic/Еритроцити.jpg',
        'answers': ['Еритроцити', 'Щільна неоформлена сполучна тканина шкіри', 'Сухожилля теляти у поздовжньому розрізі'],
        'correct_answer': 'Еритроцити',
        'incorrent': ['Щільна неоформлена сполучна тканина шкіри', 'Сухожилля теляти у поздовжньому розрізі']
    },
    {
        'text': 'Назвіть тканину зображену на фото',
        'photo': 'pic/пухкаст.jpg',
        'answers': ['Пухка сполучна тканина', 'Щільна неоформлена сполучна тканина шкіри', 'Епіфізарна пластинка'],
        'correct_answer': 'Пухка сполучна тканина',
        'incorrent': ['Щільна неоформлена сполучна тканина шкіри', 'Епіфізарна пластинка']
    },
    {
        'text': 'Дайте назву цьому пррепарату',
        'photo': 'pic/щільнанеоформлена.jpg',
        'answers': ['Пухка сполучна тканина', 'Щільна неоформлена сполучна тканина сітчастого шару шкіри', 'Ультраструктура колагенової фібрили із сухожилля щура'],
        'correct_answer': 'Щільна неоформлена сполучна тканина сітчастого шару шкіри',
        'incorrent': ['Пухка сполучна тканина', 'Ультраструктура колагенової фібрили із сухожилля щура']
    },
    {
        'text': 'Назвіть тканину зображену на фото',
        'photo': 'pic/щільнанфстщ.jpg',
        'answers': ['Щільна неоформлена сполучна тканина шкіри', 'Сухожилля теляти у поздовжньому розрізі', 'Еластична зв’язка бика'],
        'correct_answer': 'Щільна неоформлена сполучна тканина шкіри',
        'incorrent': ['Сухожилля теляти у поздовжньому розрізі', 'Еластична зв’язка бика']
    },
    {
        'text': 'Назвіть тканину зображену на фото',
        'photo': 'pic/сухожилятупр.jpg',
        'answers': ['Сухожилля теляти у поздовжньому розрізі', 'Пігментна тканина шкіри пуголовка', 'Гіаліновий хрящ ребра кроля'],
        'correct_answer': 'Сухожилля теляти у поздовжньому розрізі',
        'incorrent': ['Пігментна тканина шкіри пуголовка', 'Гіаліновий хрящ ребра кроля']
    },
    {
        'text': 'Назвіть тканину зображену на фото',
        'photo': 'pic/ультраструктура.jpg',
        'answers': ['Ультраструктура колагенової фібрили із сухожилля щура', 'Еластична зв’язка бика', 'Сухожилля теляти у поздовжньому розрізі'],
        'correct_answer': 'Ультраструктура колагенової фібрили із сухожилля щура',
        'incorrent': ['Сухожилля теляти у поздовжньому розрізі', 'Еластична зв’язка бика']
    },
    {
        'text': 'Назвіть тканину зображену на фото',
        'photo': 'pic/еластичназб.jpg',
        'answers': ['Еластична зв’язка бика', 'Ультраструктура колагенових волокон', 'Щільна неоформлена волокниста сполучна тканина.'],
        'correct_answer': 'Еластична зв’язка бика',
        'incorrent': ['Щільна неоформлена волокниста сполучна тканина.', 'Ультраструктура колагенових волокон']
    },
    {
        'text': 'Назвіть тканину зображену на фото',
        'photo': 'pic/Жироватканина.jpg',
        'answers': ['Пухка сполучна тканина', 'Сухожилля теляти у поздовжньому розрізі', 'Жирова тканина'],
        'correct_answer': 'Жирова тканина',
        'incorrent': ['Пухка сполучна тканина', 'Сухожилля теляти у поздовжньому розрізі']
    },
    {
        'text': 'Назвіть тканину зображену на фото',
        'photo': 'pic/ретикулярна.jpg',
        'answers': ['Жирова тканина', 'Ретикулярні тканина у складі кровотворних органів', 'Пігментна тканина шкіри пуголовка'],
        'correct_answer': 'Ретикулярні тканина у складі кровотворних органів',
        'incorrent': ['Пігментна тканина шкіри пуголовка', 'Жирова тканина']
    },
    {
        'text': 'Назвіть тканину зображену на фото',
        'photo': 'pic/пігмент.jpg',
        'answers': ['Ретикулярні тканина у складі кровотворних органів', 'Пігментна тканина шкіри пуголовка', 'Жирова тканина'],
        'correct_answer': 'Пігментна тканина шкіри пуголовка',
        'incorrent': ['Ретикулярні тканина у складі кровотворних органів', 'Жирова тканина']
    },
    {
        'text': 'Назвіть тканину зображену на фото',
        'photo': 'pic/сухожилля.jpg',
        'answers': ['Сухожилля теляти у поздовжньому розрізі', 'Еластичний хрящ вушної раковини свині', 'Кісткові клітини зябрової кришки оселедця'],
        'correct_answer': 'Сухожилля теляти у поздовжньому розрізі',
        'incorrent': ['Еластичний хрящ вушної раковини свині', 'Кісткові клітини зябрової кришки оселедця']
    },
    {
        'text': 'Назвіть тканину зображену на фото',
        'photo': 'pic/Гіаліновийхрк.jpg',
        'answers': ['Кісткові клітини зябрової кришки оселедця', 'Остеоцит', 'Гіаліновий хрящ ребра кроля'],
        'correct_answer': 'Гіаліновий хрящ ребра кроля',
        'incorrent': ['Кісткові клітини зябрової кришки оселедця', 'Остеоцит']
    },
    {
        'text': 'Назвіть тканину зображену на фото',
        'photo': 'pic/шггхзк.jpg',
        'answers': ['Ізогенні групи гіалінового хряща ребра кроля', 'Гомілкова кістка людини в поперечному розрізі', 'Одношаровий циліндричній облямований епітелій жовчного міхура'],
        'correct_answer': 'Ізогенні групи гіалінового хряща ребра кроля',
        'incorrent': ['Одношаровий циліндричній облямований епітелій жовчного міхура', 'Гомілкова кістка людини в поперечному розрізі']
    },
    {
        'text': 'Назвіть тканину зображену на фото',
        'photo': 'pic/ехврс.jpg',
        'answers': ['Ізогенні групи гіалінового хряща ребра кроля', 'Еластичний хрящ вушної раковини свині', 'Волокнистий хрящ міжхребцевого диску теляти'],
        'correct_answer': 'Еластичний хрящ вушної раковини свині',
        'incorrent': ['Ізогенні групи гіалінового хряща ребра кроля', 'Волокнистий хрящ міжхребцевого диску теляти']
    },
    {
        'text': 'Яка тканина зображена на фото?',
        'photo': 'pic/еластичнийхврс.jpg',
        'answers': ['Волокнистий хрящ міжхребцевого диску теляти', 'Еластичний хрящ вушної раковини свині', 'Остеоцити у пластинках остеону'],
        'correct_answer': 'Еластичний хрящ вушної раковини свині',
        'incorrent': ['Волокнистий хрящ міжхребцевого диску теляти', 'Остеоцити у пластинках остеону']
    },
    {
        'text': 'Визначте назву препарату',
        'photo': 'pic/волокнистийхмдт.jpg',
        'answers': ['Волокнистий хрящ міжхребцевого диску теляти', 'Гомілкова кістка людини в поперечному розрізі', 'Розвиток кістки на місці мезенхіми'],
        'correct_answer': 'Волокнистий хрящ міжхребцевого диску теляти',
        'incorrent': ['Гомілкова кістка людини в поперечному розрізі', 'Розвиток кістки на місці мезенхіми']
    },
    {
        'text': 'Яка назва цїєї тканини?',
        'photo': 'pic/прнмнв.jpg',
        'answers': ['Перехват Ранв’є на мієліновому нервовому волокні.', 'Астроцити', 'Мультиполярний нейрон у сірій речовині мозку'],
        'correct_answer': 'Перехват Ранв’є на мієліновому нервовому волокні.',
        'incorrent': ['Астроцити', 'Мультиполярний нейрон у сірій речовині мозку']
    },
    {
        'text': 'Назвіть цей препарат',
        'photo': 'pic/Мієлінове_нервове_волокно.jpg',
        'answers': ['Астроцити', 'Мієлінове нервове волокно', 'Спинномозковий вузол кішки'],
        'correct_answer': 'Мієлінове нервове волокно',
        'incorrent': ['Астроцити', 'Спинномозковий вузол кішки']
    },
    {
        'text': 'Назвіть тканину зображену на фото',
        'photo': 'pic/Астроцити.jpg',
        'answers': ['Мієлінове нервове волокно', 'Астроцити', 'Остеоцит'],
        'correct_answer': 'Астроцити',
        'incorrent': ['Мієлінове нервове волокно', 'Остеоцит']
    },
    {
        'text': 'Яка назва зображеного на фото препарату?',
        'photo': 'pic/Нейроглія_білої речовини_спинного_мозку.jpg',
        'answers': ['Остеоцит', 'Нейроглія білої речовини спинного мозку', 'Мультиполярний нейрон у сірій речовині мозку'],
        'correct_answer': 'Нейроглія білої речовини спинного мозку',
        'incorrent': ['Мультиполярний нейрон у сірій речовині мозку', 'Остеоцит']
    },
    {
        'text': 'Назвіть тканину зображену на фото',
        'photo': 'pic/мультипн.jpg',
        'answers': ['Нейроглія білої речовини спинного мозку', 'Мультиполярний нейрон у сірій речовині мозку', 'Псевдоуніполярний нейрон спинномозкового ганглію'],
        'correct_answer': 'Мультиполярний нейрон у сірій речовині мозку',
        'incorrent': ['Нейроглія білої речовини спинного мозку', 'Псевдоуніполярний нейрон спинномозкового ганглію']
    },
    {
        'text': 'Назвіть тканину зображену на фото',
        'photo': 'pic/псевдополярний.jpg',
        'answers': ['Псевдоуніполярний нейрон спинномозкового ганглію', 'Тигроїд', 'Волокнистий хрящ міжхребцевого диску теляти'],
        'correct_answer': 'Псевдоуніполярний нейрон спинномозкового ганглію',
        'incorrent': ['Тигроїд', 'Волокнистий хрящ міжхребцевого диску теляти']
    },
    {
        'text': 'Яка назва цієї тканини?',
        'photo': 'pic/схема.jpg',
        'answers': ['Тигроїд', 'Схема ультраструктурної будови перикаріона нейроцита', 'Поперечно-посмугована серцева м’язова тканина'],
        'correct_answer': 'Схема ультраструктурної будови перикаріона нейроцита',
        'incorrent': ['Тигроїд', 'Поперечно-посмугована серцева м’язова тканина']
    },
    {
        'text': 'Назвіть тканину зображену на фото',
        'photo': 'pic/Тигроїд.jpg',
        'answers': ['Тигроїд', 'Поперечно-посмугована скелетна м’язова тканина', ''],
        'correct_answer': 'Тигроїд',
        'incorrent': ['Поперечно-посмугована скелетна м’язова тканина', '']
    },
    {
        'text': 'Назвіть тканину зображену на фото',
        'photo': 'pic/ппс.jpg',
        'answers': ['Поперечно-посмугована скелетна м’язова тканина', 'Поперечно-посмугована серцева м’язова тканина', 'Гладенька м’язова тканина'],
        'correct_answer': 'Поперечно-посмугована серцева м’язова тканина',
        'incorrent': ['Поперечно-посмугована скелетна м’язова тканина', 'Гладенька м’язова тканина']
    },
    {
        'text': 'Назвіть тканину зображену на фото',
        'photo': 'pic/ппсп.jpg',
        'answers': ['Гладенька м’язова тканина', 'Поперечно-посмугована скелетна м’язова тканина', 'Волокниста хрящова тканина'],
        'correct_answer': 'Поперечно-посмугована скелетна м’язова тканина',
        'incorrent': ['Гладенька м’язова тканина', 'Волокниста хрящова тканина']
    },
    {
        'text': 'Назвіть тканину зображену на фото',
        'photo': 'pic/Гладенькамт.jpg',
        'answers': ['Мультиполярний нейрон у сірій речовині мозку', 'Псевдоуніполярний нейрон спинномозкового ганглію', 'Гладенька м’язова тканина'],
        'correct_answer': 'Гладенька м’язова тканина',
        'incorrent': ['Мультиполярний нейрон у сірій речовині мозку', 'Псевдоуніполярний нейрон спинномозкового ганглію']
    },
    {
        'text': 'Назвіть тканину зображену на фото',
        'photo': 'pic/Гаверсовасистема.jpg',
        'answers': ['Пухка сполучна тканина', 'Гаверсова система', 'Еластична хрящова тканина'],
        'correct_answer': 'Гаверсова система',
        'incorrent': ['Пухка сполучна тканина', 'Еластична хрящова тканина']
    },
    {
        'text': 'Назвіть тканину зображену на фото',
        'photo': 'pic/',
        'answers': ['Мультиполярний нейрон у сірій речовині мозку', 'Гаверсова система', 'Остеоцит'],
        'correct_answer': 'Остеоцит',
        'incorrent': ['Мультиполярний нейрон у сірій речовині мозку', 'Гаверсова система']
    },
    {
        'text': 'Назвіть тканину зображену на фото',
        'photo': 'pic/Остеоцит.jpg',
        'answers': ['Нейроглія білої речовини спинного мозку', 'Еластична хрящова тканина', 'Остеоцит'],
        'correct_answer': 'Остеоцит',
        'incorrent': ['Нейроглія білої речовини спинного мозку', 'Еластична хрящова тканина']
    },
    {
        'text': 'Назвіть тканину зображену на фото',
        'photo': 'pic/вбп.jpg',
        'answers': ['Еластична хрящова тканина', 'Остеоцит', 'Ділянка волокнистого хряща на місці прикріплення сухожилля'],
        'correct_answer': 'Ділянка волокнистого хряща на місці прикріплення сухожилля',
        'incorrent': ['Еластична хрящова тканина', 'Остеоцит']
    },
    {
        'text': 'Назвіть тканину зображену на фото',
        'photo': 'pic/Волокнистахрящоватканина.jpg',
        'answers': ['Остеоцит', 'Волокниста хрящова тканина', 'Еластична хрящова тканина'],
        'correct_answer': 'Волокниста хрящова тканина',
        'incorrent': ['Остеоцит', 'Еластична хрящова тканина']
    },
    {
        'text': 'Назвіть тканину зображену на фото',
        'photo': 'pic/Остеоцитик.jpg',
        'answers': ['Остеоцит', 'Потова залоза', 'Нейроцити спинного мозку щура'],
        'correct_answer': 'Остеоцит',
        'incorrent': ['Потова залоза', 'Нейроцити спинного мозку щура']
    },
    {
        'text': 'Назвіть тканину зображену на фото',
        'photo': 'pic/зонамолодогохряща.jpg',
        'answers': ['Псевдоуніполярний нейрон спинномозкового ганглію', 'Ділянка волокнистого хряща на місці прикріплення сухожилля', 'Еластична хрящова тканина. Зона молодого хряща'],
        'correct_answer': 'Еластична хрящова тканина. Зона молодого хряща',
        'incorrent': ['Псевдоуніполярний нейрон спинномозкового ганглію', 'Ділянка волокнистого хряща на місці прикріплення сухожилля']
    },
    {
        'text': 'Назвіть тканину зображену на фото',
        'photo': 'pic/зонаохрястя.jpg',
        'answers': ['Псевдоуніполярний нейрон спинномозкового ганглію', 'Потова залоза', 'Еластична хрящова тканина.Зона охрястя'],
        'correct_answer': 'Еластична хрящова тканина.Зона охрястя',
        'incorrent': ['Псевдоуніполярний нейрон спинномозкового ганглію', 'Потова залоза']
    },
    {
        'text': 'Назвіть тканину зображену на фото',
        'photo': 'pic/зрізгіалуроновогох.jpg',
        'answers': ['Мультиполярний нейрон у сірій речовині мозку', 'Ділянка волокнистого хряща на місці прикріплення сухожилля', 'Зріз гіалуронового хряща'],
        'correct_answer': 'Зріз гіалуронового хряща',
        'incorrent': ['Мультиполярний нейрон у сірій речовині мозку', 'Ділянка волокнистого хряща на місці прикріплення сухожилля']
    },
    {
        'text': 'Назвіть тканину зображену на фото',
        'photo': 'pic/Хондроцит.jpg',
        'answers': ['Остеоцит', 'Гаверсова система', 'Хондроцит'],
        'correct_answer': 'Хондроцит',
        'incorrent': ['Гаверсова система', 'Остеоцит']
    },
    {
        'text': 'Назвіть тканину зображену на фото',
        'photo': 'pic/Хондроцитик.jpg',
        'answers': ['Мієлінове нервове волокно', 'Остеоцит', 'Хондроцит'],
        'correct_answer': 'Хондроцит',
        'incorrent': ['Мієлінове нервове волокно', 'Остеоцит']
    },
    {
        'text': 'Назвіть тканину зображену на фото',
        'photo': 'pic/жироватканинаа.jpg',
        'answers': ['Мультиполярний нейрон у сірій речовині мозку', 'Гладенька м’язова тканина', 'Жирова тканина'],
        'correct_answer': 'Жирова тканина',
        'incorrent': ['Мультиполярний нейрон у сірій речовині мозку', 'Гладенька м’язова тканина']
    },
    {
        'text': 'Назвіть тканину зображену на фото',
        'photo': 'pic/Ретикулярнатканина.jpg',
        'answers': ['Потова залоза', 'Ретикулярна тканина', 'Щільна неоформлена сполучна тканина шкіри'],
        'correct_answer': 'Ретикулярна тканина',
        'incorrent': ['Щільна неоформлена сполучна тканина шкіри', 'Потова залоза']
    },
    {
        'text': 'Назвіть тканину зображену на фото',
        'photo': 'pic/Мезенхіма.jpg',
        'answers': ['Гаверсова система', 'Потова залоза', 'Мезенхіма'],
        'correct_answer': 'Мезенхіма',
        'incorrent': ['Гаверсова система', 'Потова залоза']
    },
    {
        'text': 'Назвіть тканину зображену на фото',
        'photo': 'pic/Щільнаоформленасполучнатканина.jpg',
        'answers': ['Еластична хрящова тканина. Зона молодого хряща', 'Еластична хрящова тканина.Зона охрястя', 'Щільна оформлена сполучна тканина'],
        'correct_answer': 'Щільна оформлена сполучна тканина',
        'incorrent': ['Еластична хрящова тканина. Зона молодого хряща', 'Еластична хрящова тканина.Зона охрястя']
    },
    {
        'text': 'Назвіть тканину зображену на фото',
        'photo': 'pic/Пухкаволокнистасполучнатканина.jpg',
        'answers': ['Зріз гіалуронового хряща', 'Жирова тканина', 'Пухка волокниста сполучна тканина'],
        'correct_answer': 'Пухка волокниста сполучна тканина',
        'incorrent': ['Жирова тканина', 'Зріз гіалуронового хряща']
    },
    {
        'text': 'Назвіть тканину зображену на фото',
        'photo': 'pic/щільнаост.jpg',
        'answers': ['Жирова тканина', 'Макрофаги', 'Щільна оформлена сполучна тканина (сухожилля у повздовжньому розрізі)'],
        'correct_answer': 'Щільна оформлена сполучна тканина (сухожилля у повздовжньому розрізі)',
        'incorrent': ['Макрофаги', 'Жирова тканина']
    },
    {
        'text': 'Назвіть тканину зображену на фото',
        'photo': 'pic/Фібробласти.jpg',
        'answers': ['Фібробласти клітини неправильної видовженої форми', 'Ультраструктура колагенових волокон', 'Нейросекреторні клітини СОЯ гіпоталамуса'],
        'correct_answer': 'Фібробласти клітини неправильної видовженої форми',
        'incorrent': ['Нейросекреторні клітини СОЯ гіпоталамуса', 'Ультраструктура колагенових волокон']
    },
    {
        'text': 'Назвіть тканину зображену на фото',
        'photo': 'pic/Макрофаги.jpg',
        'answers': ['Мультиполярний нейрон у сірій речовині мозку', 'Гладенька м’язова тканина', 'Макрофаги'],
        'correct_answer': 'Макрофаги',
        'incorrent': ['Мультиполярний нейрон у сірій речовині мозку', 'Гладенька м’язова тканина']
    },
    {
        'text': 'Назвіть тканину зображену на фото',
        'photo': 'pic/ультраструктураа.jpg',
        'answers': ['Ультраструктура колагенових волокон', 'Складна альвеолярна залоза', 'Проста трубчаста залоза'],
        'correct_answer': 'Ультраструктура колагенових волокон',
        'incorrent': ['Складна альвеолярна залоза', 'Проста трубчаста залоза']
    },
    {
        'text': 'Назвіть тканину зображену на фото',
        'photo': 'pic/НейросекреторніСОЯ.jpg',
        'answers': ['Нейросекреторні клітини СОЯ гіпоталамуса', 'Потова залоза', 'Одношаровий плоский епітелій'],
        'correct_answer': 'Нейросекреторні клітини СОЯ гіпоталамуса',
        'incorrent': ['Потова залоза', 'Одношаровий плоский епітелій']
    },
    {
        'text': 'Назвіть тканину зображену на фото',
        'photo': 'pic/Волокнистийхос.jpg',
        'answers': ['Волокнистий хрящ міжхребцевого диску теляти', 'Остеоцити у пластинках остеону', 'Гомілкова кістка людини в поперечному розрізі'],
        'correct_answer': 'Волокнистий хрящ міжхребцевого диску теляти',
        'incorrent': ['Остеоцити у пластинках остеону', 'Гомілкова кістка людини в поперечному розрізі']
    },
    {
        'text': 'Назвіть тканину зображену на фото',
        'photo': 'pic/кісткова.jpg',
        'answers': ['Нейроцити спинного мозку щура', 'Кісткові клітини зябрової кришки оселедця(грубоволокниста кісткова тканина)', 'Щільна неоформлена сполучна тканина шкіри'],
        'correct_answer': 'Кісткові клітини зябрової кришки оселедця(грубоволокниста кісткова тканина)',
        'incorrent': ['Щільна неоформлена сполучна тканина шкіри', 'Нейроцити спинного мозку щура']
    },
    {
        'text': 'Назвіть тканину зображену на фото',
        'photo': 'pic/Остеоцитаааа.jpg',
        'answers': ['Спинномозковий вузол кішки', 'Нейроцити спинного мозку щура', 'Остеоцит'],
        'correct_answer': 'Остеоцит',
        'incorrent': ['Нейроцити спинного мозку щура', 'Спинномозковий вузол кішки']
    },
    {
        'text': 'Назвіть тканину зображену на фото',
        'photo': 'pic/упо.jpg',
        'answers': ['Нейроглія білої речовини спинного мозку', 'Кісткові клітини зябрової кришки оселедця(грубоволокниста кісткова тканина)', 'Остеоцити у пластинках остеону'],
        'correct_answer': 'Остеоцити у пластинках остеону',
        'incorrent': ['Кісткові клітини зябрової кришки оселедця(грубоволокниста кісткова тканина)', 'Нейроглія білої речовини спинного мозку']
    },
    {
        'text': 'Назвіть тканину зображену на фото',
        'photo': 'pic/Гомілкові.jpg',
        'answers': ['Мієлінове нервове волокно', 'Зріз гіалуронового хряща', 'Гомілкова кістка людини в поперечному розрізі'],
        'correct_answer': 'Гомілкова кістка людини в поперечному розрізі',
        'incorrent': ['Мієлінове нервове волокно', 'Зріз гіалуронового хряща']
    },
    {
        'text': 'Назвіть тканину зображену на фото',
        'photo': 'pic/Розвитокзенхіми.jpg',
        'answers': ['Мультиполярний нейрон у сірій речовині мозку', 'Зріз гіалуронового хряща', 'Розвиток кістки на місці мезенхіми'],
        'correct_answer': 'Розвиток кістки на місці мезенхіми',
        'incorrent': ['Мультиполярний нейрон у сірій речовині мозку', 'Зріз гіалуронового хряща']
    },
    {
        'text': 'Назвіть тканину зображену на фото',
        'photo': 'pic/Розвитокхіми.jpg',
        'answers': ['Гладенька м’язова тканина', 'Остеоцити у пластинках остеону', 'Розвиток кістки на місці мезенхіми'],
        'correct_answer': 'Розвиток кістки на місці мезенхіми',
        'incorrent': ['Гладенька м’язова тканина', 'Остеоцити у пластинках остеону']
    },
    {
        'text': 'Назвіть тканину зображену на фото',
        'photo': 'pic/розвитокккк.jpg',
        'answers': ['Спинномозковий вузол кішки', 'Остеоцити у пластинках остеону', 'Розвиток кістки на місці хряща'],
        'correct_answer': 'Розвиток кістки на місці хряща',
        'incorrent': ['Спинномозковий вузол кішки', 'Остеоцити у пластинках остеону']
    },
    {
        'text': 'Назвіть тканину зображену на фото',
        'photo': 'pic/Нейроцитиа4.jpg',
        'answers': ['Мультиполярний нейрон у сірій речовині мозку', 'Розвиток кістки на місці мезенхіми', 'Нейроцити спинного мозку щура'],
        'correct_answer': 'Нейроцити спинного мозку щура',
        'incorrent': ['Мультиполярний нейрон у сірій речовині мозку', 'Розвиток кістки на місці мезенхіми']
    },
    {
        'text': 'Назвіть тканину зображену на фото',
        'photo': 'pic/Немієліноволокна.jpg',
        'answers': ['Поперечно-посмугована серцева м’язова тканина', 'Розвиток кістки на місці мезенхіми', 'Немієлінові нервові волокна'],
        'correct_answer': 'Немієлінові нервові волокна',
        'incorrent': ['Поперечно-посмугована серцева м’язова тканина', 'Розвиток кістки на місці мезенхіми']
    },
    {
        'text': 'Назвіть тканину зображену на фото',
        'photo': 'pic/ацинуси.jpg',
        'answers': ['Спинномозковий вузол кішки', 'Ацинуси підшлункової залози. Складна альвеолярна залоза', 'Аденогіпофіз'],
        'correct_answer': 'Ацинуси підшлункової залози. Складна альвеолярна залоза',
        'incorrent': ['Аденогіпофіз', 'Спинномозковий вузол кішки']
    },
    {
        'text': 'Назвіть тканину зображену на фото',
        'photo': 'pic/аденогіпофіз.jpg',
        'answers': ['Поперечно-посмугована серцева м’язова тканина', 'Аденогіпофіз. Аденотропоцити зібрані у трабекули', 'Щільна неоформлена волокниста сполучна тканина. Сітчастий шар дерми.'],
        'correct_answer': 'Аденогіпофіз. Аденотропоцити зібрані у трабекули',
        'incorrent': ['Поперечно-посмугована серцева м’язова тканина', 'Щільна неоформлена волокниста сполучна тканина. Сітчастий шар дерми.']
    },
    {
        'text': 'Назвіть тканину зображену на фото',
        'photo': 'pic/Мієліновінерва.jpg',
        'answers': ['Поперечно-посмугована серцева м’язова тканина', 'Мієлінові нервові волокна сідничного нерва', 'Мезотелій'],
        'correct_answer': 'Мієлінові нервові волокна сідничного нерва',
        'incorrent': ['Поперечно-посмугована серцева м’язова тканина', 'Мезотелій']
    },
    {
        'text': 'Назвіть тканину зображену на фото',
        'photo': 'pic/Спинномозковийвузолкішки.jpg',
        'answers': ['Схема ультраструктурної будови перикаріона нейроцита', 'Спинномозковий вузол кішки', 'Нефроцити канальців дистального відділу нирок Одношаровий кубічний епітелій'],
        'correct_answer': 'Спинномозковий вузол кішки',
        'incorrent': ['Схема ультраструктурної будови перикаріона нейроцита', 'Нефроцити канальців дистального відділу нирок Одношаровий кубічний епітелій']
    },
    {
        'text': 'Назвіть тканину зображену на фото',
        'photo': 'pic/Одноіхура.jpg',
        'answers': ['Схема ультраструктурної будови перикаріона нейроцита', 'Одношаровий циліндричній облямований епітелій жовчного міхура', 'Нефроцити'],
        'correct_answer': 'Одношаровий циліндричній облямований епітелій жовчного міхура',
        'incorrent': ['Схема ультраструктурної будови перикаріона нейроцита', 'Нефроцити']
    },
    {
        'text': 'Назвіть тканину зображену на фото',
        'photo': 'pic/Нефроц.jpg',
        'answers': ['Схема ультраструктурної будови перикаріона нейроцита', 'Нефроцити канальців дистального відділу нирок Одношаровий кубічний епітелій', 'Спинномозковий вузол кішки'],
        'correct_answer': 'Нефроцити канальців дистального відділу нирок Одношаровий кубічний епітелій',
        'incorrent': ['Схема ультраструктурної будови перикаріона нейроцита', 'Спинномозковий вузол кішки']
    },
    {
        'text': 'Назвіть тканину зображену на фото',
        'photo': 'pic/Одношарови.jpg',
        'answers': ['Поперечно-посмугована скелетна м’язова тканина', 'Одношаровий циліндричній облямований епітелій жовчного міхура.', 'Мезотелій. Одношаровий плоский епітелій'],
        'correct_answer': 'Одношаровий циліндричній облямований епітелій жовчного міхура.',
        'incorrent': ['Поперечно-посмугована скелетна м’язова тканина', 'Мезотелій. Одношаровий плоский епітелій']
    },
    {
        'text': 'Назвіть тканину зображену на фото',
        'photo': 'pic/Потова.jpg',
        'answers': ['Астроцити', 'Поперечно-посмугована скелетна м’язова тканина', 'Потова залоза Проста трубчаста залоза'],
        'correct_answer': 'Потова залоза Проста трубчаста залоза',
        'incorrent': ['Астроцити', 'Поперечно-посмугована скелетна м’язова тканина']
    }
]



@bot.message_handler(commands=['test'])
def test_handler(message):
    question = random.choice(questions)
    photo = open(question['photo'], 'rb')
    answers = random.sample(question['answers'], len(question['answers']))
    keyboard = telebot.types.ReplyKeyboardMarkup(
        row_width=1, resize_keyboard=True)
    for answer in answers:
        keyboard.add(telebot.types.KeyboardButton(answer))
    bot.send_photo(message.chat.id, photo,
                   caption=question['text'], reply_markup=keyboard)
    bot.register_next_step_handler(
        message, lambda m: check_answer(m, question))


def check_answer(message, question):
    nexts = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btnnext = types.KeyboardButton("Наступне питання")
    nexts.add(btnnext)

    if message.text == question['correct_answer']:
        bot.reply_to(message, 'Це правильна відповідь', reply_markup=nexts)
    else:
        bot.reply_to(
            message, f'Неправильно. Правильна відповідь: {question["correct_answer"]}', reply_markup=nexts)



@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    for a in blacklist:
        if(a in message.text):
            bot.send_chat_action(message.chat.id, 'typing')
            time.sleep(1)
            bot.send_message(
                message.chat.id, text="Налаштовую зв'язок з адміном.Очікуйте...")
            bot.send_chat_action(message.chat.id, 'typing')
            time.sleep(3)
            bot.send_message(
                message.chat.id, text='Повідомлення відправленно.')
            bot.send_message('-1001880937482', 'Адміни,вам повідомлення від ' +
                             '@{username}\n'.format(username=message.from_user.username))
            chat_id = '-1001880937482'
    # Проверяем, что сообщение содержит текст
            if message.text:
                # Удаляем команду из сообщения
                text = message.text.replace('forward', '')
        # Пересылаем сообщение
                bot.send_message(chat_id=chat_id, text=text)
    if(message.text == "Наступне питання"):
        test_handler(message)

blacklist = ['forward', 'Forward', ]
bot.polling(none_stop=True)
