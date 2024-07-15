def differentGCDSubsequence(arr):
    result = []
    curr = []
    
    def dfs(i):
        if i >= len(arr):
            if curr: 
                result.append(curr.copy())
            return

        curr.append(arr[i])
        dfs(i + 1)

        curr.pop()
        dfs(i + 1)

    dfs(0)
    # print(result)
    
    final = set()

    def compute(l):
        l.sort()
        gcd_val = l[0]  # Initialize with the first (smallest) element
        for i in range(1, l[0] + 1):
            if all(x % i == 0 for x in l):
                gcd_val = i
            
        final.add(gcd_val) 
    for subseq in result:
        compute(subseq)

    # print(final)
    return len(final)