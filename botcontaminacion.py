import discord
from discord.ext import commands
import random

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

ideas_reutilizar = {
    "ropa": [
        "Convierte camisetas viejas en trapos",
        "Haz bolsas reutilizables",
        "Fundas para cojines"
    ],
    "botellas": [
        "Macetas",
        "Portalápices",
        "Riego por goteo"
    ]
}

datos = [
    "El 99% de la población mundial respira aire contaminado.",
    "Cada año mueren 7 millones de personas por contaminación del aire.",
    "Más de 8 millones de toneladas de plástico llegan a los océanos cada año.",
    "Una botella de plástico tarda hasta 450 años en degradarse."
]

sabias_que = [
    "Los árboles ayudan a filtrar contaminantes del aire.",
    "El ruido excesivo puede causar estrés y problemas cardíacos.",
    "Los microplásticos ya están en el agua potable."
]

@bot.event
async def on_ready():
    print(f"Bot conectado como {bot.user}")

@bot.command()
async def reutilizar(ctx, *, objeto: str):
    objeto = objeto.lower()
    if objeto in ideas_reutilizar:
        await ctx.send(random.choice(ideas_reutilizar[objeto]))
    else:
        await ctx.send("No tengo ideas para eso todavía ♻️")

@bot.command()
async def dato_contaminacion(ctx):
    await ctx.send(random.choice(datos))

@bot.command()
async def sabias_que(ctx):
    await ctx.send(random.choice(sabias_que))

@bot.command()
async def como_ayudar(ctx):
    await ctx.send(
        "🌱 Puedes ayudar así:\n"
        "- Reduce el uso de plásticos\n"
        "- Usa transporte público o bicicleta\n"
        "- Recicla correctamente\n"
        "- Ahorra energía y agua"
    )



bot.run("Token goes here!")
