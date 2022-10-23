import discord
from discord.ext import commands
from random import choice, randint
from PIL import Image, ImageFont, ImageDraw
import textwrap
import os


class Commands(commands.Cog):
  def __init__(self,bot):
    self.bot = bot

  @commands.command()
  async def members(self, ctx):
    for guild in self.bot.guilds:
        for member in guild.members:
            print(member, member.joined_at, member.nick, member.id, member.roles, member.leaved_at)
#help
  @commands.command()
  async def help(self, ctx):
    await ctx.send("""```yaml
say: (aliases: söyle)
Write something then bot will delete your message and write it again in the chat --> !say <your expression>``````yaml
speak: (aliases: read, talk, oku, okut)
The bot reads your expression --> !read <your expression>``````yaml
draw: (aliases: çek, kartçek)
"Draw cards" meme template --> !draw <name> <your expression>``````yaml
cmm: 
"Change my mind" meme template --> !cmm <your expression>``````yaml
write: (aliases: yaz, yazdır)
Write something then bot will delete your message and write it again in a random picture --> !write <your expression>``````yaml
luck: (aliases: lucken) 
If you want to know possibiliy of your expression --> !luck <expression>``````yaml
sans: (aliases: şans, lucktr)
Turkish version of the luck command --> !sans <your expression>``````yaml
prob: (aliases: ihtimal, probability)
It chooses a element in 2 elements that you write. If your expressions consist of more than one word, each item must be separated by quotes (like --> !prob "cyber security"  "mobile dev") --> !prob <exp1> <exp2>``````yaml
prob3: (aliases: ihtimal3, probability3)
It chooses a element in 3 elements that you write. If your expressions consist of more than one word, each item must be separated by quotes (like --> !prob "cyber security" "web dev" "mobile dev") --> !prob <exp1> <exp2> <exp3>``````yaml
spoi: (aliases: spoiler, spo)
Cover your expressions with spoiler --> !spoi <your expression>``````yaml
tf: (aliases: truefalse)
True false command. Use !dy for tr version --> !tf <your expression>``````yaml
dy:  
Doğru Yanlış command --> !dy <your expression>``````yaml
takenote: (aliases: note, notal)
"Take note" emoji --> !takenote``````yaml
dunno: (aliases: idk, bilmem)
"Dunno" emote --> !dunno``````yaml
creator: (aliases: yapımcı, master)
Creator of the bot --> !creator``````yaml
kick:
This is exclusive to the creator```""" + "```> maybe there is a stack of commands out there that my master has carefully hidden, waiting to be discovered. 🥷```")

  # say command
  @commands.command(aliases=["söyle"])
  async def say(self, ctx, *, text="Say something and I'll delete yours and write the same"):
    message = ctx.message
    await message.delete()
    await ctx.send(f"{text}")

#okutma
  @commands.command(aliases=["oku", "okut", "read", "talk"])
  async def speak(self, ctx, *, text="Since you did not write anything, this sentence will be read in vain <:mad:895380785543131138> "):
      message = ctx.message
      await message.delete()
      await ctx.send(f"{text}", tts=True)

  @commands.command()
  async def join(self, ctx):
    channel = ctx.author.voice.channel
    await channel.connect()
  @commands.command()
  async def leave(self, ctx):
    await ctx.voice_client.disconnect()

  #random number
  @commands.command(aliases=["sayıçek"])
  async def random(self, ctx, num1=None, num2=None):
    if not num1 or not num2:
      await ctx.send("You must clarify a range")
      return
    await ctx.send(str(randint(int(num1), int(num2))))

# kart çekme -draw
  @commands.command(aliases=["çek", "kartçek"])
  async def draw(self, ctx, kisi="no name entered!", *, text="no text entered!"):
      pck_img3 = choice(os.listdir(".//discord_bot_replit/draw_kart"))
      picked_img3 = os.path.join(".//discord_bot_replit/draw_kart", pck_img3)

      img3 = Image.open(picked_img3)
      draw3 = ImageDraw.Draw(img3)

      message = ctx.message
      content = ctx.message.content
      char_len = len(content)

      if char_len > 110:
          await ctx.send("110 character limit exceeded. I'm still sending the message")

      font = ImageFont.truetype(r".//discord_bot_replit/Futura Bold font.ttf", 16)
      draw3.text(
          (105, 155),
          textwrap.fill(text, width=21),
          fill=(0, 0, 0),
          anchor="ls",
          font=font,
      )
      font2 = ImageFont.truetype(r".//discord_bot_replit/Futura Bold font.ttf", 20)
      draw3.text((330, 10), kisi, fill=(0, 0, 0), font=font2)
      img3.save("test_draw.png")
      await message.delete()
      await ctx.send(file=discord.File("test_draw.png"))

