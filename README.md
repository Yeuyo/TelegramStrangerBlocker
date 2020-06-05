# TelegramStrangerBlocker (Work in Progress)
Automatic block stranger message request unless approved by owner.
The script will automatically move message from people not in the "safeusers" to archive and auto reply a pre-defined message.

This script make use of Telethon library and is heavily motivated by the auto reply feature written by https://medium.com/@jiayu./automatic-replies-for-telegram-85075f28321

## Installation steps:
# Hosting on own machine
1. Install Python3.
2. Install Telethon by typing "python3 -m pip install telethon" on command prompt or terminal (Windows/Linux).
3. Visit https://my.telegram.org/auth and login.
4. Go to API development tool.
5. Create an new app by giving it an app title and a short name.
6. You will be directed to another page with "App api_id" and "App api_hash".
7. Replace the "api_id", "api_hash", "phone", "session_file" and "safeusers" in the script.
8. Run the script.
