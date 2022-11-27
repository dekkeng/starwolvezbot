from time import sleep
from player import Player


sleep(2)
print("Start Starwolvez Bot!")
player = Player()

try:
    player.start()
except Exception as e:
    player.log(None, e)
    pass