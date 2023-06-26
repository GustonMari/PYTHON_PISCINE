ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

#For the list
# ORDERED, MUTABLE, DUPLICATES
ft_list[1] = "World!"

#For the tuple
# ORDERED, IMMUTABLE, DUPLICATES
tmp_list = list(ft_tuple)
tmp_list[1] = "France!"
ft_tuple = tuple(tmp_list)

#For the set
# UNORDERED, IMMUTABLE (but you can add and pop), NO DUPLICATES
ft_set.pop()
ft_set.add("Paris!")

#For the dict
#As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.
# MUTABLE, NO DUPLICATES
# ft_dict["Hello"] = 42
ft_dict.update({"Hello" : '42Paris!'})

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)