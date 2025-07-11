import logging

from aiogram import types, Router, F
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from typing import List

router: Router = Router()


def keyboard_back() -> InlineKeyboardMarkup:
    """
    Создает и возвращает клавиатуру с кнопкой назад для возврата в главное меню.
    Returns: InlineKeyboardMarkup: Клавиатура с кнопками главного меню
    """
    buttons: List[List[InlineKeyboardButton]] = [
        [InlineKeyboardButton(text="🔙 Назад", callback_data="back")]
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)


def get_main_menu() -> InlineKeyboardMarkup:
    """
    Создает и возвращает главное меню бота с кнопками.
    Returns: InlineKeyboardMarkup: Клавиатура с кнопками главного меню
    """
    buttons: List[List[InlineKeyboardButton]] = [
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
    return InlineKeyboardMarkup(inline_keyboard=buttons)


@router.message(Command("start"))
async def cmd_start(message: types.Message) -> None:
    """
    Обработчик команды /start. Отправляет приветственное сообщение и главное меню.
    Args: message (types.Message): Входящее сообщение с командой /start
    """
    try:
        welcome_text: str = (
            "🛍 Мы магазин техники <b>Гаджет Севастополь</b>\n\n"
            "▪️ 🎁 подарки при покупке\n"
            "▪️ 💳 кредит, Trade-in\n"
            "▪️ 🚚 доставка"
        )
        await message.answer(welcome_text, reply_markup=get_main_menu(), parse_mode="HTML")
    except Exception as e:
        logging.error(f"Error in cmd_start: {e}")


@router.callback_query(F.data == "back")
async def process_back(callback: types.CallbackQuery) -> None:
    """
    Возвращает пользователя в главное меню.
    Args: callback (types.CallbackQuery): Колбэк от нажатия кнопки
    """
    try:
        welcome_text: str = (
            "🛍️ Мы магазин техники <b>Гаджет Севастополь</b>\n\n"
            "▪️ 🎁 подарки при покупке\n"
            "▪️ 💳 кредит, Trade-in\n"
            "▪️ 🚚 доставка"
        )
        await callback.message.edit_text(welcome_text, reply_markup=get_main_menu(), parse_mode="HTML")
        await callback.answer()
    except Exception as e:
        logging.error(f"Error in process_back: {e}")


@router.callback_query(F.data == "assortment")
async def process_assortment(callback: types.CallbackQuery) -> None:
    """Обработчик кнопки 'Ассортимент'."""
    try:
        text: str = ("📱 Ознакомиться со всем ассортиментом можно на нашем официальном сайте:"
                     "\n\n🔗 https://gadjet-sevastopol.ru")
        buttons: List[List[InlineKeyboardButton]] = [
            [InlineKeyboardButton(text="🌐 Перейти на сайт", url="https://gadjet-sevastopol.ru")],
            [InlineKeyboardButton(text="🔙 Назад", callback_data="back")]
        ]
        keyboard: InlineKeyboardMarkup = InlineKeyboardMarkup(inline_keyboard=buttons)
        await callback.message.edit_text(text, reply_markup=keyboard)
        await callback.answer()
    except Exception as e:
        logging.error(f"Error in process_assortment: {e}")


@router.callback_query(F.data == "work_hours")
async def process_work_hours(callback: types.CallbackQuery) -> None:
    """Обработчик кнопки 'Режим работы'."""
    try:
        text: str = (
            "🕒 <b>Режим работы</b>\n\n"
            "Работаем для вас ежедневно\n"
            "без перерыва и выходных\n"
            "⌛ с 10:00 до 20:00"
        )
        await callback.message.edit_text(text, reply_markup=keyboard_back(), parse_mode="HTML")
        await callback.answer()
    except Exception as e:
        logging.error(f"Error in process_work_hours: {e}")


@router.callback_query(F.data == "location")
async def process_location(callback: types.CallbackQuery) -> None:
    """Обработчик кнопки 'Как нас найти'."""
    try:
        text: str = (
            "📍 <b>Как нас найти</b>\n\n"
            "нажми кнопку маршрут, перейдя по ссылке ниже :\n\n"
            "🔗 https://yandex.eu/maps/org/gadjet_crimea/118536854805/?ll=33.457752%2C44.592044&z=15"
        )
        buttons: List[List[InlineKeyboardButton]] = [
            [InlineKeyboardButton(text="🗺️ Открыть карту",
                                  url="https://yandex.eu/maps/org/gadjet_crimea/118536854805/"
                                      "?ll=33.457752%2C44.592044&z=15")],
            [InlineKeyboardButton(text="🔙 Назад", callback_data="back")]
        ]
        keyboard: InlineKeyboardMarkup = InlineKeyboardMarkup(inline_keyboard=buttons)
        await callback.message.edit_text(text, reply_markup=keyboard, parse_mode="HTML")
        await callback.answer()
    except Exception as e:
        logging.error(f"Error in process_location: {e}")


@router.callback_query(F.data == "credit")
async def process_credit(callback: types.CallbackQuery) -> None:
    """Обработчик кнопки 'Кредит'."""
    try:
        text: str = (
            "💳 <b>Кредит на технику</b>\n\n"
            "Оформите технику в кредит на выгодных условиях!\n"
            "🚀 Быстро, удобно и без переплат\n"
            "💸 Доступно для всей продукции от 2% переплаты в месяц\n\n"
            "🏦 Кредит от ведущих банков!\n"
            "📱 Есть возможность оформить заявку онлайн\n\n"
            "Для уточнения подробностей нажмите в меню «📞 Связаться»"
        )
        await callback.message.edit_text(text, reply_markup=keyboard_back(), parse_mode="HTML")
        await callback.answer()
    except Exception as e:
        logging.error(f"Error in process_credit: {e}")


@router.callback_query(F.data == "tradein")
async def process_tradein(callback: types.CallbackQuery) -> None:
    """Обработчик кнопки 'Трейд-ин'."""
    try:
        text: str = (
            "♻️ <b>Trade-in</b>\n\n"
            "Обновите технику по системе Trade-in!\n"
            "📱 Примем ваше устройство и зачтём его стоимость при покупке нового\n"
            "⚡ Быстро, удобно и выгодно!\n\n"
            "Для уточнения подробностей нажмите в меню «📞 Связаться»"
        )
        await callback.message.edit_text(text, reply_markup=keyboard_back(), parse_mode="HTML")
        await callback.answer()
    except Exception as e:
        logging.error(f"Error in process_tradein: {e}")


@router.callback_query(F.data == "warranty")
async def process_warranty(callback: types.CallbackQuery) -> None:
    """Обработчик кнопки 'Гарантия'."""
    try:
        text: str = (
            "🛡️ <b>Гарантия</b>\n\n"
            "Покупайте с уверенностью — мы заботимся о качестве и вашей защите.\n\n"
            "🆕 Гарантия на новую технику - <b>12 месяцев</b>\n"
            "🔄 Гарантия на б/у технику - <b>2 месяца</b>"
        )
        await callback.message.edit_text(text, reply_markup=keyboard_back(), parse_mode="HTML")
        await callback.answer()
    except Exception as e:
        logging.error(f"Error in process_warranty: {e}")


@router.callback_query(F.data == "gifts")
async def process_gifts(callback: types.CallbackQuery) -> None:
    """Обработчик кнопки 'Подарки'."""
    try:
        text: str = (
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
            "Если вы впервые покупаете у нас смартфон, напишите продавцу в Telegram код "
            "<code>perviy500</code> и получите скидку 500 ₽\n\n"
            "↗️ Telegram: @GadjetSevastopol\n"
            "📞 Контакт: +7 (978) 008-02-08"
        )
        await callback.message.edit_text(text, reply_markup=keyboard_back(), parse_mode="HTML")
        await callback.answer()
    except Exception as e:
        logging.error(f"Error in process_gifts: {e}")


@router.callback_query(F.data == "reviews")
async def process_reviews(callback: types.CallbackQuery) -> None:
    """Обработчик кнопки 'Отзывы'."""
    try:
        text: str = (
            "⭐ <b>Отзывы покупателей</b>\n\n"
            "Ознакомьтесь с отзывами наших клиентов по ссылке ниже:\n\n"
            "🔗 https://yandex.eu/maps/org/gadjet_crimea/118536854805/reviews/"
            "?ll=33.457752%2C44.592044&tab=reviews&z=15"
        )
        buttons: List[List[InlineKeyboardButton]] = [
            [InlineKeyboardButton(text="📝 Читать отзывы",
                                  url="https://yandex.eu/maps/org/gadjet_crimea/118536854805/"
                                      "reviews/?ll=33.457752%2C44.592044&tab=reviews&z=15")],
            [InlineKeyboardButton(text="🔙 Назад", callback_data="back")]
        ]
        keyboard: InlineKeyboardMarkup = InlineKeyboardMarkup(inline_keyboard=buttons)
        await callback.message.edit_text(text, reply_markup=keyboard, parse_mode="HTML")
        await callback.answer()
    except Exception as e:
        logging.error(f"Error in process_reviews: {e}")


@router.callback_query(F.data == "contact")
async def process_contact(callback: types.CallbackQuery) -> None:
    """Обработчик кнопки 'Связаться с продавцом'."""
    try:
        text: str = (
            "📞 <b>Связь с продавцом</b>\n\n"
    
            "⏳ На связи с вами ежедневно\n"
            "🕒 с 10:00 до 20:00\n\n"
            "↗️ Telegram: @GadjetSevastopol\n"
            "☎️ Телефон: <code>+7 (978) 008-02-08</code>"
        )
        await callback.message.edit_text(text, reply_markup=keyboard_back(), parse_mode="HTML")
        await callback.answer()
    except Exception as e:
        logging.error(f"Error in process_contact: {e}")
