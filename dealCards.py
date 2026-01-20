import random
    
cards = ["♦1", "♦2", "♦3", "♦4", "♦5", "♦6", "♦7", "♦8", "♦9", "♦10", "♦J", "♦Q", "♦K",
         "♥1", "♥2", "♥3", "♥4", "♥5", "♥6", "♥7", "♥8", "♥9", "♥10", "♥J", "♥Q", "♥K",
         "♣1", "♣2", "♣3", "♣4", "♣5", "♣6", "♣7", "♣8", "♣9", "♣10", "♣J", "♣Q", "♣K",
         "♠1", "♠2", "♠3", "♠4", "♠5", "♠6", "♠7", "♠8", "♠9", "♠10", "♠J", "♠Q", "♠K",
         "☀", "🌙"]
    
def fy_shuffle(x, n=1):
    for i in range(n):
        target = list(x)
        result = []
        while target:
            r = random.randint(0, len(target)-1) # 步骤2
            result.append(target.pop(r)) # 步骤3
    
    return result
    
def dealCards():
    a = input("请输入第一位游戏玩家名称：")
    b = input("请输入第二位游戏玩家名称：")
    c = input("请输入第三位游戏玩家名称：")
    
    r = {}
    r[a], r[b], r[c] = [], [], []
    
    new_cards = fy_shuffle(cards, 3)
    
    for i in range(17):
        r[a].append(new_cards.pop())
        r[b].append(new_cards.pop())
        r[c].append(new_cards.pop())
    
    d = random.sample((a, b, c), 1)[0]
    print(f"\n地主是：{d}\n")
    r[d].extend((new_cards.pop(), new_cards.pop(), new_cards.pop()))
    
    print(f"[{a}]拿到的牌是：{' '.join(r[a])}\n")
    print(f"[{b}]拿到的牌是：{' '.join(r[b])}\n")
    print(f"[{c}]拿到的牌是：{' '.join(r[c])}")
    
dealCards()
