import discord
from discord.ext import commands
from PingPongTool import PingPong
from random import randint
import os
import time
import requests
import json
import asyncio

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
    messages = ["'?도움'을 입력해 띵이봇과 노는법을 알아보세요!","애브리띵#2227","이 메시지는 5초마다 변경됩니다!","https://thinge.teb.kro.kr","TEB 2.29",f"유저 {len(bot.users)}명, 길드 {len(bot.guilds)}개에서 함께하는 중!"]
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


@bot.command(name="따라해")
async def Echo(ctx, *, text: str):
    await ctx.send(text)

@bot.command(name="hellothisisverification")
async def ping(ctx):
    await ctx.send('애브리띵#2227(694017913723682946)')

@bot.command(name="공지")
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
            title="<a:info:786781344595705868>띵이봇 위키<a:info:786781344595705868>",
            description="깃허브에서 제공하는 띵이봇 위키를 살펴보세요!",
            color=RandomColor()
        )
    embed.add_field(name="띵이봇 위키", value="https://github.com/OHvrything/thingebotV2/wiki", inline=True)
    embed.add_field(name="공식 포럼", value="https://discord.gg/nrsVh8EUHE", inline=False)
    embed.set_footer(text="띵이봇의 도움말, 초대 등이 있어요!")
    await ctx.send(embed=embed)

@bot.command(name="도움")
async def help2(ctx):
    embed = discord.Embed(
            title="<a:info:786781344595705868>띵이봇 위키<a:info:786781344595705868>",
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
@bot.command(name="kick")
async def _kick(ctx, *, user_name: discord.Member, reason=None):
    await user_name.kick(reason=reason)
    await ctx.send("<a:mangchi:786785085659021364>" + str(user_name)+"을(를) 추방하였습니다!")

@commands.has_permissions(administrator=True)
@bot.command(name="ban")
async def _ban(ctx, *, user_name: discord.Member):
    await user_name.ban()
    await ctx.send("<a:mangchi:786785085659021364>" + str(user_name)+"을(를) 이 서버에서 밴해버렸습니다!")

@commands.has_permissions(administrator=True)
@bot.command(name="unban")
async def _unban(ctx, *, user_name):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = user_name.split('#')
    for ban_entry in banned_users:
        user = ban_entry.user
        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f"<a:mangchi:786785085659021364>{user.mention}을(를) 밴 해제했어요!")
            return

@commands.has_permissions(administrator=True)
@bot.command(name="지워")
async def _clear(ctx, *, amount=5):
    await ctx.channel.purge(limit=amount + 1)
    await ctx.send(f"{ctx.author.name}에 의해 메시지 {amount}개가 지워졌어요!", delete_after=3)

@bot.command(name="코로나현황")
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
        description="마스크 쓰GO! :",
        color=RandomColor()
    )
    embed.add_field(name="국내 확진자", value=f"{data['TotalCase']}(+{data['TotalCaseBefore']})", inline=False)
    embed.add_field(name="국내 완치자", value=f"{data['TotalRecovered']}(+{data['TodayRecovered']})", inline=False)
    embed.add_field(name="국내 사망자", value=f"{data['TotalDeath']}(+{data['TodayDeath']})", inline=False)
    embed.add_field(name="국내 치료중", value=f"{data['NowCase']}", inline=False)
    embed.add_field(name="해외 코로나 현황", value="https://www.worldometers.info/coronavirus/index.php", inline=False)
    await loadmsg.edit(embed=embed)

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

@bot.command(name="url단축")
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

@bot.command(name="투표")
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

@bot.command(name="이모지")
async def emoji(ctx):
    embed = discord.Embed(
            title="띵이봇에 사용된 이모지들이에요!",
            description="<a:loading:786771223929028640>로딩 : url단축, qr코드 등에 사용\n<a:poll:786499385248579615>투표 : 찬반투표 명령어에 사용\n<:covid:783582454619045910>바이러스 : 코로나현황 명령어에 사용\n<:ls:785784744382038017>확성기 : 공지에 사용됨\n<a:info:786781344595705868>물음표 : 도움말에 사용됨\n<a:mangchi:786785085659021364>망치 : 밴, 킥, 언밴 등에 사용됨",
            color=RandomColor()
        )
    embed.set_footer(text="너무 찬란해서 눈뜨고 못. 볼. 껄. 요!\n아니라고요? 죄송해요 ㅜ.ㅜ")
    await ctx.send(embed=embed)

