def find(s, n):
#write your implementation here
    for i in range (len(s)):
        for j in range (i+1,len(s)):
            if s[i]+s[j]==n:
                return print([i,j])

num1 = [2,7,11,15]
target1 = 9
example1=find(num1,target1)

num2 = [3,2,4]
target2 = 6
example2=find(num2,target2)

num3 = [3,3]
target3 = 6
example3=find(num3,target3)
