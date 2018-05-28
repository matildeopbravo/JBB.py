from __future__ import print_function
import discord
import pokebase as pb
from discord.ext import commands
from random import randint

import datetime


class Pokemon():
    
    def __init__(self, bot):
        self.bot = bot


    @commands.command(pass_context=True)
    async def pokedex(self, ctx, name):

        pokemon = pb.pokemon(name)

        #print(pk)


        embed=discord.Embed(title = pokemon.name, color=0xfbfb00)
        embed.set_thumbnail(url = 'https://vignette.wikia.nocookie.net/clubpenguin/images/4/4c/Pokeball.png/revision/latest?cb=20130901024704')
        embed.add_field(name = ":scales:Weight"          , value = pokemon.weight   , inline=True)
        embed.add_field(name = ":triangular_ruler:Height", value = pokemon.height   , inline=True)
        embed.add_field(name = ":dividers:Types"         , value = getType(pokemon) , inline=False)
        await self.bot.say(embed=embed)


def getType(pokemon):
    r = ''
    types = pokemon.types
    for i in range(0,len(types)):
        r += types[i].type.name + ', '
    return (r[:-2])

#[
#{'type':
#    {'url': 'https://pokeapi.co/api/v2/type/3/',
#     'name': 'flying'},
#     'slot': 2},
#{'type':
#    {'url': 'https://pokeapi.co/api/v2/type/4/',
#     'name': 'poison'},
#     'slot': 1}
#     ]
        



def setup(bot):
    bot.add_cog(Pokemon(bot))