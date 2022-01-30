from sanic.response import json
from .world.players import get_player_position
from .world.players import get_player_sound_sensitivity
from .world.players import get_players_in_radius
from .world.wildlife import get_fauna_in_radius
from .world.wildlife import get_flora_in_radius

def listen(request): 
  player_id = request.args.playerId
  x, y = get_player_position(player_id)
  radius = get_player_sound_sensitivity(player_id)

  flora = get_flora_in_radius(x, y, radius)
  fauna = get_fauna_in_radius(x, y, radius)
  players = get_players_in_radius(x, y, radius)

  return json({ 'flora': flora, 'fauna': fauna, 'players': players })
  