# change my mind
  @commands.command()
  async def cmm(self,ctx, *, text="no text entered"):

      pck_img2 = choice(os.listdir(".//discord_bot_replit/change_my_mind"))
      picked_img2 = os.path.join(".//discord_bot_replit/change_my_mind", pck_img2)

      img2 = Image.open(picked_img2)
      draw2 = ImageDraw.Draw(img2)

      message = ctx.message
      content = ctx.message.content
      char_len = len(content)

      if char_len > 150:
        await ctx.send("150 character limit exceeded. I'm still sending the message")

      font = ImageFont.truetype(r".//discord_bot_replit/CENTURY.TTF", 13)
      draw2.text(
        (130, 183),
        textwrap.fill(text, width=30),
        fill=(0, 0, 0),
        anchor="ls",
        font=font,
      )
      img2.save("test_cmm.png")
      await message.delete()
      await ctx.send(file=discord.File("test_cmm.png"))

      
### !yaz ###
  @commands.command(aliases=["yaz", "yazdır"])
  async def write(self, ctx, *, text="no text entered!"):

    pck_img = choice(os.listdir(".//discord_bot_replit/images"))
    picked_img = os.path.join(".//discord_bot_replit/images", pck_img)

    img = Image.open(picked_img)
    draw = ImageDraw.Draw(img)

    message = ctx.message
    content = ctx.message.content
    char_len = len(content)

    if char_len > 200:
        await ctx.send("200 character limit exceeded. I'm still sending the message")

    if pck_img == ("snoop.png"):
        font = ImageFont.truetype(r".//discord_bot_replit/Futura Bold font.ttf", 18)
        draw.text(
            (5, 100),
            textwrap.fill(text, width=25),
            fill=(0, 0, 0),
            anchor="ls",
            font=font,
        )
        img.save("test_snoop.png")
        await message.delete()
        await ctx.send(file=discord.File("test_snoop.png"))

    elif pck_img == ("jim.png"):
        font = ImageFont.truetype(r".//discord_bot_replit/Futura Bold font.ttf", 17)
        draw.text(
            (13, 55),
            textwrap.fill(text, width=31),
            fill=(0, 0, 0),
            anchor="ls",
            font=font,
        )
        img.save("test_jim.png")
        await message.delete()
        await ctx.send(file=discord.File("test_jim.png"))

    elif pck_img == ("elon.png"):
        font = ImageFont.truetype(r".//discord_bot_replit/Futura Bold font.ttf", 14)
        draw.text(
            (5, 25),
            textwrap.fill(text, width=30),
            fill=(0, 0, 0),
            anchor="ls",
            font=font,
        )
        img.save("test_elon.png")
        await message.delete()
        await ctx.send(file=discord.File("test_elon.png"))

    elif pck_img == ("harold.png"):
        font = ImageFont.truetype(r".//discord_bot_replit/Futura Bold font.ttf", 15)
        draw.text(
            (102, 215),
            textwrap.fill(text, width=30),
            fill=(0, 0, 0),
            anchor="ls",
            font=font,
        )
        img.save("test_harold.png")
        await message.delete()
        await ctx.send(file=discord.File("test_harold.png"))

    elif pck_img == ("zucker.png"):
        font = ImageFont.truetype(r".//discord_bot_replit/Futura Bold font.ttf", 17)
        draw.text(
            (53, 210),
            textwrap.fill(text, width=30),
            fill=(0, 0, 0),
            anchor="ls",
            font=font,
        )
        img.save("test.png")
        await message.delete()
        await ctx.send(file=discord.File("test.png"))

    elif pck_img == ("trump.png"):
        font = ImageFont.truetype(r".//discord_bot_replit/Futura Bold font.ttf", 14)
        draw.text(
            (50, 100),
            textwrap.fill(text, width=28),
            fill=(0, 0, 0),
            anchor="ls",
            font=font,
        )
        img.save("test_trump.png")
        await message.delete()
        await ctx.send(file=discord.File("test_trump.png"))



  #other commands

  @commands.command(aliases=["lucken"])
  async def luck(self, ctx, *, txt=None):
    if not txt:
        await ctx.send("Write something and then I'll guess")
        return

    sans_cevaplar = [
        "no doubt  💯",
        "it seems possible",
        "most probably",
        "likely high",
        "less likely possible  🤏",
        "high chance status",
        "try one more time to get the right result",
        "answers are too fuzzy try again  🧐",
        "Do not trust the answer to this, no matter what anyone says  🤫",
        "very suspicious  🤔",
        "this is unlikely",
        "good luck with that  😞",
        "it's hard  😕"
    ]

    await ctx.send(f"{choice(sans_cevaplar)}")

  @commands.command(aliases=["şans", "lucktr"])
  async def sans(self, ctx, *, txt=None):
    if not txt:
        await ctx.send("Bir şeyler yaz olacakları tahmin edeyim")
        return

    sans_cevaplar2 = [
        "şüphesiz  💯",
        "bunun imkanı var gibi gözüküyor",
        "büyük ihtimalle",
        "ihtimal yükseğe yakın",
        "az ihtimalle  🤏",
        "yüksek şans durumu",
        "doğru sonuca ulaşabilmem için bir kere daha dene",
        "cevaplar çok bulanık birdaha dene",
        "buna gelecek cevaba kim ne derse desin güvenme  🤫",
        "çok şüpheli",
        "bunun ihtimali yok",
        "hayırlısı",
        "zor be"
    ]

    await ctx.send(f"{choice(sans_cevaplar2)}")

