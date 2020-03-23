def two_oldest_ages(ages):
    oa1 = max(ages)  #  39
    ages.remove(oa1)
    oa2 = max(ages)
    res = [oa2,oa1]
    return res
