# DESCRIPTION :
# First python script
# You need to modify the string of each data object to display the following greetings:
# "Hello World", "Hello «country of your campus»", "Hello «city of your campus»", "Hello
# «name of your campus»"

ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}


# List is a collection which is ordered and changeable. Allows duplicate members.
ft_list[1] = "World!"

# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
copy = list(ft_tuple)
copy[1] = "France!"
ft_tuple = tuple(copy)


# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# ft_set[1] = "Paris!"
edit = {"Hello", "Paris!"}
ft_set.clear()
ft_set.update(edit)

# Dictionary is a collection which is ordered** and changeable. No duplicate members.
ft_dict["Hello"] = "42Paris!"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)