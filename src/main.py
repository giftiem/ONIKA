import sys
from PyQt5.QtWidgets import QApplication
from src.gui.main_window import MainWindow
from src.gui.system_tray import SystemTrayIcon
import threading

class OnikaApp:
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.main_window = MainWindow()
        self.tray = SystemTrayIcon(self.show_main_window)

    def show_main_window(self, icon, item):
        self.main_window.show()

    def run(self):
        # Start system tray in a separate thread
        tray_thread = threading.Thread(target=self.tray.run, daemon=True)
        tray_thread.start()
        sys.exit(self.app.exec_())

if __name__ == "__main__":
    app = OnikaApp()
    app.run()
