class Translation(object):
    START_TEXT = """Hi {},
I'm URL Uploader!
You can upload direct links,Youtube Links Using this bot!☺️
Just send me a direct link and see the majic 😎

/help for more details!

©️ Made by <a href="https://t.me/darkz_hacker_devil">Ravidu Yasas</a>
©️ Powered by <a href="https://t.me/media_bot_updates">Bot Shadows</a>"""
    FORMAT_SELECTION = "Select the desired format: <a href='{}'>file size might be approximate</a> \nIf you want to set custom thumbnail, send photo before or quickly after tapping on any of the below buttons.\nYou can use /deletethumbnail to delete the auto-generated thumbnail."
    SET_CUSTOM_USERNAME_PASSWORD = """If you want to download premium videos, provide in the following format:
URL | filename | username | password"""
    DOWNLOAD_START = "Downloading 📥..."
    UPLOAD_START = "Uploading 📤..."
    RCHD_TG_API_LIMIT = "Downloaded in {} seconds.\nDetected File Size: {}\nSorry. But, I cannot upload files greater than 2GB due to Telegram API limitations."
    AFTER_SUCCESSFUL_UPLOAD_MSG = "Thanks for using @crazy_url_upload_bot\n\n<b>Join : @media_bot_updates</b>"
    AFTER_SUCCESSFUL_UPLOAD_MSG_WITH_TS = "Downloaded in {} seconds.\nUploaded in {} seconds.\n\n@crazy_url_upload_bot"
    SAVED_CUSTOM_THUMB_NAIL = "Custom video / file thumbnail saved. This image will be used in the video / file."
    DEL_ETED_CUSTOM_THUMB_NAIL = "Custom thumbnail cleared succesfully. ✅"
    CUSTOM_CAPTION_UL_FILE = "{}"
    NO_VOID_FORMAT_FOUND = "ERROR❌❌❌\n<b>YouTubeDL</b> said: {}"
    HELP_USER = """How to Use Me? Follow These steps!
    
1. Send url (example.domain/File.mp4 | New Filename.mp4).
2. Send Image As Custom Thumbnail (Optional).
3. Select the button.
   SVideo - Give File as video with Screenshots
   DFile  - Give File (video) as file with Screenshots
   Video  - Give File as video without Screenshots
   File   - Give File without Screenshots

If bot didn't respond, contact @helpingbotbyfatsgbot"""
    REPLY_TO_MEDIA_ALBUM_TO_GEN_THUMB = "Reply /generatecustomthumbnail to a media album, to generate custom thumbail @media_bot_updates"
    ERR_ONLY_TWO_MEDIA_IN_ALBUM = """Media Album should contain only two photos. Please re-send the media album, and then try again, or send only two photos in an album."
You can use /rename command after receiving file to rename it with custom thumbnail support.
"""
    CANCEL_STR = "Process Cancelled"
    ZIP_UPLOADED_STR = "Uploaded {} files in {} seconds @media_bot_updates"
    SLOW_URL_DECED = "Gosh that seems to be a very slow URL. Since you were screwing my home, I am in no mood to download this file. Meanwhile, why don't you try this:==> https://shrtz.me/PtsVnf6 and get me a fast URL so that I can upload to Telegram, without me slowing down for other users."
