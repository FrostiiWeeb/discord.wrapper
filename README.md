# discord.wrapper
<a href="https://pypi.org/project/discord.wrapper" traget="_blank">
    <img alt="PyPI - Version" src="https://img.shields.io/pypi/v/discord.wrapper">
</a>

<a href="https://pypi.org/project/discord.wrapper" traget="_blank">
	<img alt="PyPI - Downloads" src="https://pepy.tech/badge/discord.wrapper">
</a>

<a href="https://pypi.org/project/discord.wrapper" traget="_blank">
    <img alt="PyPI - Supported Python Versions" src="https://img.shields.io/pypi/pyversions/discord.wrapper.svg">
</a>

An API wrapper for discord wich uses `async` and `await`.

# How to install

```shell
python3 -m pip install discord.wrapper
```

## Bot Example
```python
from discord import wrapper

bot = wrapper.Bot(public_key = "Your Public Key", token="Your Bot Token")

bot.run()
```

## Subclassed Bot

```python
from discord import wrapper

class MyBot(wrapper.Bot):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

bot = MyBot(public_key = "public_key", token="Your Bot Token")

bot.run()
```

## Fore more info, check out the docs.

# Links:
• [Official Support Server](https://discord.gg/Ns5W4pqguE)