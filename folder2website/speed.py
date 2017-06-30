import os
import sys
import time

absjoin = lambda x, y: os.path.abspath(os.path.join(x, y))
ROOT_DIR = os.getcwd()
data = {}

def walk():
    for root, dirs, files in os.walk(ROOT_DIR):
        for fname in files:
            if fname.endswith('.md') or fname.endswith('.txt'):
                fpath = absjoin(root, fname)
                try:
                    with open(fpath) as fp:
                        data[fpath] = fp.read()
                except:
                    pass

def main():
    start = time.time()
    walk()
    end = time.time()
    return end-start

if __name__ == '__main__':
    speed = []
    for i in range(10):
        speed.append(main())
        print(i, end='\r')

    print(sum(speed)/len(speed))

