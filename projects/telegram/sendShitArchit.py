# cancel the test. Telegram dev site is doing shit
import telegram_config as tgconf
from telethon import TelegramClient, sync

client = TelegramClient('xypnox', tgconf.app_id, tgconf.api_hash)
client.start()
me = client.get_me()
print("Hi, ", me.first_name, "Welcome to this world")
client.send_message('evi1haxor', "This is a telethon test")
primes = []


def is_prime(x):
    a = True
    for i in primes:
        if x % i == 0:
            a = False
            break
        if i > int(x ** 0.5):
            break
    if a:
        primes.append(x)
        message = "Hi I found a prime : " + str(x)
        client.send_message('evi1haxor', message)
    return a


if __name__ == "__main__":
    for i in range(2, int(input('Till where primes =]'))):
        is_prime(i)
    print("Mission Successful")
    client.disconnect()
