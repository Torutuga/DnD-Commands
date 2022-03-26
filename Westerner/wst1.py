import discord, os, random

client = discord.Client()

prepare_quit = False

money = []
experience = []
notes = []

def Gold(string):
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
    experience.append(int(string[2:]))
    return string[2:] + 'xp'

def Note(string):
    return '```CSS\n' + string[2:] + '\n```'

def Totals():
    total_xp = 'Experience:' + str(sum(experience)) + '\n'
    total_g = 'Gold:' + str(sum(money)) + '\n'
    return '```CSS\n' + total_xp + total_g + '```'

def Quit():
    global prepare_quit

    if not prepare_quit:
        prepare_quit = True
        return 'Resetting? Type !ResetYES'
    if prepare_quit:
        money.clear()
        experience.clear()
        notes.clear()
        prepare_quit = False
        return 'Reset Complete'

@client.event
async def on_ready():
    print('Logged as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('!'):
        if message.content != '!resetYES':
            prepare_quit = False
        if message.content[1] == 'g' or message.content[1] == 'G':
            answer = Gold(message.content)
        if message.content[1] == 'e' or message.content[1] == 'E':
            answer = Experience(message.content)
        if message.content[1] == '#':
            answer = Note(message.content)
        if message.content == '!total':
            answer = Totals()
        if message.content == '!reset' or message.content == '!resetYES':
            answer = Quit()
        await message.channel.purge(limit=1)
        await message.channel.send(answer)

dmchannel = discord.DMChannel 

@client.event
async def Clean():
    for message in dmchannel.history(limit=100):
        if message.author == client.user:
            await message.delete()

client.run('OTUxMjM5NDgwMzQwMjgzNDcz.YikkzQ.hTdiV1Qu1VzaN303ub08jZxhF20')
