import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtTest import QTest
from PyQt5.QtCore import Qt
from gbclient.client import Ui_client_window


class TestGui(object):

    def setup_method(self, method):
        """Create the GUI"""
        self.app = QApplication(sys.argv)
        self.form = Ui_client_window()
        self.window = QMainWindow()
        self.form.setupUi(self.window)

    def teardown_method(self, method):
        pass

    def test_gui_default_run(self):
        """Test the GUI in its default state"""
        assert self.form.send_button.text() == "Отправить"
        assert self.window.windowTitle() == "Messanger Client"
        QTest.mouseClick(self.form.send_button, Qt.LeftButton)
        def test_show_current_user(self):
            pass

    def test_show_dialogs_list_for_user(self):
        pass

    def test_show_messages_for_select_dialog(self):
        pass

    def test_create_new_dialog(self):
        pass

    def test_send_message(self):
        pass

    def test_receive_message(self):
        pass