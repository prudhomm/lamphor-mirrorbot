from speedtest import Speedtest
from bot.helper.telegram_helper.filters import CustomFilters
from bot import dispatcher
from bot.helper.telegram_helper.bot_commands import BotCommands
from bot.helper.telegram_helper.message_utils import sendMessage, editMessage, deleteMessage, sendPhoto
from telegram.ext import CommandHandler


def speedtest(update, context):
    speed = sendMessage("<code>Running speed test...</code>", context.bot, update)
    test = Speedtest()
    test.get_best_server()
    test.download()
    test.upload()
    test.results.share()
    result = test.results.dict()
    result_msg = (
        f"<b>Started at {result['timestamp']}</b>\n\n"

        f"<b>Client</b>\n"
        f"<b>Country:</b> <code>{result['client']['country']}</code>\n"
        f"<b>ISP:</b> <code>{result['client']['isp']}</code>\n\n"

        f"<b>Server</b>"
        f"<b>Name:</b> <code>{result['server']['name']}</code>\n"
        f"<b>Country:</b> <code>{result['server']['country']}, {result['server']['cc']}</code>\n"
        f"<b>Sponsor:</b> <code>{result['server']['sponsor']}</code>\n\n"

        f"<b>SpeedTest Results</b>\n"
        f"<b>Upload:</b> <code>{speed_convert(result['upload'] / 8)}</code>\n"
        f"<b>Download:</b>  <code>{speed_convert(result['download'] / 8)}</code>\n"
        f"<b>Ping:</b> <code>{result['ping']} ms</code>\n"
        f"<b>ISP Rating:</b> <code>{result['client']['isprating']}</code>\n\n"
    )

    deleteMessage(context.bot, speed)
    sendPhoto(context.bot, result['share'],
              caption=result_msg)


def speed_convert(size):
    """Hi human, you can't read bytes?"""
    power = 2 ** 10
    zero = 0
    units = {0: "", 1: "Kb/s", 2: "MB/s", 3: "Gb/s", 4: "Tb/s"}
    while size > power:
        size /= power
        zero += 1
    return f"{round(size, 2)} {units[zero]}"


SPEED_HANDLER = CommandHandler(BotCommands.SpeedCommand, speedtest, 
                                                  filters=CustomFilters.owner_filter | CustomFilters.authorized_user, run_async=True)

dispatcher.add_handler(SPEED_HANDLER)
