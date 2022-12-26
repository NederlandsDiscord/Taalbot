import sys
sys.path.insert(0, 'src')


import glob
import os
import pytest_asyncio
import discord.ext.test as dpytest
from taalbot import Taalbot
from guildconfig import *


@pytest_asyncio.fixture
async def bot():
    # Setup the bot for testing.
    bot = Taalbot()
    await bot._async_setup_hook()
    await bot.add_cogs()
    
    # Add clien (bot) to the config and retrieve it for further steps.
    dpytest.configure(bot, 0, 0, 0)
    config = dpytest.get_config()
    
    # Create the guild.
    guild = dpytest.back.make_guild(name='Nederlands Leren')
    
    # Create the channels.
    greeting_channel = dpytest.back.make_text_channel(name=GREETING_CHANNEL, guild=guild)
    log_channel = dpytest.back.make_text_channel(name=LOGGING_CHANNEL, guild=guild)
    channels = [greeting_channel, log_channel]
    
    # Create roles.
    dpytest.back.make_role(name=ROLE_NAME_STAFF, guild=guild)
    dpytest.back.make_role(name=ROLE_NAME_NATIVE, guild=guild)
    dpytest.back.make_role(name=ROLE_NAME_NL, guild=guild)
    dpytest.back.make_role(name=ROLE_NAME_BE, guild=guild)
    dpytest.back.make_role(name=ROLE_NAME_SA, guild=guild)
    dpytest.back.make_role(name=ROLE_NAME_LEVEL_O, guild=guild)
    dpytest.back.make_role(name=ROLE_NAME_LEVEL_A, guild=guild)
    dpytest.back.make_role(name=ROLE_NAME_LEVEL_B, guild=guild)
    dpytest.back.make_role(name=ROLE_NAME_LEVEL_C, guild=guild)
    dpytest.back.make_role(name=ROLE_NAME_WVDD, guild=guild)
    dpytest.back.make_role(name=ROLE_NAME_SESSIONS, guild=guild)
    dpytest.back.make_role(name=ROLE_NAME_CORRECT_ME, guild=guild)
    dpytest.back.make_role(name=ROLE_NAME_BN, guild=guild)

    # Create members.
    test_user = dpytest.back.make_user(username='ManualTestUser', discrim=1)
    test_member = dpytest.back.make_member(user=test_user, guild=guild, nick='ManualTestNickName')
    members = [test_member]
    
    # Assign the test setup to the config.
    config.guilds.append(guild)
    config.channels.append(channels)
    config.members.append(members)
    
    return bot


@pytest_asyncio.fixture(autouse=True)
async def cleanup():
    yield
    await dpytest.empty_queue()


def pytest_sessionfinish(session, exitstatus):
    print("\n-------------------------\nClean dpytest_*.dat files")
    fileList = glob.glob('./dpytest_*.dat')
    for filePath in fileList:
        try:
            os.remove(filePath)
        except Exception:
            print("Error while deleting file: ", filePath)
