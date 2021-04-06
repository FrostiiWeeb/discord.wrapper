# discord.api
<a href="https://pypi.org/project/discord.api" traget="_blank">
    <img alt="PyPI - Version" src="https://img.shields.io/pypi/v/discord.api">
</a>

<a href="https://pypi.org/project/discord.api" traget="_blank">
	<img alt="PyPI - Downloads" src="https://pepy.tech/badge/discord.api">
</a>

<a href="https://pypi.org/project/discord.api" traget="_blank">
    <img alt="PyPI - Supported Python Versions" src="https://img.shields.io/pypi/pyversions/discord.api.svg">
</a>

<a href="https://pypi.org/project/discord.api" traget="_blank">
    <img alt="PyPI - License" src="https://img.shields.io/github/license/FrostiiWeeb/discord.api">
</a>

An api wrapper for discord wich uses `async` and `await`.

# How to install

```shell
python3 -m pip install discord.api
```

## Bot Example
```python
from discord import api

bot = api.Bot(token="Your Bot Token")

bot.run()
```

## Subclassed Bot

```python
from discord import api

class MyBot(api.Bot):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

bot = MyBot(token="Your Bot Token")

bot.run()
```