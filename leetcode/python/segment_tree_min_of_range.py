class SegmentTree(object):
    def __init__(self, array):
        self.array = array

        self.nodes = [0 for _ in range(2 * len(self.array) + 1)]
        self.construct(0, len(self.array) - 1, 0)

    @staticmethod
    def get_mid(si, ei):
        return si + (ei - si) / 2

    def construct(self, si, ei, ci):
        print(si, ei, ci)
        if si == ei:
            result = self.array[si]
        else:
            mid = SegmentTree.get_mid(si, ei)
            result = min(self.construct(si, mid, 2 * ci + 1),
                         self.construct(mid + 1, ei, 2 * ci + 2))
        self.nodes[ci] = result
        return self.nodes[ci]

    def get_min(self, si, ei, sq, eq, ci):
        if sq <= si and ei <= eq:
            return self.nodes[ci]

        if si > eq or ei < sq:
            return 2 * 32

        mid = SegmentTree.get_mid(si, ei)
        return min(self.get_min(si, mid, sq, eq, 2 * ci + 1),
                   self.get_min(mid + 1, ei, sq, eq, 2 * ci + 2))

    def query(self, sq, eq):
        return self.get_min(0, len(self.array) - 1, sq, eq, 0)


if __name__ == '__main__':
    st = SegmentTree([3, 7, 5, 4, 9, 1])
    print(st.nodes)

    print(st.query(1, 3))
