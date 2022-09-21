import discord
import random
import requests
from discord.ext import commands
import argparse

TOKEN = 'OTc1NjcyODE0NzQyOTU4MTEw'
TOKEN2 = '.GRlvah.2zlf'
TOKEN3 = 'Jt8Js0A3'
__tOKEN4 = '-pppHx0clY'
TOKEN5 = '--qwwrGEadasd11'
Manifushi = 'q4JlAcoRY7DZ9RnY'
TOKEN6 = 'wejfi481321'


# Ver.2.0 with 4 models
# coserOnly = 0 
# jojo = 1
# protitan = 2
# gyatePro = 3


client = discord.Client()
def real2jojo(filePath, savePath="test.png"):
    requestID = random.randint(100000,999999)

    @client.event
    async def on_ready():
        try:
            channel = client.get_channel(975673523886522379)
            await channel.send(content=f"$R::B2A>{requestID}$1",file=discord.File(filePath))

        except Exception as e:
            await client.close()
            print("The client is closed.")

    @client.event
    async def on_message(message):
        if(message.content == f'$I>{requestID}'):
            urls = message.attachments[0].url
            myfile = requests.get(urls)
            open(savePath,'wb').write(myfile.content)
            await client.close()
            print("The client is closed.")
        
    client.run(TOKEN+TOKEN2+TOKEN3+__tOKEN4+Manifushi)
    
    return savePath


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--savepath',default="test_out.png", type=str)
    parser.add_argument('--path',default ="test.png" , type=str)

    args = parser.parse_args()

    real2jojo(args.path, savePath = args.savepath)