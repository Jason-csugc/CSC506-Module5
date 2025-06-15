#main.py

import random
from alg.hash import Hash

def main():
    BUCKET_SIZE = 10

    hash = Hash(BUCKET_SIZE)

    arr = random.sample(range(BUCKET_SIZE * 10), BUCKET_SIZE * 10)
    print(arr)
    for x in arr:
        hash.insertItem(x)
    
    hash.displayHash()

if __name__ == "__main__":
    main()
