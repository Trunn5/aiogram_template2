from aiogram import executor 

from loader import dp

import filters, handlers

# уведомление админов о старте
from utils.notify_admins import on_startup_notify

# устанавливает стандратные команды в боковкую менюшку бота
from utils.set_bot_commands import set_default_commands 


async def on_startup(dispatcher): 
    
    await set_default_commands(dispatcher)

    await on_startup_notify(dispatcher)

if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)