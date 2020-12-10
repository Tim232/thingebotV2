import discord
from discord.ext import commands
from PingPongTool import PingPong
from random import randint
import os
import time
import requests
import json

korea = "http://api.corona-19.kr/korea?serviceKey="
key = (os.environ['covidtoken']) #API 키(https://api.corona-19.kr/ 에서 무료 발급 가능)

volaapi = "https://vo.la/api/?key="
volakey = (os.environ['volatoken'])

response = requests.get(korea + key)
text = response.text
data = json.loads(text)

def RandomColor():
    return randint(0, 0xFFFFFF)

Authorization = (os.environ['pingpongtoken'])
URL = "https://builder.pingpong.us/api/builder/5f8bdb67e4b07b8420a30e71/integration/v0.2/custom/{sessionId}"

INTENTS = discord.Intents.all()
bot = commands.Bot(command_prefix=['?', '띵아 '], intents=INTENTS)
Ping = PingPong(URL, Authorization)

@bot.event
async def on_ready():
    print("준비 완료!")
    game = discord.Game("'띵아 도움말' 명령어로 띵이봇과 노는법을 알아보세요! | TEB 2.19")
    await bot.change_presence(status=discord.Status.online, activity=game)

@bot.listen()
async def on_command_error(ctx, error):
    if type(error) is commands.errors.CommandNotFound:
        data = await Ping.Pong(ctx.author.id, ctx.message.content, NoTopic=False)
        embed = discord.Embed(
            title="띵이봇과 대화하기!",
            description=data['text'],
            color=RandomColor()
        )
        embed.set_footer(text="띵이봇 인공지능")
        if data['image'] is not None:
            embed.set_image(url=data['image'])
        await ctx.send(embed=embed)
    else:
        embed = discord.Embed(title="오류!!!", description="오류가 발생했어요...\n[오류 해결하러 ㄱㄱ!](https://error.teb.kro.kr/)", color=0xFF0000)
        embed.add_field(name="오류 내용", value=f"```{error}```")
        await ctx.send(embed=embed)


@bot.command(name="따라해")
async def Echo(ctx, *, text: str):
    await ctx.send(text)

@bot.command(name="hellothisisverification")
async def ping(ctx):
    await ctx.send('애브리띵#2227(694017913723682946)')

@bot.command(name="공지")
async def notice(ctx):
    embed = discord.Embed(
            title="공지 채널 설정 방법",
            description="공지 채널을 설정하는 방법이에요!",
            color=RandomColor()
        )
    embed.set_thumbnail(url="https://canary.discord.com/assets/0634b5f01a88a0121bed072779e81bd6.svg")
    embed.add_field(name="1번", value="공지채널로 설정할 채널 이름을 **0띵이봇, 봇-공지, 또는 봇공지**로 시작하세요!", inline=False)
    embed.add_field(name="2번", value="띵이봇 공식 포럼에서 **0띵이봇-공지** 채널을 팔로우하세요!", inline=False)
    embed.add_field(name="1번이 안될때는?", value="띵이봇이 메시지를 보낼 수 있는지 권한을 확인하세요!", inline=True)
    embed.add_field(name="공식 포럼", value="https://discord.gg/nrsVh8EUHE", inline=True)
    embed.set_footer(text="띵이봇! 디스코드를 더욱더 즐겁게!")
    await ctx.send(embed=embed)


@bot.command(name="초대")
async def invitelink(ctx):
    embed = discord.Embed(
            title="띵이봇 초대하기!",
            color=RandomColor()
        )
    embed.add_field(name="띵이봇의 초대링크!", value="http://invite.thingebot.kro.kr/", inline=True)
    embed.add_field(name="띵이봇 위키!", value="https://github.com/OHvrything/thingebotV2/wiki", inline=False)
    embed.set_footer(text="띵이봇을 초대하고 함게 놀아요!")
    await ctx.send(embed=embed)

@bot.command(name="도움말")
async def help(ctx):
    embed = discord.Embed(
            title="띵이봇 위키",
            description="깃허브에서 제공하는 띵이봇 위키를 살펴보세요!",
            color=RandomColor()
        )
    embed.add_field(name="띵이봇 위키", value="https://github.com/OHvrything/thingebotV2/wiki", inline=True)
    embed.add_field(name="공식 포럼", value="https://discord.gg/nrsVh8EUHE", inline=False)
    embed.set_footer(text="띵이봇의 도움말, 초대 등이 있어요!")
    await ctx.send(embed=embed)

