import discord
from discord.ext import commands
from discord_slash import SlashCommand
import requests

client = commands.Bot(command_prefix='$')
slash = SlashCommand(client, sync_commands=True)
guild_ids = [722437023981633546]
@client.event
async def on_ready():
        print(f"[!] Initializing...")
        print(f"[!] Initialization complete!")
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="YOU 👁️👄👁️"))


@client.command()
async def embed(ctx):
        msg = ctx.message
        message = ctx.message.content
        member=ctx.message.author
        name=''
        message = message.replace('$embed', '')
        if ctx.message.author.nick != None:
                name = ctx.message.author.nick
        else:
                name = ctx.message.author.name
        await msg.delete()
        roles = member.roles
        roles.reverse()
        top_role = roles[0]
        print(type(top_role.color))
        emb = discord.Embed(description = message,colour=top_role.color)
        emb.set_author(name=name,icon_url=ctx.message.author.avatar_url)
        await ctx.channel.send(embed=emb)



@client.command()
async def news(ctx):
        member = ctx.message.author
        try:
                response = requests.get('https://newsapi.org/v2/top-headlines?country=in&apiKey=6576af9650c7402390715daa3e1f8ae4')
        except:
                await ctx.channel.send('News servers dowm')

        print(response)
        news = response.json()
        print(news)
        head=[]
        desc=[]
        for new in news['articles']:
              head.append(str(new['title']))
              desc.append(str(new['description']))
        roles = member.roles
        roles.reverse()
        top_role = roles[0]
        print(type(top_role.color))
        embed = discord.Embed(title='NEWS with Bot', color= top_role.color)
        n = len(head)
        if n>10:
                n=9
        for i in range(0,n):
                embed.add_field(name=head[i], value=desc[i], inline=True)
        await ctx.channel.send(embed=embed)

@slash.slash(name="embed", guild_ids=guild_ids)
async def em(ctx):
        msg = ctx.message
        message = ctx.message.content
        member = ctx.message.author
        name = ''

        message = message.replace('$embed', '')
        if ctx.message.author.nick != None:
                name = ctx.message.author.nick
        else:
                name = ctx.message.author.name
        await msg.delete()
        roles = member.roles
        roles.reverse()
        top_role = roles[0]
        print(type(top_role.color))
        emb = discord.Embed(description=message, colour=top_role.color)
        emb.set_author(name=name, icon_url=ctx.message.author.avatar_url)
        await ctx.channel.send(embed=emb)

client.run('ODY2NzQxNDY2MDU5MTEyNDc4.YPW95A.wOOwOu5erlaF4hxHMdDKH9zPcXc')

