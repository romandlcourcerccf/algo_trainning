class Codec:
    def __init__(self):
        self._encode_map = {}
        self._decode_map = {}
        self._base = "http://tinyurl.com/"

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL."""

        if longUrl not in self._encode_map:
            short_url = self._base + str(len(self._encode_map) + 1)
            self._encode_map[longUrl] = short_url
            self._decode_map[short_url] = longUrl

        return self._encode_map[longUrl]

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL."""
        return self._decode_map[shortUrl]


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
