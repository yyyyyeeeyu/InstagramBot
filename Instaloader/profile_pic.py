import os
import shutil
import instaloader
from pyrogram import Client, filters
from instaloader.exceptions import QueryReturnedNotFoundException, ProfileNotExistsException


@Client.on_message(filters.private & filters.command(["profile_pic", "dp"]))
async def dp(_, msg):
    status = await msg.reply('Lütfen bekleyin...', quote=True)
    if len(msg.command) == 1:
        await msg.reply("Lütfen boş komut kullanmayın. Profil resmi almak için doğru format aşağıdadır. "
                        "\n\n`/profile_pic instagram-username` \n\nMisal : `/profile_pic thebloodper`")
        return
    elif len(msg.command) > 2:
        await msg.reply("Bir seferde 1 kullanıcı adı kullanın.")
        return
    text = msg.command[1]
    if text.startswith('@'):
        text = text[1:]
    try:
        instaloader.Instaloader().download_profile(text, profile_pic_only=True)
    except (QueryReturnedNotFoundException, ProfileNotExistsException):
        await status.delete()
        await msg.reply("Böyle Bir Instagram Hesabı Yok.", quote=True)
        return
    files = os.listdir(text.lower())
    for file in files:
        if file.endswith(".jpg"):
            caption = f"Profil Resmi [@{text}](https://instagram.com/{text}) \n\n @EpicEyeBots"
            await msg.reply_photo(f"{text}/{file}", caption=caption)
            await status.delete()
    shutil.rmtree(text)
