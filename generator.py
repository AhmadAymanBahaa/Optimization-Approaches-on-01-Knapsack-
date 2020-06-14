import random
#file format generated is>
# inst_id, number, capacity, [(weight,value),(weight,value),...]

def GenerateInstances(numberofknapsacks):
    f = open("testdata.txt", "w")
    for i in range(numberofknapsacks):
        #numberofitems = pow(10,i)
        numberofitems = (i+1)*5
        capacity = numberofitems*10
        f.write("{} {} {}".format((i+1),numberofitems, capacity))
        for i in range(numberofitems):
            f.write(" {} {}".format(random.randint(1,30), random.randint(1,30)))
        f.write("\n")
    f.close()
