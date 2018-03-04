class SegmentTree(object):
    def __init__(self, array):
        self.array = array

        # All nodes are stored in an array.
        self.nodes = [0 for _ in 2 * range(len(array) + 2)]
        print(self.nodes)
        self.construct(0, len(array) - 1, 0)

    @staticmethod
    def get_mid(si, ei):
        return si + (ei - si) / 2

    def construct(self, si, ei, ci):
        if si == ei:
            self.nodes[ci] = self.array[si]
            return self.nodes[ci]

        mi = SegmentTree.get_mid(si, ei)
        self.nodes[ci] = (self.construct(si, mi, 2 * ci + 1) +
                          self.construct(mi + 1, ei, 2 * ci + 2))
        return self.nodes[ci]

    def get_sum(self, si, ei, sq, eq, ci):
        if si >= sq and ei <= eq:
            return self.nodes[ci]

        if ei < sq or  si > eq:
            return 0

        print(si, ei, sq, eq, ci)
        mi = SegmentTree.get_mid(si, ei)
        return (self.get_sum(si, mi, sq, eq, 2 * ci + 1) +
                self.get_sum(mi + 1, ei, sq, eq, 2 * ci + 2))

    def query(self, qs, qe):
        return self.get_sum(0, len(self.array) - 1, qs, qe, 0)



if __name__ == '__main__':
    st = SegmentTree([1, 3, 5, 7, 9, 11])
    print(st.nodes)

    print(st.query(1, 3))


