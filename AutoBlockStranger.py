import time
from telethon import TelegramClient, events, sync, types, functions
api_id = [number here]
api_hash = '[hash here]'

phone = '[with country code]'
session_file = '[@id]' #'/path/to/session/file'  # use your username if unsure
#password = 'YOUR_PASSWORD'  # if you have two-step verification enabled

#safeusers="Yew Yan Wong" #if you want to add another list of users beside mutual contacts to allow list
number_of_pinned_chat=5
# content of the automatic reply
message = "```You have messaged Yeuyo without prior agreement, this chat has been archived and will be deleted unless a reason is given.```"

if __name__ == '__main__':
    # Create the client and connect
    # use sequential_updates=True to respond to messages one at a time
    client = TelegramClient(session_file, api_id, api_hash, sequential_updates=True)


    @client.on(events.NewMessage(incoming=True))
    async def handle_new_message(event):
        if event.is_private: # only auto-reply to private chats
            print(event.chat_id) # to enable the next step to be carried out smoothly
            from_ = await event.client.get_entity(event.from_id)  # this lookup will be cached by telethon
            if not from_.bot and not from_.mutual_contact: # don't auto-reply to bots and mutual contacts
                dialogs = await client.get_dialogs()
                first = dialogs[number_of_pinned_chat]
                #print(first.title)
            #if first.title not in safeusers: #if you want to add another list of users beside mutual contacts to allow list
                await event.respond(message)
                #await client.send_file(first.id, 'C:/image.jpg') #uncomment to reply with a photo
                await client.edit_folder(dialogs[number_of_pinned_chat], 1) #add chat to archive, 0 to unarchive
                #await client.delete_dialog(dialogs[number_of_pinned_chat]) #delete chat

                #print(time.asctime(), '-', event.message)  # optionally log time and message
                #time.sleep(1)  # pause for 1 second to rate-limit automatic replies
                #await event.respond(message)



    print(time.asctime(), '-', 'Auto-replying...')
    client.start(phone)#, password)
    client.run_until_disconnected()
    print(time.asctime(), '-', 'Stopped!')
