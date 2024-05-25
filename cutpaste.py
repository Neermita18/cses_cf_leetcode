def process_operations(n, m, s, operations):
    for a, b in operations:
        # Cut the substring and paste it to the end of the string
        substring = s[a - 1:b]
        s = s[:a - 1] + s[b:] + substring

    return s

n, m = map(int, input().split())
s = input()
operations = [tuple(map(int, input().split())) for _ in range(m)]

result = process_operations(n, m, s, operations)
print(result)