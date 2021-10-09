import discord
from discord.ext import commands
from random import choice
from PIL import Image, ImageFont, ImageDraw
import textwrap
import os

class Komutlar(commands.Cog):
  def __init__(self,bot):
    self.bot = bot

#okutma
  @commands.command(aliases=["oku"])
  async def okut(self, ctx, *, text="Bir şey yazmadığın için bu cümle boşu boşuna okunacak <:mad:895380785543131138> "):
      message = ctx.message
      await message.delete()
      await ctx.send(f"{text}", tts=True)

# kart çekme -draw
  @commands.command(aliases=["çek", "kartçek"])
  async def draw(self, ctx, kisi="kişi girilmedi", *, text="metin girilmedi"):
      resim_sec3 = choice(os.listdir(".//discord_bot_replit/draw_kart"))
      resim_secildi3 = os.path.join(".//discord_bot_replit/draw_kart", resim_sec3)

      img3 = Image.open(resim_secildi3)
      draw3 = ImageDraw.Draw(img3)

      message = ctx.message
      content = ctx.message.content
      karakter_uzunluk = len(content)

      if karakter_uzunluk > 110:
          await ctx.send("110 karakter limiti aşıldı. Mesajı yine de gönderiyorum")

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
  @commands.command(aliases=["yazdır2", "yaz2"])
  async def cmm(self,ctx, *, text="metin girilmedi"):

      resim_sec2 = choice(os.listdir(".//discord_bot_replit/change_my_mind"))
      resim_secildi2 = os.path.join(".//discord_bot_replit/change_my_mind", resim_sec2)

      img2 = Image.open(resim_secildi2)
      draw2 = ImageDraw.Draw(img2)

      message = ctx.message
      content = ctx.message.content
      karakter_uzunluk = len(content)

      if karakter_uzunluk > 150:
        await ctx.send("150 karakter limiti aşıldı. Mesajı yine de gönderiyorum")

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
  @commands.command(aliases=["yaz"])
  async def yazdır(self, ctx, *, text="metin girilmedi"):

    resim_sec = choice(os.listdir(".//discord_bot_replit/resimler"))
    resim_secildi = os.path.join(".//discord_bot_replit/resimler", resim_sec)

    img = Image.open(resim_secildi)
    draw = ImageDraw.Draw(img)

    message = ctx.message
    content = ctx.message.content
    karakter_uzunluk = len(content)

    if karakter_uzunluk > 200:
        await ctx.send("200 karakter limiti aşıldı. Mesajı yine de gönderiyorum.")

    if resim_sec == ("snoop.png"):
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

    elif resim_sec == ("jim.png"):
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

    elif resim_sec == ("elon.png"):
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

    elif resim_sec == ("harold.png"):
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

    elif resim_sec == ("zucker.png"):
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

    elif resim_sec == ("trump.png"):
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



  # diğer komutlar

  @commands.command(aliases=["yapimci"])
  async def yapımcı(self, ctx):
    await ctx.send("sincertarius")

  @commands.command(aliases=["şans"])
  async def sans(self, ctx, *, txt=None):
    if not txt:
        await ctx.send("bir şeyler yaz tahmin edeyim")
        return
    sans_cevaplar = [
        "şüphesiz",
        "büyük ihtimalle",
        "gördüğüm kadarıyla bunun olma ihtimali yüksek",
        "cevaplar çok bulanık birdaha dene",
        "bunu söylememek daha iyi",
        "bir sonuca varamadım birdaha dene",
        "ihtimal yükseğe yakın",
        "cevap sakıncalı bunu sana söyleyemem",
        "belirsiz",
        "daha düzgün sor anlamadım",
        "buna gelecek cevaba kim ne derse desin güvenme",
        "gördüğüm kadarıyla bunun cevabı pek hoş değil",
        "çok şüpheli",
        "imkanı yok",
        "bunun imkanı var gibi gözüküyor"
        "oluru hem var hem yok",
        "bunun imkanı yok gibi gözüküyor",
    ]

    await ctx.send(f"{choice(sans_cevaplar)}")


# ihtimaller
  @commands.command()
  async def ihtimal(self, ctx, iht1=None, iht2=None):
    if not iht1 or not iht2:
        await ctx.send(
            "2 tane öğe yazmadan olasılığı hesaplayamam. Her öğe tırnak işaretleri ile ayırılmalı ('cyber security' 'mobile-dev' gibi)"
        )
        return
    secim_iht = choice([iht1, iht2])
    await ctx.send(secim_iht)


  @commands.command()
  async def ihtimal3(self, ctx, iht1=None, iht2=None, iht3=None):
    if not iht1 or not iht2 or not iht3:
        await ctx.send(
            "3 tane öğe yazmadan olasılığı hesaplayamam. Her öğe tırnak işaretleri ile ayırılmalı ('cyber security' 'web dev' 'mobile-dev' gibi)"
        )
        return
    secim_iht = choice([iht1, iht2, iht3])
    await ctx.send(secim_iht)


#spoiler
  @commands.command(aliases=["spoiler", "spo"])
  async def spoi(self, ctx, *, text="Herhangi bir şey yazmadın ama ben bunu yine de gizli bir şeymiş gibi yazıyorum <:happy2:895380897312952350>"):
    message = ctx.message
    await message.delete()
    await ctx.send(f"||{text}||")


# doğru yanlış
  @commands.command(aliases=["doğru_yanlış", "dogru_yanlis", "tf"])
  async def dy(self, ctx, *, txt_dy=None):
    if not txt_dy:
        await ctx.send("bir şeyler yaz ki doğru mu yanlış mı söyleyeyim")
        return
    cevap_dy = ["doğru", "yanlış"]
    secim_dy = choice(cevap_dy)
    await ctx.send(f"{secim_dy}")


# emojiler
  @commands.command(aliases=["not"])
  async def notal(self, ctx):
    message = ctx.message
    await message.delete()
    await ctx.send("<:note:895380794300833844>")


  @commands.command(aliases=["bilmem", "idk"])
  async def dunno(self, ctx):
    message = ctx.message
    await message.delete()
    await ctx.send("<:peepo_shrug:895380755868446751>")

# mesaj kopyalama
  @commands.command(aliases=["say"])
  async def söyle(self, ctx, *, text="Bir şeyler söyle aynısını yazayım"):
    message = ctx.message
    await message.delete()
    await ctx.send(f"{text}")

def setup(bot):
  bot.add_cog(Komutlar(bot))
