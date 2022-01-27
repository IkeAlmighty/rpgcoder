# RPG Coder

uuuiuoiupoiuiuerup
dog booty

### An rpg where you gotta code to do anything lol

# It will consist of:

1. A way for players to join a lobby
2. REST api for interacting with any given lobby
3. lots of stuff that is cool.

## To install dependencies:

Create a virtualenv, activate the virtualenv, and run:

    pip install -r requirements.txt

## To Run the Server in Dev Mode:

    sanic server.app --dev

## To Run the Server in Production Mode:

    sanic server.app

# Gameplay

To start playing the game, send a GET request to

    <server_address>/auth/token

Make sure to provide a username and password

    <server_address>/auth/token?username=&password=

The token response will contain a json object with

    {
      auth_token: { exp: [int] },
      refresh_token:
    }

You can get a new token using the refresh api route:

    <server_address>/auth/refresh?refresh_token=

All other API routes take an auth token as an argument.

# List of Endpoints

    /auth/token
    /auth/refresh
    /auth/signup

    /walk
    /swing
    /kick
    /speak
    /run
    /search
    /dodge
    /sniff
    /listen
    /touch

Each endpoint can be passed an object_id of something in the game world (or no object_id at all) to alter the behavior of the function. Not all arguments are made equally though! If you /kick a palace guard, you are likely to end up in a fight, and then possibily in jail...

# Game Play

As you interact with the game world through the restapi, you will start to realize that the information returned is probably more readable in a non-json format. Good luck creating a nice graphical interface, I'm too lazy to do so lol.
