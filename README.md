# discord.wrapper
<a href="https://pypi.org/project/discord.wrapper" traget="_blank">
    <img alt="PyPI - Version" src="https://img.shields.io/pypi/v/discord.wrapper">
</a>

<a href="https://pypi.org/project/discord.wrapper" traget="_blank">
	<img alt="PyPI - Downloads" src="https://pepy.tech/badge/discord.wrapper">
</a>

<a href="https://pypi.org/project/discord.wrapper" traget="_blank">
    <img alt="PyPI - Supported Python Versions" src="https://img.shields.io/pypi/pyversions/discord.wrapper.svg">
</a>s

An API wrapper for discord wich uses `async` and `await` api.

# How to install

```shell
python3 -m pip install discord.wrapper
```

## Bot Example
```python
import sys
from discord import wrapper

bot = wrapper.Bot(token="your bot token")

@bot.event()
async def on_ready():
	print("Ready!")

if __name__ == "__main__":
	bot.run()
```

## Subclassed Bot

```python
from discord import wrapper

class MyBot(wrapper.Bot):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

bot = MyBot(token="Your Bot Token")

bot.run()
```

## For more info, check out the docs.

# Links:
• [Official Support Server](https://discord.gg/Ns5W4pqguE)