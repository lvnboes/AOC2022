from dataclasses import dataclass
from datetime import datetime
from typing import Callable, Any, Optional


@dataclass
class TimedResult:
    duration: int
    result: Optional[Any] = None


def timed(f: Callable[[], Optional[Any]]) -> TimedResult:
    start = datetime.now()
    result = f()
    end = datetime.now()
    return TimedResult(result=result, duration=round((end-start).total_seconds()*1000000))


def print_tr(n: int, timed_result: TimedResult):
    print(f'Result {n} : {timed_result.result}')
    print(f'Duration {n} : {timed_result.duration} µs')


def print_day(day: int, f: Callable[[], None]):
    print(f'--- Day {day} ---')
    f()
    print()
