'''
Rose — A utility bot for Project Compass.
'''
import discord
from discord.ext import commands as commandsExt

from . import config
from . import commands
from . import events


class Rose:
    '''
    Initalizes and manages an instance of the bot.
    '''

    def __init__(self, home: str):
        '''
        '''
        self.configManager = config.ConfigManager(home+'/config')
        self.bot = self.configManager.newInstance(commandsExt.Bot)
        self.bot.event(events.on_ready)
        self.bot.event(events.on_command_error)
        self.bot.add_cog(commands.CoreCommands(self.bot))

    def start(self):
        '''
        Login to Discord and begin execution.
        
        .. warning::
        
            This method is blocking. Later versions may initate a terminal
            interface for local management of the bot while it's running.
        '''
        # For now, we're just going to run by using the blocking Bot.run()
        # method. Later on we might switch to using the Bot.start() coroutine
        # as a task and add an interactive mode for monitoring and/or control
        # from the terminal.
        self.bot.run(self.configManager.token())
