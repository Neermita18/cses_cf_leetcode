def recurse_apples(index, sum1, sum2):
    # We've added all apples- return the absolute difference
    if index == n:
        return abs(sum1 - sum2)

    # Try adding the current apple to either the first or second set
    return min(recurse_apples(index + 1, sum1 + weights[index], sum2),
               recurse_apples(index + 1, sum1, sum2 + weights[index]))

n = int(input())
weights = list(map(int, input().split()))

# Solve the problem starting at apple 0 with both sets being empty
print(recurse_apples(0, 0, 0))




