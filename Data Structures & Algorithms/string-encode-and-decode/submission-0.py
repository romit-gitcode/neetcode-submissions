class Solution:

    def encode(self, strs: List[str]) -> str:
        A = []
        for s in strs:
            A.append(str(len(s)))
            A.append('#')
            A.append(s)
        return "".join(A)



    def decode(self, s: str) -> List[str]:
        A = []
        i = 0
        while i< len(s):
            j = i
            while s[j] !='#':
                j+=1
            length = int(s[i:j])
            i = j+1
            j = i + length
            A.append(s[i:j])
            i = j
        return A

