#    Copyright (C) 2020 KeinShin

#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.



"""Created By @keinshin and
If You Are Goin To kang Give Credits and My Copyright

Kang with credits....

Special Credits For Helping Out:
@Midhun_xD
@Shivam_Patel
@NOOBIzBack
"""





import os

import re

from math import ceil
from userbot.thunderconfig import Config

from telethon import Button, custom, events, functions


import requests
from userbot import ALIVE_NAME, CMD_HELP, CMD_LIST, DETAIL_CMD_HELP, bot

from var import Var
DETAIL_CMD = {}
FOR_EG = {}
LIGHT_LOGS = Config.PM_LOGGR_BOT_API_ID 
lightning_bot = Var.TG_BOT_USER_NAME_BF_HER
import asyncio

from datetime import datetime
from pathlib import Path


from userbot.utils import lightning_cmd, load_module, remove_plugin

DELETE_TIMEOUT = 5


thumb_image_path = "./resources/541200.png"

LIGHTNINGUSER = str(ALIVE_NAME) if ALIVE_NAME else "Lightning"
LIGHTNINGBOT = Var.TG_BOT_TOKEN_BF_HER



@borg.on(lightning_cmd(pattern="install"))
async def install(lightning):
    if lightning.fwd_from:
        return
    if lightning.reply_to_msg_id:
        try:
            downloaded_file_name = (
                await lightning.client.download_media(  # pylint:disable=E0602
                    await lightning.get_reply_message(),
                    "userbot/plugins/",  # pylint:disable=E0602
                )
            )
            if "(" not in downloaded_file_name:
                path1 = Path(downloaded_file_name)
                filename = path1.stem
                load_module(filename.replace(".py", ""))
                await lightning.edit(f"`Wait Installing....` ")
                await asyncio.sleep(2)
                await lightning.edit(
                    "`{} SucessFully Installed ....`".format(
                        os.path.basename(downloaded_file_name)
                    )
                )
            else:
                os.remove(downloaded_file_name)
                await lightning.edit("**Master You Already Have This Plugin \nPlz Try `.help <cmd name>` To See.**")
        except Exception as e:  # pylint:disable=C0103,W0703
            await lightning.edit(str(e))
            os.remove(downloaded_file_name)
    await asyncio.sleep(DELETE_TIMEOUT)
    await lightning.delete()




@borg.on(lightning_cmd(pattern=r"load (?P<filename>\w+)$"))
async def load(lightning):
    if lightning.fwd_from:
        return
    filename = lightning.pattern_match["filename"]
    try:
        try:
            remove_plugin(filename)
        except BaseException:
            pass
        load_module(filename)
        await lightning.edit(f"Successfully loaded {filename}")
    except Exception as e:
        await lightning.edit(
            f"Sorry,{filename} can not be loaded\nbecause of the following error.\n{str(e)}"
        )

 # created by @cyper666
"""xoxbot: Avaible commands: .xnxx picx les<link>
"""


from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError




@borg.on(lightning_cmd(pattern="xnxx?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    await event.get_reply_message()
    chat = "@SeXn1bot"
    await event.edit("```Checking...```")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=264121194)
            )
            await event.client.send_message(chat, "💋2016 Videolar🔞{}".format(input_str))
            response = await response
        except YouBlockedUserError:
            await event.reply("```Unblock @SeXn1bot```")
            return
        if response.text.startswith("I can't find that"):
            await event.edit("😐")
        else:
            await event.delete()
            await event.client.send_file(event.chat_id, response.message)


@borg.on(lightning_cmd(pattern="picx?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    await event.get_reply_message()
    chat = "@SeXn1bot"
    await event.edit("```Checking...```")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=264121194)
            )
            await event.client.send_message(chat, "♨️Old photo👙{}".format(input_str))
            response = await response
        except YouBlockedUserError:
            await event.reply("```Unblock @SeXn1bot```")
            return
        if response.text.startswith("I can't find that"):
            await event.edit("😐")
        else:
            await event.delete()
            await event.client.send_file(event.chat_id, response.message)


