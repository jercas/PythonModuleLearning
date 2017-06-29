import argparse

parser = argparse.ArgumentParser(description="calculate X with Y")

group = parser.add_mutually_exclusive_group()
group.add_argument('-m',"--multiplication",action="store_true")
group.add_argument('-d',"--division",action="store_true")

parser.add_argument('x',type=int,help="the base")
parser.add_argument('y',type=int,help="the operand")

args = parser.parse_args()
if args.multiplication:
    print("multiplication: {} * {} = {}".format(args.x,args.y,args.x*args.y))
elif args.division:
    print("division: {} / {} = {}".format(args.x,args.y,args.x/args.y))
else:
    print("I don't konw which kind operation that you want to use!")