from keep_alive import keep_alive

import discord
from discord.ext import commands,tasks
from itertools import cycle

intents = discord.Intents(messages = True , guilds = True ,  reactions = True , members = True , presences = True)
client  = commands.Bot(command_prefix = 'in.', intents = intents)

@client.event 
async def on_ready():
  change_status.start()
  print("Let's run!!")

status = cycle(['With Google','With Discord','With Stackoverflow','With Stackexchange'])

@tasks.loop(seconds=5)
async def change_status():
  await client.change_presence(activity=discord.Game(f'{next(status)} | in.help'))  

@client.event
async def on_member_join(member):

  channel = client.get_channel((name of the channel you want to drop your intro)) #check check check
  
  embed = discord.Embed(title = "୨୧ Welcome to HACKET Discord ୨୧",description = "- - - - - - - - - - - - - - - - - - - - - - - - - - - - -\n× make sure to read the <channel id>\n× chat in <channel id>\n× write an <channel id>\nx get started in <channel id>\n× enjoy your stay :large_blue_diamond: \n- - - - - - - - - - - - - - - - - - - - - - - - - - - - -", colour=discord.Colour.purple())  #check check check


  embed.set_image(url="https://media.giphy.com/media/xsE65jaPsUKUo/giphy.gif")

  embed.set_footer(text="\nHope you have a great coding journey ahead ✌️")

  await member.send("Welcome to (organisation) Discord server", embed=embed)

  await channel.send(member.mention , embed=embed)


@client.event
async def on_command_error(ctx, error):
  if isinstance(error, commands.CommandNotFound):
    await ctx.send('Invalid Command Used. Type in.help to know the commands')
                       
  if isinstance(error, commands.MissingRequiredArgument):
    await ctx.send('Give proper values to the command an argument is missing')


#OTHER COMMANDS

#CLEAR/PURGE
@client.command(aliases = ['clean','erase','purge'])
async def clear(ctx, num = 1):
  await ctx.channel.purge(limit = num+1)  


#ABOUT

@client.command(aliases=['about'])
async def post(ctx):
  img = "https://cdn.discordapp.com/attachments/818926984624078868/821881609375449128/about.png"
  embed = discord.Embed(colour=discord.Colour.purple())
  embed.set_image(url=img)
  await ctx.send(embed=embed)
  embed2 = discord.Embed(title="The Official Discord server of (your organisation or server name)", description="\n:small_blue_diamond: An exclusive server for (your organisation name) to hang out, experience the technical community and learn with/from others.\n\n:small_blue_diamond: You can find and hangout with seniors and juniors, study with everyone, discuss doubts and find useful resources.\n\n:small_blue_diamond: A helpful community with helpful admins, moderators and a bunch of bots.",colour=discord.Colour.purple())
  await ctx.send(embed=embed2)

#FAQ

@client.command()
async def faq(ctx):
  img = discord.embed(colour=discord.Colour.purple())
  src="https://bigbaddice.pl/wp-content/uploads/2017/07/WATCH_DOGS%C2%AE-2_20170719192157-1024x576.jpg"
  img.set_image(url=src)
  await ctx.send(embed=img)
  embed = discord.Embed(title="Frequently Asked Questions",description="\n:small_blue_diamond: **How do I use discord?**\nCheckout this guide https://support.discord.com/hc/en-us/articles/360045138571-Beginner-s-Guide-to-Discord\n\n:small_blue_diamond: **What is server boosting?**\nBy boosting a server, the user gets a special badge that identifies them as a booster and also get a special role designated in the server.The server is given boosting perks like more emoji slots and animated server icon, the booster also gets perks such as a private channel and vc.\n\n:small_blue_diamond: **I have some more questions where should I ask them?**\nSend a DM to <@575252669443211264>, and an Admin or Mod will get in touch with you",colour=discord.Colour.purple())
  await ctx.send(embed=embed)


#RULES

@client.command(aliases=['rules'])
async def rule(ctx):
  #check check check give the modmail id
  embed=discord.Embed(title="RULES AND GUIDELINES:",description="Please read through the rules which are to be followed while interacting in the server -\n\n**1. NSFW/NSFL**\nNo amount of nudity will be accepted in the chats, directly either in the form of images, GIFs and texts, or indirectly in the form of links to another sites. Links to a cancerous websites or other website for harassment like tapping IP address or not wanting to close easily are grounds for instant ban.\n\n**2. Raids or spam**\nExtreme spamming in the chats will NOT be tolerated. Any user found to be participating in raiding or mass spamming will receive an immediate ban.\n\n**3. Behave nicely**\nMembers who are unreasonably or excessively rude to a certain member of group will be met with a warning. We understand that the use of vulgar and inappropriate language can sometimes help you emphasize the point you are trying to make, but overuse of language or remarks (determined by the discretion of the staff) will not be tolerated. We have strict intolerance for members showing genuine signs of homophobia, racism, or any discrimination towards certain groups.\n\n**4. Pings**\nPinging any member (not just the staff) without any reason whatsover is grounds for a warning. This includes spam pinging. Do not ping Owner or Staff who do not want to be pinged.\n\n**5. Nickname / Usernames/Profile Pictures**\nNo use of special font for Nicknames/Usernames. No blank, inappropriate, offensive or sexually explicit nicknames are allowed. Same goes for profile pictures.\n\n**6. The Staff have the final say in decisions enforced as per the rules**\nStaff decision are considered final. If you attempt to circumvent any moderation action such as mutes via any method, you will be banned. Disagreeing with staff decisions are allowed but you may not publicly argue about it in the server. Discuss the disagreement in the DMs. Do not go around asking them for roles, if you do you are just lowering your chances of getting one.\n\n**7. Please conduct yourselves in accordance with Discord's ToS**\nAll members are expected to absolutely abide by the Discord TOS at all times, they can be found here - [Discord Community Guidelines](https://discord.com/guidelines).\n\n**8. No Impersonations**\nPlease do not impersonate any Moderator, Administrator or Staff.If you see someone with a name of any big User / Staff , verify the identity and inform the staff.\n\n**9. Common Sense**\nAnything that doesnt fall under the above mentioned rules will most likely fall under this. If you are following common sense you are already doing better than most. There is no need to be a robot and follow every line of this, just follow common decency and mutual respect. If you have a problem with someone who isn't directly a harm to the server then kindly block them and do not engage. If you are witnessing someone violating rules, kindly suggest them or try to stop them from doing so.\n\n**10. Any Issues?**\nIf you have an issue with a member or something is getting out of hand, let us know ASAP through <@modmailuserid>.",colour=discord.Colour.purple())
  await ctx.send(embed=embed)

keep_alive()
client.run('id of your bot')

