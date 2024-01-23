import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.utils import get_random_id
import time

# ID пользователя, которому нужно отправить личное сообщение
third_party_id = 224257016
third_party_id_two = 348334565
is_first_message = True

# Ваш токен VK API
token = ''


# Функция для отправки сообщения
def send_message(vk, event, message, is_spamming):
    vk.messages.send(user_id=event.user_id,
                     random_id=get_random_id(),
                     message=message,
                     is_spamming=is_spamming)


# Функция для формирования ссылки на диалог
def generate_dialog_link(user_id):
    return f'https://vk.com/ссылка_на_группу?sel={user_id}'


comand_list = 'Привет! Я бот, созданный для помощи и отвечаю на часто задаваемые вопросы. Я постараюсь предоставить тебе информацию, которую ты ищешь, но если у меня не получится, то ты можешь позвать администратора.\n\nИспользуй эти команды, что бы получить интересующую тебя информацию: \n\n 1. /cfg - информация о покупке или скачке cfg наших игроков. \n 2. /ac -  информация о покупке аккаунтов.\n 3. /ad - информация о покупке рекламы в нашем сообществе. \n 4. /ts - информация о покупке настройки ts3 серверов. \n 5. /tsr - информация о покупке или получении комнат на нашем ts3 сервере. \n 6. /admin - позвать администратора. '


# Функция для вывода списка команд
def display_commands(vk, event, comand_list):
    vk.messages.send(user_id=user_id, message=comand_list, random_id=0)


# Авторизация в ВКонтакте
vk_session = vk_api.VkApi(token=token)
longpoll = VkLongPoll(vk_session)
vk = vk_session.get_api()
text_cfg = 'Начиная с 07.06.2021 мы больше не продаём cfg в группе, тогда же мы выложили пак со всеми конфигурациями на тот момент в открытый доступ. Вы можете скачать его по ссылке - https://vk.cc/.Если вам нужны более поздние версии конфигов, вы можете попробовать приобрести их у игроков лично.'
text_ac = 'На данный момент продажа аккаунтов в нашем сообществе осуществляется только им - https://vk.com/чья-тоссылка.  Информация о ценах и ассортименте постоянно изменяется, поэтому уточняйте её напрямую или дождитесь его ответа тут, но для этого используйте команду "позвать администратора".'
text_ad = 'Репост в группу на сутки - 100 ₽ \n Пост от нашей группы с вашей рекламой на сутки - 150 ₽ \n\n *Мы не размещаем рекламу всего что не соответствует правилам данной соц. сети.\n\n Эффективность рекламы зависит от вашего контента и тематики.\n\n Возможны для обсуждения дополнительные способы рекламы если есть идеи пишите. В любом случаи мы не гарантируем какого-либо результата. /n В рекламе может быть отказано без объяснения причин.'
text_ts = 'Настройка и оформление голосовых серверов TeamSpeak 3 - 300 ₽'
text_tsr = 'Слоты в нашем ts3 сервере ограничены, поэтому мы предоставляем бесплатные комнаты и привилегии только друзьям и знакомым. \n\n Остальные могут приобрести:\n\nПостоянная обычная комната (желтая, нижу респауна) навсегда - 200 ₽Постоянная элитная комната (красная, выше респауна) навсегда - 300 ₽ \n\nВместе с комнатой вам будет выдана привилегия "Владелец комнаты", которая предоставит вам некоторые привилегии.'
text_admin = 'Администратора по какому вопросу вы бы хотели позвать. От этого зависит кто именно вам ответит.\n\n /adc - вопрос насчет аккаунтов\n /adt - вопрос насчет ts3'
text_adc = 'Ваше сообщение отправлено Администратору отвечающему за аккаунты, ожидайте его ответа'
text_adt = 'Ваше сообщение отправлено Администратору отвечающему за настройку ts3, ожидайте его ответа'
# Список поддерживаемых команд
commands = {
    '/cfg': text_cfg,
    '/ac': text_ac,
    '/ad': text_ad,
    '/ts': text_ts,
    '/tsr': text_tsr,
    '/admin': text_admin,
    '/adc': text_adc,
    '/adt': text_adt
    # Добавьте свои команды здесь
}


