import asyncio
from os import path

from pyrogram import filters
from pyrogram.types import (InlineKeyboardMarkup, InputMediaPhoto, Message,
                            Voice)
from youtube_search import YoutubeSearch

from Yukki import (BOT_USERNAME, DURATION_LIMIT, DURATION_LIMIT_MIN,
                   MUSIC_BOT_NAME, app, db_mem)
from Yukki.Decorators.permission import PermissionCheck
from Yukki.Inline import song_download_markup, song_markup
from Yukki.Utilities.url import get_url
from Yukki.Utilities.youtube import get_yt_info_query, get_yt_info_query_slider



loop = asyncio.get_event_loop()


__MODULE__ = "Şarkı Bul"
__HELP__ = """

/bul [Youtube URL'si veya Arama Sorgusu] 
- Belirli bir sorguyu ses veya video biçiminde indirin.
"""

@app.on_message(filters.command(["bul", f"bul@{BOT_USERNAME}"]))
@PermissionCheck



@app.on_callback_query(filters.regex(pattern=r"song_right"))
async def song_right(_, CallbackQuery):
    callback_data = CallbackQuery.data.strip()
    callback_request = callback_data.split(None, 1)[1]
    what, type, query, user_id = callback_request.split("|")
    if CallbackQuery.from_user.id != int(user_id):
        return await CallbackQuery.answer(
            "Kendi müziğinizi arayın. Bu düğmeyi kullanmanıza izin verilmiyor.",
            show_alert=True,
        )
    what = str(what)
    type = int(type)
    if what == "F":
        if type == 9:
            query_type = 0
        else:
            query_type = int(type + 1)
        await CallbackQuery.answer("Sonraki Sonucu Alma", show_alert=True)
        (
            title,
            duration_min,
            duration_sec,
            thumb,
            videoid,
        ) = await loop.run_in_executor(
            None, get_yt_info_query_slider, query, query_type
        )
        buttons = song_markup(
            videoid, duration_min, user_id, query, query_type
        )
        med = InputMediaPhoto(
            media=thumb,
            caption=f"📎 Başlık: **{title}\n\n⏳ Süre:** {duration_min} Dakika\n\n__[Video Hakkında Ek Bilgi Alın](https://t.me/{BOT_USERNAME}?start=info_{videoid})__",
        )
        return await CallbackQuery.edit_message_media(
            media=med, reply_markup=InlineKeyboardMarkup(buttons)
        )
    if what == "B":
        if type == 0:
            query_type = 9
        else:
            query_type = int(type - 1)
        await CallbackQuery.answer("Önceki Sonucu Alma", show_alert=True)
        (
            title,
            duration_min,
            duration_sec,
            thumb,
            videoid,
        ) = await loop.run_in_executor(
            None, get_yt_info_query_slider, query, query_type
        )
        buttons = song_markup(
            videoid, duration_min, user_id, query, query_type
        )
        med = InputMediaPhoto(
            media=thumb,
            caption=f"📎 Başlık: **{title}\n\n⏳ Süre:** {duration_min} Dakika\n\n__[Video Hakkında Ek Bilgi Alın](https://t.me/{BOT_USERNAME}?start=info_{videoid})__",
        )
        return await CallbackQuery.edit_message_media(
            media=med, reply_markup=InlineKeyboardMarkup(buttons)
        )
