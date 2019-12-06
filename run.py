from excuses import PROGRAMMINGEXCUSES
import random
import argparse

def build_excuse():
    return random.sample(PROGRAMMINGEXCUSES, 1)

def run():
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--number',
        help='how many lines of funny words to generate',
        type=int, default=1)
    args = parser.parse_args()

    for n in range(args.number):
        print(build_excuse())

if __name__ == '__main__':
    run()

