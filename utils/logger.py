import logging
import datetime
import os
from traceback import format_exc


class Logger:
    _logger = None

    @staticmethod
    def get_logger():
        if Logger._logger is None:
            # создаем папку для логов, если ее нет.
            log_dir = 'logs'
            os.makedirs(log_dir, exist_ok=True)

            # уникальное имя файла лога с временной меткой
            log_filename = datetime.datetime.now().strftime('test_run%d-%m-%Y-%H-%M-%S.log')
            log_filepath = os.path.join(log_dir, log_filename)

            # создаем экземпляр логгера
            Logger._logger = logging.getLogger('autotest_logger')
            # устанавливаем уровень логирования
            Logger._logger.setLevel(logging.DEBUG)

            formatter = logging.Formatter(
                                          '%(asctime)s - %(levelname)s - %(name)s'
                                          ' - [%(filename)s] - %(message)s')

            file_handler = logging.FileHandler(log_filepath)
            # в файл логов пишем все с уровня debug
            file_handler.setLevel(logging.DEBUG)

            # связываем форматировщик с обработчиком
            file_handler.setFormatter(formatter)

            # связываем обработчик с логгером
            Logger._logger.addHandler(file_handler)

            Logger._logger.info('Логирование инициализировано.')

        return Logger._logger

# экземпляр для удобного импорта
log = Logger.get_logger()