# ihtimaller
  @commands.command(aliases=["ihtimal", "probability"])
  async def prob(self, ctx, iht1=None, iht2=None):
    if not iht1 or not iht2:
        await ctx.send(
            'I can\'t calculate probability without writing 2 items. Each item must be separated by double quotes (like --> !prob "cyber security" "mobile dev")'
        )
        return
    secim_iht = choice([iht1, iht2])
    await ctx.send(secim_iht)


  @commands.command(aliases=["ihtimal3", "probability3"])
  async def prob3(self, ctx, iht1=None, iht2=None, iht3=None):
    if not iht1 or not iht2 or not iht3:
        await ctx.send(
            'I can\'t calculate probability without writing 2 items. Each item must be separated by double quotes (like --> !prob "cyber security" "web dev" "mobile dev")'
        )
        return
    secim_iht = choice([iht1, iht2, iht3])
    await ctx.send(secim_iht)



    
#spoiler
  @commands.command(aliases=["spoiler", "spo"])
  async def spoi(self, ctx, *, text="You didn't write anything, but I'm writing this like it's a secret anyway <:happy2:895380897312952350>"):
    message = ctx.message
    await message.delete()
    await ctx.send(f"||{text}||")


# true false
  @commands.command(aliases=["truefalse"])
  async def tf(self, ctx, *, txt_dy=None):
    if not txt_dy:
        await ctx.send("Write something so I can tell if it's true or false")
        return
    cevap_dy = ["true", "false"]
    secim_dy = choice(cevap_dy)
    await ctx.send(f"{secim_dy}")

  # doğru yanlış
  @commands.command()
  async def dy(self, ctx, *, txt_dy=None):
    if not txt_dy:
        await ctx.send("Bir şey yaz, doğru mu yanlış mı söyleyeyim")
        return
    cevap_dy = ["doğru", "yanlış"]
    secim_dy = choice(cevap_dy)
    await ctx.send(f"{secim_dy}")


# emojiler
  @commands.command(aliases=["note", "notal"])
  async def takenote(self, ctx):
    message = ctx.message
    await message.delete()
    await ctx.send("<:note:895380794300833844>")


  @commands.command(aliases=["bilmem", "idk"])
  async def dunno(self, ctx):
    message = ctx.message
    await message.delete()
    await ctx.send("<:peepo_shrug:895380755868446751>")

  @commands.command(aliases=["sadge"])
  async def sad(self, ctx):
    message = ctx.message
    await message.delete()
    await ctx.send("<:sad:924777692203712552>")

  #say but without deleting just send the channel
  @commands.command()
  async def ecr(self, ctx, mes_id, text="👋"):
    message = ctx.fetch_message(mes_id)
    await ctx.message.add_reaction(emoji=text)

  @commands.command()
  async def scr(self, ctx, chan_id=0, *, text="Write something"):
    channel = self.bot.get_channel(chan_id)
    await channel.send(text)

  #creator
  @commands.command(aliases=["yapımcı", "master"])
  async def creator(self, ctx):
    await ctx.send("Sincertarius")

  @commands.command()
  async def mak(self, ctx):
    message = ctx.message
    await message.delete()
    await ctx.send("Metin Aktaş's grading method")
    await ctx.send(file=discord.File("ma.sucks.png"))

def setup(bot):
  bot.add_cog(Commands(bot))
