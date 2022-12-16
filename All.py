from utils import timed, print_day
import Day1
import Day2
import Day3
import Day4
import Day5
import Day6


def run_all():
    print_day(day=1, f=Day1.main)
    print_day(day=2, f=Day2.main)
    print_day(day=3, f=Day3.main)
    print_day(day=4, f=Day4.main)
    print_day(day=5, f=Day5.main)
    print_day(day=6, f=Day6.main)


def main():
    duration = timed(f=run_all).duration
    print('---------------------*')
    print(f'Duration : {duration} µs')


if __name__ == '__main__':
    main()
