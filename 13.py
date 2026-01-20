# 展示所有牌型（考虑到用户自己输入比较麻烦，展示出来便于拷贝）
def show_cards():
    all_cards = ["♦3", "♦4", "♦5", "♦6", "♦7", "♦8", "♦9", "♦10", "♦J", "♦Q", "♦K", "♦1", "♦2",
                 "♥3", "♥4", "♥5", "♥6", "♥7", "♥8", "♥9", "♥10", "♥J", "♥Q", "♥K", "♥1", "♥2",
                 "♣3", "♣4", "♣5", "♣6", "♣7", "♣8", "♣9", "♣10", "♣J", "♣Q", "♣K", "♣1", "♣2",
                 "♠3", "♠4", "♠5", "♠6", "♠7", "♠8", "♠9", "♠10", "♠J", "♠Q", "♠K", "♠1", "♠2",
                 "🌙", "☀"]
    
    all_cards = all_cards[::-1]

    for i in range(54):
        print(all_cards.pop(), end=' ')
        if (i+1) % 13 == 0:
            print()
    print()
    

# 2 张拍的情况：对牌
def is_pair(cards):
    if cards[0] == cards[1]:
        return True
    else:
        return False


# 2 张牌的情况：火箭
def is_rocket(cards):
    if 14 in cards and 15 in cards:
        return True
    else:
        return False


# 3 张牌的情况：三张牌相同
def is_three(cards):
    if len(set(cards)) == 1:
        return True
    else:
        return False


# 4 张牌的情况：炸弹
def is_bomb(cards):
    if len(set(cards)) == 1:
        return True
    else:
        return False


def is_31(cards):
    if len(set(cards)) == 2:
        return True
    else:
        return False


def is_32(cards):
    if len(set(cards)) == 2:
        return True
    else:
        return False


def is_42(cards):
    if len(set(cards)) == 2 and (len(set(cards[:4])) == 1 or len(set(cards[2:])) == 1):
        return True
    else:
        return


def is_ds(cards):
    if 13 not in cards:
        for i in range(len(cards)-1):
            if cards[i+1] - cards[i] == 1:
                continue
            else:
                return False
        else:
            return True
    else:
        return False


def is_ss(cards):
    if len(set(cards)) == 3 and cards[4]-cards[2]==cards[2]-cards[0]==1 and 13 not in cards:
        return True
    else:
        return False


def is_fj(cards):
    if len(set(cards)) == 2 and cards[3] - cards[0] == 1 and (13 not in cards):
        return True
    else:
        return False


def is_fjd(cards):
    if (len(set(cards)) == 4 or len(set(cards)) == 6) and (13 not in cards):
        return True
    else:
        return False


# 获取用户输入的扑克牌
def get_input():
    cards = input("请出牌（空格间隔，退出请输入Q）：")
    if cards == 'Q':
        return 0
    else:
        cards = cards.split() # "♠1 ♠2 ♠3 ♠4 ♠5" -> ['♠1', '♠2', '♠3', '♠4', '♠5']
        return cards


# 将扑克牌映射成代表权限的数字
def change_input(cards):
    result = []
    target = {'3':1, '4':2, '5':3, '6':4, '7':5, '8':6, '9':7, '10':8, 'J':9, 'Q':10, 'K':11, '1':12, '2':13}
    for each in cards:
        num = target.get(each[1:])
        if num:
            result.append(num)
        else:
            result.append(14 if each == '🌙' else 15)

    return result


# 检查组合是否符合出牌规则
def check(cards):
    # 检查2张牌的情况
    if len(cards) == 2:
        if is_pair(cards):
            print("符合规则：对牌")
        elif is_rocket(cards):
            print("符合规则：火箭")
        else:
            print("不符合规则！")
            
    # 检查3张牌的情况       
    elif len(cards) == 3:
        if is_three(cards):
            print("符合规则：三张牌相同")
        else:
            print("不符合规则！")
            
    # 检查4张牌的情况
    elif len(cards) == 4:
        if is_bomb(cards):
            print("符合规则：炸弹")
        elif is_31(cards):
            print("符合规则：三带一")
        else:
            print("不符合规则！")
    elif len(cards) == 5:
        if is_32(cards):
            print("符合规则：三带二")
        elif is_ds(cards):
            print("符合规则：单顺")
        else:
            print("不符合规则！")
    elif len(cards) == 6:
        if is_42(cards):
            print("符合规则：四带二")
        elif is_ss(cards):
            print("符合规则：双顺")
        elif is_fj(cards):
            print("符合规则：三顺（飞机）")
        else:
            print("不符合规则！")
    elif len(cards) == 10 or len(cards) == 12:
        if is_fjd(cards):
            print("符合规则：飞机带翅膀")
        else:
            print("不符合规则！")

# 程序主流程
show_cards()
cards = get_input()
while cards:
    cards = change_input(cards)
    check(cards)
    cards = get_input()
