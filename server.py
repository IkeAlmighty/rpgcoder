from sanic import Sanic
from sanic.response import json
from sanic.response import text

from endpoints import dodge, kick, listen, run, search, sniff, speak, swing, taste, touch, walk

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