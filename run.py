from excuses import PROGRAMMINGEXCUSES
import random

def build_excuse():
    return random.sample(PROGRAMMINGEXCUSES, 1)

def run():
    print(build_excuse())

if __name__ == '__main__':
    run()

