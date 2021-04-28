import json
import base64
import hashlib
from collections import OrderedDict
from quart import url_for
from typing import NamedTuple, Optional, List, Dict
from sqlite3 import Row


class Jukebox(NamedTuple):
    id: str
    title: str
    wallet: str
    sp_user: str
    sp_secret: str
    sp_token: str
    sp_device: str
    sp_playlists: str
    price: int

    @classmethod
    def from_row(cls, row: Row) -> "Jukebox":
        return cls(**dict(row))
