def ratestore():
    l=[]
    r=int(input("Out of 5 rate the movie: "))
    if r>=1 and r<=5:
        with open("ratings.txt",'a') as f:
            f.write(str(r))
            f.write(' ')
def rating():
    with open ("ratings.txt",'r') as f:
        j=0
        x=f.read()
        l=[]
        s=x.split()
        for i in s:
            l.append(int(i))
        for i in l: 
            j=i+j
        avg=j//len(l)
        print(avg)

ratestore()
rating()