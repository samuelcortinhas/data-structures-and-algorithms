def linear_search(lst, target):
    for i, x in enumerate(lst):
        if x == target:
            return i
        
if __name__ == "__main__":
    lst = range(10)

    print(linear_search(lst, 12))
    print(linear_search(lst, 6))
