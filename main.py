from discord.ext import commands
from rep import User

client = commands.Bot(command_prefix='$')



@client.event
async def on_ready():
        print(f"[!] Initializing...")
        print(f"[!] Initialization complete!")
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="YOU 👁️👄👁️"))



client.add_cog(User(client))
client.run('ODY2NzQxNDY2MDU5MTEyNDc4.YPW95A.wOOwOu5erlaF4hxHMdDKH9zPcXc')