@borg.on(lightning_cmd(pattern="les?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    await event.get_reply_message()
    chat = "@SeXn1bot"
    await event.edit("```Checking...```")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=264121194)
            )
            await event.client.send_message(chat, "🔞Uz_sex♨️{}".format(input_str))
            response = await response
        except YouBlockedUserError:
            await event.reply("```Unblock @SeXn1bot```")
            return
        if response.text.startswith("I can't find that"):
            await event.edit("😐")
        else:
            await event.delete()
            await event.client.send_file(event.chat_id, response.message)


BOT_MSG = os.environ.get("BOT_MSG", None)
if BOT_MSG is None:
    BOT_LIT = f"Hello Sir MySelf Black Lightning Here For  {LIGHTNINGUSER}'s Protection "
else:
    BOT_LIT = BOT_MSG   


LIGHTNING_WARN = os.environ.get("LIGHTNING_WARN", None)
if LIGHTNING_WARN is None:
    WARNING = (
    f"**{BOT_LIT}"
    f"** Im Here To Protect {LIGHTNINGUSER} Dont Under Estimate Me 😂😂  **\n\n"
    f"**My Master {LIGHTNINGUSER} is Busy Right Now !** \n\n"
    f"{LIGHTNINGUSER} Is Very Busy Why Came Please Lemme Know Choose The Reason\n\n"
    f"**Btw Dont Spam Or Get Banned** 😂 \n\n"
    f"**Choose Any Reason Then Get Lost**\n"
)
else:
    WARNING = LIGHTNING_WARN

LIGHTNING_BOT_PIC = os.environ.get("LIGHTNING_BOT_PIC", None)
if LIGHTNING_BOT_PIC is None:
    LIGHTNING_WARNING = "https://telegra.ph/file/07d55d71944a852ac6d5e.jpg"
else:
    LIGHTNING_WARNING = LIGHTNING_BOT_PIC









@tgbot.on(events.InlineQuery)
async def inline_handler(lightning):
    builder = lightning.builder
    result = None
    query = lightning.text
    if lightning.query.user_id == bot.uid and query.startswith("**Black") or query.startswith("Black"):
        rev_text = query[::-1]
        buttons = lightnings_menu_for_help(0, CMD_LIST, "helpme")
        result = builder.article(
            f"Help Menu",
            text="\n{}\n`Plugins`: {}".format(query, len(CMD_LIST)),
            buttons=buttons,
            link_preview=False,
        )
        await lightning.answer([result])
    elif lightning.query.user_id == bot.uid and query == "**Cool":
        result = builder.article(
            title="Cool",
            text=f"**How If Face Problem \n{LIGHTNINGUSER}** \nChoose Your Problem For Help ",
            buttons=[
                [custom.Button.inline("Help", data="what?")],
                [Button.url("Commands Not Working🥺", "https://t.me/lightningsupport")],
                [Button.url("Help Article 🤓", "https://app.gitbook.com/@poxsisofficial/s/help/")],
                [
                    Button.url(
                
                    "Want To Learn CMDS😅",
                    "https://t.me/lightningsupport" ,
                    )
                ], 
            ],
        )
        await lightning.answer([result])
    elif lightning.query.user_id == bot.uid and query.startswith("**Hello Sir"):
        result = builder.photo(
            file=LIGHTNING_WARNING,
            text=WARNING,
            buttons=[
                [custom.Button.inline("Wanna Spam ?😉", data="lightning_is_here_cant_spam")],
                [
                    custom.Button.inline(
                        "My Friend❤️❤️",
                        data="he_sucks",
                    )
                ],
                [custom.Button.inline("Requesting🙏", data="fck_ask")],
                [
                    custom.Button.inline(
                        "Lemme In", 
                        data="lol_u_think_so",
                        
                    )
                        
                ],

            ],
            )
        await lightning.answer([result] if result else None)
    else:
        return
    


@tgbot.on(
    events.callbackquery.CallbackQuery(  # pylint:disable=E0602
        data=re.compile(b"helpme_next\((.+?)\)")
    )
)
async def lightning_pugins_query_hndlr(lightning):
    if lightning.query.user_id == bot.uid:  # pylint:disable=E0602
        lightning_page = int(lightning.data_match.group(1).decode("UTF-8"))
        buttons = lightnings_menu_for_help(
            lightning_page + 1, CMD_LIST, "helpme"  # pylint:disable=E0602
        )
        # https://t.me/TelethonChat/115200
        await lightning.edit(buttons=buttons)
    else:
        lightning_is_best = "Oh C'mon You Think You Can Touch This? ಠ╭╮ಠ!"
        await lightning.answer(lightning_is_best, cache_time=0, alert=True)




            # Thanks To Friday For This Deatiled Idea of detail button
