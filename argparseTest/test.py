import argparse

descStr = "This program is a test example of how to use argparse to analyze command"
usageStr = "Test usage"

parser = argparse.ArgumentParser(usage=usageStr,description=descStr)
parser.add_argument('-e', "--echo", required=False, help="echo the string you use here")
parser.add_argument('-s', "--square", required=False, type=int, help="display a square of a given number")
parser.add_argument('-a',"--arzone", action='store_true',help="open the AR zone!")
args = parser.parse_args()

# 经过parse_args()函数后参数名称去掉了前面的"--"，所有的"-"转换为"_"
if args.echo:
    print(args.echo)
elif args.square:
    print(args.square**2)
elif args.arzone:
    print("AR zone open!")
else:
    print("Please input the right argument!")
    #查看解析对象命名环境
    print(args)