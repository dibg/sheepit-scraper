from time import sleep
from app import single_data_snapshot


if __name__ == '__main__':
    while True:
        single_data_snapshot()
        sleep(900)
