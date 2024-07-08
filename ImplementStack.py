print("-----Stack Operation-----")
repeat=1
arr=[]
while repeat==1:
    print("1.push 2.pop 3.display")
    n=int(input("Enter choice: "))
    if n in [1,2,3]:
        if n==1:
            num=int(input("Enter number to push: "))
            arr.append(num)
        if n==2:
            if arr:
                print("popped element is : ",arr.pop())
            else:
                print("Stack is empty")
        if n==3:
            print(arr)
    repeat=int(input("Press 1 to repeat or else press anything: "))
else:
    print("invalid choice ")
        