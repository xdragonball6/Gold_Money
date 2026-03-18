import os
import sys

# 프로젝트 루트를 Python 경로에 추가
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from PySide6.QtWidgets import QApplication
from ui import MainWindow
from config import *


def logic(q_in, q_out):
    from logic.LogicProcess import LogicProcess
    logic = LogicProcess(q_in, q_out)


def main():
    # logic 프로세스
    logic_process = multiprocessing.Process(target=logic, args=(UI_QUEUE, LOGIC_QUEUE), daemon=True)
    logic_process.start()

    app = QApplication(sys.argv)
    window = MainWindow(logic_process)
    # window.show()
    app.exec()


if __name__ == '__main__':
    multiprocessing.freeze_support()
    main()
