if __name__ == '__main__':
    mlist=[1,2,3]
    mset={1,2,3}
    print(type(mset))
    print(type(mlist))

    mlist=[i**2 for i in range(1,11)]
    print(mlist)

    mlist = [i ** 2 for i in range(1, 11) if i%2==0]
    print(mlist)

    mlist= [1,2,3]
    nlist=['a','b','c']
    qlist=[]
    for m in mlist:
        for n in nlist:
            qlist.append(str(m)+n)
    print(qlist)

    qlist=[]
    qlist=[str(m)+n for m in mlist for n in nlist]
    print(qlist)

    mlist=[i for i in range(1,100)]
    print(mlist)

    dict = dict()
    dict={m:n for m in mlist for n in nlist}
    print(dict)