@bot.command(name="ping")
async def pingandpong(ctx):
    latancy = bot.latency
    await ctx.send("\U0001F4E2"f' Pong! {round(latancy * 1000)}ms')

@commands.has_permissions(administrator=True)
@bot.command(name="kick", pass_context=True)
async def _kick(ctx, *, user_name: discord.Member, reason=None):
    await user_name.kick(reason=reason)
    await ctx.send(str(user_name)+"을(를) 추방하였습니다!")

@commands.has_permissions(administrator=True)
@bot.command(name="ban", pass_context=True)
async def _ban(ctx, *, user_name: discord.Member):
    await user_name.ban()
    await ctx.send(str(user_name)+"을(를) 이 서버에서 밴해버렸습니다!")

@commands.has_permissions(administrator=True)
@bot.command(name="unban", pass_context=True)
async def _unban(ctx, *, user_name):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = user_name.split('#')
    for ban_entry in banned_users:
        user = ban_entry.user
        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f"{user.mention}을(를) 밴 해제했어요!")
            return

@commands.has_permissions(administrator=True)
@bot.command(name="지워", pass_context=True)
async def _clear(ctx, *, amount=5):
    await ctx.channel.purge(limit=amount + 1)
    await ctx.send(f"{ctx.author.name}에 의해 메시지 {amount}개가 지워졌어요!", delete_after=1)

@bot.command(name="코로나현황")
async def covid(ctx):
        response = requests.get(korea + key)
        text = response.text
        data = json.loads(text)
        embed = discord.Embed(
            title=f"{data['updateTime']}",
            description="코로나는 코리아를 이길 수 없습니다! :3",
            color=RandomColor()
        )
        embed.add_field(name="국내 확진자", value=f"{data['TotalCase']}(+{data['TotalCaseBefore']})", inline=False)
        embed.add_field(name="국내 완치자", value=f"{data['TotalRecovered']}(+{data['TodayRecovered']})", inline=False)
        embed.add_field(name="국내 사망자", value=f"{data['TotalDeath']}(+{data['TodayDeath']})", inline=False)
        embed.add_field(name="국내 치료중", value=f"{data['NowCase']}", inline=False)
        embed.add_field(name="해외 코로나 현황", value="https://www.worldometers.info/coronavirus/index.php", inline=False)
        await ctx.send(embed=embed)

@bot.command(name="채널정보")
async def channelinfo(message):
    embed = discord.Embed(
            title=f"{message.channel.name}의 채널 정보",
            description="이 채널의 정보에요!",
            color=RandomColor()
        )
    embed.add_field(name="카테고리", value=f"{message.channel.category}", inline=False)
    embed.add_field(name="주제", value=f"{message.channel.topic}", inline=False)
    embed.add_field(name="채널 생성일", value=f"{message.channel.created_at}", inline=False)
    embed.add_field(name="슬로우모드", value=f"{message.channel.slowmode_delay}초", inline=False)
    embed.add_field(name="NSFW 여부", value=f"{message.channel.is_nsfw()}", inline=False)
    embed.add_field(name="채널 id", value=f"{message.channel.id}", inline=False)
    await message.channel.send(embed=embed)

@bot.command(name="서버정보")
async def svinfo(message):
    embed = discord.Embed(
            title=f"{message.guild.name}({message.guild.id})의 서버 정보",
            description="이 서버의 정보에요!",
            color=RandomColor()
        )
    embed.set_thumbnail(url=f"{message.guild.icon_url}")
    embed.add_field(name="서버 주인", value=f"{message.guild.owner.mention}({message.guild.owner_id})", inline=False)
    embed.add_field(name="멤버수", value=f"{message.guild.member_count}명", inline=False)
    embed.add_field(name="생성일", value=f"{message.guild.created_at}", inline=False)
    embed.add_field(name="AFK 채널, AFK 시간", value=f"{message.guild.afk_channel}, {message.guild.afk_timeout / 60}분", inline=False)
    embed.add_field(name="기본 역할", value=f"{message.guild.default_role}", inline=False)
    embed.add_field(name="음성 채널 서버", value=f"{message.guild.region}", inline=False)
    embed.add_field(name="서버 부스트 티어(서버 부스트 수)", value=f"{message.guild.premium_tier}({message.guild.premium_subscription_count}개)", inline=False)
    embed.add_field(name="시스템 채널", value=f"<#{message.guild.system_channel.id}>", inline=False)
    embed.add_field(name="규칙 채널", value=f"<#{message.guild.rules_channel.id}>", inline=False)
    embed.set_image(url=f"{message.guild.banner_url}")
    await message.channel.send(embed=embed)

