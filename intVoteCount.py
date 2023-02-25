
class intVoteCount:
    def intVoteCountTrans(self, a):
        chr, k, count = a[len(a) - 1], 0, 1
        a = a[:len(a) - 1:] if a[len(a) - 1] == "M" or a[len(a) - 1] == "K" else a

        for i in range(len(a)):
            if a[i] == ".":
                count = (len(a) - 1 - i) * 10
                k = int(a[:i:] + a[i + 1::])
                return int(k / count * (1000000 if chr == "M" else 1000))
            elif "." not in a:
                return int(int(a) * (1000000 if chr == "M" else 1000))
        return int(a)