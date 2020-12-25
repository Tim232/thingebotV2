import discord
from discord.ext import commands
from PingPongTool import PingPong
from random import randint
import os
import time
import requests
import json
import asyncio
import ast
import sys
import koreanbots

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
KBot = koreanbots.Client(bot, (os.environ['kbtoken']))

@bot.event
async def on_ready():
    print(bot.user.name)
    print(bot.user.id)
    print("준비 완료!")
    c = 786076322945564682
    embed = discord.Embed(
            title="띵이봇이 켜졌습니다!!",
            description=f"띵이봇의 전원이 켜졌어요!",
            color=RandomColor()
        )
    await bot.get_channel(int(c)).send(embed=embed)
    messages = ["'?help'을 입력해 띵이봇과 노는법을 알아보세요!","애브리띵#2227","이 메시지는 5초마다 변경됩니다!","https://thinge.teb.kro.kr","TEB 2.37",f"유저 {len(bot.users)}명, 길드 {len(bot.guilds)}개에서 함께하는 중!"]
    while True:
        await bot.change_presence(status=discord.Status.online, activity=discord.Game(name=messages[0]))
        messages.append(messages.pop(0))
        await asyncio.sleep(5)

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
        c = 786076322945564682
        try:
            embed = discord.Embed(
                    title="띵이봇에게 오류가 발생했어요...",
                    description="띵이봇에게 오류가 발생했어요... ㅜㅜ",
                    color=RandomColor()
                )
            embed.add_field(name="오류 내용", value=f"```{error}```")
            embed.add_field(name="오류 발생 서버, 채널", value=f"{ctx.author.guild.name}({ctx.channel.guild.id}), {ctx.channel.name}({ctx.channel.id})")
            embed.add_field(name="오류 발생 커맨드", value=f"{ctx.message.content}")
            embed.add_field(name="오류 발생자", value=f"{ctx.author.mention}")
            await bot.get_channel(int(c)).send(embed=embed)
        except:
            embed = discord.Embed(
                    title="띵이봇에게 오류가 발생했어요...",
                    description="띵이봇에게 오류가 발생했어요... ㅜㅜ",
                    color=RandomColor()
                )
            embed.add_field(name="오류 내용", value=f"```{error}```")
            embed.add_field(name="오류 발생 커맨드", value=f"{ctx.message.content}")
            embed.add_field(name="오류 발생자", value=f"{ctx.author.mention}")
            await bot.get_channel(int(c)).send(embed=embed)

@bot.command(name="따라해", help="띵이봇이 당신의 말을 따라합니다!", usage="[따라할 말]", aliases=['repeat'])
async def Echo(ctx, *, text: str):
    await ctx.send(text)

@bot.command(name="hellothisisverification", help="띵이봇의 개발자를 확인하세요!", usage="")
async def ping(ctx):
    await ctx.send('애브리띵#2227(694017913723682946)')

