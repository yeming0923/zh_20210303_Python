'''
函数内部调用自己

'''

def sum_number(num):
    print(num)
    if num==1:
        return
    sum_number(num-1)


sum_number(13)



def sum_nums(num):
    if num==1:
        return 1
    temp=sum_nums(num-1)
    return num+temp

result=sum_nums(998)#最多998层
print(result)