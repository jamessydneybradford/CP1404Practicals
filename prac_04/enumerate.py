"""
When you use enumerate(), the function gives you back two loop variables:
- The count of the current iteration
- The value of the item at the current iteration
Just like with a normal for loop, the loop variables can be named whatever you want them to be named.
You use count and value in this example, but they could be named i and v or any other valid Python names.
With enumerate(), you don’t need to remember to access the item from the iterable,
and you don’t need to remember to advance the index at the end of the loop.
Everything is automatically handled for you by the magic of Python!
"""

def main():
    values = ['a', 'b ', 'c', 'd', 'e', 'f', 'g']

    for count, value in enumerate(values):
        print(count, value)

main()