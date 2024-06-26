from twittercomplaint import InternetSpeedTwitterBot

PROMISED_DOWN = 150
PROMISED_UP = 10
TWITTER_EMAIL = ''
TWITTER_PASSWORD = ''
TWITTER_URL = 'https://x.com/home'

# Create a new object from class InternetSpeedTwitterBot
internet_speed_bot = InternetSpeedTwitterBot()

# Call the speed check function and get the speed of download and upload of internet VIA speedtest website
download_upload = internet_speed_bot.speedtest_check()

# If the download and upload lower then promised call function for connecting to twitter and tweet about it
if float(download_upload['download']) < PROMISED_DOWN and float(download_upload['upload']) < PROMISED_UP:
    tweet = (f'The promised Download is {PROMISED_DOWN} and the promised Upload is {PROMISED_UP} and instead'
             f'i got a download of {download_upload["download"]} and upload of {download_upload["upload"]}')
    internet_speed_bot.connect_twitter(tweet,TWITTER_EMAIL, TWITTER_PASSWORD)

# Close the speed test page after finishing test
internet_speed_bot.close_windows()