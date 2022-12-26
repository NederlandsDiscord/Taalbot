import pytest
import discord.ext.test as dpytest
from guildconfig import GREETING_CHANNEL


@pytest.mark.asyncio
async def test_greeting(bot):
    _ = await dpytest.member_join()
    #assert dpytest.verify().message().contains().content("Welcome ")