@tgbot.on(
        events.callbackquery.CallbackQuery(  # pylint:disable=E0602
            data=re.compile(b"detailed_(.*)")
   )
)
async def detailed(lightning):
    if not lightning.query.user_id == bot.uid:
        how = "Not For  Bitch.🖕( ͡❛ ͜ʖ ͡❛)"
        await lightning.answer(how, cache_time=0, alert=True)
        return
    light_pulu_name = lightning.data_match.group(1).decode("UTF-8")
    try:
            if light_pulu_name in CMD_HELP:
                    lightning_help_strin = "Commands found in {}:\n".format(light_pulu_name)
                    
                    lightning_help_strin += f"**🔺 NAME 🔺 :** `{light_pulu_name}` \n\n `{CMD_HELP[light_pulu_name]}"
                    lightning_help_strin += "\n    " + i
                    lightning_help_strin += "\n\n`Tottal Command Found Inside  {}`".format(len(light_pulu_name))
                    lightning_help_strin += "\n"
                    await lightning.edit(
                message=lightning_help_strin,
                
                buttons=[
                        [custom.Button.inline("ѕανє", data="krish".format(light_pulu_name)
                )],
                        [custom.Button.inline("нσмє 💢", data="lghtback22")],
              ],
        )
            else:
               lightning_help_strin  = f"**🔺 NAME 🔺 :** `{light_pulu_name}` \n\n`{CMD_HELP[light_pulu_name]}`"
               lightning_is_best = lightning_help_strin 
               lightning_is_best += "\n\n`Tottal Command Found Inside  {}`".format(len(light_pulu_name))
               lightning_is_best += "\n\n**In Case Any Problem @lightningsupport** ".format(light_pulu_name)
               await lightning.edit(
                message=lightning_help_strin,
                
                buttons=[
                        [custom.Button.inline("ѕανє", data="krish".format(light_pulu_name)
                )],
                        [custom.Button.inline("нσмє 💢", data="lghtback22")],
              ],
        )
    except KeyError:
            light_pulu_name = lightning.data_match.group(1).decode("UTF-8")

            if light_pulu_name in CMD_HELP:
                lightning_help_strin = "Commands found in {}:\n".format(light_pulu_name)
                for light_pulu_name in CMD_HELP:
                    lightning_help_strin  = f"**🔺 NAME 🔺 :** `{light_pulu_name}` \n\n `{CMD_HELP[light_pulu_name]}"
                    lightning_help_strin += "\n    " + light_pulu_name
                    lightning_help_strin += "\n\n`Tottal Command Found Inside  {}`".format(len(light_pulu_name))
                    lightning_help_strin += "\n"
                    await lightning.edit(
                message=lightning_help_strin,
                
                buttons=[
                        [custom.Button.inline("ѕανє", data="krish".format(light_pulu_name)
                )],
                        [custom.Button.inline("нσмє 💢", data="lghtback22")],
                ],
                    )
        
            else:
               lightning_help_strin  = f"**🔺 NAME 🔺 :** `{light_pulu_name}` \n\n`{CMD_HELP[light_pulu_name]}`"
               lightning_is_best = lightning_help_strin 
               lightning_is_best += "\n\n`Tottal Command Found Inside  {}`".format(len(light_pulu_name))
               lightning_is_best += "\n\n**In Case Any Problem @lightningsupport** ".format(light_pulu_name)
               await lightning.edit(
                message=lightning_help_strin,
                
                buttons=[
                        [custom.Button.inline("ѕανє", data="krish".format(light_pulu_name)
                )],
                        [custom.Button.inline("нσмє 💢", data="lghtback22")],
              ],
        )
    
 
                
