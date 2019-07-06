def rle(string):
    prev = ''
    count = 0
    result = []
    for char in string:
        if char != prev and count:
            if count > 1:
                result.append(str(count))
            result.append(prev)
            count = 1
            prev = char
        elif char != prev and not count:
            prev = char
            count = 1
        elif char == prev:
            count += 1
    if count > 1:
        result.append(str(count))
    result.append(prev)
    return len(''.join(result))

print(rle('abbcaaa'))
