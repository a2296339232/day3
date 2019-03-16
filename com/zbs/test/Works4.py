import random
if __name__ == '__main__':
    mlist=[]
    for i in range(0,11):
        mlist.append(random.choice(range(0,1000)))

    print(mlist)
    mlist.reverse()
    print(mlist)