@tgbot.on(
        events.callbackquery.CallbackQuery(  # pylint:disable=E0602
            data=re.compile(b"_lightning_plugins_(.*)")
   )
) # Thanks To Friday Userbot
async def lightning_pugins_query_hndlr(lightning):
    if not lightning.query.user_id == bot.uid:
        how = "Not For  Bitch.🖕( ͡❛ ͜ʖ ͡❛)"
        await lightning.answer(how, cache_time=0, alert=True)
        return
    light_pulu_name = lightning.data_match.group(1).decode("UTF-8")
    
    try:
        if light_pulu_name in CMD_HELP:
           
           lightning_help_strin  = f"**🔺 NAME 🔺 :** `{light_pulu_name}` \n\n{CMD_HELP[light_pulu_name]}"
           lightning_is_best = lightning_help_strin 
           lightning_is_best += "\n\n**In Case Any Problem @lightningsupport** ".format(light_pulu_name)
        
        else:
            lightning_help_strin = "Commands found in {}:\n".format(light_pulu_name)
            for i in CMD_HELP:
                lightning_help_strin += "ℹ️ " + i + "\n"
                for iter_list in CMD_HELP[i]:
                    lightning_help_strin += "    `" + str(iter_list) + "`"
                    lightning_help_strin += "\n"
                    lightning_help_strin += "\n\n`Tottal Command Found Inside  {}`".format(len(light_pulu_name))
                    lightning_help_strin += "\n"
    except KeyError:
     if light_pulu_name in CMD_LIST:
                lightning_help_strin = "Commands found in {}:\n".format(light_pulu_name)
                for i in CMD_LIST[light_pulu_name]:
                    lightning_help_strin  = f"**🔺 NAME 🔺 :** `{light_pulu_name}` \n\n `{CMD_LIST[light_pulu_name]}\n`Click On That Detail Button for more`"
                    lightning_help_strin += "\n    " + i
                    lightning_help_strin += "\n\n`Tottal Command Found Inside  {}`".format(len(light_pulu_name))
                    lightning_help_strin += "\n"
    else:
           lightning_help_strin  = f"**🔺 NAME 🔺 :** `{light_pulu_name}` \n\n`{CMD_LIST[light_pulu_name]}`\n`Click On That Detail Button for more`"
           lightning_is_best = lightning_help_strin 
           lightning_is_best += "\n\n`Tottal Command Found Inside  {}`".format(len(light_pulu_name))
           lightning_is_best += "\n\n**In Case Any Problem @lightningsupport** ".format(light_pulu_name)
    pass
   
    if light_pulu_name in CMD_LIST:
                lightning_help_strin = "Commands found in {}:\n".format(light_pulu_name)
                for i in CMD_LIST[light_pulu_name]:
                    lightning_help_strin  = f"""**🔺 NAME 🔺 :** `{light_pulu_name}` \n\n `{CMD_LIST[light_pulu_name]}\n`Click On That Detail Button for more`"""
                    lightning_help_strin += "\n\n`Tottal Command Found Inside  {}`".format(len(light_pulu_name))
                    lightning_help_strin += "\n    " + i
                    lightning_help_strin += "\n"
                
    else:
           lightning_help_strin  = f"""**🔺 NAME 🔺 :** `{light_pulu_name}` \n\n`{CMD_LIST[light_pulu_name]}`\n`Click On That Detail Button for more`"""
           lightning_is_best = lightning_help_strin 
           lightning_is_best += "\n\n`Tottal Command Found Inside  {}`".format(len(light_pulu_name))
           lightning_is_best += "\n\n**In Case Any Problem @lightningsupport** ".format(light_pulu_name)

    lightning_help_strin = f"""**🔺 NAME 🔺 :** `{light_pulu_name}` \n\n`{CMD_LIST[light_pulu_name]}`\n`Click On That Detail Button for more`"""
    lightning_is_best = lightning_help_strin 
    lightning_is_best += "\n\n`Tottal Command Found Inside  {}`".format(len(light_pulu_name))
    lightning_is_best += "\n\n**In Case Any Problem @lightningsupport** ".format(light_pulu_name)    
    if len(lightning_is_best) >= 4096:
          keinshin = "`Wait.( ͡🔥 ͜ʖ ͡🔥)`"
          await lightning.answer(keinshin, cache_time=0, alert=True)
          out_file = lightning_is_best
          lig_url = "https://del.dog/documents"
          r = requests.post(lig_url, data=out_file.encode("UTF-8")).json()
          lig_url = f"https://del.dog/{r['key']}"
          await lightning.edit(
               f"Pasted {light_pulu_name} to {lig_url}",
               link_preview=False,
               buttons=[
                [custom.Button.inline("ᗪETᗩIᒪEᗪ", data="detailed_{}".format(light_pulu_name)
                )],
                [custom.Button.inline("Ⴆαƈƙ 💢", data="lghtback")],
            ],
         )
    else:
           await lightning.edit(
            message=lightning_is_best,
            buttons=[
                [custom.Button.inline("ᗪETᗩIᒪEᗪ", data="detailed_{}".format(light_pulu_name)
                )],
                [custom.Button.inline("Ⴆαƈƙ 💢", data="lghtback")],
            ],
         )

