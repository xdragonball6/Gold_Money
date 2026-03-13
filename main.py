import os
import sys

# 프로젝트 루트를 Python 경로에 추가
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from PySide6.QtWidgets import QApplication
from ui import MainWindow


def main():
    app = QApplication(sys.argv)
    app.setApplicationName("Gold & Stock Monitor")
    window = MainWindow()
    window.show()
    app.exec()


if __name__ == '__main__':
    main()
