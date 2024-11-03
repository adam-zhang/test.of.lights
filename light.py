#!/usr/bin/python3
import random
import copy

class Item:
    def __init__(self, serial, description, light):
        self.serial = serial
        self.description = description
        self.light = light

def getUniqueRandomIntegers(start, end, k):
    if k > (end - start + 1):
        raise ValueError("k cannot be greater than the number of integers in the range")
    return random.sample(range(start, end + 1), k)

def getItems():
    return [Item(0, "夜间与机动车会车", 0),
            Item(1, "夜间在照明良好的道路行驶", 0),
            Item(2, "夜间同方向近距离跟车", 0),
            Item(3, "夜间直行通过路口", 0),
            Item(4, "夜间通过没有交通信号控制的路口", 1),
            Item(5, "夜间通过急弯、坡路", 1),
            Item(6, "夜间超越前方车辆", 1),
            Item(7, "夜间在没有路灯照明不良条件下行驶", 2)]

def getShowing():
    numbers = getUniqueRandomIntegers(0, 7, 4)
    assert(len(numbers) == 4)
    answers = []
    #print(numbers)
    items = getItems()  # 调用一次并存储结果
    for number in numbers:  # 直接迭代numbers
        if number < len(items):  # 确保序号在范围内
            it = copy.deepcopy(items[number])
            answers.append(it)
    answers.append(Item(8, "夜间在道路上发生故障，妨碍交通以难以移动", 3))
    assert(len(answers) == 5)
    return answers

def lightDict():
    return {0:"近光灯"
            ,1:"远近交替"
            ,2:"远光灯"
            ,3:"示廓灯"
            }

def show(item):
    # 实现显示项目的详细信息
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    RESET = "\033[0m"
    print(RESET)
    print(item.description + "\n")
    print("0:\t近光灯")
    print("1:\t远近交替")
    print("2:\t远光灯")
    print("3:\t示廓灯和报警灯")
    answer = int(input())
    if answer == item.light:
        print(GREEN + "Congratulations\n")
    else:
        print(RED + "Sorry\nand the right anwser is " + lightDict()[answer])
        
def main():
    showing = getShowing()
    assert(len(showing) == 5)
    for item in showing:
        show(item)  # 显示每个项目的详细信息

if __name__ == "__main__":
    main()
