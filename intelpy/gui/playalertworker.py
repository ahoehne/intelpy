"""Module providing a threaded worker process to play alert sounds"""
from PyQt5.QtCore import QThread
from PyQt5.QtWidgets import QMessageBox
import playsound


class PlayAlertWorker(QThread):
    """Class providing a threaded worker process to play alert sounds"""
    def __init__(self, configuration, logger=None):
        super(PlayAlertWorker, self).__init__()
        # Watchdog
        self.configuration = configuration
        self.logger = logger

    def run(self):
        """plays the alert sound"""
        alarm_sound = self.configuration.value["alarm_sound"]
        try:
            playsound.playsound(alarm_sound)
        except FileNotFoundError as e:
            self.handle_error("Error: Could not play alert sound! File not found.", str(e))
        except Exception as e:
            self.handle_error("Error: Could not play alert sound!", str(e))

    def handle_error(self, message, error):
        """unified error handling"""
        if self.logger:
            self.logger.write_log(message, error)
        msg_dialog = QMessageBox()
        msg_dialog.setWindowTitle("Alert sound error")
        msg_dialog.setText(message)
        msg_dialog.setDetailedText(error)
        msg_dialog.setInformativeText(self.configuration.value["alarm_sound"])
        msg_dialog.setStandardButtons(QMessageBox.Ok)
        msg_dialog.setIcon(QMessageBox.Warning)
        msg_dialog.exec_()
