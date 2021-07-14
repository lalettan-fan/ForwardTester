from os import environ
class Config(object):
    API_ID = environ.get("API_ID", None)
    API_HASH = environ.get("API_HASH", None)
    BOT_TOKEN = environ.get("BOT_TOKEN", None)
    STRING_SESSION = environ.get("STRING", None)
    SUDO_USERS = environ.get("SUDO_USERS", None)
    DB_URI = environ.get("DATABASE_URL", None)
    HELP_MSG = """
    The Commands in the Bot are:
    
    **Command :** /forward
    **Usage : ** Forwards messages from a channel to other.
    **Command :** /count
    **Usage : ** Returns the Total message sent using the Bot.
    **Command :** /reset
    **Usage : ** Resets the message count to 0.
    **Command :** /restart
    **Usage : ** Updates and Restarts the Bot.
    **Command :** /join
    **Usage : ** Joins the channel.
    **Command :** /help
    **Usage : ** Get the help of this Bot.
    **Command :** /status
    **Usage :** Check current status of Bot.
    **Command :** /uptime
    **Usage :** Check uptime of Bot.
    
    Bot is created by @lal_bakthan and @subinps
    """
