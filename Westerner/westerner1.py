import discord, os, random

client = discord.Client()

money = []

def Gold(string):
    if string[1] == 'g' or string[1] == 'G':
        g = 0
        for x in range(1, len(string)):
            if string[x] == 'g':
                g += random.randint(1, 6)
            if string[x] == 'G':
                g += random.randint(1, 10)
            if string[x] == '+':
                g += int(string[x:])
                break

        money.append(g)
        return str(g) + 'g'

def Experience(string):
    if string[1] == 'E' or string[1] == 'e':
        experience.append(int(string[2:]))
        return string[2:] + 'xp'

def Note(string):
    if string[1] == '#':
        return '```CSS\n' + string[2:] + '\n```'

@client.event
async def on_ready():
    print('Logged as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('!'):
        try:
            answer = Gold(message.content)
            answer = Experience(message.content)
            answer = Note()
        except:
            pass
        await message.channel.send(answer)

client.run('OTUxMjM5NDgwMzQwMjgzNDcz.YikkzQ.hTdiV1Qu1VzaN303ub08jZxhF20')
