
if __name__ == '__main__':
    n = int(input().strip())
    if(n%2!=0):
        print('Weird')
    elif(n>=2 and n<=5):
        print('Not Weird')
    elif(n>=6and n<=20):
        print('Weird')
    else:
        print('Not Weird')

