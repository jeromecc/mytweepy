# Tweepy
# Copyright 2009-2022 Joshua Roesslein
# See LICENSE for details.

"""
Tweepy.asynchronoous

Asynchronous interfaces with the Twitter API
"""

try:
    import aiohttp
    import async_lru
    import oauthlib
except ModuleNotFoundError:
    from mytweepy.errors import TweepyException
    raise TweepyException(
        "tweepy.asynchronous requires aiohttp, async_lru, and oauthlib to be "
        "installed"
    )

from mytweepy.asynchronous.streaming import AsyncStream, AsyncStreamingClient
from mytweepy.asynchronous.client import AsyncClient
