
from exceptions import InvalidNumberError, UnsupportedOperationError, NegativeResultError
from messages import TASK4
from logging import getLogger

logger = getLogger(__name__)

def validate_digits(digits: list[int]) -> None:
    if not all(isinstance(d, int) and 0 <= d <= 9 for d in digits):
        raise InvalidNumberError(TASK4["error_invalid_digit"])

def digits_to_int(digits: list[int]) -> int:
    validate_digits(digits)
    return int(''.join(map(str, digits)))

def int_to_digits(n: int) -> list[int]:
    if n < 0:
        raise ValueError("Ожидалось неотрицательное число")
    return [int(d) for d in str(n)]

def process_big_numbers(a: list[int], b: list[int], operation: str) -> list[int]:
    num_a = digits_to_int(a)
    num_b = digits_to_int(b)

    if operation == 'add':
        result = num_a + num_b
        return int_to_digits(result)
    elif operation == 'sub':
        result = num_a - num_b
        if result < 0:
            raise NegativeResultError(TASK4["negative_result"])
        return int_to_digits(result)
    else:
        raise UnsupportedOperationError(TASK4["invalid_op"])

def run_task4():
    print(f"\n{TASK4['title']}")
    print(TASK4["intro"])
    try:
        a_str = input(TASK4["prompt_a"]).strip()
        if not a_str:
            raise InvalidNumberError(TASK4["empty_input"])
        a = list(map(int, a_str.split()))

        b_str = input(TASK4["prompt_b"]).strip()
        if not b_str:
            raise InvalidNumberError(TASK4["empty_input"])
        b = list(map(int, b_str.split()))

        op = input(TASK4["prompt_op"]).strip().lower()
        if op not in ('add', 'sub'):
            raise UnsupportedOperationError(TASK4["invalid_op"])

        result = process_big_numbers(a, b, op)
        logger.info(f"Операция '{op}' с числами {a} и {b} → результат: {result}")
        print(TASK4["result"].format(result))

    except (ValueError, InvalidNumberError) as e:
        msg = str(e) if str(e) else TASK4["error_invalid_digit"]
        logger.error(f"Ошибка ввода числа: {msg}", exc_info=True)
        print(TASK4["error_input"].format(msg))
    except (UnsupportedOperationError, NegativeResultError) as e:
        logger.warning(f"Логическая ошибка в задании 4: {e}")
        print(e)
    except Exception as e:
        logger.critical(f"Непредвиденная ошибка в задании 4: {e}", exc_info=True)
        print(f"Критическая ошибка: {e}")