@bot.command(name="공지", help="띵이봇의 공지설정 방법이에요!", usage="공지", aliases=['notice'])
async def notice(ctx):
    embed = discord.Embed(
            title="<:ls:785784744382038017>공지 채널 설정 방법<:ls:785784744382038017>",
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


@bot.command(name="초대", help="띵이봇을 초대하세요!", usage="", aliases=['invite'])
async def invitelink(ctx):
    embed = discord.Embed(
            title="띵이봇 초대하기!",
            color=RandomColor()
        )
    embed.add_field(name="띵이봇의 초대링크!", value="http://invite.thingebot.kro.kr/", inline=True)
    embed.add_field(name="띵이봇 위키!", value="https://github.com/OHvrything/thingebotV2/wiki", inline=False)
    embed.set_footer(text="띵이봇을 초대하고 함게 놀아요!")
    await ctx.send(embed=embed)

@bot.command(name="ping", help="띵이봇의 핑을 확인하세요!", aliases=['핑', '반응속도'])
async def pingandpong(ctx):
    latancy = bot.latency
    await ctx.send("\U0001F4E2"f' Pong! {round(latancy * 1000)}ms')

@commands.has_permissions(kick_members=True)
@bot.command(name="kick", pass_context=True, help="유저를 서버에서 킥해줍니다!", usage="[멘션 Mention] [사유 Reason]", aliases=['킥', '추방'])
async def _kick(ctx, user_name: discord.Member, *, reason=None):
    await user_name.kick(reason=reason)
    await ctx.send("<a:mangchi:786785085659021364>" + str(user_name)+"을(를) 추방하였습니다!")
    await user_name.send(f"{user_name.mention}님! 당신은 {ctx.channel.guild.name} 서버에서 아래의 사유로 추방되었습니다...\n추방 사유 : {reason}")

@commands.has_permissions(ban_members=True)
@bot.command(name="ban", pass_context=True, help="유저를 서버에서 밴해버립니다!", usage="[멘션 Mention] [사유 Reason]", aliases=['밴', '차단'])
async def _ban(ctx, user_name: discord.Member, *, reason=None):
    await user_name.ban(reason=reason)
    await ctx.send("<a:mangchi:786785085659021364>" + str(user_name)+"을(를) 이 서버에서 밴해버렸습니다!")
    await user_name.send(f"{user_name.mention}님! 당신은 {ctx.channel.guild.name} 서버에서 아래의 사유로 차단되었습니다...\n차단 사유 : {reason}")

@commands.has_permissions(ban_members=True)
@bot.command(name="unban", pass_context=True, help="유저를 밴 해제합니다!", usage="[닉네임#태그 Username#Tag]", aliases=['언밴', '차단해제'])
async def _unban(ctx, *, user_name):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = user_name.split('#')
    for ban_entry in banned_users:
        user = ban_entry.user
        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f"<a:mangchi:786785085659021364>{user.mention}을(를) 밴 해제했어요!")
            return

@commands.has_permissions(manage_messages=True)
@bot.command(name="지워", pass_context=True, help="띵이봇이 개수만큼 메시지를 지워줘요!", usage="[개수(기본값 5) Amount(default 5)]", aliases=['delete', 'purge'])
async def _clear(ctx, *, amount=5):
    await ctx.channel.purge(limit=amount + 1)
    await ctx.send(f"{ctx.author.name}에 의해 메시지 {amount}개가 지워졌어요!", delete_after=3)

@bot.command(name="코로나현황", help="코로나 19 바이러스 현황을 보여드려요!", usage="", aliases=['koreacorona'])
async def covid(ctx):
    embed = discord.Embed(
        title=f"<a:loading:786771223929028640>코로나 현황 로딩중...<a:loading:786771223929028640>",
        description="코로나 현황을 로딩중입니다!",
        color=RandomColor()
    )
    loadmsg = await ctx.send(embed=embed)
    response = requests.get(korea + key)
    text = response.text
    data = json.loads(text)
    embed = discord.Embed(
        title=f"<:covid:783582454619045910>{data['updateTime']}<:covid:783582454619045910>",
        description="코로나는 코리아를 이길 수 없습니다! :3",
        color=RandomColor()
    )
    embed.add_field(name="국내 확진자", value=f"{data['TotalCase']}(+{data['TotalCaseBefore']})", inline=False)
    embed.add_field(name="국내 완치자", value=f"{data['TotalRecovered']}(+{data['TodayRecovered']})", inline=False)
    embed.add_field(name="국내 사망자", value=f"{data['TotalDeath']}(+{data['TodayDeath']})", inline=False)
    embed.add_field(name="국내 치료중", value=f"{data['NowCase']}", inline=False)
    embed.add_field(name="해외 코로나 현황", value="https://www.worldometers.info/coronavirus/index.php", inline=False)
    await loadmsg.edit(embed=embed)

@bot.command(name="채널정보", help="당신이 있는 이 채널의 정보를 알려드려요!", usage="", aliases=['channelinfo'])
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