@tgbot.on(
    events.callbackquery.CallbackQuery(  # pylint:disable=E0602
        data=re.compile(rb"helpme_prev\((.+?)\)")
    )
)
async def lightning_pugins_query_hndlr(lightning):
    if lightning.query.user_id == bot.uid:  # pylint:disable=E0602
        lightning_page = int(lightning.data_match.group(1).decode("UTF-8"))
        buttons = lightnings_menu_for_help(
            lightning_page - 1, CMD_LIST, "helpme"  # pylint:disable=E0602
        )
        # https://t.me/TelethonChat/115200
        await lightning.edit(buttons=buttons)
    else:
        lightning_is_best = "Oh C'mon You Think You Can Touch This? ಠ╭╮ಠ!"
        await lightning.answer(lightning_is_best, cache_time=0, alert=True)

@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"what?")))
async def what(lightning):
    if lightning.query.user_id == bot.uid:
        fck_bit = f"{LIGHTNINGUSER}  Use The Buttons Bellow "
        await lightning.answer(fck_bit, alert=True)
    else:
        txt = f"Ohh C'mon You Think That This Is For You?\n Ok I Will Complain To {LIGHTNINGUSER}👀👀"
        await lightning.answer(txt, alert=True)


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"lightning_is_here_cant_spam")))
async def lightning_is_better(lightning):
    if lightning.query.user_id == bot.uid:
        fck_bit = f"Oh! C'mon Master {LIGHTNINGUSER} Im Try To Get Rid Of This Nigga Pls Dont Touch"
        await lightning.answer(fck_bit, cache_time=0, alert=True)
        return
    await lightning.get_chat()
    lightning_id = lightning.query.user_id
    text1 = f"LOL **You Think So You Can**😂😂\n\n**[Nibba](tg://user?id={lightning_id}) Bye Goin To Block You Gay**😂😂"
    await lightning.edit("Off Course Go To Hell Dude")
    await bot.send_message(lightning.query.user_id, text1)
    await bot(functions.contacts.BlockRequest(lightning.query.user_id))
    await lightning.edit("🖕")
    await bot.send_message(
        LIGHT_LOGS,
        f"Hey Master Sorry Disturb You, [Noob](tg://user?id={lightning_id}) Tryin To Spam 😂\n\n**So Blocked**.",
    )

@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"lol_u_think_so")))
async def lightning_is_better(lightning):
    if lightning.query.user_id == bot.uid:
        fck_bit = f"Oh! C'mon Master {LIGHTNINGUSER} Im Try To Get Rid Of This Nigga Pls Dont Touch"
        await lightning.answer(fck_bit, cache_time=0, alert=True)
        return
    await lightning.get_chat()
    lightning_id = lightning.query.user_id
    text1 = f"LOL You Think So You Can😂😂\nGo and wait😂😂"
    await lightning.edit("Off Course Go To Hell Dude🖕")
    await bot.send_message(lightning.query.user_id, text1)
    await bot(functions.contacts.BlockRequest(lightning.query.user_id))
    await bot.send_message(
        LIGHT_LOGS,
        f"Hey Master Sorry Disturb You, [Noob](tg://user?id={lightning_id}) Tryin To Enter With Out approval😂 \n.",
    )





