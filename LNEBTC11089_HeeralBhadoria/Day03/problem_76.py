from collections import Counter
def minWindow(s, t):
    need = Counter(t)
    left = 0
    count = 0
    min_len = float('inf')
    result = ""
    for right in range(len(s)):
        if s[right] in need:
            if need[s[right]] > 0:
                count += 1
            need[s[right]] -= 1
        while count == len(t):
            if right - left + 1 < min_len:
                min_len = right - left + 1
                result = s[left:right+1]

            if s[left] in need:
                need[s[left]] += 1
                if need[s[left]] > 0:
                    count -= 1
            left += 1
    return result
s = input()
t = input()
print(minWindow(s, t))