@bot.command(name="서버정보", help="당신이 지금 계신 이 서버의 정보를 알려드려요!", usage="", aliases=['serverinfo'])
async def svinfo(message):
    embed = discord.Embed(
            title=f"{message.guild.name}({message.guild.id})의 서버 정보",
            description="이 서버의 정보에요!",
            color=RandomColor()
        )
    embed.set_thumbnail(url=f"{message.guild.icon_url}")
    embed.add_field(name="서버 주인", value=f"{message.guild.owner.mention}({message.guild.owner_id})", inline=False)
    embed.add_field(name="멤버수", value=f"{message.guild.member_count}명(사람 {len(list(filter(lambda x: not x.bot, message.guild.members)))}명, 봇 {len(list(filter(lambda x: x.bot, message.guild.members)))})", inline=False)
    embed.add_field(name="생성일", value=f"{message.guild.created_at}", inline=False)
    embed.add_field(name="AFK 채널, AFK 시간", value=f"{message.guild.afk_channel}, {message.guild.afk_timeout / 60}분", inline=False)
    embed.add_field(name="기본 역할", value=f"{message.guild.default_role}", inline=False)
    embed.add_field(name="음성 채널 서버", value=f"{message.guild.region}", inline=False)
    embed.add_field(name="서버 부스트 티어(서버 부스트 수)", value=f"{message.guild.premium_tier}({message.guild.premium_subscription_count}개)", inline=False)
    embed.add_field(name="시스템 채널", value=f"<#{message.guild.system_channel.id}>", inline=False)
    embed.add_field(name="규칙 채널", value=f"<#{message.guild.rules_channel.id}>", inline=False)
    embed.set_image(url=f"{message.guild.banner_url}")
    await message.channel.send(embed=embed)

@bot.event
async def on_guild_join(guild):
    try:
        c = 786076322945564682
        invite = await guild.invites()
        embed = discord.Embed(
                title="띵이봇이 새로운 서버에 초대되었어요!",
                description=f"띵이봇이 {guild.name}({guild.id})에 초대되었습니다!",
                color=RandomColor()
            )
        embed.set_thumbnail(url=f"{guild.icon_url}")
        embed.add_field(name="초대 링크", value=f"{invite}", inline=False)
    except:
        c = 786076322945564682
        embed = discord.Embed(
                title="띵이봇이 새로운 서버에 초대되었어요!",
                description=f"띵이봇이 {guild.name}({guild.id})에 초대되었습니다!",
                color=RandomColor()
            )
        embed.set_thumbnail(url=f"{guild.icon_url}")
    await bot.get_channel(int(c)).send(embed=embed) 

