# cancel the test. Telegram dev site is doing shit
import telegram_config as tgconf
from telethon import TelegramClient, sync
from telethon.tl import types
import sys
import os
import argparse
import socks
from time import sleep


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
            sys.stdout.write(
                "Please respond with 'yes' or 'no' (or 'y' or 'n').\n")


def download(msgs, dp):
    # print(msgs)
    wait = 0
    for msg in msgs:
        if not hasattr(msg, 'media') or msg.media is None:
            continue

        # if wait > 100:
        #     print("Dozing off")
        #     sleep(60)
        #     print("We are back")
        #     wait = 0

        elif hasattr(msg.media, 'document'):
            # Get the filename
            for attribute in msg.media.document.attributes:
                if isinstance(attribute, types.DocumentAttributeFilename):
                    file_name = dp + attribute.file_name

            if not os.path.isfile(file_name):
                msg.download_media(file_name)
                print(msg.id, " Downloaded as : ", file_name)

            else:
                wait += 1
                print(msg.id, "Already Present")

        elif hasattr(msg.media, 'photo'):
            if len(msg.message) < 140 and len(msg.message) != 0:
                file_name = dp + "Photo_" + msg.message
            else:
                file_name = dp + "Photo_" + str(msg.media.photo.id)

            if not os.path.isfile(file_name) and not os.path.isfile(file_name + ".jpg"):
                msg.download_media(file_name)
                print(msg.id, "Downloaded as : ", file_name)
            else:
                wait += 1
                print(msg.id, "Already Present")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--conf', '-c')
    # Start the client
    client = TelegramClient('xypnox', tgconf.app_id, tgconf.api_hash,
                            proxy=(socks.HTTP, '172.16.2.30', 8080)
                            )
    client.start()
    me = client.get_me()
    print("Hi, ", me.first_name, "Welcome to this world")

    # This is a joke, ignore this line
    # client.send_message('evi1haxor', "This is a telethon test")

    for entry in tgconf.chats:
        chat = client.get_entity(entry)

        download_path = os.path.expanduser(
            '~') + '/Downloads/' + chat.title + '/'

        if not os.path.exists(download_path):
            os.makedirs(download_path)

        # Get messages
        msgs = client.get_messages(entry, limit=None)

        # Count the number of messages with media
        count = 0
        for msg in msgs:
            if hasattr(msg, 'media') and msg.media is not None:
                count += 1
        print(chat.title, " has Total Messages with media = ", count)

        answer = query_yes_no("Do you want to download these files?")

        if answer is True:
            print("Downloading...")
            download(msgs, download_path)
            print("Wow such speed much style")
    client.disconnect()
