
import logging
from messages import MENUS
from tasks import task1_unique_words, task2_longest_word, task4_big_numbers

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler("app.log", encoding='utf-8')]
)

def main_menu():
    logger = logging.getLogger(__name__)
    logger.info("Запуск главного меню")
    try:
        while True:
            print("\n" + "="*50)
            print(MENUS["main_title"])
            print("1. " + MENUS["task1"])
            print("2. " + MENUS["task2"])
            print("3. " + MENUS["task4"])
            print("4. " + MENUS["exit"])
            choice = input(MENUS["prompt_choice"]).strip()

            if choice == '1':
                logger.info("Выбрано задание 1")
                task1_unique_words.run_task1()
            elif choice == '2':
                logger.info("Выбрано задание 2")
                task2_longest_word.run_task2()
            elif choice == '3':
                logger.info("Выбрано задание 4")
                task4_big_numbers.run_task4()
            elif choice == '4':
                logger.info("Выход из программы")
                print(MENUS["exit_message"])
                break
            else:
                logger.warning(f"Неверный выбор: '{choice}'")
                print(MENUS["invalid_choice"])
    except (KeyboardInterrupt, EOFError):
        logger.info("Программа прервана пользователем")
        print("\n" + MENUS["interrupted"])
    except Exception as e:
        logger.critical(MENUS["unexpected_error"].format(e), exc_info=True)
        print(MENUS["unexpected_error"].format(e))

if __name__ == "__main__":
    main_menu()