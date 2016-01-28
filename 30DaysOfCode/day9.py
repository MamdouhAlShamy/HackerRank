def find_gcd(a,b):
    if a == b:
        return a
    return find_gcd(max(a,b) - min(a,b) , min(a,b))

#Take input
inp = raw_input().split()
a = int(inp[0])
b = int(inp[1])
gcd = find_gcd(a,b)
print gcd