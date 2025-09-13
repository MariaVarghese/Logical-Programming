# Slicing ([::-1])
# is concise and creates a new reversed list, which is useful if you need to preserve the original.
my_list = [1, 2, 3, 4, 5]
reversed_list = my_list[::-1]
print(reversed_list)
# list.reverse()
# is efficient for in-place reversal when you don't need the original order.
my_list = [1, 2, 3, 4, 5]
my_list.reverse()
print(my_list)
# reversed()
# is memory-efficient when dealing with large lists as it provides an iterator rather than creating a full new list immediately.
my_list = [1, 2, 3, 4, 5]
reversed_iterator = reversed(my_list)
reversed_list = list(reversed_iterator)
print(reversed_list)
# Manual swapping
# can be useful for understanding the underlying logic or in specific scenarios where you need fine-grained control.
def reverse_list_manual(arr):
    start = 0
    end = len(arr) - 1
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]  # Swap elements
        start += 1
        end -= 1

my_list = [1, 2, 3, 4, 5]
reverse_list_manual(my_list)
print(my_list)
