import sys
import io
import folium #pip install folium
from PyQt5.QtWidgets import *
#from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView #pip install PyQtWebEngine

class MyApp(QWidget):
	def __init__(self):
		super().__init__()
		self.setWindowTitle('Location on Map')
		self.window_width, self.window_height = 1600, 1200
		self.setMinimumSize(self.window_width, self.window_height)

		layout = QVBoxLayout()
		self.setLayout(layout)


		coordinate = (2.3281,48.8607)
		m = folium.Map(
			title = 'the location',
			zoom_start = 13,
			location = coordinate
			)
		# save map data
		data = io.BytesIO()
		m.save(data, close_file = False)

		webView = QWebEngineViwe()
		webView.setHtml(data.getvalue().decode())
		layout.addWidget(webView)




if __name__ == '__main__':
	app = QApplication(sys.argv)
	app.setStyleSheet('''
		QWidget{
			font-size: 35px;
		}
		''')
	myApp = MyApp()
	myApp.show()

	try:
		ses.exit(app.exec_())
	except SystemExit:
		print('Closing Window...')