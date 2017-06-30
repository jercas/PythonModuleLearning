# coding=utf-8
# By JerCas
# 2017-6-28
# 测试argparse，选择+位置参数

# 导入该模块
import argparse

# 获取一个解析对象
parser = argparse.ArgumentParser()
# 添加参数
parser.add_argument('-v',"--verbose", action="count", default=0, help="echo the string you input here")
parser.add_argument('square',help='display a square of a given number',type=int)
# 调用parse_args()函数进行解析
args = parser.parse_args()

answer = args.square ** 2
# 输出该参数处理的操作
if args.verbose >= 2:
    print("the square of {} equals {}".format(args.square, answer))
elif args.verbose >= 1:
    print("{}^2 == {}".format(args.square, answer))
else:
    print(answer)


