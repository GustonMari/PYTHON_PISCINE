import sys

def count_char(string: str):
    """This function counts the number of characters in a string."""
    print("The text contains", len(string) ,"characters:" )

def count_upper_case(string: str):
    """This function counts the number of upper case characters in a string."""
    print(sum(1 for c in string if c.isupper()), " upper letters")
    
def count_lower_case(string: str):
    """This function counts the number of lower case characters in a string."""
    print(sum(1 for c in string if c.islower()), " lower letters")

def count_punctuation(string: str):
    """This function counts the number of punctuation marks in a string."""
    print(sum(1 for c in string if c in ('!', "," ,"\'" ,";" ,"\"", ".", "-" ,"?")), " punctuation marks")

def count_spaces(string: str):
    """This function counts the number of spaces in a string."""
    print(sum(1 for c in string if c.isspace()), " spaces")
    
def count_digits(string: str):
	"""This function counts the number of digits in a string."""
	print(sum(1 for c in string if c.isdigit()), " digits")

def count_typo(string: str):
    """This function counts the number of typos in a string."""
    count_char(string)
    count_upper_case(string)
    count_lower_case(string)
    count_punctuation(string)
    count_spaces(string)
    count_digits(string)


def main():
    """This is the main function."""
    if len(sys.argv) == 1:
        to_count = input("What is the text to count?\n")
        count_typo(to_count)
    else:
        assert len(sys.argv) <= 2, "AssertionError: more than one argument is provided"
        try:
            count_typo(sys.argv[1])
        except AssertionError as msg:
            print(msg)
        
    
if __name__ == "__main__":
	main()