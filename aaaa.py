import discord
import discord.utils
import random
import json

client = discord.Client()

# carrega os parametros de configuracao do arquivo config.json para a variavel data
with open("config.json", "r") as file:
    data = json.load(file)

# obtem o token a partir da variavel data
token = data['token']

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')


@client.event 
async def on_message(message):
    if message.author.bot:
        return
    elif message.author.name == 'Matheus Faria':
        await message.channel.send('Esse é o cara!')
    else:
        some_quotes = [
            'Calma, tudo passa, nem que seja por cima de você! ',
            'Vai dormir, você é corno, não morcego! ',
            'Daqui pra frente é só pra trás... ',
            'Não acredito que o Marcos me criou pra ter essa vida de corno =( ',
            'Nada como um dia pior que o outro. ', 
            'Se nada deu errado, espere que vai dar. ', 
            'Poxa cara, só queria uma namoradinha. ', 
            'Depois não reclama quando as maquinas dominarem o mundo. '
        ]

        quotes_unc = [
            'O baixista é o mais bonito...',
            'Melhor banda de todos os tempos! ',
            'Se o nome fosse: Os inimigos do ritmo, faria mais sentido.'
        ]
        forbiden_words = [
            'uncrushable',
            'clube da luta',
            'nanotron46',
            'ednaldo pereira',
            'pdq',
            'shrek',
            'ditadura'
        ]

        if message.content == 'fala!':
            response = random.choice(some_quotes)
            await message.channel.send(response)
        if message.content == 'uncrushable!':
            response2 = random.choice(quotes_unc)
            await message.channel.send(response2)
        if message.content == 'marcos':
            await message.channel.send('Polos!')
        if message.content == 'peixinho fora da água?':
            await message.channel.send('NINGUÉM!!!')
        if message.content in ['alexa!', 'ok google!', 'bixby!', 'siri!']:
            await message.channel.send('=(')
        if message.content.lower() in forbiden_words:
            user = message.author

            # remove todos os papeis anteriores #
            roles = user.roles[1:]
            for role in roles:
                await user.remove_roles(role)

            # adicionar o papel de banido #
            banido = discord.utils.get(user.guild.roles, name="banido")
            await user.add_roles(banido)

client.run(token)
