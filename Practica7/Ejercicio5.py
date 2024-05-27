def pertenece(s: list[int], e: int) -> bool:
    for i in range(len(s)):
        if e == s[i]:
            return True
    return False

def pertenece_a_cada_uno_version_2(s:list[list[int]], e: int, result:list[bool]):
    result.clear()
    length = len(s)
    for i in range(length):
        result.append(pertenece(s[i],e))
    return result 

a: list[list[int]] = [[3,4,5],[2,4,8],[10,23,54]]


if __name__ == '__main__':
    print(pertenece_a_cada_uno_version_2(a, 4))