@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"he_sucks")))
async def lightning_is_better(lightning):
    if lightning.query.user_id == bot.uid:
        fck_bit = f"Oh! C'mon Master {LIGHTNINGUSER} Im Try To Get Rid Of This Nigga Pls Dont Touch"
        await lightning.answer(fck_bit, cache_time=0, alert=True)
        return
    await lightning.get_chat()
    lightning_id = lightning.query.user_id
    await lightning.edit("Oh You Wanna Talk With My Master\n\nPls Wait Dear \n\n**Btw** **You Can Wait For My Master**")
    await asyncio.sleep(2)
    await lightning.edit(
        "Name Which Type Of Friend?", buttons= [
        [Button.inline("School", data="school")],
        [Button.inline("Tg Causal Friend", data="tg_okay")],
        ], 
    )
    light_text = "`Warning`- ❗️⚠️Dont Try Anything Stupid  Wait Kindly!!!❗️⚠️"
    await bot.send_message(lightning.query.user_id, light_text)
    
    
    
    
    
    
    
@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"tg_okay")))
async def yeahbaba(lightning):
        if lightning.query.user_id == bot.uid:
            fck_bit = f"Oh! C'mon Master {LIGHTNINGUSER} "
            await lightning.answer(fck_bit, cache_time=0, alert=True)
            return
        light_text = "**So You  Are TG Friend** Okay wait"
        lightning_id = lightning.query.user_id
        await asyncio.sleep(2)
        await lightning.edit(f"`Informing To Master {LIGHTNINGUSER}`")
        await asyncio.sleep(2)
        await lightning.edit("`Done Informed`")
        await bot.send_message(lightning.query.user_id, light_text)
        await bot.send_message(
        LIGHT_LOGS,
        message=f"Hello, Master  [Friend](tg://user?id={lightning_id}). Your Casual Telegram Friend His Here To Chat pls See The Message [Tg Friend](tg://user?id={lightning_id}) Is Waiting.",
    
    )
@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"School")))
async def yeahbaba(lightning):
        if lightning.query.user_id == bot.uid:
            fck_bit = f"Oh! C'mon Master {LIGHTNINGUSER} "
            await lightning.answer(fck_bit, cache_time=0, alert=True)
            return
        light_text = "**So You  Are  Friend** Okay wait"
        lightning_id = lightning.query.user_id
        await asyncio.sleep(2)
        await lightning.edit(f"`Informing To Master {LIGHTNINGUSER}`")
        await asyncio.sleep(2)
        await lightning.edit("`Done Informed`")
        await bot.send_message(lightning.query.user_id, light_text)
        await bot.send_message(
        LIGHT_LOGS,
        message=f"Hello, Master  [Friend](tg://user?id={lightning_id}). Your Casual Telegram Friend His Here To Chat pls See The Message [Tg Friend](tg://user?id={lightning_id}) Is Waiting.",
        )


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"fck_ask")))
async def lightning_is_better(lightning):
    if lightning.query.user_id == bot.uid:
        fck_bit = f"Oh! C'mon Master {LIGHTNINGUSER} Im Try To Get Rid Of This Nigga Pls Dont Touch"
        await lightning.answer(fck_bit, cache_time=0, alert=True)
        return
    await lightning.get_chat()
    lightning_id = lightning.query.user_id
    await lightning.edit("Okay let Me Think🤫")
    await asyncio.sleep(2)
    await lightning.edit("Okay Giving You A Chance🤨")
    await asyncio.sleep(2)
    await lightning.edit(
        "You Will Spam?", buttons= [
        [Button.inline("Yes", data="lemme_ban")],
        [Button.inline("No", data="hmm")],
        ],
    )

    
    reqws = "`Warning`- ❗️⚠️Dont Try Anything Stupid  Wait Kindly!!!❗️⚠️"


    await bot.send_message(lightning.query.user_id, reqws)
    await bot.send_message(
        LIGHT_LOGS,
        message=f"Hello, Master  [Nibba](tg://user?id={lightning_id}). Wants To Request Something.",
        buttons=[Button.url("Contact Him", f"tg://user?id={lightning_id}")],
    )

