from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
Selam {}

Hoşgeldiniz {}

Instagram'dan profil resimleri, videolar, resimler ve makaraları yazı başlığıyla birlikte indirebilirim.
Ayrıca özel gönderileri indirmem için bana yetki verebilirsiniz..

Daha fazla bilgi edinmek için aşağıdaki düğmeleri kullanın.

Tarafından: @EpicEye @EpicEyeBots
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton(text="🏠 Eve dön 🏠", callback_data="home")]
    ]

    # Rest Buttons
    buttons = [
        [InlineKeyboardButton("✨ Bot Durumu ve Daha Fazla Bot ✨", url="https://t.me/EpicEyeBots")],
        [
            InlineKeyboardButton("Nasıl kullanılır ❔", callback_data="help"),
            InlineKeyboardButton(" Hakkında ", callback_data="about")
        ],
        [InlineKeyboardButton(" Daha Şaşırtıcı botlar ", url="https://t.me/EpicEyeBots")],
    ]

    # Help Message
    HELP = """
1) **Resimler, Videolar ve Makaralar**
Altyazı dahil gönderi içeriğini almak için bağlantıyı buraya gönderin.

2) **Profil fotoğrafları**
komutu kullanın `/profile_pic` veya `/dp` profil resmini almak için instagram kullanıcı adı ile birlikte.
Example : `/dp StarkProgrammer`

3) **Özel Gönderiler**
Botu özel gönderileri indirmesi için yetkilendirin. Kullanmak /auth

**Not** : Hikayeler ve IGTV desteklenmez.

Yetkilendirmek için /auth - Yetkisini kaldırmak için /unauth 
"""

    # About Message
    ABOUT = """
**Bu Bot Hakkında** 

Instagram içeriğini indirmek için bir telegram botu: @EpicEyeBots

Kanal: @EpicEyeBots

Grubumuz : @SohbetAlley

Developer : @Bloodpers
    """
