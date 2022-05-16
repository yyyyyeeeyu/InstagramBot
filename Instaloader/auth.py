import asyncio
from pyrogram import Client, filters
from .database.users_sql import set_info, delete_info


@Client.on_message(filters.private & filters.incoming & filters.command("auth"))
async def _auth(bot, msg):
    await msg.reply("**Yalnızca bize güveniyorsanız yetkilendirin** \n\n"
                    "1) Yetki vermek için hesabınız için instagram kullanıcı adı ve şifre sağlamanız gerekir. "
                    " size soruldugunda.\n"
                    "2) Bu amaçla yeni bir hesap açmanızı öneririz çünkü instagram hesabınızı yasaklayabilir. "
                    "Size Sorulduğunda. \n\n"
                    "**Not** : Hesap yasaklarından sorumlu değiliz")
    confirmation = await bot.ask(msg.from_user.id,
                                 "**Devam etmek istiyor musunuz?** \n\n '`yes`' veya '`y`' yazın "
                                 "Onayla.\n iptal etmek için '`no`' veya '`n`' Yazın.")
    if not confirmation.text.lower() in ['yes', 'y']:
        await confirmation.reply("Yetkilendirme İptal Edildi", quote=True)
        await msg.stop_propagation()
        return
    username = await bot.ask(msg.from_user.id, "Lütfen Instagram kullanıcı adınızı gönderin", filters=filters.user(msg.from_user.id))
    password = await bot.ask(msg.from_user.id, "Lütfen Instagram Şifrenizi gönderin", filters=filters.user(msg.from_user.id))
    await msg.reply("Checking if login credentials are valid...")
    command = f"instaloader -l {username.text} -p {password.text}"
    proc = await asyncio.subprocess.create_subprocess_shell(
        command,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await proc.communicate()
    if "login error" in str(stderr).lower():
        await msg.reply(f'Log in failed. \n\n{str(stderr.decode("utf-8")).replace("Fatal error: Login error: ", "")} '
                        f'\n Lütfen şununla yeniden yetkilendirmeyi deneyin: /auth.')
        return
    await set_info(msg.from_user.id, username.text, password.text)
    await msg.reply("Yetkilendirme başarılı oldu. Özel gönderileri şimdi indirebilirsiniz!")


@Client.on_message(filters.private & filters.incoming & filters.command("unauth"))
async def _unauth(_, msg):
    success = await delete_info(msg.from_user.id)
    if success:
        await msg.reply("Kimlik bilgileriniz veritabanımdan silindi. \n\n"
                        "Artık hesabınıza erişemiyorum ve özel gönderileri indiremiyorsunuz")
    else:
        await msg.reply("Yine de bana yetki vermedin!")
