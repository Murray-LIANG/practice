class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        t = []
        for p in filter(None, path.split(r'/')):
            if p == '.':
                continue
            elif p == '..':
                if not t:
                    continue
                t.pop()
            else:
                t.append(p)
        return '/' + '/'.join(t)


if __name__ == '__main__':
    datas = [
        ('/home/', '/home'),
        ('/a/./b/../../c/', '/c'),
        ('/a/../../c/', '/c'),
        ('/a/./b///../c/../././../d/..//../e/./f/./g/././//.//h///././/..///',
         '/e/f/g'),
    ]

    for i, (path, expected) in enumerate(datas, 1):
        print('>>> Test #{} <<<'.format(i))
        print('path: {}.'.format(path))
        result = Solution().simplifyPath(path)
        print('Result: {}. Expected:{}. {}.'.format(
            result, expected,
            'PASS' if result==expected else 'FAIL'))
