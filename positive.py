count = 0
positive_count = 0
negative_count = 0
input_sum = 0
userinput = int(input("enter number: "))
while userinput != 0:
    userinput = int(input("enter number: "))
    if userinput < 0:
        negative_count += 1
    else:
        positive_count += 1

    input_sum = input_sum + userinput
    count += 1

print("negative=",negative_count)
print("positive=",positive_count)
print("sum=",input_sum)
print("average",input_sum / count)