def banned_text(user_id, message):
    vk.messages.send(user_id=user_id,
                     message="Вы заблокированы на 1 минуту за спам командами",
                     random_id=0)


def not_spam(user_id, message):
    vk.messages.send(user_id=user_id,
                     message="Пожалуйста, не спамьте командами так быстро",
                     random_id=get_random_id())
    is_spamming = True


def message_one(vk, event, commands, is_spamming):
    user_id = event.user_id
    dialog_link = generate_dialog_link(user_id)
    vk.messages.send(
        user_id=third_party_id,
        random_id=get_random_id(),
        message=
        f"Вот ссылка на диалог с пользователем {user_id}: {dialog_link}",
        from_group=True,
        is_spamming=is_spamming)


def message_two(vk, event, commands, is_spamming):
    user_id = event.user_id
    dialog_link = generate_dialog_link(user_id)
    vk.messages.send(
        user_id=third_party_id_two,
        random_id=get_random_id(),
        message=
        f"Вот ссылка на диалог с пользователем {user_id}: {dialog_link}",
        from_group=True,
        is_spamming=is_spamming)


def reset_counters():
    global is_spamming, last_request_time, request_count
    is_spamming = False
    last_request_time = time.time()
    request_count = 0


def is_admin_user(user_id):
    print(f"User ID: {user_id}")
    vk_session = vk_api.VkApi(token=token)
    try:
        response = vk_session.method('users.get', {
            'user_ids': user_id,
            'fields': 'is_admin'
        })
        print(f"Response: {response}")
        if response[0].get('is_admin', 0) == 1:
            return True
    except Exception as e:
        print(f"Ошибка при проверке администратора: {e}")
    return False


def get_dialog_users():
    # Подключение к API ВКонтакте
    vk_session = vk_api.VkApi(token=token)
    vk = vk_session.get_api()

    # Получение информации о текущем пользователе
    current_user = vk.users.get()
    if current_user:
        current_user_id = current_user[0]['id']

        # Получение информации о беседе / диалоге
        dialog_id = 2000000000 + current_user_id

        # Получение пользователей диалога
        members = vk.messages.getConversationMembers(peer_id=dialog_id)

        # Формирование списка пользователей
        dialog_users = []
        for member in members['items']:
            if member['member_id'] > 0:
                dialog_users.append(member['member_id'])

        return dialog_users

    else:
        print("Ошибка при получении информации о текущем пользователе.")
        return []


dialog_users = get_dialog_users()

is_first_message = True
is_spamming = False
last_request_time = time.time()
request_count = 0
banned_users = {}
bot_muted_until = 0
is_mute_active = False


def reset_counters():
    global is_spamming, last_request_time, request_count
    is_spamming = False
    last_request_time = time.time()
    request_count = 0


for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
        user_id = event.user_id
        message = event.text.lower()

        if user_id in banned_users:
            ban_expiration_time = banned_users[user_id]
            if time.time() < ban_expiration_time:
                continue
            else:
                del banned_users[user_id]
                reset_counters()

        if is_first_message:
            display_commands(vk, event, comand_list)
            is_first_message = False
            is_mute_active = False
            print(is_first_message)

        current_time = time.time()
        time_difference = current_time - last_request_time

        if time_difference < 1.5:
            if not is_spamming:
                not_spam(user_id, message)
                continue  # Пропустить выполнение команды при срабатывании антиспам защиты
        else:
            is_spamming = False

        last_request_time = current_time
        request_count += 1

        if time_difference >= 60:
            reset_counters()

        if 'пoмoчь' in message:
            is_spamming = True
            bot_muted_until = current_time + 60  # Установить время на 1 минуту
            is_mute_active = True
            continue

        if not is_spamming and not is_mute_active:
            if message == '/bot':
                display_commands(vk, event, comand_list)
            elif message in commands:
                send_message(vk, event, commands[message], is_spamming)
                if message == "/adc":
                    message_two(vk, event, commands[message], is_spamming)
                if message == '/adt':
                    message_one(vk, event, commands[message], is_spamming)

        if 'дoбрoгo' in message or current_time >= bot_muted_until:
            is_spamming = False
            is_mute_active = False