

def ft_mean(*args: any) -> float:
    """function mean"""
    if len(args) == 0:
        return None
    res = sum(args) / len(args)
    return res

# ! technique tres cool pour la mediane
# ! https://www.geeksforgeeks.org/find-median-of-list-in-python/
def ft_median(*args: any):
    """function median"""
    args = sorted(args)
    # args.sort()
    mid = len(args) // 2
    res = (args[mid] + args[~mid]) / 2
    print("median: ", res)

# ! this operator // is floor division, it returns the quotient
def ft_quartile(*args: any):
    """function quartile"""
    args = sorted(args)
    args_len = len(args)
    q1 = args[(args_len + 1) // 4]
    q3 = args[((args_len + 1) * 2) // 4]
    res = []
    res.append(float(q1))
    res.append(float(q3))
    print("quartile: ", res)

# ! https://www.scribbr.com/statistics/standard-deviation/
def ft_std(*args: any):
    mean = ft_mean(*args)
    tmp_list = args
    tmp_list = [x - mean for x in tmp_list]
    tmp_list = [x ** 2 for x in tmp_list]
    res =  sum([x for x in tmp_list]) / (len(tmp_list) - 1)
    res = res ** 0.5
    print("std: ", res)

def ft_var(*args: any):
    pass

def ft_statistics(*args: any, **kwargs: any) -> None:
    """function statistics"""
    for x in kwargs.values():
        match x:
            case "mean":
                print("mean :", ft_mean(*args))
            case "median":
                ft_median(*args)
            case "quartile":
                ft_quartile(*args)
            case "std":
                ft_std(*args)
            case "var":
                ft_var(*args)
            case default:
                return None