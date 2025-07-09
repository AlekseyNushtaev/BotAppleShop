from aiogram import types, Router
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


router = Router()


# Главное меню с эмодзи и 2 кнопки в ряд
def get_main_menu():
    buttons = [
        [
            InlineKeyboardButton(text="📱 Ассортимент", callback_data="assortment"),
            InlineKeyboardButton(text="🕒 Режим работы", callback_data="work_hours")
        ],
        [
            InlineKeyboardButton(text="📍 Как нас найти", callback_data="location"),
            InlineKeyboardButton(text="💳 Кредит", callback_data="credit")
        ],
        [
            InlineKeyboardButton(text="♻️ Trade-in", callback_data="tradein"),
            InlineKeyboardButton(text="🛡️ Гарантия", callback_data="warranty")
        ],
        [
            InlineKeyboardButton(text="🎁 Подарки", callback_data="gifts"),
            InlineKeyboardButton(text="⭐ Отзывы", callback_data="reviews")
        ],
        [
            InlineKeyboardButton(text="📞 Связаться с продавцом", callback_data="contact")
        ]
    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard

# Обработчик команды /start
@router.message(Command("start"))
async def cmd_start(message: types.Message):
    try:
        welcome_text = (
            "🛍 Мы магазин техники <b>Гаджет Севастополь</b>\n\n"
            "▪️ 🎁 подарки при покупке\n"
            "▪️ 💳 кредит, Trade-in\n"
            "▪️ 🚚 доставка"
        )
        await message.answer(welcome_text, reply_markup=get_main_menu(), parse_mode="HTML")
    except:
        pass


# Обработчик кнопки "Назад"
async def back_to_main(callback: types.CallbackQuery):
    welcome_text = (
        "🛍️ Мы магазин техники <b>Гаджет Севастополь</b>\n\n"
        "▪️ 🎁 подарки при покупке\n"
        "▪️ 💳 кредит, Trade-in\n"
        "▪️ 🚚 доставка"
    )
    await callback.message.edit_text(welcome_text, reply_markup=get_main_menu(), parse_mode="HTML")
    await callback.answer()

# Обработчики кнопок меню
@router.callback_query(lambda c: c.data == "assortment")
async def process_assortment(callback: types.CallbackQuery):
    try:
        text = "📱 Ознакомиться со всем ассортиментом можно на нашем официальном сайте:\n\n🔗 https://gadjet-sevastopol.ru"
        buttons = [
            [InlineKeyboardButton(text="🌐 Перейти на сайт", url="https://gadjet-sevastopol.ru")],
            [InlineKeyboardButton(text="🔙 Назад", callback_data="back")]
        ]
        keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
        await callback.message.edit_text(text, reply_markup=keyboard)
        await callback.answer()
    except:
        pass


@router.callback_query(lambda c: c.data == "work_hours")
async def process_work_hours(callback: types.CallbackQuery):
    try:
        text = (
            "🕒 <b>Режим работы</b>\n\n"
            "Работаем для вас ежедневно\n"
            "без перерыва и выходных\n"
            "⌛ с 10:00 до 20:00"
        )
        buttons = [[InlineKeyboardButton(text="🔙 Назад", callback_data="back")]]
        keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
        await callback.message.edit_text(text, reply_markup=keyboard, parse_mode="HTML")
        await callback.answer()
    except:
        pass


@router.callback_query(lambda c: c.data == "location")
async def process_location(callback: types.CallbackQuery):
    try:
        text = (
            "📍 <b>Как нас найти</b>\n\n"
            "нажми кнопку маршрут, перейдя по ссылке ниже :\n\n"
            "🔗 https://yandex.eu/maps/org/gadjet_crimea/118536854805/?ll=33.457752%2C44.592044&z=15"
        )
        buttons = [
            [InlineKeyboardButton(text="🗺️ Открыть карту", url="https://yandex.eu/maps/org/gadjet_crimea/118536854805/?ll=33.457752%2C44.592044&z=15")],
            [InlineKeyboardButton(text="🔙 Назад", callback_data="back")]
        ]
        keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
        await callback.message.edit_text(text, reply_markup=keyboard, parse_mode="HTML")
        await callback.answer()
    except:
        pass

@router.callback_query(lambda c: c.data == "credit")
async def process_credit(callback: types.CallbackQuery):
    try:
        text = (
            "💳 <b>Кредит на технику</b>\n\n"
            "Оформите технику в кредит на выгодных условиях!\n"
            "🚀 Быстро, удобно и без переплат\n"
            "💸 Доступно для всей продукции от 2% переплаты в месяц\n\n"
            "🏦 Кредит от ведущих банков!\n"
            "📱 Есть возможность оформить заявку онлайн\n\n"
            "Для уточнения подробностей нажмите в меню «📞 Связаться»"
        )
        buttons = [[InlineKeyboardButton(text="🔙 Назад", callback_data="back")]]
        keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
        await callback.message.edit_text(text, reply_markup=keyboard, parse_mode="HTML")
        await callback.answer()
    except:
        pass


@router.callback_query(lambda c: c.data == "tradein")
async def process_tradein(callback: types.CallbackQuery):
    try:
        text = (
            "♻️ <b>Trade-in</b>\n\n"
            "Обновите технику по системе Trade-in!\n"
            "📱 Примем ваше устройство и зачтём его стоимость при покупке нового\n"
            "⚡ Быстро, удобно и выгодно!\n\n"
            "Для уточнения подробностей нажмите в меню «📞 Связаться»"
        )
        buttons = [[InlineKeyboardButton(text="🔙 Назад", callback_data="back")]]
        keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
        await callback.message.edit_text(text, reply_markup=keyboard, parse_mode="HTML")
        await callback.answer()
    except:
        pass


@router.callback_query(lambda c: c.data == "warranty")
async def process_warranty(callback: types.CallbackQuery):
    try:
        text = (
            "🛡️ <b>Гарантия</b>\n\n"
            "Покупайте с уверенностью — мы заботимся о качестве и вашей защите.\n\n"
            "🆕 Гарантия на новую технику - <b>12 месяцев</b>\n"
            "🔄 Гарантия на б/у технику - <b>2 месяца</b>"
        )
        buttons = [[InlineKeyboardButton(text="🔙 Назад", callback_data="back")]]
        keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
        await callback.message.edit_text(text, reply_markup=keyboard, parse_mode="HTML")
        await callback.answer()
    except:
        pass


@router.callback_query(lambda c: c.data == "gifts")
async def process_gifts(callback: types.CallbackQuery):
    try:
        text = (
            "🎁 <b>Подарки при покупке</b>\n\n"
            "Забота о вашем устройстве с первого дня!\n\n"
            "При покупке нового смартфона дарим:\n"
            "📱 Чехол\n"
            "🖥️ Защитное стекло\n\n"
            "Также мы:\n"
            "🔁 Перенесем данные со старого устройства\n"
            "🍎 Поможем создать Apple ID\n"
            "📲 Установим приложения вне AppStore\n\n"
            "🎉 <b>Специальное предложение!</b>\n"
            "Если вы впервые покупаете у нас смартфон, напишите продавцу в Telegram код <code>perviy500</code> и получите скидку 500 ₽\n\n"
            "↗️ Telegram: @GadjetSevastopol\n"
            "📞 Контакт: +7 (978) 008-02-08"
        )
        buttons = [[InlineKeyboardButton(text="🔙 Назад", callback_data="back")]]
        keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
        await callback.message.edit_text(text, reply_markup=keyboard, parse_mode="HTML")
        await callback.answer()
    except:
        pass


@router.callback_query(lambda c: c.data == "reviews")
async def process_reviews(callback: types.CallbackQuery):
    try:
        text = (
            "⭐ <b>Отзывы покупателей</b>\n\n"
            "Ознакомьтесь с отзывами наших клиентов по ссылке ниже:\n\n"
            "🔗 https://yandex.eu/maps/org/gadjet_crimea/118536854805/reviews/?ll=33.457752%2C44.592044&tab=reviews&z=15"
        )
        buttons = [
            [InlineKeyboardButton(text="📝 Читать отзывы", url="https://yandex.eu/maps/org/gadjet_crimea/118536854805/reviews/?ll=33.457752%2C44.592044&tab=reviews&z=15")],
            [InlineKeyboardButton(text="🔙 Назад", callback_data="back")]
        ]
        keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
        await callback.message.edit_text(text, reply_markup=keyboard, parse_mode="HTML")
        await callback.answer()
    except:
        pass


@router.callback_query(lambda c: c.data == "contact")
async def process_contact(callback: types.CallbackQuery):
    try:
        text = (
            "📞 <b>Связь с продавцом</b>\n\n"
    
            "⏳ На связи с вами ежедневно\n"
            "🕒 с 10:00 до 20:00\n\n"
            "↗️ Telegram: @GadjetSevastopol\n"
            "☎️ Телефон: <code>+7 (978) 008-02-08</code>"
        )
        buttons = [[InlineKeyboardButton(text="🔙 Назад", callback_data="back")]]
        keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
        await callback.message.edit_text(text, reply_markup=keyboard, parse_mode="HTML")
        await callback.answer()
    except:
        pass


# Обработчик кнопки "Назад"
@router.callback_query(lambda c: c.data == "back")
async def process_back(callback: types.CallbackQuery):
    try:
        await back_to_main(callback)
    except:
        pass
