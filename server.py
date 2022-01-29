from sanic import Sanic
from sanic.response import json
from sanic.response import text

from endpoints.dodge import dodge 
from endpoints.kick import kick 
from endpoints.listen import listen 
from endpoints.look import look
from endpoints.run import run 
from endpoints.search import search 
from endpoints.sniff import sniff 
from endpoints.speak import speak 
from endpoints.swing import swing 
from endpoints.taste import taste 
from endpoints.touch import touch
from endpoints.walk import walk

app = Sanic("RPG_CODER")

@app.route("/")
async def test(request):
  return text("Welcome to RPG Coder. To begin, send a post request to /signup")

@app.route('/auth/token')
async def authToken(request):
  return json({}) # TODO

@app.route('/auth/refresh')
async def authRefresh(request):
  return json({}) # TODO

app.add_route(dodge, '/dodge')
app.add_route(kick, '/kick')
app.add_route(listen, '/listen')
app.add_route(look, '/look')
app.add_route(run, '/run')
app.add_route(search, '/search')
app.add_route(sniff, '/sniff')
app.add_route(speak, '/speak')
app.add_route(swing, '/swing')
app.add_route(taste, '/taste')
app.add_route(touch, '/touch')
app.add_route(walk, '/walk')

if __name__ == '__main__':
    app.run()