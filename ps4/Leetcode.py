string = 'ababcbb'

longest_len = 0
for i in range(len(string)):
    dict = {}
    for j in range(i, len(string)):
        if string[j] not in dict:
            dict[string[j]] = 1
        else:
            if longest_len < len(dict.keys()):
                longest_len = len(dict.keys())
                break

print(longest_len)