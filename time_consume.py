import math,random
from sklearn.metrics.pairwise import cosine_similarity
import datetime,time

def norm(vector):
    return math.sqrt(sum(x * x for x in vector))

def fun1(vec_a, vec_b):
    norm_a = norm(vec_a)
    norm_b = norm(vec_b)
    dot = sum(a * b for a, b in zip(vec_a, vec_b))
    return dot / (norm_a * norm_b)

def fun2(vec):
    return cosine_similarity(vec)

if __name__=="__main__":
    i,j=1000,300 #用于设置随机列表的大小
    # i,j=2,5
    list_all=[]
    for m in range(i):
        a=[]
        b=[]
        for n in range(j):
            a.append(random.random())
            b.append(random.random())
        list_all.append([a,b])
    curr_time = datetime.datetime.now()
    print(curr_time)  # 输出：2020-08-04 18:53:33.463004
    cos_list=[]
    for item in list_all:
        cos_list.append(fun1(item[0],item[1]))
    curr_time2 = datetime.datetime.now()
    print(curr_time2-curr_time)
    cos_list2=[]
    for item in list_all:
        cos_list2.append(fun2(item))
    curr_time3 = datetime.datetime.now()
    print(curr_time3-curr_time2)
