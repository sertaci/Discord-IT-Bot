import os
import discord
from discord.ext import commands
from bot_acik_tut import keep_alive


activity = activity = discord.Game(name="Visual Studio Code")
bot = commands.Bot(
    command_prefix="!",
    case_insensitive=True,
    activity=activity,
    status=discord.Status.idle,
)


@bot.event
async def on_ready():
    print("Yorungeye {0.user}".format(bot) + " olarak giris yapildi!")

@bot.event
async def on_command_error(ctx, error):
  if isinstance(error, commands.CommandNotFound):
    return
  if isinstance(error, commands.CommandInvokeError):
    await ctx.send("yüklenemedi")
    return
  raise error


# ana fonk.


####### KOMUTLAR #######
# * işaretini kullanmanın sebebi 6.45sn  https://www.youtube.com/watch?v=THj99FuPJmI&ab_channel=Lucas

# kick
@bot.command(aliases=["kick", "kov"])
async def at(ctx, member: discord.Member, *, reason=None):
    if ctx.message.author.id == 184317914441187328:
        await member.kick(reason=reason)
        await ctx.send(
            str(member) + " bu sunucudan kovuldu.\nKovulma nedeni: " + str(reason)
        )
    else:
        await ctx.send(
            "Bu komut bütünlüğü bozar düşüncesi ile şuanlık sadece yapımcı tarafından kullanılıyor."
        )


###### resime yazı yazma ######

# kart çekme -draw



# change my mind


### !yaz ###



####### cog yükleme falan
@bot.command()
async def ekle(ctx, extension=None):
  if ctx.message.author.id == 184317914441187328:
    if not extension:
      await ctx.send("cog ismini girmeden bunu yapamam")
      return
    else:
      bot.load_extension(f"cogs.{extension}")
      await ctx.send(f"{extension} eklendi.")
  else:
    await ctx.send("yalnızca yapımcı ekleme yapabilir <:mad:895380785543131138>")  

@bot.command(aliases=["çıkar"])
async def cikar(ctx, extension=None):
  if ctx.message.author.id == 184317914441187328:
    if not extension:
      await ctx.send("cog ismini girmeden bunu yapamam")
      return
    else:
      bot.unload_extension(f"cogs.{extension}")
      await ctx.send(f"{extension} çıkarıldı.")
  else:
    await ctx.send("yalnızca yapımcı çıkarma yapabilir <:mad:895380785543131138>")

@bot.command(aliases=["yükle"])
async def yukle(ctx, extension=None):
  if ctx.message.author.id == 184317914441187328:
    if not extension:
      await ctx.send("cog ismini girmeden bunu yapamam")
      return
    else:  
      bot.unload_extension(f"cogs.{extension}")
      bot.load_extension(f"cogs.{extension}")
    await ctx.send(f"{extension} yeniden yüklendi.")
  else:
    await ctx.send("yalnızca yapımcı yükleme yapabilir <:mad:895380785543131138>")

    
for filename in os.listdir("./cogs"):
  if filename.endswith(".py"):
    bot.load_extension(f"cogs.{filename[:-3]}")



keep_alive()
# run
my_secret = os.environ["TOKEN"]
bot.run(my_secret)