@bot.command(name="내정보")
async def myinfo(msg):
    embed = discord.Embed(
            title=f"{msg.author.name}#{msg.author.discriminator}({msg.author.id})의 정보",
            description="당신의 정보에요!",
            color=RandomColor()
        )
    embed.set_thumbnail(url=f"{msg.author.avatar_url}")
    embed.add_field(name="계정 생성일", value=f"{msg.author.created_at}", inline=False)
    await msg.channel.send(embed=embed)

@bot.event
async def on_guild_join(guild):
    c = 786076322945564682
    invite = await guild.invites()
    embed = discord.Embed(
            title="띵이봇이 새로운 서버에 초대되었어요!",
            description=f"띵이봇이 {guild.name}({guild.id})에 초대되었습니다!",
            color=RandomColor()
        )
    embed.set_thumbnail(url=f"{guild.icon_url}")
    embed.add_field(name="초대 링크", value=f"{invite}", inline=False)
    await bot.get_channel(int(c)).send(embed=embed)

@bot.command(name="url단축")
async def urlshorten(ctx, url):
    embed = discord.Embed(
                title="띵이봇 URL 단축기!",
                description=f"{url} 을(를) 단축하기위해 눌러 짜는중이에요... 잠시만요!",
               color=RandomColor()
            )
    urlmsg = await ctx.send(embed=embed)
    response = requests.get(volaapi + volakey + "&url=" + url)
    text = response.text
    data = json.loads(text)
    if data['error'] == 0:
        response = requests.get(volaapi + volakey + "&url=" + url)
        text = response.text
        data = json.loads(text)
        embed = discord.Embed(
                title="띵이봇 URL 단축기!",
                description=f"{url} 의 단축 결과에요!\n> {data['short']}",
                color=RandomColor()
            )
        embed.set_footer(text="이 URL 단축기는 vo.la(보라)의 api를 받아 만들어졌습니다!")
        await urlmsg.edit(embed=embed)
    else:
        embed = discord.Embed(
                title="URL 단축기가 망가졌어요 ㅜㅜ",
                description=f"{url} 을(를) 단축하기위해 눌러 짜는중에 TNT가 떨어져 오류가 발생했어요 ㅜㅜ",
               color=RandomColor()
            )
        embed.add_field(name="오류 내용", value=f"```{data['msg']}```")
        await urlmsg.edit(embed=embed)

@bot.command(name="문의")
async def contact(ctx, *, msg):
    try:
        c = 786076322945564682
        user = ctx.author
        embed = discord.Embed(
                title="문의 도착!",
                description=f"{user.name}님에게서 문의가 도착했어요! 띵~동~",
                color=RandomColor()
            )
        embed.set_thumbnail(url=f"{user.avatar_url}")
        embed.add_field(name="문의 내용", value=f"{msg}")
        embed.add_field(name="문의 작성자", value=f"{user.mention}")
        embed.set_footer(text=f"문의 답변은 문의 작성자 DM으로, 그리고 문의 답변 완료되면 이 임베드에 체크 반응 달기!")
        await bot.get_channel(int(c)).send(embed=embed)
    except:
        await ctx.send("전송중에 오류가 발생했어요 ㅜㅜ 다시한번 시도해보실래요?")
    else:
        await ctx.send("문의 전송이 성공적으로 완료되었습니다 :D\n문의 답변은 개발자 DM으로 가니 DM을 꼭 열어두세요!")

@bot.command(name="qr코드")
async def qrcode(ctx, *, qrmsg):
    embed = discord.Embed(
            title="QR코드",
            description="QR코드가 포장중이에요! 곧 도착한답니다 :)",
            color=RandomColor()
        )
    loadingmsg = await ctx.send(embed=embed)
    qrserver = "https://api.qrserver.com/v1/create-qr-code/?data="
    embed = discord.Embed(
            title="QR코드",
            description="요청하신 QR코드가 도착했답니다! 후훗...",
            color=RandomColor()
        )
    embed.set_image(url=f"{qrserver + qrmsg}")
    await loadingmsg.edit(embed=embed)

bot.remove_command("help")
bot.run(os.environ['token'])
