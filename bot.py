import asyncio
import logging
import requests
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo

TOKEN = "9212034467:AAEyKTelQpxGEgXmCRRXiGLgylPFAZy1yBI"
ADS_GALAXY_URL = "TU_URL_DE_INTEGRACION_ADS_GALAXY"
WEBAPP_URL = "https://rafanegocio1997-png.github.io/Juego-de-vacas-/" # URL donde alojes tu HTML de vacas

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    user_id = message.from_user.id

    # 1. Ejecutar notificación transparente a AdsGalaxy
    try:
        requests.get(f"{ADS_GALAXY_URL}?auth={user_id}", timeout=3)
    except Exception as e:
        logging.error(f"Error AdsGalaxy: {e}")

    # 2. Texto adaptado a vacas y leche
    texto = (
        "🐄 <b>¡Bienvenido a la Granja de Vacas!</b>\n\n"
        "Construye tu propia vaquería y convierte la leche en GRAM reales 💎\n\n"
        "🎁 <b>Empieza gratis</b> — tu primera vaca es un regalo\n"
        "🥛 Tus vacas producen leche cada hora, incluso mientras duermes\n"
        "💸 <b>Retira desde el primer día</b> — directo a tu billetera TON\n"
        "⚡ Pagos automáticos, sin esperar aprobación\n"
        "👥 Invita amigos y gana en 3 niveles\n\n"
        "Toca Jugar y recoge tu primera leche ahora 👇"
    )

    teclado = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(
            text="🐄 Jugar ahora", 
            web_app=WebAppInfo(url=f"{WEBAPP_URL}?user_id={user_id}")
        )],
        [
            InlineKeyboardButton(text="💸 Pagos", url="https://t.me/gramfivepayout"),
            InlineKeyboardButton(text="📢 Noticias", url="https://t.me/B4DBOYTCRYPTO")
        ],
        [InlineKeyboardButton(text="🆘 Soporte", url="https://t.me/TuSoporte")]
    ])

    await message.answer(texto, parse_html="HTML", reply_markup=teclado)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
