from mctools import RCONClient  # Import the RCONClient

HOST = '0.0.0.0'  # Hostname of the Minecraft server
PORT = 25575  # Port number of the RCON server

# Create the RCONClient:

rcon = RCONClient(HOST, port=PORT)

# Login to RCON:

if rcon.login("password"):

    # Send command to RCON - broadcast message to all players:

    resp = rcon.command("say RCON Live!")
    print(resp)

print("Done")

def sendCommand(command):
    if rcon.login("password"):
        resp = rcon.command(command)
        return resp
    else:
        return "Couldn't login"