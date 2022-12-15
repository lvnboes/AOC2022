from utils import timed, print_day
import Day1
import Day2
import Day3


def run_all():
    print_day(day=1, f=Day1.main)
    print_day(day=2, f=Day2.main)
    print_day(day=3, f=Day3.main)


def main():
    duration = timed(f=run_all).duration
    print('--------------------')
    print(f'Duration : {duration} µs')


if __name__ == '__main__':

    main()
