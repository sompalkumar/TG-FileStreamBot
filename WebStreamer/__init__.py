# This file is a part of TG-FileStreamBot
# Coding : Jyothis Jayanth [@EverythingSuckz]
import pyrogram.utils

# 64-bit Telegram Channel IDs (-1004xxxxxxxxx) को सपोर्ट करने के लिए पैच
pyrogram.utils.MIN_CHANNEL_ID = -10099999999999

def patched_get_peer_type(peer_id: int) -> str:
    peer_id_str = str(peer_id)
    if not peer_id_str.startswith("-"):
        return "user"
    elif peer_id_str.startswith("-100"):
        return "channel"
    else:
        return "chat"

pyrogram.utils.get_peer_type = patched_get_peer_type

import time
from .vars import Var
from WebStreamer.bot.clients import StreamBot

__version__ = "2.2.4"
StartTime = time.time()
