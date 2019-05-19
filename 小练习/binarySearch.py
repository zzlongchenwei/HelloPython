# binarySearch
def search(sequence, number, lower=0, upper=None):
    """二分法查找"""
    if upper is None: upper = len(sequence) - 1
    # 设置默认值，如果没有设置初值，将默认设置第一个数和最后一个
    if lower == upper:  # 如果lower和upper值相同
        assert number == sequence[upper]  # 断言查到该数字
        return upper  # 返回数字位置
    else:
        middle = (lower + upper) // 2  # 取中间位置
        if number > sequence[middle]:  # 如果number比中间位置的值大
            return search(sequence, number, middle + 1, upper)  # 说明在右边，递归，最小位置设为middle+1
        else:  # 如果number比中间位置的值小
            return search(sequence, number, lower, middle)  # 说明在左边，递归，把最大位置设为middle