@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"hmm")))
async def yes_ucan(lightning):
    if lightning.query.user_id == bot.uid:
           lmaoo = "You Are Not Requesting , Lol."
           await lightning.answer(lmaoo, cache_time=0, alert=True)
           return          
    await lightning.get_chat()
    await asyncio.sleep(2)
    await lightning.edit("Okay You Can Wait Till Wait")
    hmmmmm = "Okay Kindly wait  i will inform you"
    await bot.send_message(
              lightning.query.user_id, hmmmmm)
          
@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"lemme_ban")))
async def yes_ucan(lightning):
    if lightning.query.user_id == bot.uid:
           lmaoo = "You Are Not Requesting , Lol."
           await lightning.answer(lmaoo, cache_time=0, alert=True)
           return    
    await lightning.get_chat()
    await asyncio.sleep(2)
    await lightning.edit("Get Lost Retard")
    ban = "Get Lost Goin To Block You" 
    await bot.send_message(
         lightning.query.user_id, ban)
    await bot(functions.contacts.BlockRequest(lightning.query.user_id))

@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"stta")))
async def hmm(lightning):
    if lightning.query.user_id == bot.uid:
        text = "🇲‌🇾‌ 🇭‌🇪‌🇱‌🇵‌ 🇸‌🇹‌🇦‌🇹‌🇸‌\n\nᴘʟᴜɢɪɴ-- All Good ✔\nʜᴇʀᴏᴋᴜ - Connected ✔\nʟᴏɢs -- Looks Good :/\nTottal Plugs: {}".format(len(CMD_LIST))
        await lightning.answer(text, alert=True)
    else:
        txt = f"Stats For {LIGHTNINGUSER} Not For You :)"
        await lightning.answer(txt, alert=True)



@tgbot.on(
        events.callbackquery.CallbackQuery(  # pylint:disable=E0602
            data=re.compile(b"krish(.*)")
        )
    )
async def chill(lightning):
    light_pulu_name = lightning.data_match.group(1).decode("UTF-8")
    try:
             if light_pulu_name in CMD_HELP:
                   lightning_help_strin = "Commands found in {}:\n".format(light_pulu_name)
                   for light_pulu_name in CMD_HELP[light_pulu_name]:
                        lightning_help_strin  = f"**🔺 NAME 🔺 :** `{light_pulu_name}` \n\n {CMD_HELP[light_pulu_name]}\n**Any Help?**\n\n**Ask ngsupport"
                        lightning_help_strin += "\n    " + light_pulu_name
                        lightning_help_strin += "\n"   
                        await lightning.edit("`Saving Command`")
                        await asyncio.sleep(2)
                        await lightning.edit("`Check You Saved Message....`")
                        lightning_help_strin = bot.session.save()
                        await bot.send_message("me", lightning_help_strin)
                   
		          
          
                        await lightning.edit(
                    f"`Check Your Save`",
                    link_preview=False,
                    buttons=[
                
                [custom.Button.inline("Ⴆαƈƙ 💢", data="lghtback")],
                
                ],
         )
             else:
                   for light_pulu_name in CMD_HELP[light_pulu_name]:
                       lightning_help_strin  = f"**🔺 NAME 🔺 :** `{light_pulu_name}` \n\n `{CMD_HELP[light_pulu_name]}\n`**Any Help?**\n\n**Ask ngsupport"
                       lightning_help_strin += "\n    " + light_pulu_name
                       lightning_help_strin += "\n"
                       await lightning.edit(
                   message=lightning_help_strin,
                   buttons=[
                
                [custom.Button.inline("нσмє 💢", data="lghtback22")],
                
                ],
         )
    except KeyError:
              if light_pulu_name in CMD_HELP:
                   lightning_help_strin = "Commands found in {}:\n".format(light_pulu_name)
                   for light_pulu_name in CMD_HELP[light_pulu_name]:
                        lightning_help_strin  = f"**🔺 NAME 🔺 :** `{light_pulu_name}` \n\n {CMD_HELP[light_pulu_name]}\n**Any Help?**\n\n**Ask ngsupport"
                        lightning_help_strin += "\n    " + light_pulu_name
                        lightning_help_strin += "\n"   
                   if len(lightning_help_strin) >= 2:
                        await lightning.edit("`Saving Command`")
                        await asyncio.sleep(2)
                        await lightning.edit("`Check You Saved Message....`")
                        lightning_help_strin = bot.session.save()
                        await bot.send_message("me", lightning_help_strin)
                   
		          
          
                        await lightning.edit(
                    f"`Check Your Save`",
                    link_preview=False,
                    buttons=[
                
                [custom.Button.inline("нσмє 💢", data="lghtback22")],
                
                ],
         )
                   else:
                      for light_pulu_name in CMD_HELP[light_pulu_name]:
                       lightning_help_strin  = f"**🔺 NAME 🔺 :** `{light_pulu_name}` \n\n `{CMD_HELP[light_pulu_name]}\n`**Any Help?**\n\n**Ask ngsupport"
                       lightning_help_strin += "\n    " + light_pulu_name
                       lightning_help_strin += "\n"
                       await lightning.edit(
                   message=lightning_help_strin,
                   buttons=[
                
                [custom.Button.inline("нσмє 💢", data="lghtback22")],
                
                ],
         )


