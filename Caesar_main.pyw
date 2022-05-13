from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtCore import QSettings
import sys

from Caesar_ui import Caesar_ui
from Caesar_logic import Caesar

class Caesar_MainWindow(QMainWindow, Caesar_ui):
    def __init__(self):
        super().__init__()
        self.setup_UI()
        self.settings = QSettings('Caesar_settings')
        self.restoreSettings()
        self.Caesar = Caesar()

    # Восстановить сохраненные параметры
    def restoreSettings(self):
        self.textEdit_Log.setText(self.settings.value('log'))

    # Добавить перевод в историю
    def updateTranslateLog(self, message, translated_message):
        currentText = self.textEdit_Log.toPlainText()
        updatedText = currentText + message + ' --> ' + translated_message + '\n'

        self.textEdit_Log.setText(updatedText)
        self.settings.setValue('log', updatedText)

    # Перевести текст
    def onTranslateClicked(self):
        message = self.textEdit_Input.toPlainText() # Сообщение на перевод
        offset = self.spin_offset.value()           # Текущее значение сдвига
        box_index = self.box_mode.currentIndex()    # Текущий режим перевода

        # Перевод текста функцией Caesar.encrypt / Caesar.decrypt
        translated_message = self.Caesar.modes[box_index](message, offset)
        self.textEdit_Output.setText(translated_message)

        # Запись в историю
        self.updateTranslateLog(message, translated_message)

    # Очистить историю
    def onClearLog(self):
        self.textEdit_Log.clear()
        self.settings.setValue('log', '')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Caesar_MainWindow()
    window.show()
    sys.exit(app.exec_())
