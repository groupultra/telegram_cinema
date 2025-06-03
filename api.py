from telethon import types

async def send_text_to_chat(client, chat_id, message):
    peer = types.PeerChat(chat_id=chat_id)
    await client.send_message(peer, message)
