import discord
import os
import requests
from discord.ext import commands
from threading import Thread
from time import time, sleep
from colorama import Fore

b = Fore.LIGHTBLACK_EX
w = Fore.WHITE
r = Fore.RESET
p = Fore.MAGENTA
r2 = Fore.RED

token = input(f'{w}[{r}{p}BOT TOKEN{r}{w}] : {r}')
os.system('clear')

intents = discord.Intents.all()
intents.members = True
client = commands.Bot(command_prefix='tsu', intents=intents)

class Tsu:
  async def tsuxlux(self):
    print(f'{w}[{r}{p}Og Mass DM | Logged In As {client.user}{r}{w}]{r}')
    print(f''' 
            {p}╔═╗╔═╗  ╔╦╗╔═╗╔═╗╔═╗  ╔╦╗╔╦╗{r}
            {b}║ ║║ ╦  ║║║╠═╣╚═╗╚═╗   ║║║║║{r}
            {w}╚═╝╚═╝  ╩ ╩╩ ╩╚═╝╚═╝  ═╩╝╩ ╩{r}
        {p}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{r}
                  {p}Made By tsu#1800{r}
        {p}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{r}
              {p}Option 1{r}{w}: SCRAPES USERS{r}
              {p}Option 2{r}{w}: MASS DM{r} 
        {p}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{r}''')
    option = input(f'{w}[{r}{p}OPTION{r}{w}] : {r}')
    if option == '1':
      os.system('clear')
      await self.scrape() # SCRAPE TO GET USER IDS
      await self.tsuxlux()
    elif option == '2':
      os.system('clear')
      await self.tsumassdm()
      await self.tsuxlux()

  async def scrape(self):
    guild = input(f'{w}[{r}{p}GUILD TO SCRAPE{r}{w}] : {r}')
    await client.wait_until_ready()
    tsunami = client.get_guild(int(guild))
    members = await tsunami.chunk()

    try:
      os.remove('members.tsu')
    except:
      pass

    membercount = 0
    with open('members.tsu', 'a') as m:
      for member in members:
        m.write(str(member.id) + '\n')
        membercount += 1
      print(f'{w}[{r}{p}SCRAPED {membercount} MEMBERS{r}{w}]{r}')
      m.close()

  def massdm(self, guild, user, message):
    while True:
      data = {
        'recipient_id': user,
        'content': message
      }

      re = requests.post(f'https://discord.com/api/v9/users/@me/channels', headers={'Authorization': f'Bot {token}'}, json=data)
      if re.status_code == 200 or re.status_code == 201 or re.status_code == 204:
        print(f'{w}[{r}{p}SUCCESSFULLY MESSAGED {user.strip()}{r}{w}]{r}')
        break
      elif re.status_code == 429:
        tsu = re.json()['retry_after']
        print(f'{w}[{r}{r2}RETRYING AFTER {tsu} SECONDS{r}{w}]{r}')
        sleep(tsu)
        break
      else:
        print(f'{w}[{r2}FAILED TO DM {user.strip()}{r}{w}]{r}')   
        break      

  async def tsumassdm(self):
    guild = input(f'{w}[{r}{p}GUILD ID{r}{w}] : {r}')
    message = input(f'{w}[{r}{p}MESSAGE{r}{w}] : {r}')
    members = open('members.tsu')
    for member in members:
      Thread(target=self.massdm, args=(guild, member, message)).start()

  @client.event
  async def on_ready():
    await Tsu().tsuxlux()

client.run(token)
