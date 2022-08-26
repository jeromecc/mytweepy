# Tweepy
# Copyright 2009-2022 Joshua Roesslein
# See LICENSE for details.

"""
Tweepy Twitter API library
"""
__version__ = '4.10.1'
__author__ = 'Joshua Roesslein'
__license__ = 'MIT'

from mytweepy.api import API
from mytweepy.auth import (
    AppAuthHandler, OAuthHandler, OAuth1UserHandler, OAuth2AppHandler,
    OAuth2BearerHandler, OAuth2UserHandler
)
from mytweepy.cache import Cache, FileCache, MemoryCache
from mytweepy.client import Client, Response
from mytweepy.cursor import Cursor
from mytweepy.errors import (
    BadRequest, Forbidden, HTTPException, NotFound, TooManyRequests,
    TweepyException, TwitterServerError, Unauthorized
)
from mytweepy.list import List
from mytweepy.media import Media
from mytweepy.pagination import Paginator
from mytweepy.place import Place
from mytweepy.poll import Poll
from mytweepy.space import Space
from mytweepy.streaming import (
    Stream, StreamingClient, StreamResponse, StreamRule
)
from mytweepy.tweet import ReferencedTweet, Tweet
from mytweepy.user import User

# Global, unauthenticated instance of API
api = API()
