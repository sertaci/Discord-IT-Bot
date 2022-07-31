import os
import discord
from discord.ext import commands
from bot_wakey import keep_alive

intents = discord.Intents.default()
intents.members = True

activity = activity = discord.Game(name="Visual Studio Code")
bot = commands.Bot(
    command_prefix="!",
    help_command=None,
    case_insensitive=True,
    activity=activity,
    status=discord.Status.idle, 
    intents=intents
)

# kick
@bot.command(aliases=["at", "kov"])
async def kick(ctx, member: discord.Member, *, reason=None):
  if ctx.message.author.id == 184317914441187328:
    await member.kick(reason=reason)
    await ctx.send(
        str(member) + " Kicked from this server.\nReason for being kicked out: " + str(reason))
  else:
    await ctx.send(
            "This command is currently only used by the creator because of the thought of breaking the integrity."
        )

@bot.event
async def on_ready():
    print("Yorungeye {0.user}".format(bot) + " olarak giris yapildi!")

@bot.event
async def on_command_error(ctx, error):
  if isinstance(error, commands.CommandNotFound):
    return
  
  if isinstance(error, commands.MemberNotFound):
    await ctx.send("Couldn't find the member <:peepo_shrug:895380755868446751>")
    return
  raise error

####### cog inserting etc.
@bot.command(aliases=["ekle"])
async def insert(ctx, extension=None):
  if ctx.message.author.id == 184317914441187328:
    if not extension:
      await ctx.send("I can't do this without entering the cog name")
      return
    else:
      bot.load_extension(f"cogs.{extension}")
      await ctx.send(f"{extension} inserted. 🌪️")
  else:
    await ctx.send("only the creator can insert <:mad:895380785543131138>")  

@bot.command(aliases=["çıkar"])
async def extract(ctx, extension=None):
  if ctx.message.author.id == 184317914441187328:
    if not extension:
      await ctx.send("I can't do this without entering the cog name")
      return
    else:
      bot.unload_extension(f"cogs.{extension}")
      await ctx.send(f"{extension} extracted. 🌪️")
  else:
    await ctx.send("only the creator can extract <:mad:895380785543131138>")

@bot.command(aliases=["yükle"])
async def reload(ctx, extension=None):
  if ctx.message.author.id == 184317914441187328:
    if not extension:
      await ctx.send("I can't do this without entering the cog name")
      return
    else:  
      bot.unload_extension(f"cogs.{extension}")
      bot.load_extension(f"cogs.{extension}")
    await ctx.send(f"{extension} reloaded. 🌪️")
  else:
    await ctx.send("only the creator can reload <:mad:895380785543131138>")
    
for filename in os.listdir("./cogs"):
  if filename.endswith(".py"):
    bot.load_extension(f"cogs.{filename[:-3]}")

keep_alive()
# run
my_secret = os.environ["TOKEN"]
bot.run(my_secret)
