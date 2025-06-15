#main.py

import random
from alg.hash import Hash

def main():
    BUCKET_SIZE = 10

    hash = Hash(BUCKET_SIZE)

    arr = random.sample(range(BUCKET_SIZE * 20), BUCKET_SIZE * 10)
    for x in arr:
        hash.insertItem(x)

    print(f"Array (total elements: {len(arr)}):")

    for i in range(10):
        print(f"elements {i*10} - {i * 10 + 10}: {arr[i * 10: i * 10 + 10]}")
    
    print("")
    print("Hash Table:")
    hash.displayHash()

if __name__ == "__main__":
    main()
