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

<a href="https://pypi.org/project/discord.wrapper" traget="_blank">
    <img alt="PyPI - License" src="https://img.shields.io/github/license/FrostiiWeeb/discord.wrapper">
</a>

An wrapper wrapper for discord wich uses `async` and `await`.

# How to install

```shell
python3 -m pip install discord.wrapper
```

## Bot Example
```python
from discord import wrapper

bot = wrapper.Bot(token="Your Bot Token")

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