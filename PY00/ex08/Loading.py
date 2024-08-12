# yield: is a way to create iterator objects that produce values lazily
# converting the function that contains yield into a generator function
# the function runs and iterates normally till encounters yield, at this point
# the value specified after yield is returned and
# the function state is saved, the function effectively pauses at this point

# enumerate: help to enumerate the elements of an object in this case
# to start the index from 1 instead of 0 so i get 100% and 333
# instead of 99% an 332

# progress: calculates the percentage of the range
# img_progress: calculates the len of the progress bar based on the progress %
# img : determines how mane '=' are in the progress bar

def ft_tqdm(lst: range) -> None:
    """Prints an extensible progress bar"""
    total = len(lst)
    img_len = 63
    for i, item in enumerate(lst, start=1):
        progress = (i * 100) // total
        img_progress = (progress * img_len) // 100
        img = "=" * (img_len if (img_len < img_progress) else img_progress)
        print(f'\r{progress}%| [{img}>]| {i}/{total}', end='', flush=True)
        yield item
