from discord import RawReactionActionEvent, TextChannel, Message
from discord.ext import commands


class AutoPin:
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        print('Addon "{}" loaded'.format(self.__class__.__name__))

    async def on_raw_reaction_add(self, ev: RawReactionActionEvent):
        if str(ev.emoji) == "📍":  # Emoji which should be used to AutoPin
            chan: TextChannel = self.bot.get_channel(ev.channel_id)
            mes: Message = await chan.get_message(ev.message_id)
            for reaction in mes.reactions:
                if str(reaction.emoji) == "📍" and reaction.count >= 2:  # Amount of Reactions needed for AutoPin
                    await mes.pin()

    async def on_raw_reaction_remove(self, ev: RawReactionActionEvent):
        if str(ev.emoji) == "📍":  # Emoji which should be used to AutoPin
            chan: TextChannel = self.bot.get_channel(ev.channel_id)
            mes: Message = await chan.get_message(ev.message_id)
            for reaction in mes.reactions:
                if str(reaction.emoji) == "📍" and reaction.count < 2:  # Amount of Reactions needed for AutoPin
                    await mes.unpin()


def setup(bot):
    bot.add_cog(AutoPin(bot))
