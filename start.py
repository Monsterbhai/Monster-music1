from pyrogram.types import InlineKeyboardButton

import config
from DAXXMUSIC import app


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["MONSTER"], url=f"https://t.me/{app.username}?startgroup=true"
            ),
            InlineKeyboardButton(text=_["SUPPORT"], url=config.SUPPORT_CHAT),
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["MONSTER"],
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(text=_["BACK"], callback_data="settings_back_helper"),
        ],
        [
            InlineKeyboardButton(text=_["SUPPORT"], url=config.SUPPORT_CHANNEL),
            InlineKeyboardButton(text=_["CHAT"], url=config.SUPPORT_CHAT),
        ],
        [
            InlineKeyboardButton(text=_["MONSTER"], user_id=config.OWNER_ID),
        ],   
    ]
    return buttons
