import json
import asyncio

from api import send_text_to_chat

chat_id_cinema = 4739919472
chat_id_groupultra = 4745387056

async def send_messages(clients):
    await send_text_to_chat(clients['shitdelicious'], chat_id_cinema, '这里是调试群，野猪准备拉屎！')
    await asyncio.sleep(5)

    # 脚本中的talker_id 和 accounts.json中的name的对应关系
    clients_map = {
        1: clients['shitdelicious'],
        2: clients['GUTest005'],
        3: clients['GUTest006']
    }

    # 第一版，先不管time，只是按顺序发言
    # 读取scripts
    with open('scripts/tech_tools.json', 'r', encoding='utf-8') as f:
        scripts = json.load(f)
    # 按顺序发言
    for script in scripts['scripts']:
        await send_text_to_chat(clients_map[script['talker_id']], chat_id_cinema, script['content'])
        await asyncio.sleep(5)
        
        