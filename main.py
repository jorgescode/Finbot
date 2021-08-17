import os
import discord
import random
from keep_alive import keep_alive

token = os.environ['DISCORD_TOKEN']

client = discord.Client()


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    content = message.content
    new_content = ''
    if content.lower().startswith('finbot'):
        content = content[6:]
        for character in content:
            if character == ' ':
                new_content += ' '
                continue

            if not character.isalpha():
                continue

            coin_flip = random.choice([0, 1])
            if coin_flip:
                if character.isupper():
                    new_content += character.lower()
                else:
                    new_content += character.upper()
            else:
                new_content += character
        await message.channel.send(new_content)

    if 'we have to work as a unit' in content.lower():
        await message.channel.send('suck my unit')


keep_alive()

client.run(token)
