class Solution(object):
    def validIPAddress(self, IP):
        """
        :type IP: str
        :rtype: str
        """
        if '.' in IP and ':' not in IP:
            # Could be an IPv4.
            def valid_v4(x):
                if not x.strip():
                    return False
                if filter(lambda c:
                          (ord(c) not in range(ord('0'), ord('9') + 1)),
                          x):
                    return False
                return ((int(x) == 0 and len(x) == 1)
                        or (not x.startswith('0') and int(x) in range(1, 256)))

            groups = IP.split('.')
            if len(groups) != 4:
                return 'Neither'
            groups = filter(valid_v4, groups)
            return 'IPv4' if len(groups) == 4 else 'Neither'

        elif '.' not in IP and ':' in IP:
            # Could be an IPv6.
            def valid_v6(x):
                if not x:
                    return False
                if len(x) > 4:
                    return False
                if filter(lambda c:
                          (ord(c) not in (range(ord('a'), ord('f') + 1) +
                                          range(ord('A'), ord('F') + 1) +
                                          range(ord('0'), ord('9') + 1))),
                          x):
                    return False
                return True
            groups = IP.split(':')
            if len(groups) != 8:
                return 'Neither'
            groups = filter(valid_v6, groups)
            return 'IPv6' if len(groups) == 8 else 'Neither'

        return 'Neither'

if __name__ == '__main__':
    datas = [
        ('111.111.111.111', 'IPv4'),
        ('011.111.111.111', 'Neither'),
        ('111.111.111.00', 'Neither'),
        ('111.111.111.0', 'IPv4'),
        ('111.111.111.255', 'IPv4'),
        ('111.111.111.256', 'Neither'),
        ('111.111.111', 'Neither'),
        ('111.111.111.111.111', 'Neither'),
        ('111.111.111.', 'Neither'),
        ('111.111.111.111.', 'Neither'),
        ('2001:0db8:85a3:0:0:8A2E:0370:7334', 'IPv6'),
        ('02001:0db8:85a3:0:0:8A2E:0370:7334', 'Neither'),
        ('20019:0db8:85a3:0:0:8A2E:0370:7334', 'Neither'),
        ('200%:0db8:85a3:0:0:8A2E:0370:7334', 'Neither'),
        ('2001:0db8::::8A2E:0370:7334', 'Neither'),
        ('2001:db8:85a3:0::8a2E:0370:7334', 'Neither'),
    ]

    for i, (IP, expected) in enumerate(datas, 1):
        print('>>> Test #{} <<<'.format(i))
        print('IP: {}.'.format(IP))
        result = Solution().validIPAddress(IP)
        print('Result: {}. Expected: {}. {}.'.format(
            result, expected,
            'PASS' if result==expected else 'FAIL'))
