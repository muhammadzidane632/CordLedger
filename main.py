import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
import database

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)



@bot.event
async def on_ready():
    print(f'Bot {bot.user} Telah Online!')
    database.init_db()
    print("Database Siap digunakan ")

@bot.command()
async def masuk(ctx, amount: float, *,description: str):
    user_id = ctx.author.id
    database.add_transactions(user_id,'pemasukan',amount,description)
    await ctx.send(f'Berhasil Mencatt Pemasukan : Rp{amount} ({description})')

@bot.command()
async def keluar(ctx, amount:float, *, description:str):
    user_id = ctx.author.id
    database.add_transactions(user_id,'pengeluaran',amount,description)
    await ctx.send(f'Berhasil Mencatat Pengeluaran : Rp{amount} ({description})')

if __name__ == '__main__':
    bot.run(TOKEN)