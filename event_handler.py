import asyncio
from story_talker import send_messages

# 定义事件处理函数
# clients 需要 main.py 传入
async def message_handler(event, clients):
    print(event)
    if 'ding' == event.raw_text:
        await event.reply('野猪开始拉屎！')
        await asyncio.sleep(3)
        await event.reply('野猪拉屎完毕！')
    
    elif '讲故事' == event.raw_text:
        await event.reply('野猪开始讲故事！')
        await send_messages(clients)