import base64

from aiogram import Router, Bot
from aiogram.types import Message, FSInputFile
from aiogram.filters import Command

from aiogram.utils.deep_linking import decode_payload, create_start_link
from aiogram.filters import CommandStart, CommandObject

import segno

from keyboards import main_keyboard
from lexicon import start_text

router: Router = Router()


def get_points(uid: str, dir="scan_bot/data.json"):
    from json import load
    with open(dir, 'r') as file:
        data = load(file)
    if uid in data:
        return data[uid]
    else:
        return 0


@router.message(Command(commands=["lk"]))
async def start_cmd(message: Message, bot: Bot):
    uid = message.from_user.id
    await message.answer(text=f"Сдавайте вторсырье, копите баллы и получайте приятные призы!"
                              f"\nВы собрали баллов: {get_points(str(uid))}\nСледующий раз при сдаче вторсырья покажите qr-код и вам начислят баллы", parse_mode="HTML")

    uid_bytes = str(uid).encode('utf-8')
    uid_64base = base64.b64encode(uid_bytes).decode('utf-8')
    link = "https://t.me/Ptichka_scan_qr_code_bot?start="+uid_64base

    qrcode = segno.make_qr(link)
    filename = "qrcodes/"+str(uid)+".png"
    qrcode.save(filename, scale=10, border=2)

    await message.answer_photo(photo=FSInputFile(filename), caption="QR-code")