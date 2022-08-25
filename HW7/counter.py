class DigitalCounter:
    def __init__(self, start: int = 0, end: int = 100, current: int | None = None) -> None:
        self._start = start
        self._end = end
        self._current = max(current, start) if current is not None else start

    def increase(self) -> None:
        self._current += 1

    def get_current_value(self) -> int:
        return min(self._current, self._end)


if __name__ == "__main__":
    d = DigitalCounter(current=100)
    print(d.get_current_value())
