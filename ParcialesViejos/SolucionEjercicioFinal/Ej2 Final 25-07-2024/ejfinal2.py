def maximo(l: list[int]) -> int:
    curr_max: int = l[0]
    for num in l:
        if num > curr_max:
            curr_max = num
    return curr_max

def maximoPorSubseq(s1: list[int], s2: list[int]) -> list[int]:
    res: list[int] = []
    subseq: list[int]
    for num in s1:
        subseq = []
        i: int = 0
        while i <= num:
            if i < len(s2):
                subseq.append(s2[i])
            i += 1
        res.append(maximo(subseq))
    return res

if __name__ == "__main__":
    l1 = [3,2,1]
    l2 = [0,1,4]
    print(maximoPorSubseq(l1,l2))