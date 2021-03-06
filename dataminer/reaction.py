from discord.ext import commands
from datetime import datetime
from . import utcnow
import unicodedata

"""
COLLECT DATA FROM REACTIONS !
"""

class Reaction(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        """EVENT IS CALLED WHEN A USER ADDS AN REACTION"""
        if not reaction.message.guild:
            return
        if user.bot:
            return
        _roles = []
        for role in user.roles:
            _roles.append(str(role))
        emote = unicodedata.name(reaction.emoji[0])
        push_data = {"reactionname": str(emote.lower()), "timestamp": utcnow, "roles": _roles, "channelid": str(reaction.message.channel.id)}
        # push the date into the database
        self.bot.db.update({"_id": str(reaction.message.guild.id)}, {"$push": {"reaction": push_data}})
        del _roles
        return

def setup(bot):
    bot.add_cog(Reaction(bot))