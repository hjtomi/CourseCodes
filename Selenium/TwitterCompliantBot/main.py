import twitter_compliant_bot
from twitter_compliant_bot import TwitterBot
from speedtest_bot import SpeedtestBot
import os

twitter_bot = TwitterBot(os.environ.get("EMAIL"), os.environ.get("PASSWORD"))
speedtest_bot = SpeedtestBot()

speeds = speedtest_bot.check_speeds()
download_speed = speeds["download"]
upload_speed = speeds["upload"]

if download_speed > 750 and upload_speed > 200:
    twitter_bot.send_tweet(f"Wow, my download speed is {download_speed} and my upload speed is {upload_speed}!")