@bot.command(name="url단축", help="url을 단축해 드립니다!", usage="[url]", aliases=['urlshorten'])
async def urlshorten(ctx, url):
    embed = discord.Embed(
                title="띵이봇 URL 단축기!",
                description=f"<a:loading:786771223929028640>{url} 을(를) 단축하기위해 눌러 짜는중이에요... 잠시만요!<a:loading:786771223929028640>",
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

@bot.command(name="문의", help="띵이봇 개발자에게 메시지를 보내세요!", usage="[문의 내용 Contents]", aliases=['contact', 'messagedev'])
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

@bot.command(name="qr코드", help="qr코드를 만들어드려요!", usage="[내용 Contents]", aliases=['qrcode', 'QR코드', 'QRcode'])
async def qrcode(ctx, *, qrmsg):
    embed = discord.Embed(
            title="QR코드",
            description="<a:loading:786771223929028640>QR코드가 포장중이에요! 곧 도착한답니다 :)<a:loading:786771223929028640>",
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

@bot.command(name="투표", help="찬반투표를 만들어드려요!", usage="[투표 내용 Poll info]", aliases=['poll', 'vote'])
async def chanbanpoll(ctx, *, msg):
    embed = discord.Embed(
            title="<a:poll:786499385248579615>찬반투표<a:poll:786499385248579615>",
            description=f"찬성 반대를 투표해주세요! :)\n\n{msg}",
            color=RandomColor()
        )
    embed.set_footer(text=f"개표는 '메시지 더보기 클릭 > 반응 선택'의 단계로 간단히 진행하실 수 있습니다!")
    poll = await ctx.send(embed=embed)
    await poll.add_reaction("👍")
    await poll.add_reaction("👎")

@bot.event
async def on_guild_remove(guild):
    try:
        c = 786076322945564682
        invite = await guild.invites()
        embed = discord.Embed(
                title="띵이봇이 서버에서 쫓겨났어요 ㅜ.ㅜ",
                    description=f"띵이봇이 {guild.name}({guild.id}) 서버에서 띵이봇이 쫓겨났어요 ㅜ.ㅜ.ㅜ.ㅜ.ㅜ.ㅜ.ㅜ.ㅜ.ㅜ.ㅜ.ㅜ.ㅜ.ㅜ.ㅜ.ㅜ.ㅜ.ㅜ!",
                color=RandomColor()
            )
        embed.set_thumbnail(url=f"{guild.icon_url}")
        embed.add_field(name="초대 링크", value=f"{invite}", inline=False)
    except:
        c = 786076322945564682
        embed = discord.Embed(
                title="띵이봇이 서버에서 쫓겨났어요 ㅜ.ㅜ",
                description=f"띵이봇이 {guild.name}({guild.id}) 서버에서 띵이봇이 쫓겨났어요 ㅜ.ㅜ.ㅜ.ㅜ.ㅜ.ㅜ.ㅜ.ㅜ.ㅜ.ㅜ.ㅜ.ㅜ.ㅜ.ㅜ.ㅜ.ㅜ.ㅜ!",
                color=RandomColor()
            )
        embed.set_thumbnail(url=f"{guild.icon_url}")
    await bot.get_channel(int(c)).send(embed=embed)

@bot.command(name="이모지", help="띵이봇에 사용된 눈뜨고 못. 볼. 정. 도. 로 멋진 이모지를 보여드려요!", usage="", aliases=['emoji'])
async def emoji(ctx):
    embed = discord.Embed(
            title="띵이봇에 사용된 이모지들이에요!",
            description="<a:loading:786771223929028640>로딩 : url단축, qr코드 등에 사용\n<a:poll:786499385248579615>투표 : 찬반투표 명령어에 사용\n<:covid:783582454619045910>바이러스 : 코로나현황 명령어에 사용\n<:ls:785784744382038017>확성기 : 공지에 사용됨\n<a:info:786781344595705868>물음표 : 도움말에 사용됨\n<a:mangchi:786785085659021364>망치 : 밴, 킥, 언밴 등에 사용됨",
            color=RandomColor()
        )
    embed.set_footer(text="너무 찬란해서 눈뜨고 못. 볼. 껄. 요!\n아니라고요? 죄송해요 ㅜ.ㅜ")
    await ctx.send(embed=embed)

@bot.command(name="크레딧", help="띵이봇의 모듈 등의 제작자를 알려드려요!", usage="", aliases=['credit'])
async def credit(ctx):
    embed = discord.Embed(
            title="크레딧",
            color=RandomColor()
        )
    embed.add_field(name="띵이봇 크레딧", value="https://github.com/TEAMTEB/thingebotV2/wiki/%ED%81%AC%EB%A0%88%EB%94%A7-%7C-Credits", inline=False)
    embed.set_footer(text="띵이봇의 크레딧입니다!")
    await ctx.send(embed=embed)

@commands.has_permissions(manage_channels=True)
@bot.command(name="채널생성", help="채널을 생성해드려요!", usage="[채팅/음성/카테고리] [제목]", aliases=['createchannel'])
async def createchannel(ctx, ctype, *, name):
    embed = discord.Embed(
        title="<a:loading:786771223929028640>채널 만드는중...<a:loading:786771223929028640>",
        description=f"띵이봇이 {name}이라는 이름의 {ctype} 채널을 만드는 중이에요!",
        color=RandomColor()
        )
    loadingmsg2 = await ctx.send(embed=embed)
    if ctype == "채팅":
        c = await ctx.channel.guild.create_text_channel(name)
        embed = discord.Embed(
            title="채널 완성!",
            description=f"띵이봇이 <#{c.id}>이라는 이름의 {ctype} 채널을 만드는데 성공했어요!",
            color=RandomColor()
            )
        await loadingmsg2.edit(embed=embed)
    if ctype == "음성":
        c = await ctx.channel.guild.create_voice_channel(name)
        inv = await c.create_invite()
        embed = discord.Embed(
            title="채널 완성!",
            description=f"띵이봇이 [{c.name}]({inv})라는 이름의 {ctype} 채널을 만드는데 성공했어요!",
            color=RandomColor()
            )
        await loadingmsg2.edit(embed=embed)
    if ctype == "카테고리":
        await ctx.channel.guild.create_category(name)
        embed = discord.Embed(
            title="카테고리 완성!",
            description=f"띵이봇이 {name}이라는 이름의 {ctype}를 만드는데 성공했어요!",
            color=RandomColor()
            )
        await loadingmsg2.edit(embed=embed)
    if ctype is not "음성" and not "채팅" and not "카테고리":
        embed = discord.Embed(
            title="채널 생성 실패...!",
            description=f"띵이봇이 {name}이라는 이름의 {ctype} 채널을 만드는데 실패했어요...\n그런데 {ctype}이란 채널 종류가 있었나?",
            color=RandomColor()
            )
        await loadingmsg2.edit(embed=embed)

@commands.has_permissions(manage_nicknames=True)
@bot.command(name="닉네임변경", help="사용자의 닉네임을 설정해요!", usage="[멘션 Mention] [새 닉네임 New Nickname] - 닉네임변경 Change Nickname\n또는 or\n[멘션 Mention] - 닉네임 원래대로 Reset Nickname", aliases=['nickchange', 'nicknamechange'])
async def id_(ctx, user: discord.Member, *, newname=None):
    if newname is not None:
        await user.edit(nick=newname)
        await ctx.send(f"{user.mention}님의 닉네임을 {newname}으로 변경했어요!!")
    else:
        await user.edit(nick=user.name)
        await ctx.send(f"{user.mention}님의 닉네임을 초기화했어요!")

@bot.command(name="프로필", help="띵이봇이 당신의 디스코드 프로필을 보여드려요!", usage="[멘션(안할시 자신) Mention(If not, you)]", aliases=['profile'])
async def myinfo(msg, *, user: discord.Member=None):
    status_dict: statusd = {discord.Status.online: '<a:online:787316219694546955>온라인',
        discord.Status.offline: '<a:offline:787574825496608808>오프라인',
        discord.Status.idle: '<a:idle:787573715298418739>자리비움',
        discord.Status.do_not_disturb: '<a:dnd:787577042425479189>방해금지',
    }
    if msg.channel is not discord.DMChannel:
        if user is not None:
            try:
                user_status = status_dict[user.status]
                embed = discord.Embed(
                        title=f"{user.name}#{user.discriminator}의 정보",
                        description=f"{user.mention}의 정보를 보여드립니다...",
                        color=RandomColor()
                    )
                embed.set_thumbnail(url=f"{user.avatar_url}")
                embed.add_field(name="ID", value=f"{user.id}", inline=False)
                embed.add_field(name="계정 생성일", value=user.created_at.strftime("%Y-%m-%d %H:%M:%S"), inline=False)
                embed.add_field(name="서버에 들어온 날!", value=f"{user.joined_at.year}년 {user.joined_at.month}월 {user.joined_at.day}일", inline=False)
                embed.add_field(name="서버 닉네임", value=f"{user.display_name}", inline=False)
                embed.add_field(name="현재 상태", value=f"{user_status}({user.status})", inline=False)
                embed.add_field(name="봇 여부", value=f"{user.bot}", inline=False)
                embed.add_field(name="디스코드 시스템 메시지 여부", value=f"{user.system}", inline=False)
                embed.add_field(name="역할들", value="".join([role.mention for role in user.roles]), inline=False)
                embed.add_field(name="하는중...", value=f"{user.activity}", inline=False)
                await msg.send(embed=embed)
            except:
                await msg.send("오류가 발생했습니다.\n혹시 DM 채널에서 사용하고계신가요? 서버에서 사용 부탁드려요 :)")
                pass
        else:
            try:
                user_status = status_dict[msg.author.status]
                embed2 = discord.Embed(
                        title=f"{msg.author.name}#{msg.author.discriminator}의 정보",
                        description=f"{msg.author.mention}의 정보에요!",
                        color=RandomColor()
                    )
                embed2.set_thumbnail(url=f"{msg.author.avatar_url}")
                embed2.add_field(name="ID", value=f"{msg.author.id}", inline=False)
                embed2.add_field(name="계정 생성일", value=msg.author.created_at.strftime("%Y-%m-%d %H:%M:%S"), inline=False)
                embed2.add_field(name="서버에 들어온 날!", value=f"{msg.author.joined_at.year}년 {msg.author.joined_at.month}월 {msg.author.joined_at.day}일", inline=False)
                embed2.add_field(name="서버 닉네임", value=f"{msg.author.display_name}", inline=False)
                embed2.add_field(name="현재 상태", value=f"{user_status}({msg.author.status})", inline=False)
                embed2.add_field(name="봇 여부", value=f"{msg.author.bot}", inline=False)
                embed2.add_field(name="디스코드 시스템 메시지 여부", value=f"{msg.author.system}", inline=False)
                embed2.add_field(name="역할들", value="".join([role.mention for role in msg.author.roles]), inline=False)
                embed2.add_field(name="하는중...", value=f"{msg.author.activity}", inline=False)
                await msg.send(embed=embed2)
            except:
                await msg.send("오류가 발생했습니다.\n혹시 DM 채널에서 사용하고계신가요? 서버에서 사용 부탁드려요 :)")
                pass
    
@bot.command(name="계산", help="띵이봇이 수학 계산도 해드려요! 아 머리아파...", usage="[더하기(+)/빼기(-)/곱하기(*)/나누기(/)] [숫자1 Num1] [숫자2 Num2]", aliases=['math'])
async def math(ctx, mtype, num1, num2):
    if mtype == "더하기" or "+":
        await ctx.send(f"결과가 나왔어요!\n**{int(num1)}+{int(num2)}**는 **{int(num1) + int(num2)}**에요!")
    elif mtype == "빼기" or "-":
        await ctx.send(f"결과가 나왔어요!\n**{int(num1)}-{int(num2)}**는 **{int(num1) - int(num2)}**에요!")
    elif mtype == "곱하기" or "*":
        await ctx.send(f"결과가 나왔어요!\n**{int(num1)}×{int(num2)}**는 **{int(num1) * int(num2)}**에요!")
    elif mtype == "나누기" or "/":
        await ctx.send(f"결과가 나왔어요!\n**{int(num1)}÷{int(num2)}**는 **{int(num1) / int(num2)}**에요!")
    else:
        await ctx.send("알 수 없는 계산 타입이에요...\n사용 가능한 계산 타입은 **더하기, 빼기, 곱하기, 나누기**에요!")

@bot.command(name="봇정보", help="띵이봇의 정보를 보여드려요!", usage="", aliases=['botinfo'])
async def botinfo(ctx):
    embed = discord.Embed(
        title=f"띵이봇의 정보",
        description=f"띵이봇의 정보에요!",
        color=RandomColor()
    )
    embed.add_field(name="서버 수", value=f"{len(bot.guilds)}", inline=False)
    embed.add_field(name="유저 수", value=f"{len(bot.users)}", inline=False)
    embed.add_field(name="파이썬 버전", value=f"{sys.version}", inline=False)
    await ctx.send(embed=embed)

def insert_returns(body):
    if isinstance(body[-1], ast.Expr):
        body[-1] = ast.Return(body[-1].value)
        ast.fix_missing_locations(body[-1])

    if isinstance(body[-1], ast.If):
        insert_returns(body[-1].body)
        insert_returns(body[-1].orelse)

    if isinstance(body[-1], ast.With):
        insert_returns(body[-1].body)

@bot.command(name='실행', help="주인용 명령어!", usage="[실행할 커맨드]", aliases=['cmd', 'run', 'eval'])
async def eval_fn(ctx, *, cmd):
    owner = [694017913723682946, 724862211251765250]
    if ctx.author.id in owner:
        msgembed = discord.Embed(title='실행', description='', color=RandomColor())
        msgembed.add_field(name='**INPUT**', value=f'```py\n{cmd}\n```', inline=False)
        msgembed.set_footer(text=f'{ctx.author}', icon_url=ctx.author.avatar_url)
        try:
            fn_name = "_eval_expr"
            cmd = cmd.strip("` ")
            cmd = "\n".join(f"    {i}" for i in cmd.splitlines())
            body = f"async def {fn_name}():\n{cmd}"
            parsed = ast.parse(body)
            body = parsed.body[0].body
            insert_returns(body)
            env = {
                'bot': bot,
                'commands': commands,
                'ctx': ctx,
                '__import__': __import__,
                'discord': discord
                }
            exec(compile(parsed, filename="<ast>", mode="exec"), env)

            result = (await eval(f"{fn_name}()", env))
        except Exception as a:
            result = a
        if result == '':
            result = 'None'
        msgembed.add_field(name="**OUTPUT**", value=f'```py\n{result}```', inline=False)    
        await ctx.send(embed=msgembed)
    else:
        await ctx.send("당신의 말은 듣지 못하게 설정되어있어요 ㅜㅜ...")

@bot.event
async def on_member_join(member):
    embed = discord.Embed(
        title=f"👋안녕하세요!",
        description=f"안녕하세요! {member.mention}님! {member.guild.name} 서버에 오신것을 환영해요!",
        color=RandomColor()
    )
    embed.set_thumbnail(url=member.avatar_url)
    embed.set_footer(text=member.joined_at.strftime("%Y-%m-%d %H:%M:%S"))
    await member.guild.system_channel.send(f"{member.mention}", embed=embed)
    
@bot.event
async def on_member_remove(member):
    embed = discord.Embed(
        title=f"🖐안녕히가세요...",
        description=f"안녕히가세요... {member.mention}님. {member.guild.name} 서버에 꼭 다시 오셔야해요...!",
        color=RandomColor()
    )
    embed.set_thumbnail(url=member.avatar_url)
    await member.guild.system_channel.send(embed=embed)

@bot.command(name="타이머", help="타이머를 맟춰줘요!", usage="[m/s] [숫자 Number] [내용 Content]", aliases=['timer'])
async def timer(ctx, mors, num, *, desc="없음"):
    if mors == "m":
        embed = discord.Embed(
            title=f"{num}분동안 타이머를 시작합니다!\n\n{ctx.author.mention}님의 타이머입니다!",
            description=f"{desc}",
            color=RandomColor()
        )
        await ctx.send(embed=embed)
        await asyncio.sleep(int(num) * 60)
        await ctx.send(f"{ctx.author.mention}님! {num}분의 타이머가 끝났어요!\n내용: {desc}")
    if mors == "s":
        embed = discord.Embed(
            title=f"{num}초동안 타이머를 시작합니다!",
            description=f"{desc}\n\n{ctx.author.mention}님의 타이머입니다!",
            color=RandomColor()
        )
        await ctx.send(embed=embed)
        await asyncio.sleep(int(num))
        await ctx.send(f"{ctx.author.mention}님! {num}초의 타이머가 끝났어요!\n내용: {desc}")
    else:
        await ctx.send(f"{ctx.author.mention}, 으에? 그런 단위는 없는것같은데...\n사용 가능한 시간의 단위는 분(m) 그리고 초(s)에요!")
                       
bot.run(os.environ['token'])
