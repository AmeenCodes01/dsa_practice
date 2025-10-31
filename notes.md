# binary search
 - take note of signs
 - when you go through all indexes (find a target) go for while left <= right & if a index (boundary), left < right (so it just stops with one left)

upper bound ( to find first duplicate in a array)

    🧩 Core logic difference from lower bound

Lower bound keeps mid if it’s >= target → because that means mid might be the first time target appears.

Upper bound keeps mid if it’s > target → because that means mid might be the first time something larger appears.

They’re mirror images: one is “first >= target”, the other is “first > target”.

⚡ So the logic is:
We’re always shrinking toward the first place the condition becomes true.

For lower bound → condition is >= target.

For upper bound → condition is > target.

So instead of asking “where’s the last target?” we flip the question to:
👉 “where’s the first element that’s strictly greater than target?”

Once we find that, the last target is just one step before.


## Square root check

if mid == x // mid:  # avoid mid*mid  (this gives the floored int sqr root of x as mid. so 4 = 16//4 )
