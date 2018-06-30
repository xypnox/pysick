# cancel the test. Telegram dev site is doing shit
import telegram_config as tgconf
from telethon import TelegramClient, sync
import sys


def query_yes_no(question, default="yes"):
    """Ask a yes/no question via raw_input() and return their answer.
    "question" is a string that is presented to the user.
    "default" is the presumed answer if the user just hits <Enter>.
        It must be "yes" (the default), "no" or None (meaning
        an answer is required of the user).
    The "answer" return value is True for "yes" or False for "no".
    """
    valid = {"yes": True, "y": True, "ye": True,
             "no": False, "n": False}
    if default is None:
        prompt = " [y/n] "
    elif default == "yes":
        prompt = " [Y/n] "
    elif default == "no":
        prompt = " [y/N] "
    else:
        raise ValueError("invalid default answer: '%s'" % default)

    while True:
        sys.stdout.write(question + prompt)
        choice = input().lower()
        if default is not None and choice == '':
            return valid[default]
        elif choice in valid:
            return valid[choice]
        else:
            sys.stdout.write("Please respond with 'yes' or 'no' (or 'y' or 'n').\n")


client = TelegramClient('xypnox', tgconf.app_id, tgconf.api_hash)
client.start()
me = client.get_me()
print("Hi, ", me.first_name, "Welcome to this world")
client.send_message('evi1haxor', "This is a telethon test")

# for dialog in client.get_dialogs(limit=10):
#     print(dialog.name, dialog.draft.text)


msgs = client.get_messages(tgconf.test_channel, limit=100)

count = 0

for msg in msgs.data:
    print(msg.id)
    if hasattr(msg, 'media'):
        count += 1
        print("Has media")

print("Total Messages with media = ", count)

# Download the most recent file
# Recommended t install `cryptg` package to speedup downloads
msgs.data[0].download_media()


# answer = query_yes_no("Do you want to download the files?")
# if answer is True:
#     print("Downloading...")
#     for msg in msgs.data:
#         print(msg.id)
#         if hasattr(msg, 'media'):
#             msg.download_media()
client.disconnect()
