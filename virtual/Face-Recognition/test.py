with open("db.txt",'a+')as f:
    f1 = open("db1.txt",'a')
    f1.write(f.read())
    f1.close()