# Author: Pradeep K. Pant, ppant@cpan.org
# Read an integer N
# Without using any string methods, try to print the following:
#    123..N
#    Ex: if N=3
#    Output: 123
n = int(input())
for x in range(1,n+1):
    print(x, end='')