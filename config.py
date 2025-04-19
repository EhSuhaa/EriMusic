import re
import os
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("API_ID", 26792227))
API_HASH = getenv("API_HASH", "279cafdde7f7fce91b4868261a0578b2")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = "7321688096:AAHlF-3S-HDlWU6fx0GyG2haselZ3-BCWmA"

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://api:api@indiabeatz.lbxe2o1.mongodb.net/?retryWrites=true&w=majority&appName=indiabeatz")
MUSIC_BOT_NAME = "Eri Music"
PRIVATE_BOT_MODE = getenv("PRIVATE_BOT_MODE", None)

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 900))

# Chat id of a group for logging bot's activities
LOGGER_ID = -1002505086730

# Get this value from @BRANDRD_ROBOT on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID", "6833733930"))

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/EhSuhaa/MEst",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = "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" 

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/IndiaBeatzStatus")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/IndiaBeatzStatus")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))

# Auto Gcast/Broadcast Handler (True = broadcast on , False = broadcast off During Hosting, Dont Do anything here.)
AUTO_GCAST = os.getenv("AUTO_GCAST")

# Auto Broadcast Message That You Want Use In Auto Broadcast In All Groups.
AUTO_GCAST_MSG = getenv("AUTO_GCAST_MSG", "")

# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "3f07a3dfc18c44278c0737a92f6f8cc3")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "c4031e1e47944a978ec43c71359689b5")


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
SERVER_PLAYLIST_LIMIT = int(getenv("SERVER_PLAYLIST_LIMIT", "50"))
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", "25"))

SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "180"))
SONG_DOWNLOAD_DURATION_LIMIT = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "2000"))

# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from @BRANDEDSTRINGSESSION_BOT on Telegram
STRING1 = getenv("STRING_SESSION",  "BQGY0SMAMA06wV--P8WAt-zkzSb1taZ8qMZ2lVoJe8ijB_02wZUxZ5nEtuwd7WFvXVBfmLLpUjEjU2L_B6cFm-66vVVC95OsZn-0oe2XH3kdTc8fVb7bOTBrEmd6n9Lp3b1di01BTwm7R7bHj6sYayUIKkZX_SC0B64ADDFrPRBM277EqFL4edCQWJQR8dagfQcsU_DFLzXSYvE82orEZj5jl6PU4ofXANSFlS4LlbcW1DXMxm0o3-GvD8jLBfHLaIwBwmXIkXuJQhlRrxpnHKfr9vwEYyIOXW9T8J17LBm5M_TBXzG-Ts_5oj3WHpe1AYLjnU09INB0XSj9lAEStn3YZxsz5wAAAAGbuxDPAA")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
LOG = 2
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv(
    "START_IMG_URL", "https://files.catbox.moe/mvpxyj.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://te.legra.ph/file/4f59fb748e1990acfa297.jpg"
)
PLAYLIST_IMG_URL = "https://files.catbox.moe/tq8l4a.jpg"
STATS_IMG_URL = "https://files.catbox.moe/tq8l4a.jpg"
TELEGRAM_AUDIO_URL = "https://files.catbox.moe/tq8l4a.jpg"
TELEGRAM_VIDEO_URL = "https://files.catbox.moe/tq8l4a.jpg"
STREAM_IMG_URL = "https://files.catbox.moe/tq8l4a.jpg"
SOUNCLOUD_IMG_URL = "https://files.catbox.moe/tq8l4a.jpg"
YOUTUBE_IMG_URL = "https://files.catbox.moe/tq8l4a.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://files.catbox.moe/tq8l4a.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://files.catbox.moe/tq8l4a.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://files.catbox.moe/tq8l4a.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
