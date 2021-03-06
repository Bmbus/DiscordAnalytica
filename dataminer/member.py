from discord.ext import commands
from . import utcnow

"""
COLLECT DATA IF A USER JOIN/LEAVES A SERVER
"""

class Member(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        push_data = {"timestamp": utcnow}
        self.bot.db.update({"_id": str(member.guild.id)}, {"$push": {"userjoins": push_data}})
        return

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        push_data = {"timestamp": utcnow}
        self.bot.db.update({"_id": str(member.guild.id)}, {"$push": {"userleave": push_data}})
        return


def setup(bot):
    bot.add_cog(Member(bot))