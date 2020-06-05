import time
from telethon import TelegramClient, events, sync, types, functions
api_id = [number here]
api_hash = '[hash here]'

phone = '[with country code]'
session_file = '[@id]' #'/path/to/session/file'  # use your username if unsure
#password = 'YOUR_PASSWORD'  # if you have two-step verification enabled

safeusers="Yew Yan Wong"
# content of the automatic reply
message = "```You have messaged Yeuyo without prior agreement, this chat has been archived and will be deleted unless a reason is given.```"

if __name__ == '__main__':
    # Create the client and connect
    # use sequential_updates=True to respond to messages one at a time
    client = TelegramClient(session_file, api_id, api_hash, sequential_updates=True)


    @client.on(events.NewMessage(incoming=True))
    #@client.on(events.NewMessage(incoming=True))
    async def handle_new_message(event):
        if event.is_private:  # only auto-reply to private chats
            #await event.respond(message)
            dialogs = await client.get_dialogs()
            first = dialogs[5] #replace 5 with your number of pinned messages

            if first.title not in safeusers:
                await event.respond(message)
                await client.edit_folder(dialogs[5], 1) #add chat to archive, 0 to unarchive
                #await client.delete_dialog(dialogs[5]) #delete chat number 6



    print(time.asctime(), '-', 'Auto-replying...')
    client.start(phone)#, password)
    client.run_until_disconnected()
    print(time.asctime(), '-', 'Stopped!')