import random
import time
from multiprocessing import Pool


def worker(name: str) -> None:
    print(f"Started worker {name}")
    worker_time = random.choice(range(1, 5))
    time.sleep(worker_time)
    print(f"{name} worker finished in {worker_time} seconds")


if __name__ == "__main__":
    # worker("first")
    # worker("second")
    # worker("third")

    # [ worker(each) for each in ["first", "second", "third"]]

    # map(worker, ["first", "second", "third"])

    pool = Pool(processes=5)  # to limit no. of processes running to 5
    pool.map(worker, ["first", "second", "third"])
    pool.terminate()
