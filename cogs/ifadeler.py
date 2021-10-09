from discord.ext import commands
from random import choice


class Ifadeler(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.Cog.listener()
  async def on_message(self, message):
    if message.author.id == 895376282131525653:
        return

    # kanala özel cevap
    kanal_id = message.channel.id
    if kanal_id == 856259013774671893:
        await message.channel.send("<:note:895380794300833844>")

    # kişiye özel cevap (id için sağ menüden sağ tıklayıp al)
    """if message.author.id == 280066172542517248:
        await message.channel.send('sen gonuşma soner')"""
    # seslenme vs.

    kole_seslenme = ["la bot", "lan bot" ,"bot", "hey bot"]
    kole_ses_cevap = [
        "buyrun efendim",
        "emrinize amadeyim",
        "ne istersiniz?",
        "nasıl yardımcı olabilirim?",
        "ne arzu etmiştiniz?",
        "birisi beni mi çağırdı",
        "galiba bana seslendiniz",
        "yeter lan ne botmuş",

    ]
    ses_cevap = choice(kole_ses_cevap)
    for seslenme in kole_seslenme:
        if message.content.lower().startswith(seslenme):
            await message.channel.send(ses_cevap)

    kole_merb_cevap = ["merhaba efendim", "hoşgeldiniz",]
    kole_merb_cevap_sec = choice(kole_merb_cevap)
    kole_merhaba = message.content.lower()
    if kole_merhaba == "merhaba" or kole_merhaba == "mrhaba" or kole_merhaba == "meraba" or kole_merhaba == "mrb" or kole_merhaba == "merhava":
        await message.channel.send(kole_merb_cevap_sec)
        await message.add_reaction("👋")

    kole_aferim = ["aferim köle", "you have done good work my slave", "aferim bot"]
    for aferim in kole_aferim:
        if message.content.lower().startswith(aferim):
            await message.channel.send("sağ olun efendim!")

    tamam_cevap = ["tm", "tamam", "tmm"]
    tamam_cvp = choice(tamam_cevap)
    tamam_tek = message.content.lower()
    if tamam_tek == "tamam" or tamam_tek == "tmam" or tamam_tek == "tm" or tamam_tek == "tmm" or tamam_tek == "tamamdır":
        await message.channel.send(tamam_cvp)
        await message.add_reaction("👍")

    aynen_list = ["aynen"]
    for aynen in aynen_list:
        if message.content.lower().startswith(aynen):
            await message.channel.send("aynen")

    kole_git = [
        "çık git",
        "sana demedim",
        "sen değil",
    ]
    kole_git_cevap = "o zaman gidiyorum <:sad:895380906750132224>"
    for git in kole_git:
        if message.content.lower().startswith(git):
            await message.channel.send(kole_git_cevap)

    kole_gel = [
        "geri gel",
        "kendine gel",
        "gel geri",
        "gel bura",
    ]
    kole_gel_cevap = [
        "geldim <:happy2:895380897312952350>",
        "geliyorum <:happy2:895380897312952350>",
]
    
    gel_cevap = choice(kole_gel_cevap)
    for gel in kole_gel:
        if message.content.lower().startswith(gel):
            await message.channel.send(gel_cevap)

    gel_geri = message.content.lower()
    if gel_geri == "gel":
        await message.channel.send(gel_cevap)

    kole_selam = [
        "selam",
        "slm",
        "selamun",
    ]
    kole_slm_cevap = [
        "as",
        "selam",
]

    slm_cevap = choice(kole_slm_cevap)
    for selam in kole_selam:
        if message.content.lower().startswith(selam):
            await message.channel.send(slm_cevap)
            await message.add_reaction("<:happy2:895380897312952350>")

    if message.content.lower().startswith("sa "):
        await message.channel.send("as")
        await message.add_reaction("<:happy2:895380897312952350>")

    sa_message = message.content.lower()
    if sa_message == "sa":
        await message.channel.send("as")  
        await message.add_reaction("<:happy2:895380897312952350>")

    test_message1 = message.content.lower()
    if test_message1 == "test":
      if message.author.id == 184317914441187328:
        await message.channel.send("deneme 1 2 3")
      else:
        await message.channel.send("Yalnızca yapımcı test yapabilir <:mad:895380785543131138>")

    kole_nasil = [
        "nasılsın",
        "nasilsin",
        "iyi misin",]

    kole_nasil_cevap = [
        "iyiyim sen?",
        "iyiyim <:happy2:895380897312952350>",
        "iyiyim emmi <:happy2:895380897312952350>",
        "Allah a şükür",
    ]
    nasil_cevap = choice(kole_nasil_cevap)
    for nasil in kole_nasil:
        if message.content.lower().startswith(nasil):
            await message.channel.send(nasil_cevap)

    naber_message = message.content.lower()
    if naber_message == "naber":
        await message.channel.send(nasil_cevap)
  
def setup(bot):
  bot.add_cog(Ifadeler(bot))
