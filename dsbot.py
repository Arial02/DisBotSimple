import discord

SETTINGS = {"token":"сюда токен",
            "bot":"сюда имя бота", "id":1234567890, "prefix":"?"} # вообще тут используется только токен и префикс, но можно и остальное вписать, а можно забить хуй, шикарный вариант


class BotHandler(discord.Client):
    async def on_message(self, message):
        if message.content == f"{SETTINGS['prefix']}ping": # - ?ping - pong
            await message.reply("pong", delete_after=5)
        elif message.author.guild_permissions.administrator: # ONLY ADMINS' COMMANDS
            if message.content.startswith(f"{SETTINGS['prefix']}prefix"): # - ?prefix ! - Ready!     это изменяет префикс команд бота
                SETTINGS["prefix"]=message.content[len(SETTINGS['prefix'])+7:]
                await message.reply("Ready!", delete_after=5)
            elif message.content.startswith(f"{SETTINGS['prefix']}calc_role"): # - ?calc_role admin - 12    считает членов сервера с этой ролью
                await message.reply(len(list(filter(lambda user:message.content[len(SETTINGS['prefix'])+10:] in list(map(lambda role: role.name, user.roles)),message.guild.members))), delete_after=60)
            elif message.content == f"{SETTINGS['prefix']}members": # - ?members - Petya, Sasha, Vasya, ...    делает список членов сервера
                await message.reply(", ".join(sorted(list(map(lambda user: user.name, message.guild.members)))), delete_after=60)
            elif message.content.startswith(f"{SETTINGS['prefix']}role"): # - ?role admin - Petya, Vasya, ...    делает список членов сервера с этой ролью
                await message.reply(", ".join(sorted(list(map(lambda user: user.name, list(filter(lambda user:message.content[len(SETTINGS['prefix'])+5:] in
                                                                                                              list(map(lambda role: role.name, user.roles)),message.guild.members)))))), delete_after=60)
        elif message.content.startswith(f"{SETTINGS['prefix']}"): # посылает нахуй, если в чате использован префикс с несуществующей командой (или с той, к которой у юзера нет доступа)
            await message.reply("Sorry, but you're not an admin or command doesn't exist.", delete_after=5)

intents = discord.Intents.default()
intents.members = True # даём разрешение читать списки членов сервера, там надо будет в настройке приложения во вкладке бот свайпнуть два триггера: presence intent & server members intent

client = BotHandler(intents=intents)

client.run(SETTINGS['token'])
