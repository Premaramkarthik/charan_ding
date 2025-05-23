# using parser arguments ---> add two numbers 

import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument('--inp1',type=int,required=True,help="pass the input1")
    parser.add_argument('--inp2',type=int,required=True,help="pass the input2")

    args = parser.parse_args()
    var1 = args.inp1
    var2 = args.inp2

    print(var1+var2)