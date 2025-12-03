
import re
from exceptions import InvalidInputError
from messages import TASK2

def find_longest_words(text: str):
    if not isinstance(text, str) or not text.strip():
        raise InvalidInputError(TASK2["empty_input"])
    words = re.findall(r'\b\w+\b', text)
    if not words:
        return [], 0
    max_len = max(len(w) for w in words)
    unique_longest = list(dict.fromkeys(w for w in words if len(w) == max_len))
    return unique_longest, max_len

def run_task2():
    from logging import getLogger
    logger = getLogger(__name__)
    print(f"\n{TASK2['title']}")
    try:
        text = input(TASK2["prompt_text"]).strip()
        words, length = find_longest_words(text)
        if words:
            logger.info(f"Самые длинные слова: {words}, длина: {length}")
            print(TASK2["result"].format(words, length))
        else:
            logger.info("Слов не найдено")
            print(TASK2["no_words"])
    except InvalidInputError as e:
        logger.warning(f"Ошибка в задании 2: {e}")
        print(e)
    except Exception as e:
        logger.error(f"Ошибка в задании 2: {e}", exc_info=True)
        print(f"Ошибка: {e}")