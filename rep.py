import discord
from discord.ext import commands
import requests
import time


class User(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.time_var = time.time()
        self.guild_ids = [722437023981633546]
        self.c = 0

    @commands.Cog.listener()
    async def on_ready(self):
        print('BOT RUNNING')

    @commands.Cog.listener()
    async def on_message(self,message):
        server= message.author.guild
        print(message.content)
        if (time.time()-self.time_var)>900:
            self.time_var=time.time()
            msg = self.get_quote()
            emb = discord.Embed(title='A word from the wise',description=msg,colour=discord.Colour.random())
            channel= discord.utils.get(server.channels, name='general')
            await channel.send(embed=emb)
    
    @commands.command()
    async def embed(self,ctx):
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

    @commands.command()
    async def motivation(self, ctx):
        data = self.get_quote()
        print(data)
        emb = discord.Embed(description=data,colour=discord.Colour.random())
        await ctx.channel.send(embed=emb)

    @commands.command()
    async def news(self,ctx):
        member = ctx.message.author
        try:
            response = requests.get(
                'https://newsapi.org/v2/top-headlines?country=in&apiKey=6576af9650c7402390715daa3e1f8ae4')
        except:
            await ctx.channel.send('News servers dowm')

        print(response)
        news = response.json()
        print(news)
        head = []
        desc = []
        for new in news['articles']:
            head.append(str(new['title']))
            desc.append(str(new['description']))
        roles = member.roles
        roles.reverse()
        top_role = roles[0]
        print(type(top_role.color))
        embed = discord.Embed(title='NEWS with WALL•E', color=top_role.color)
        n = len(head)
        if n > 10:
            n = 9
        for i in range(0, n):
            embed.add_field(name=head[i], value=desc[i], inline=True)
        await ctx.channel.send(embed=embed)


    def get_quote(self):
        api = 'http://api.quotable.io/random'
        content = requests.get(api).json()
        quote = content['content']
        author = content['author']
        print((quote+'\n'+'\n'+'-'+author))
        return (quote+'\n'+'\n'+'-'+author)
