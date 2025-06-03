from dotenv import load_dotenv

load_dotenv()

api_id = os.getenv('API_ID')
api_hash = os.getenv('API_HASH')

from telethon import TelegramClient, events
import asyncio
import json
from functools import partial
from story_talker import send_messages
from event_handler import message_handler


# load accounts
with open('accounts.json', 'r') as f:
    accounts = json.load(f)

# create clients
clients = {}

async def setup_clients():
    for account in accounts:
        client = TelegramClient(account['name'], api_id, api_hash)
        await client.start(account['phone'])
        clients[account['name']] = client
    message_handler_with_clients = partial(message_handler, clients=clients) # 将clients作为参数传递给message_handler
    for client in clients.values():
        client.add_event_handler(message_handler_with_clients, events.NewMessage)


async def main():
    # 首先设置所有客户端
    await setup_clients()
    
    # 创建所有任务
    tasks = []
    # 添加消息发送任务
    # tasks.append(send_messages(clients))
    # 添加所有客户端的连接保持任务
    for client in clients.values():
        tasks.append(client.run_until_disconnected())
    
    # 同时运行所有任务
    try:
        await asyncio.gather(*tasks)
    except Exception as e:
        print(f"发生错误: {e}")
    finally:
        # 确保所有客户端正确断开连接
        for client in clients.values():
            await client.disconnect()

# 启动事件循环
if __name__ == '__main__':
    asyncio.run(main())
