                    #Data Importing
import discord
from discord.ext import commands
import os
from keep_alive import keep_alive
import colorama
from colorama import Fore, Style
import random
import time

#_____________________________________________________________
                    #Naming Variables

bot = commands.Bot(command_prefix="!") 
#Sets what symbol activates command

#_____________________________________________________________

     # Notification for bot connecting to discord's server

@bot.event 
async def on_connect():
  print(Fore.CYAN + "Bot is online") 
  #"Fore" command to choose print color in console

#_____________________________________________________________

                    # Bot Commands  

@bot.command() #All lowercase command
async def choosegame(ctx):
  await ctx.send("Searching Library...")
  with open("game_cat.txt", "r") as f: #Pulls data from list
      gameList = f.read()
      chosenList = list(map(str, gameList.splitlines()))
      time.sleep(2) # two second delay before printing game.
      await ctx.send("✨ You should play, " + random.choice(chosenList) + " ✨")

@bot.command() #Capital "C" command
async def Choosegame(ctx):
  await ctx.send("Searching Library...")
  with open("game_cat.txt", "r") as f: #Pulls data from list
      gameList = f.read()
      chosenList = list(map(str, gameList.splitlines()))
      time.sleep(2) # two second delay before printing game.
      await ctx.send("✨ You should play, " + random.choice(chosenList) + " ✨")

@bot.command()
async def ChooseGame(ctx): #Capital "C" & "G" Command
  await ctx.send("Searching Library...")
  with open("game_cat.txt", "r") as f: #Pulls data from list
      gameList = f.read()
      chosenList = list(map(str, gameList.splitlines()))
      time.sleep(2) # two second delay before printing game.
      await ctx.send("✨ You should play, " + random.choice(chosenList) + " ✨")

@bot.command()
async def CHOOSEGAME(ctx): # All Capital Command
  await ctx.send("Searching Library...")
  with open("game_cat.txt", "r") as f: #Pulls data from list
      gameList = f.read()
      chosenList = list(map(str, gameList.splitlines()))
      time.sleep(2) # two second delay before printing game.
      await ctx.send("✨ You should play, " + random.choice(chosenList) + " ✨")

#___________________________________________________________
                        #Server Stuff
    
keep_alive() #Keeps Server Alve

my_secret = os.environ['DISCORD_TOKEN'] #Grabs Token from "My Secret File"
bot.run(my_secret) #Runs token from "My Secret File"
