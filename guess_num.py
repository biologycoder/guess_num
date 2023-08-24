# -*- coding: utf-8 -*-
import text
import random

class GuessNum:
    def __init__(self):
        "从文本中读取数据"
        self.text = text.TEXT
        self.score = text.score
        self.scoreplus = text.scoreplus
        self.chance = text.chance
        self.chanceplus = text.chanceplus
        self.left = text.left
        self.right = text.right
        self.times = 0
    
    def randnum(self):
        return random.randint(self.left,self.right)
    
    def compiles(self,guess,number):
        "比较输入与答案"
        if guess==number:
            return '猜对了!!!',1
        elif guess<=number:
            return '小了!!!',0
        elif guess>=number:
            return '大了!!!',2
    
    def plus(self):
        "数据更新"
        self.score += self.scoreplus
        self.chance += self.chanceplus
    
    def roundloop(self):
        "每一轮猜数"
        while True:
            if self.times < self.chance:
                #异常处理
                try:
                    self.guess=int(input('输入你猜的数:'))
                except:
                    print('这不是一个合法的数哦!!!')
                    continue
                #计算机会，显示结果
                self.times+=1
                print(self.compiles(self.guess,self.number)[0],
                      '剩余机会:',self.chance-self.times)
                #猜对处理
                if self.compiles(self.guess,self.number)[1]==1:
                    self.plus()
                    print('得分:',self.score)
                    break                       #结束一轮游戏
            else:
                print('你已经没有机会了，答案是：',self.number)
                print('最终得分：',self.score)
                break
    
    def main(self):
        "猜数"
        print(self.text)
        while True:
            #每一轮游戏
            self.number=self.randnum()
            #猜数循环
            self.roundloop()
            #询问是否继续下一轮
            #按下'y'继续下一轮，其他键均退出
            self.play=input('继续吗？(y/n):')
            if self.play == 'y':
                self.times=0
            else:
                break
        print('再见!!!')

if __name__ == '__main__':
    a = GuessNum()
    a.main()        