# Thanks To Friday Userbot and @Midhun_xD For This idea





@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"lghtback")))
async def ho(event):
    if event.query.user_id != bot.uid:
        how = "Not For You Idiot 🖕( ͡❛ ͜ʖ ͡❛)."
        await event.answer(how, cache_time=0, alert=True)
        return
    await event.answer("( ͡🔥 ͜ʖ ͡🔥)", cache_time=0, alert=False)
    # This Is Copy of Above Code. (C) @SpEcHiDe
    buttons = lightnings_menu_for_help(0, CMD_LIST, "helpme")
    ho = f"""**Black Lightning Is Here With Stunning Help !\n
In Case Any Problem @lightningsupport** \n`Tottal Plugs( ͡🔥 ͜ʖ ͡🔥): {len(CMD_LIST)}`"""
    await event.edit(message=ho, buttons=buttons)


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"lghtback22")))
async def ho(event):
    if event.query.user_id != bot.uid:
        how = "Not For You Idiot 🖕( ͡❛ ͜ʖ ͡❛)."
        await event.answer(how, cache_time=0, alert=True)
        return
    await event.answer("Returned To Home", cache_time=0, alert=False)
    # This Is Copy of Above Code. (C) @SpEcHiDe
    buttons = lightnings_menu_for_help(0, CMD_LIST, "helpme")
    ho = f"""**Black Lightning Is Here With Stunning Help !\n
In Case Any Problem @lightningsupport** \n`Tottal Plugs( ͡🔥 ͜ʖ ͡🔥): {len(CMD_LIST)}`"""
    await event.edit(message=ho, buttons=buttons)





        


    
def lightnings_menu_for_help(b_lac_krish, lightning_plugs, lightning_lol):
    lightning_no_rows = 10
    lightning_no_coulmns = 3
    lightning_plugins = []
    for p in lightning_plugs:
        if not p.startswith("_"):
            lightning_plugins.append(p)
    lightning_plugins = sorted(lightning_plugins)
    plugins = [
        custom.Button.inline(
            "{} {} {}".format("⨵", x, "⨵"), data="_lightning_plugins_{}".format(x)
        )
        for x in lightning_plugins
    ]
    pairs = list(zip(plugins[::lightning_no_coulmns], plugins[1::lightning_no_coulmns]))
    if len(plugins) % lightning_no_coulmns == 1:
        pairs.append((plugins[-1],))
    max_fix = ceil(len(pairs) / lightning_no_rows)
    lightning_plugins_pages = b_lac_krish % max_fix
    if len(pairs) > lightning_no_rows:
        pairs = pairs[
            lightning_plugins_pages * lightning_no_rows : lightning_no_rows * (lightning_plugins_pages + 1)
        ] + [
            (
                custom.Button.inline(
                    "🗡яιgнт ρℓυgιи", data="{}_prev({})".format(lightning_lol, lightning_plugins_pages)
                ),
               # Thanks To Friday For This Idea
               custom.Button.inline("〽️Stats〽️", data="stta"
               ),
               custom.Button.inline(
                    "ℓєfт ρℓυgιи ", data="{}_next({})".format(lightning_lol, lightning_plugins_pages)
                ),
                
            )
        ]
    return pairs
