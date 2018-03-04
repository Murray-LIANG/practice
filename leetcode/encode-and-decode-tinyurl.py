# https://leetcode.com/problems/encode-and-decode-tinyurl

import random
import string

class Codec:

    USABLE_CHAR = string.ascii_letters + '0123456789'
    PREFIX = 'http://tinyurl.com/'

    def __init__(self):
        self.url2code = {}
        self.code2url = {}

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.

        :type longUrl: str
        :rtype: str
        """
        while longUrl not in self.url2code:
            code = ''.join(random.choice(self.USABLE_CHAR) for _ in range(6))
            if code not in self.url2code.values():
                self.url2code[longUrl] = code
                self.code2url[code] = longUrl

        return self.PREFIX + code


    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.

        :type shortUrl: str
        :rtype: str
        """
        return self.code2url[shortUrl[-6:]]



# Your Codec object will be instantiated and called as such:
codec = Codec()
tiny_abc = codec.encode('abc')
print(tiny_abc)
abc = codec.decode(tiny_abc)
print(abc)
tiny_efg = codec.encode('efg')
print(tiny_efg)
efg = codec.decode(tiny_efg)
print(efg)
