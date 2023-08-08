#(©)Codexbotz

from aiohttp import web
from plugins import web_server
import asyncio
import pyromod.listen
from pyrogram import Client, filters
from pyrogram.enums import ParseMode
from pyrogram.types import Message
import sys
from datetime import datetime

from config import API_HASH, APP_ID, TG_BOT_TOKEN, PORT, ADMINS
import requests as ree
from bs4 import BeautifulSoup

'''
Sample output(bunch link)
<a class="noSelect content" data-minutelytitle="Dance Karnataka Dance Season 7 - August 06, 2023" href="/tv-shows/details/dance-karnataka-dance-season-7/0-6-4z5349291/dance-karnataka-dance-season-7-august-06-2023/0-1-6z5403327"><img alt="Dance Karnataka Dance Season 7 - August 06, 2023 Episode 30" crossorigin="anonymous" src="https://akamaividz2.zee5.com/image/upload/w_522,h_294,c_scale,f_webp,q_auto:eco/resources/0-1-6z5403327/list/0000015567f16274865e439785f652b73fc99ff5.jpg" title="Dance Karnataka Dance Season 7 - August 06, 2023 Episode 30" width="100%"/></a>
<a class="noSelect content" data-minutelytitle="Trinayani - August 07, 2023" href="/tv-shows/details/trinayani/0-6-3199/trinayani-august-07-2023/0-1-6z5407627"><img alt="Trinayani - August 07, 2023 Episode 795" crossorigin="anonymous" src="https://akamaividz2.zee5.com/image/upload/w_522,h_294,c_scale,f_webp,q_auto:eco/resources/0-1-6z5407627/list/000001923292163834464dcba493c303e3d85a8e.jpg" title="Trinayani - August 07, 2023 Episode 795" width="100%"/></a>

'''

class Bot(Client):
    def __init__(self):
        super().__init__(
            name="Bot",
            api_hash=API_HASH,
            api_id=APP_ID,
            plugins={
                "root": "plugins"
            },
            bot_token=TG_BOT_TOKEN
        )

    async def start(self):
        await super().start()
        usr_bot_me = await self.get_me()
        self.uptime = datetime.now()

       
        #web-response
        app = web.AppRunner(await web_server())
        await app.setup()
        bind_address = "0.0.0.0"
        await web.TCPSite(app, bind_address, PORT).start()

    async def stop(self, *args):
        await super().stop()

link1=[1]
listlink=[1]
@Bot.on_message(filters.private & filters.user(ADMINS) & filters.command('notify'))
async def notify(client: Client, message: Message):
    while True:
        #kannada serials link
        url = ('https://www.zee5.com/tv-shows/collections/before-tv-episodes-zee-kannada/0-8-670')

        response = ree.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find the HTML element that contains information about the latest episode
        episode_element = soup.find_all("a", class_="noSelect content", href=True)
        
        for l in episode_element:
            if l['href'] not in listlink:
                listlink.append(l['href'])
                
        #here we check the episode is new or not
        new_link = set(listlink).difference(set(link1))
        newlist=list(new_link)
        for i in newlist:
            link1.append(i)
            b=str(i)
            await client.send_message(message.chat.id, f"https://www.zee5.com{b}")
            # print(f"https://www.zee5.com{b}\n\n")
            await asyncio.sleep(3)
            
        #here we delete the old episode link(premium free)
        duplicatelinks = set(link1).difference(set(listlink))
        duplicatelist=list(duplicatelinks)
        for j in duplicatelist:
            link1.remove(j)
        notify(client,message)
        break

