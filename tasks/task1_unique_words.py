
import re
from collections import Counter
from exceptions import InvalidInputError
from messages import TASK1

def find_unique_words(text: str) -> list[str]:
    if not isinstance(text, str):
        raise InvalidInputError("Входной текст должен быть строкой")
    if not text.strip():
        raise InvalidInputError(TASK1["empty_input"])
    words = re.findall(r'\b\w+\b', text.lower())
    word_counts = Counter(words)
    return [word for word, count in word_counts.items() if count == 1]

def run_task1():
    from logging import getLogger
    logger = getLogger(__name__)
    print(f"\n{TASK1['title']}")
    try:
        text = input(TASK1["prompt_text"]).strip()
        unique = find_unique_words(text)
        if unique:
            logger.info(f"Найдено {len(unique)} уникальных слов: {unique}")
            print(TASK1["result"].format(unique))
        else:
            logger.info("Уникальные слова не найдены")
            print(TASK1["no_unique"])
    except InvalidInputError as e:
        logger.warning(f"Ошибка в задании 1: {e}")
        print(e)
    except Exception as e:
        logger.error(f"Непредвиденная ошибка в задании 1: {e}", exc_info=True)
        print(f"Ошибка: {e}")