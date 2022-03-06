from config import ASSISTANT_PREFIX
from Yukki import BOT_NAME, BOT_USERNAME
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

START_TEXT = f"""
✨ **Merhaba MENTION !**

**Kullanabilirsiniz [{BOT_NAME}](https://t.me/{BOT_USERNAME}) Grup Görüntülü Sohbetinizde Müzik veya Video oynatmak için.**

💡 **Bot'un tüm komutlarını ve nasıl çalıştıklarını öğrenin. ➤ 📚 Komutlar düğmesi**
"""

COMMANDS_TEXT = f"""
✨ **Merhaba MENTION !**

**Komutlarımı öğrenmek için aşağıdaki düğmelere tıklayın.**
"""

START_BUTTON_GROUP = InlineKeyboardMarkup(
    [   
        [
            InlineKeyboardButton(
                text="📚 Komut", callback_data="command_menu"
            ),
            InlineKeyboardButton(
                text="🔧 Ayarlar", callback_data="settingm"
            ),                                   
        ],
        [
            InlineKeyboardButton(
                text="📣 Resmi Kanal", url="https://t.me/Sohbetdestek"
            ),
            InlineKeyboardButton(
                text="💬 Destek Grubu", url="https://t.me/BotDestekGrubu"
            ),                       
        ],        
    ]
)

START_BUTTON_PRIVATE = InlineKeyboardMarkup(
    [   [
            InlineKeyboardButton(
                text="➕ Beni Gruba Ekle ➕", url=f"https://t.me/{BOT_USERNAME}?startgroup=true"
            ),            
        ],
        [   
            InlineKeyboardButton(
                text="📚 Komut", callback_data="command_menu"
            ),                       
        ],
        [
            InlineKeyboardButton(
                text="📣 Resmi Kanal", url="https://t.me/Sohbetdestek"
            ),
            InlineKeyboardButton(
                text="💬 Destek Grubu", url="https://t.me/BotDestekGrubu"
            ),                       
        ],        
    ]
)

COMMANDS_BUTTON_USER = InlineKeyboardMarkup(
    [   [
            InlineKeyboardButton(
                text="Yönetici Komutları", callback_data="admin_cmd"
            ),
            InlineKeyboardButton(
                text="Bot Komutları", callback_data="bot_cmd"
            ),            
        ],
        [
            InlineKeyboardButton(
                text="Komutları Yürüt", callback_data="play_cmd"
            ),            
            InlineKeyboardButton(
                text="Ek Komutlar", callback_data="extra_cmd"
            ),                                   
        ],
        [
            InlineKeyboardButton(
                text="↪️ Geri", callback_data="command_menu"
            ),
            InlineKeyboardButton(
                text="🔄 Kapat", callback_data="close_btn"
            ),            
        ],                
    ]
)

COMMANDS_BUTTON_SUDO = InlineKeyboardMarkup(
    [   [
            InlineKeyboardButton(
                text="Yönetici Komutları", callback_data="admin_cmd"
            ),
            InlineKeyboardButton(
                text="Bot Komutları", callback_data="bot_cmd"
            ),            
        ],
        [
            InlineKeyboardButton(
                text="Komutları Yürüt", callback_data="play_cmd"
            ),
            InlineKeyboardButton(
                text="Sudo Komutları", callback_data="sudo_cmd"
            ),            
        ],
        [
            InlineKeyboardButton(
                text="Ek Komutlar", callback_data="extra_cmd"
            ),                                   
        ],
        [
            InlineKeyboardButton(
                text="↪️ Geri", callback_data="command_menu"
            ),
            InlineKeyboardButton(
                text="🔄 Kapat", callback_data="close_btn"
            ),            
        ],                
    ]
)

BACK_BUTTON = InlineKeyboardMarkup(
    [   [
            InlineKeyboardButton(
                text="↪️ Geri", callback_data="advanced_cmd"
            ),
            InlineKeyboardButton(
                text="🔄 Kapat", callback_data="close_btn"
            ),            
        ],                        
    ]
)

SUDO_BACK_BUTTON = InlineKeyboardMarkup(
    [   [
            InlineKeyboardButton(
                text="Diğer Sudo Komutları", url="https://telegra.ph/SiestaXMusic-Sudo-Commands-02-08"
            ),                        
        ],
        [
            InlineKeyboardButton(
                text="↪️ Geri", callback_data="advanced_cmd"
            ),
            InlineKeyboardButton(
                text="🔄 Kapat", callback_data="close_btn"
            ),            
        ],                        
    ]
)


