def ft_tqdm(lst: range) -> None:
    """Prints a progress bar of the list's iteration"""
    assert isinstance(lst, range), "Not a range"
    try:
        progress = 0
        total = len(lst)
        width=96
        char='█'
        
        for item in lst:
            yield item
            progress += 1
            if total is not None:
                percentage = progress / total
                bar_width = int(width * percentage)
                bar = char * bar_width + ' ' * (width - bar_width)
                print(f"{percentage:.0%}|{bar}| {item + 1}/{total}", end='\r')
    except AssertionError as msg:
        print(msg)
    return None