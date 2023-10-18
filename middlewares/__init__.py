from aiogram import Dispatcher


from .ThrottlingMiddleWare import *

def setup(dp: Dispatcher):
    dp.middleware.setup(ThrottlingMiddleware())