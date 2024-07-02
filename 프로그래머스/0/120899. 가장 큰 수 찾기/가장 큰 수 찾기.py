def solution(array):
    mx = max(array)
    idx = array.index(mx)
    return [mx, idx]