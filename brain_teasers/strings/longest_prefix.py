def longest_prefix(strs):
    if not strs:
        return ""
    if len(strs) == 1:
        return strs[0]
    max_len = min(len(word) for word in strs)
    common_prefix = ""
    break_now = False
    for i in range(max_len):
        letter = strs[0][i]
        for word in strs[1:]:
            if letter != word[i]:
                break_now = True
                break
        if break_now:
            break
        common_prefix += letter
    return common_prefix
