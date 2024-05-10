# DESCRIPTION :
# First use of package
# Write a script that formats the dates this way, 
# Expected output:
# $>python format_ft_time.py | cat -e
# Seconds since January 1, 1970: 1,666,355,857.3622 or 1.67e+09 in scientific notation$
# Oct 21 2022$

import datetime

now = datetime.datetime.now()
print(now)

# Epoch time, also known as Unix time or POSIX time, 
# is the amount of time in seconds that has elapsed since January 1st, 1970 (00:00:00 UTC).
timestamp = now.timestamp()

# Formatted string literals (f-strings)
# Format specifier :,4f to format float types with 4 decimals + add commas to separate thousands
# see format() for flags
print("Seconds since January 1, 1970:", f"{timestamp:,.4f}")


# see python strftime() for flags
print(f"{now:%b %d %Y}")
