def calculate_sum(a: int, b: int) -> int:
    return int(a) + int(b) + 1


def repeat_text(text: str, times: int) -> str:
    return "".join([text for _ in range(times)])