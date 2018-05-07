def findFirstBadVersion(n):
    if n is None:
        return None
    if n <= 1:
        return n

    start, end = 0, n

    while (start + 1 < end):
        mid = start + (end - start)//2
        if SVNRepo.isBadVersion(mid):
            end = mid
        else:
            start = mid

    if SVNRepo.isBadVersion(start):
        return start
    if SVNRepo.isBadVersion(end):
        return end

    return None