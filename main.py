import telebot
import os
from telebot import types

token = '7397438773:AAFBGRSljr34t_P2HyWfM_-4dxnqjEO6iP4'
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(message):
  bot.send_message(1798172827, f'/start: ID:{message.chat.id}, Имя: {message.chat.first_name}, Фамилия: {message.chat.last_name}, Username: @{message.chat.username}')
  markup = types.InlineKeyboardMarkup()
  btn1 = types.InlineKeyboardButton('🏡 Наши проекты', callback_data='projects0')
  btn2 = types.InlineKeyboardButton('❓ Частые вопросы', callback_data='qustions')
  btn3 = types.InlineKeyboardButton('📞 Контакты', callback_data='contacts')
  btn4 = types.InlineKeyboardButton('📝 О нас', callback_data='about')
  markup.row(btn1, btn2)
  markup.row(btn4, btn3)
  bot.send_photo(message.chat.id, open('start.jpg', 'rb'))
  bot.send_message(message.chat.id, text=f"Здравствуйте, {message.chat.first_name}! Это бот кампании <a href = 'https://www.stroymashllc.ru/'><b>СтройМаш</b></a> и я помогу вам с быстрым и качественным ремонтом в <b>Екатеринбурге</b>", parse_mode='HTML', reply_markup=markup)

@bot.message_handler(commands=['call'])
def call_user(message):
  if message.chat.id in [1798172827, 267977568]:
    mess = message.text.split(f'\n')
    id_user = mess[0].split()[1]
    bot.send_message(id_user, f'Сообщение от представителя СтройМаш:\n{mess[1]}')
  else:
    bot.send_message(message.chat.id, 'У вас нет доступа к этой команде, она доступна только администраторам')

@bot.message_handler(content_types=['text'])
def mes_text(message):
  if len(message.text) > 3:
    bot.send_message(267977568 and 1798172827, f'Сообщение в бот от пользователя {message.chat.first_name} ID:{message.chat.id}, Username: {"@"+message.chat.username if message.chat.username !=None else "Отсутствует"};\nТекст: {message.text}')

