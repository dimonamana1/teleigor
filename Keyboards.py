import telebot
from telebot import types


markup = types.ReplyKeyboardMarkup(True)
markup.row('⚔️Арена', '🏘Город')
markup.row('🎖 Герой', '🏰 Клан')
markup.row('🏆 Лиги', '📜 Летопись')
markup.row('❓Помощь', '⚙️ Настройки')

markup1 = types.ReplyKeyboardMarkup(True)
markup1.row('⚔️ Одиночный', '👥 Командный')
markup1.row('💀 Хаотический', '👊 Тренировочный')
markup1.row('⬅️ Назад')

markup11 = types.ReplyKeyboardMarkup(True)
markup11.row('Отмена')

markup12 = types.ReplyKeyboardMarkup(True)
markup12.row('⚔️ Новый бой')
markup12.row('⬅️ Назад')

markup13 = types.ReplyKeyboardMarkup(True)
markup13.row('Создать (1 мин)', 'Создать (2 мин)')
markup13.row('Создать (3 мин)', 'Создать (5 мин)')
markup13.row('⬅️ Назад')

markup14 = types.ReplyKeyboardMarkup(True)
markup14.row('Отмена')

markup2 = types.ReplyKeyboardMarkup(True)
markup2.row('🏠 Торговец', '🎲 Лотерея', '🏛 Академия')
markup2.row('🏫 Ратуша', '💒 Храм', '🏚 Таверна')
markup2.row('🐺 Зверинец', '💎 Банк', '⬅️ Назад')

markup21 = types.ReplyKeyboardMarkup(True)
markup21.row('🗡 Оружие', '🛡 Броня')
markup21.row('💍 Украшения', '⚗️ Зелья')
markup21.row('🛍 Разное', '💎 Donate')
markup21.row('💰 Продать вещи', '🔨 Починить вещи')
markup21.row('⬅️ Назад')

markup22 = types.ReplyKeyboardMarkup(True)
markup22.row('Сделать ставку 10💰')
markup22.row('Сделать ставку 5💰')
markup22.row('Сделать ставку 3💰')
markup22.row('Сделать ставку 1💰')
markup22.row('⬅️ Назад')

markup23 = types.ReplyKeyboardMarkup(True)
markup23.row('💈 Услуги', '📚 Способности')
markup23.row('⬅️ Назад')

markup24 = types.ReplyKeyboardMarkup(True)
markup24.row('Вступить в клан')
markup24.row('Зарегистрировать клан')
markup24.row('⬅️ Назад')

markup25 = types.ReplyKeyboardMarkup(True)
markup25.row('⬅️ Назад')

markup26 = types.ReplyKeyboardMarkup(True)
markup26.row('🤠 Найти задание')
markup26.row('⬅️ Назад')

markup261 = types.ReplyKeyboardMarkup(True)
markup261.row('✅ Взять задание/❌ Отказаться от задания')
markup261.row('⬅️ Назад')

markup27 = types.ReplyKeyboardMarkup(True)
markup27.row('Купить зверя')
markup27.row('⬅️ Назад')

markup28 = types.ReplyKeyboardMarkup(True)
markup28.row('🔄 Обменник')
markup28.row('💎 Купить алмазы')
markup28.row('🗄 История платежей')
markup28.row('⬅️ Назад')

markup282 = types.ReplyKeyboardMarkup(True)
markup282.row('⬅️ Назад')

markup283 = types.ReplyKeyboardMarkup(True)
markup283.row('⬅️ Назад')

markup3 = types.ReplyKeyboardMarkup(True)
markup3.row('🏅 Статистика', '⭐️ Навыки')
markup3.row('🗡 Профиль', '🎒 Инвентарь')
markup3.row('🤺 Владение', '🐺 Зверь')
markup3.row('👤 Аватар', '📚 Способности')
markup3.row('⬅️ Назад')

markup4 = types.ReplyKeyboardMarkup(True)
markup4.row('👥 Состав', '🏰 Замок')
markup4.row('📬 Заявки', '📩 Приглашения')
markup4.row('👑 Управление', '❌ Покинуть клан')
markup4.row('⬅️ Назад')

markup44 = types.ReplyKeyboardMarkup(True)
markup44.row('🔍 Искать по имени')
markup44.row('🕵 Нанять скаута')
markup44.row('📥 Отправленные')
markup44.row('⬅️ Назад')

markup441 = types.ReplyKeyboardMarkup(True)
markup441.row('⬅️ Назад')

markup442 = types.ReplyKeyboardMarkup(True)
markup442.row('Да', 'Нет')

markup46 = types.ReplyKeyboardMarkup(True)
markup46.row('Да', 'Нет')

markup5 = types.ReplyKeyboardMarkup(True)
markup5.row('🏆 Лига', '🏅 Зал славы')
markup5.row('⬅️ Назад')

markup51 = types.ReplyKeyboardMarkup(True)
markup51.row('🎖 Рейтинг героев', '🏰 Рейтинг кланов')
markup51.row('⬅️ Назад')
