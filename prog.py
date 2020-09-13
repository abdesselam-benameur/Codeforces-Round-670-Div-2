def mex(arr):
    if len(arr) == 0: return 0
    arr.sort()
    if arr[0] > 0: return 0

    for j in range(len(arr) - 1):
        if arr[j + 1] - arr[j] > 1: return arr[j] + 1

    return arr[-1] + 1


if __name__ == '__main__':
    input_file = open("in2.txt")
    num_test_cases = int(input_file.readline())

    for i in range(num_test_cases):
        size = int(input_file.readline())
        occ = {}
        my_set = []
        tmp = input_file.readline().strip().split(" ")
        for n in tmp:
            m = int(n)
            my_set.append(m)
            occ[m] = occ.get(m, 0) + 1
        keys_sorted = sorted(occ)
        my_set = []
        for key in keys_sorted:
            if occ[key] >= 2:
                my_set += [key, key]
            else:
                my_set += [key]

        if my_set[0] != 0:
            print(0)
            continue

        if len(my_set) > 1 and my_set[1] == 0:
            # my_set contains two zeros at least
            i = 1
            end = len(keys_sorted)
            while True and i < end:
                if keys_sorted[i] != i or occ[keys_sorted[i]] < 2:
                    break
                i += 1

            if i == end:
                result = (keys_sorted[i - 1] + 1) * 2
            else:
                if occ[keys_sorted[i]] >= 2:
                    result = i * 2
                elif keys_sorted[i] == i:
                    i += 1
                    result = i
                    while True and i < end:
                        if keys_sorted[i] != i:
                            break
                        i += 1
                    result += keys_sorted[i - 1]
                else:
                    result = i * 2
            print(result)
        else:
            print(mex(my_set))
