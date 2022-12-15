from dataclasses import dataclass
from datetime import datetime
from typing import Callable, Any


@dataclass
class TimedResult:
    result: Any
    duration: int


def timed(f: Callable[[], Any]) -> TimedResult:
    start = datetime.now()
    result = f()
    end = datetime.now()
    return TimedResult(result=result, duration=round((end-start).total_seconds()*1000000))
