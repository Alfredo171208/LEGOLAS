def list():
    list1 = [1,2,3,4,5]
    list2 = [5,6,7,8,9]
    list3 = set(list1 + list2)
    return list3

alex = list()
print (alex)

def alex (number, letter):
    test = ''.join([char * num for char, num in zip(letter, number)])
    
    return test

print(alex((1,2,3,4), 'alex'))

