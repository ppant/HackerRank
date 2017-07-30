# Author: Pradeep K. Pant, ppant@cpan.org
# You are given the firstname and lastname of a person on two different lines. 
# Your task is to read them and print the following:
# Hello Firstname lastname You just delved into python.

def print_full_name(firstname, lastname):
    print("Hello " +firstname+" "+lastname + "! You just delved into python.")
firstname = str(input())
lastname = str(input())
if (len(firstname) and len(lastname) <=10):
    print_full_name(firstname,lastname)
else:
    print ("Long words")