@bot.command(name="크레딧")
async def credit(ctx):
    embed = discord.Embed(
            title="크레딧",
            color=RandomColor()
        )
    embed.add_field(name="띵이봇 크레딧", value="https://github.com/TEAMTEB/thingebotV2/wiki/%ED%81%AC%EB%A0%88%EB%94%A7-%7C-Credits", inline=False)
    embed.set_footer(text="띵이봇의 크레딧입니다!")
    await ctx.send(embed=embed)

@commands.has_permissions(administrator=True)
@bot.command(name="채널생성")
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

@commands.has_permissions(administrator=True)
@bot.command(name="닉네임변경")
async def id_(ctx, user: discord.Member, *, newname=None):
    if newname is not None:
        await user.edit(nick=newname)
        await ctx.send(f"{user.mention}님의 닉네임을 {newname}으로 변경했어요!!")
    else:
        await user.edit(nick=user.name)
        await ctx.send(f"{user.mention}님의 닉네임을 초기화했어요!")

@bot.command(name="프로필")
async def myinfo(msg, *, user: discord.Member=None):
    status_dict: statusd = {discord.Status.online: '온라인',
        discord.Status.offline: '오프라인',
        discord.Status.idle: '자리비움',
        discord.Status.do_not_disturb: '방해금지',
    }
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
            if msg.author.premium_since is not None:
                embed.add_field(name="서버 부스트 시작일", value=user.premium_since.strftime("%Y-%m-%d %H:%M:%S"), inline=False)
            embed.add_field(name="현재 상태", value=f"{user_status}", inline=False)
            embed.add_field(name="봇 여부", value=f"{user.bot}", inline=False)
            embed.add_field(name="디스코드 시스템 메시지 여부", value=f"{user.system}", inline=False)
            embed.add_field(name="역할들", value="".join([role.mention for role in user.roles]), inline=False)
        except:
            pass
        await msg.channel.send(embed=embed)
    else:
        try:
            user_status = status_dict[msg.author.status]
            embed = discord.Embed(
                    title=f"{msg.author.name}#{msg.author.discriminator}의 정보",
                    description=f"{msg.author.mention}의 정보에요!",
                    color=RandomColor()
                )
            embed.set_thumbnail(url=f"{msg.author.avatar_url}")
            embed.add_field(name="ID", value=f"{msg.author.id}", inline=False)
            embed.add_field(name="계정 생성일", value=msg.author.created_at.strftime("%Y-%m-%d %H:%M:%S"), inline=False)
            embed.add_field(name="서버에 들어온 날!", value=f"{msg.author.joined_at.year}년 {msg.author.joined_at.month}월 {msg.author.joined_at.day}일", inline=False)
            embed.add_field(name="서버 닉네임", value=f"{msg.author.display_name}", inline=False)
            if msg.author.premium_since is not None:
                embed.add_field(name="서버 부스트 시작일", value=msg.author.premium_since.strftime("%Y-%m-%d %H:%M:%S"), inline=False)
            embed.add_field(name="현재 상태", value=f"{user_status}", inline=False)
            embed.add_field(name="봇 여부", value=f"{msg.author.bot}", inline=False)
            embed.add_field(name="디스코드 시스템 메시지 여부", value=f"{msg.author.system}", inline=False)
            embed.add_field(name="역할들", value="".join([role.mention for role in msg.author.roles]), inline=False)
        except:
            pass
        await msg.channel.send(embed=embed)
                        
@bot.command(name="계산")
async def math(ctx, mtype, num1, num2):
    if mtype == "더하기":
        await ctx.send(f"결과가 나왔어요!\n**{int(num1)}+{int(num2)}**는 **{int(num1) + int(num2)}**에요!")
    elif mtype == "빼기":
        await ctx.send(f"결과가 나왔어요!\n**{int(num1)}-{int(num2)}**는 **{int(num1) - int(num2)}**에요!")
    elif mtype == "곱하기":
        await ctx.send(f"결과가 나왔어요!\n**{int(num1)}×{int(num2)}**는 **{int(num1) * int(num2)}**에요!")
    elif mtype == "나누기":
        await ctx.send(f"결과가 나왔어요!\n**{int(num1)}÷{int(num2)}**는 **{int(num1) / int(num2)}**에요!")
    else:
        await ctx.send("알 수 없는 계산 타입이에요...\n사용 가능한 계산 타입은 **더하기, 빼기, 곱하기, 나누기**에요!")

bot.remove_command("help")
bot.run(os.environ['token'])
