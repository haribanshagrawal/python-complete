def infinite_sequence(val):
    num = 0
    while num<=val:
        yield num
        print(num,end='^')
        num += 1
        
        
if __name__=='__main__':
    for i in infinite_sequence(50):
        print(i,end=" ")