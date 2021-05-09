from dogey import Dogey
from dogey.classes import Context

dogey = Dogey(token='your token',
              refresh_token='your refresh token', prefix='.')

bot = dogey.bot


@dogey.event
async def on_ready():
    print(f'{bot.name} is up! (prefix is {bot.prefix})')
    await dogey.create_room('dogey.py', description='A simple command example bot', is_private=False)


@dogey.command
async def command_count(ctx: Context):
    # Shows the number of bot commands
    await dogey.send(f'Available commands: {len(dogey.get_commands())}')


@dogey.command
async def getmyinfo(ctx: Context):
    # Fetches a user's info
    await dogey.get_user_info(ctx.author.id)


@dogey.command
async def doiexist(ctx: Context):
    # Checks if a user exists in dogey's cache
    await dogey.send(str(ctx.author.id in dogey.room_members))


@dogey.event
async def on_user_info_get(info: dict):
    print(info)

dogey.start()