ADMIN_TEXT = f"""
İşte yardım **Yönetici Komutları:**


--**YALNIZCA SESİ YÖNETEN YÖNET KOMUTLARI:**--

/durdur 
- Sesli sohbette çalan müziği duraklatma.

/devam 
- Sesli sohbette duraklatılmış müziği sürdürme.

/atla 
- Sesli sohbette geçerli müzik çalmayı atlama

/son 
- Müzik çalmayı durdurma.


--**Yetkili Kullanıcılar Listesi:**--

**{BOT_NAME} yönetici komutlarını kullanmak isteyen yönetici olmayan kullanıcılar için ek bir özelliğe sahiptir**
- Kimlik doğrulama kullanıcıları, Yönetici Hakları olmadan bile Sesli Sohbetleri atlayabilir, duraklatabilir, durdurabilir, sürdürebilir.


/auth [Kullanıcı Adı veya İletiyi Yanıtlama] 
- Grubun AUTH LİSTESİ'ne kullanıcı ekleme.

/unauth [Kullanıcı Adı veya İletiyi Yanıtlama] 
- Kullanıcıyı grubun AUTH Listesinden kaldırma.

/authusers 
- Grubun AUTH LIST'ini denetleyin.
"""

BOT_TEXT = """
İşte yardım **Bot Komutları:**


/start 
- Müzik Bot'ını başlat.

/help 
- Komutların ayrıntılı açıklamalarını içeren Komutlar Yardımcısı Menüsünü Alıp Al.

/settings 
- Bir grubun Ayarlar panosunu alıp alın. Kimlik Doğrulama Kullanıcıları Modu'nu yönetebilirsiniz. Buradan Komut modu.

/ping
- Bot ping ve Kontrol Ram, Cpu vb Müzik Bot istatistikleri."""

PLAY_TEXT = """
İşte yardım fo **Oynat Komut:**


--**Youtube ve Telegram Dosyaları:**--

/oynat __[Müzik Adı]__(Bot Youtube'da arama yapacak)
/oynat __[Youtube Bağlantıyı veya Çalma Listesini izleme]__
/oynat __[Video, Canlı, M3U8 Bağlantıları]__
/oynat __[Ses veya Video Dosyasını Yanıtlama]__
- Elde ettiğiniz satır içi Düğmeler'i seçerek Sesli Sohbette Video veya Müzik Akışı


--**Çalma Listeleri:**--

/playplaylist 
- Kaydedilmiş Çalma Listenizi oynatmaya başlayın.

/playlist 
- Sunucularda Kayıtlı Çalma Listenizi Denetleme.

/delmyplaylist
- Çalma listenizdeki kaydedilmiş müzikleri silme

/delgroupplaylist
- Grubunuzun çalma listesindeki kaydedilmiş müzikleri silme [Yönetici Hakları Gerektirir.]
"""

SUDO_TEXT = f"""
İşte yardımı **Sudo Komutları:**

**<u>ADD & REMOVE SUDO USERS :</u>**
/addsudo [Username or Reply to a user]
/delsudo [Username or Reply to a user]

**<u>BOT COMMANDS:</u>**
/restart - Restart Bot. 
/update - Update Bot.
/stats - Check Bots Stats

**<u>BLACKLIST CHAT FUNCTION:</u>**
/blacklistchat [CHAT_ID] - Blacklist any chat from using Music Bot
/whitelistchat [CHAT_ID] - Whitelist any blacklisted chat from using Music Bot

**<u>BROADCAST FUNCTION:</u>**
/broadcast [Message or Reply to a Message] - Broadcast message.
/broadcast_pin [Message or Reply to a Message] - Broadcast message with pin [Disabled Notifications].
/broadcast_pin_loud [Message or Reply to a Message] - Broadcast message with pin [Enabled Notifications].

**<u>GBAN FUNCTION:</u>**
/gban [Username or Reply to a user] - Ban a user globally in Bot's Served Chats and prevents user from using bot commands.
/ungban [Username or Reply to a user] - Remove a user from Bot's GBan List.
"""

EXTRA_TEXT = """
Here is the help for **Extra Commands:**


/lyrics [Music Name]
- Searches Lyrics for the particular Music on web.

/sudolist 
- Check Sudo Users of Music Bot

/song [Track Name] or [YT Link]
- Download any track from youtube in mp3 or mp4 formats via Bot.

/queue
- Check Queue List of Music.
"""

BASIC_TEXT = """
💠 **Basic Commands:**

/start - start the bot
/help - get help message
/oynat - play songs or videos in vc
/dinle - play songs directly in vc
/spotify - play songs from spotify
/resso - play songs from resso
/lyrics - get lyrics of song
/ping - ping the bot
/playlist - play your playlist
/song - download a song as music or video
/settings - settings of the group
/queue - get queued song
"""

BASIC_BACK_BUTTON = InlineKeyboardMarkup(
    [   [
            InlineKeyboardButton(
                text="↪️ Back", callback_data="command_menu"
            ),
            InlineKeyboardButton(
                text="🔄 Close", callback_data="close_btn"
            ),            
        ],                        
    ]
)

COMMAND_MENU_BUTTON = InlineKeyboardMarkup(
    [   [
            InlineKeyboardButton(
                text="🔍 Basic Commands", callback_data="basic_cmd"
            ),                                   
        ],
        [
            InlineKeyboardButton(
                text="📚 Advanced Commands", callback_data="advanced_cmd"
            ),
        ],
        [
            InlineKeyboardButton(
                text="↪️ Back", callback_data="open_start_menu"
            ),
            InlineKeyboardButton(
                text="🔄 Close", callback_data="close_btn"
            ),            
        ],                        
    ]
)
