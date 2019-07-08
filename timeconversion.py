
def timeConversion(s):
    #
    # Write your code here.
    #
    if s[8] == 'A':
        print( s[0:8])
    elif s[8] == 'P':
        a = int(s[0:2])+12
        print(str(a)+s[2:8])

s = input()
timeConversion(s)