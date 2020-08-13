# https://leetcode.com/problems/iterator-for-combination/

# generting all combinations (sorted) with bit masks

class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.comb = []
        self.idx = 0
        for b in range(2**len(characters)):
            bb = bin(b)[2:][::-1]
            if bb.count('1') == combinationLength:
                # print(bb)
                comb_str = ""
                for i, cb in enumerate(bb):
                    if cb == '1':
                        comb_str = comb_str + characters[i]
                self.comb.append(comb_str)
                
        self.comb.sort()
        # print(self.comb)
                        

    def next(self) -> str:
        idx_cop = self.idx
        self.idx += 1
        return self.comb[idx_cop]
        

    def hasNext(self) -> bool:
        if self.idx >= len(self.comb):
            return False
        return True
        


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()