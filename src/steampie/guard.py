import hmac
import struct
import time
from base64 import b64decode, b64encode
from hashlib import sha1
from typing import Literal


def generate_one_time_code(shared_secret: str, timestamp: float | None = None) -> str:
    if timestamp is None:
        timestamp = time.time()

    time_buffer = struct.pack(">Q", int(timestamp) // 30)
    time_hmac = hmac.new(b64decode(shared_secret), time_buffer, digestmod=sha1).digest()
    begin = ord(time_hmac[19:20]) & 0xF
    full_code = struct.unpack(">I", time_hmac[begin : begin + 4])[0] & 0x7FFFFFFF
    chars = "23456789BCDFGHJKMNPQRTVWXY"
    code = []

    for _ in range(5):
        full_code, i = divmod(full_code, len(chars))
        code.append(chars[i])

    return "".join(code)


def generate_confirmation_key(
    identity_secret: str,
    tag: Literal["list", "accept", "reject"],
    timestamp: float | None = None,
) -> str:
    if not identity_secret:
        raise ValueError("identity_secret cannot be empty!")

    if timestamp is None:
        timestamp = time.time()

    buffer = struct.pack(">Q", int(timestamp)) + tag.encode("ascii")
    buffer_hmac = hmac.new(b64decode(identity_secret), buffer, digestmod=sha1).digest()

    return b64encode(buffer_hmac).decode("ascii")
