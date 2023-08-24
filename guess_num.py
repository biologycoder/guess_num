import random
def compile(num,ans):
    "比较输入与答案"
    if num==ans:
        return 'right!!!'
    elif num<=ans:
        return 'small!!!'
    elif num>=ans:
        return 'big!!!'
i=0
score=0
limit=6
while True:
    ans=random.randint(1,100)
    while True:
        if i<=limit:
            #异常处理
            try:
                num=int(input('type in your num:'))
            except:
                print('you have type in a wrong num!!!')
                continue
            i+=1
            print(compile(num,ans),'left:',limit-i+1)
            if compile(num,ans)=='right!!!':
                score+=10
                print('score:',score)
                break
        else:
            print('you\'ve got no chance!!!answer is',ans)
            break
    play=input('continue playing?(y/n):')
    if play=='y':
        i=0
    else:
        break
print('bye!!!')
