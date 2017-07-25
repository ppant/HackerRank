# Author: Pradeep K. Pant, ppant@cpan.org
# Python If-Else

n = int(input())
# number is odd
if n%2!=0:
    print ("Weird")
# number is even in between 2 and 6
elif n in range (2,5) and n%2==0:
    print ("Not weird")
# number is even between 6 to 20
elif n in range(6,21) and n%2==0:
    print ("Weird")
# number is greater than 20 and is even
elif n>20 and n%2==0:
    print ("Not weird")