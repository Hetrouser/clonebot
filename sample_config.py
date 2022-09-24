#----------------------------------- https://github.com/m4mallu/clonebot --------------------------------------------#
import os
import logging

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

class Config(object):

    # Get a bot token from botfather
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "5417576584:AAE5B-Jj9FElzb60X6soD4FYh7VVRA8UJG4")

    # Get from my.telegram.org
    APP_ID = int(os.environ.get("APP_ID", "13400206"))

    # Get from my.telegram.org
    API_HASH = os.environ.get("API_HASH", "36d57bba68536f3f6f9a24a61f87de26")

    # Authorized users to use this bot
    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "").split())

    # Generate a user session string
    TG_USER_SESSION = os.environ.get("TG_USER_SESSION", "AQC5HoxNDDra0G5CwgD_2__EqvyLPUToeBuSiLuvSXklF-FAqS7dcp--f463Z6T6FHt4flW72YD5ON9Eop59oHFiuAqirWFKTLFNSE0EUCDHH5aE-zMIcmT_sGNWmKbge40rTH47l8vTebYXJ_IXvhSWS3Wh7enEMRDc-lHQZdNW8_pIteudylsucxJzzpb02sTyiBAritZ5NYR15Ic482Vy-Tg9WqWGuF8eJgyNQR8mADkJjRun_P-1WztdPhMMuOksGU0wq7Mvl23CPF6bALkEEB6pd50r77TiqOSFJi96hK5zzsigevLjOFnWKCPqkJWl4CmlhTzX8Mlx0Y9zVgITAAAAAVafVZgA")

    # Database URI
    DB_URI = os.environ.get("DATABASE_URL", "postgres://kwipjosbpahxjc:88aa63b96d47ac9c3b0a93a8115b47464444a220e9d955a3877a0d1e6c53bd48@ec2-52-16-194-155.eu-west-1.compute.amazonaws.com:5432/d3b8k537b157ft")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
