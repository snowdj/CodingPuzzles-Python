def permute(nums):
    if nums is None:
        return [[]]
    elif len(nums) <= 1:
        return [nums]

    result = []
    for i, item in enumerate(nums):
        print("i={0}, item={1}".format(i, item))
        for p in permute(nums[:i] + nums[i + 1:]):
            print("p={0}, item={1}, append {2}".format(p, item, p + [item]))
            result.append(p + [item])
            print("now result is ... {0}".format(result))

    return result

def test():
    print(permute([1,2,3]))

if __name__ == "__main__":
    test()