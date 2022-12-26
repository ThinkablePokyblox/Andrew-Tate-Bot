# Imports
import interactions
import requests
from flask import Flask
from threading import Thread
import json
# Setup
token = ""
file = open("Token.json")
fileJson = json.load(file)
token = fileJson["TOKEN"]
print(token)
file.close()
bot = interactions.Client(token=token)
# Server
app = Flask(__name__)
@app.route('/')
def wakeup():
    print("Wakeup page requested.")
    return "Wake up command recieved..."
def Server():
    app.run(host='0.0.0.0', port=8080)
# Commands
button = interactions.Button(
    style=interactions.ButtonStyle.PRIMARY,
    label="Another Quote?",
    custom_id="Quote"
)
@bot.command(
    name="quote",
    description="Will give you a quote from the Top G (NOTE: Some quotes may offend some people)",
)
@bot.component("Quote")
async def quote(ctx: interactions.CommandContext):
    QuoteReq = requests.get("https://www.tateapi.com/api/quote")
    await ctx.send(QuoteReq.json()["quote"],components=button)
    ctx.message.components[0].components[0].disabled = True
# Start
def startBot():
  t = Thread(target=Server)
  t.start()
  bot.start()
startBot()