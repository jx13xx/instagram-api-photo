from instabot import Bot
from instapy_cli import client

def bot_func(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


    # bot = Bot()
    # bot.login(username = "randomshitisgoingrightnow", password = "95323752@Sharonjeen")
    #
    # bot.upload_photo("meme1.jpg", caption="Meme is always a meme")
    # bot.login(username = "randomshitisgoingrightnow", password = "95323752@Sharonjeen")
    #
    # bot.upload_photo("meme1.jpg", caption="Meme is always a meme")

    username = ''
    pasword = ''

    image = 'C:\\Users\jeenx\Desktop\kylie.jpg'
    text = 'sometimes a meme got a be a meme lol'

    with client(username, pasword) as cli:
        cli.upload(image,text)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    bot_func('PyCharm')


