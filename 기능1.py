import datetime
from email import message
import discord
from discord.ext import commands
from discord.utils import get
import pytz

bot = commands.Bot(command_prefix='`')

front_command = "`"

user_input = ""
user_output = ""
check_number = 0

@bot.event
async def on_ready():
    print('다음으로 로그인합니다: ')
    print(bot.user.name)
    print('connection was succesful')
    await bot.change_presence(status=discord.Status.online, activity=discord.Game("바닥 기어 다니기"))

@bot.event
async def on_message(message):

    if message.content.startswith(f"`채널메세지"):
        ch = bot.get_channel(int(message.content[7:25]))
        await ch.send(message.content[26:])

    if message.content.startswith("`청소"):
        number = int(message.content.split(" ")[1])
        await message.delete()
        await message.channel.purge(limit=number)
        await message.channel.send(f"{number}개의 메세지를 성공적으로 삭제했습니다!")

@bot.event

async def on_message(message):

    if message.content.startswith("`투표"):
        vote = message.content[4:].split("/")
        await message.channel.send("투표 - " + vote[0])
        for i in range(1, len(vote)):
            choose = await message.channel.send("```" + vote[i] + "```")
            await choose.add_reaction('👍')

    if message.content.startswith ("`인증 "):
        if message.author.guild_permissions.administrator:
            await message.delete()
            user = message.mentions[0]

            embed = discord.Embed(title="인증 시스템", description="인증이 정상적으로 완료 되었습니다 !",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0xff0000)
            embed.add_field(name="인증 대상자", value=f"{user.name} ( {user.mention} )", inline=False)
            embed.add_field(name="담당 관리자", value=f"{message.author} ( {message.author.mention} )", inline=False)
            embed.set_footer(text="Bot Made by. Regenwurm#3955")
            await message.author.send (embed=embed)
            role = discord.utils.get(message.guild.roles, name = '인증된 친구들')
            await user.add_roles(role)

        else:
            await message.delete()
            await message.channel.send(embed=discord.Embed(title="권한 부족", description = message.author.mention + "님은 권한이 없습니다", color = 0xff0000))

bot.run('OTUxNjU1OTA2NDE5MDI3OTc4.YiqooQ.wKB75Is_v8eW05WDPvqtt6pqPDY')