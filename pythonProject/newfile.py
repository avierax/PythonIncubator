import random


def merge(llist, rlist):
    result = []
    il: int = 0
    ir: int = 0
    while il < len(llist) & ir < len(rlist):
        if llist[il] <= rlist[ir]:
            result.append(llist[il])
            il = il + 1
        else:
            result.append(rlist[ir])
            ir = ir + 1
    result.extend(llist[il:])
    result.extend(rlist[ir:])
    return result


def merge_sort(list):
    if len(list) == 1:
        return list
    left = merge_sort(list[0::len(list) / 2])
    right = merge_sort(list[len(list) / 2::])
    return merge(left, right)


if __name__ == "__main__":
    print(merge_sort([random.randrange(0, 10) for i in range(10)]))
