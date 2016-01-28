from collections import defaultdict
from sys import stdin

next(stdin)
by_abs_diff = defaultdict(list)
nums = sorted(int(a) for a in set(next(stdin).split()))
output = '{} {}'.format

for b, c in zip(nums, nums[1:]):
    by_abs_diff[abs(b - c)].append((b, c))

print(' '.join(output(*d) for d in by_abs_diff[min(by_abs_diff)]))