@bot.callback_query_handler(func=lambda callback: True)
def callback_mes(callback):
  if callback.data[:8] == 'projects':
    num = int(callback.data[8:])
    if num == 15:
      num = 0
    call = 'projects' + str(num+1)
    if num == 0:
      bot.send_message(callback.message.chat.id, '🏢Наши проекты:🏡')
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('🏢 Ещё ➡', callback_data=str(call))
    btn2 = types.InlineKeyboardButton('❓ Частые вопросы', callback_data='qustions')
    btn3 = types.InlineKeyboardButton('📝 О нас', callback_data='about')
    markup.row(btn1)
    markup.row(btn2, btn3)
    bot.send_photo(callback.message.chat.id, open(f'Photos/photo{num}.jpg', 'rb'), reply_markup=markup)
  elif callback.data == 'qustions':
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('🏡 Наши проекты', callback_data='projects0')
    btn2 = types.InlineKeyboardButton('📝 О нас', callback_data='about')
    markup.row(btn1, btn2)
    bot.send_message(callback.message.chat.id,
    '📝❓<b><i>Самые часто задаваемые вопросы:</i></b>❓📝\n\n<b><u>Где работаете?</u></b>\nМы работаем во всех районах Екатеринбурга;\n<b><u>Какие услуги вы предоставляете?</u></b>\nОсновное направление нашей деятельности – дизайн и ремонт квартир. Мы предоставляем любые строительные и отделочые работы в рамках квартиры или дома;\n<b><u>Что по цене?</u></b>\nУ нас все цены фиксированы и зависят от сложности, можно подобрать пакет на любой бюджет, но в среднем за <u>полный</u> пакет услуг от 18000 за кв.м\n<b><u>Сколько по времени?</u></b>\nВсе сроки фиксированы и называются сразу. Влияет только объем и сложность, Обычно полный рабочий цикл занимает 2–3 месяца.\n<b><u>Проекты для ремонта</u></b>\nМы поможем вам опредилиться со стилем и создадим дизайн или воплатим ваш проект\n\nЗдесь приведины ответы на основные вопросы, а также обобщённую информацию о ценах и сроках. Важно понимать, что каждая ситуация уникальна, могут существенно различаться. Для более индивидуального ответа мы можите обратиться по ссылкам в "📞 Контакты" или написать вопрос прямо в чат бота и менеджер обязательно свяжется с вами', parse_mode='HTML', reply_markup=markup)
  elif callback.data == 'contacts':
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('На главную', callback_data='start'))
    bot.send_message(callback.message.chat.id, f'📞<b><i>Контакты:</i></b>📞\n\n🖥️<a href = "https://www.stroymashllc.ru"><b>Наш сайт</b></a>💻 <i>(временно недоступен)</i>\n📨<a href = "https://vk.com/stroymashh"><b>Группа VK</b></a>💬\n📩<b>Телеграм</b>📲- @Slugina\n\n👨‍💻Telegram Bot🤖- @Psdon4k', parse_mode='HTML', reply_markup=markup)
  elif callback.data == 'about':
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('🏡 Наши проекты', callback_data='projects0')
    btn2 = types.InlineKeyboardButton('❓ Частые вопросы', callback_data='qustions')
    btn3 = types.InlineKeyboardButton('📞 Контакты', callback_data='contacts')
    markup.row(btn1, btn2)
    markup.row(btn3)
    bot.send_message(callback.message.chat.id,
'''📝<b><i>О нас:</i></b>📝
Мы компания СтройМаш. Основное направление нашей деятельности – дизайн и ремонт квартир в Екатеринбурге.
Дизайн квартир в Екатеринбурге от компании СтройМаш – это:
– реальная возможность увидеть результат ремонта до его начала по дизайн-проекту;
– пакеты дизайна, то есть возможность выбрать необходимый уровень проработки дизайн-проекта, а значит, возможность получить дизайн даже при экономичном бюджете;
– услуги нескольких дизайнеров: разные стили, разные концепции одной площади;
– помощь в подборе материалов;
– дополнительная услуга авторского надзора при проведении отделочных работ.

Ремонт квартир от компании СтройМаш – это:
– профессиональный ремонт от загородного дома;
– выполнение работ на объекте под руководством грамотного специалиста-прораба;
– закупка и доставка отделочных материалов, скидка на материалы и помощь в их подборе;
– любые работы с гипсокартоном, сантехникой, электричеством, отделочные работы, монтаж систем отопления и водоснабжения;
– выполнение как отдельных видов работ, так и ремонт квартир в Екатеринбурге под ключ;
– официальный договор на ИП, документальное подтверждение оплат и закупок;
– гарантия на выполненные работы до пяти лет.

А еще у нас есть интересные дополнительные услуги:
– монтаж качественной шумоизоляции помещений (пол, потолок, стены) и систем канализации и водоснабжения;
– защита поверхностей в процессе ремонта от пыли и грязи, пломбировка комнат при ремонте;
– опрессовка системы водоснабжения профессиональным аппаратом для гидравлических испытаний;
– клининг квартиры после ремонта по желанию клиента;
– предпродажная подготовка квартиры;
– помощь в аренде съемной квартиры на время ремонта.

Каждому клиенту мы бесплатно предоставляем регулярный отчет о проделанной работе, потраченных средствах, закупленных отделочных материалах в личном кабинете клиента''', parse_mode='HTML', reply_markup=markup)
  elif callback.data == 'start':
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('🏡 Наши проекты', callback_data='projects0')
    btn2 = types.InlineKeyboardButton('❓ Частые вопросы', callback_data='qustions')
    btn3 = types.InlineKeyboardButton('📝 О нас', callback_data='about')
    btn4 = types.InlineKeyboardButton('📞 Контакты', callback_data='contacts')
    markup.row(btn1, btn2)
    markup.row(btn3, btn4)
    bot.send_photo(callback.message.chat.id, open('start.jpg', 'rb'), reply_markup=markup)
  else:
    bot.send_message(callback.message.chat.id, 'Этого просто не должно, не может быть. Это ошибка...')
bot.polling(none_stop=True)