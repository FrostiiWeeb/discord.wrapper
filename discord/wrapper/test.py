import sys
from pathlib import Path
sys.path[0] = str(Path(sys.path[0]).parent)
from .bot import Bot

bot = Bot(token="Nzg0MTIyMDYxMjE5OTU0NzA4.X8kskw.7HcfjZ-onzkEeTPZ0KWTyCLw7IY")

if __name__ == "__main__":
	bot.run()