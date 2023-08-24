# -*- coding: utf-8 -*-
TEXT = '''
游戏规则：
电脑随机生成一个0到99数字，玩家来猜。电脑会给出“大了”“小了”“猜对了”的提示。
初始有6次机会，猜对分数+10，增加5次猜数机会。你能得到多少分数？
'''
score = 0
scoreplus = 10
chance = 6
chanceplus = 5
left = 0
right = 100