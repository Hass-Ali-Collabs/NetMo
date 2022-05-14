import building as bl
from PyQt5.QtWidgets import*
from PyQt5.QtCore import*
from PyQt5.QtGui import*
from Layout import Ui_MainWindow
import folium
import webbrowser
import pandas as pd





class MainWindow(QMainWindow, Ui_MainWindow):


	


	def __init__(self, parent=None):
		"""initializes the GUI"""
		super(MainWindow, self).__init__(parent)
		self.setupUi(self)
		
		self.btn_web_filter.clicked.connect(self.clicker)
		self.themes()
		self.btn_browse.clicked.connect(lambda: self.st_browse_path(self.lineEdit, 'pcapng'))
		self.pushButton.clicked.connect(lambda: self.st_browse_path(self.lineEdit_2, 'html'))
		self.comboBox.currentTextChanged.connect(lambda:self.selectCombo(self.l))
		self.btn_import.clicked.connect(self.importer)
		self.Resetbtn.clicked.connect(lambda:self.screanShow(self.l))



	def create_map_first(self):	
		"""create an html file to stor the map in"""
		global m
		m = folium.Map(location=[0, 0], zoom_start=3)
		m.save(self.lineEdit_2.text())





	def clicker(self):
		"""opens the map in web browser"""

		url = self.lineEdit_2.text()

		webbrowser.open(url,new=2)
		




	def st_browse_path(self, lineEd, typ):
		"""grabs the path of the chosen file""" 
		if typ == 'pcapng':	
			s=QFileDialog.getOpenFileName(self, 'Open a file', '','All Files (*.{})'.format(typ))
			lineEd.setText(s[0])
		else:
			s=QFileDialog.getSaveFileName(self, 'Save a file', '','All Files (*.{})'.format(typ))
			lineEd.setText(s[0])




 
	def importer(self):
		"""prompts the program to go threw the runing proccess"""
		if self.lineEdit.text() != '' and self.lineEdit_2.text() != '':
			self.l=bl.infile(r""+self.lineEdit.text(), self.progressBar)
			self.test(self.l)
			self.ip_numb()

			self.combo()
			self.paKnumb()
			self.web_numb()
			self.plotting(self.maping(self.l))
			self.screanShow(self.l)
			with open(self.lineEdit_2.text(), 'r') as myfile:
				f = myfile.read()
			self.webEngineView.setHtml(f)
			self.btn_web_filter.setEnabled(True)
			self.Resetbtn.setEnabled(True)		
		else:
			QMessageBox.warning(self, 'Warning', 'Please fill all fields!')





	def maping(self,pks):
		"""collect the logitude and latitude in a form the plotting needs""" 
		lon=[]
		lat=[]
		name=[]
		for x in pks:
			if x.lat!=None:
				lon.append(x.long)
				lat.append(x.lat)
				name.append(x.src_ip+"->"+x.des_ip)


		data = pd.DataFrame({
				'lon':lon,
				'lat':lat,
				'name':name
							}, dtype=str)


		return data





	def plotting(self,ds):
		"""plots the latitude and logitue on the map"""
		self.create_map_first()
		for i in range(0,len(ds)):
			folium.Marker(
			location=[ds.iloc[i]['lat'], ds.iloc[i]['lon']],
			popup=ds.iloc[i]['name'],
			).add_to(m)
		m.save(self.lineEdit_2.text())
		



 
	def combo(self):
		"""fills the drop down menue with distincet soruce ip adresses"""
		comb_ls=[]
		for x in self.l:
			if x.src_ip not in comb_ls and x.src_ip!="":
				self.comboBox.addItem(str(x.src_ip))
				comb_ls.append(x.src_ip)







	def test(self,ls):
		"""prints the final result into the comand line for troubleshooting purpeces """
		print(self.printer(self.l))
		# for x in range(0,len(ls)):

		# 	if ls[x].src_ip !="":
		# 		print(self.stringing(ls[x]))
		# 		print()




 
	def screanShow(self,ls):
		"""sets a string into the display aria"""
		self.display.setText(self.printer(ls))
		





	def web_numb(self):
		"""counts the number of packets with a DNS host name """
		self.web_num.setText(str(len(self.only_web(self.l))))








	def ip_numb(self):#combine with the function combo
		"""counts the number of destinct source IP addresses are in the capture"""
		comb_ls=[]
		for x in self.l:
			if x.src_ip not in comb_ls and x.src_ip!="":
				comb_ls.append(x.src_ip)
		self.ip_num.setText(str(len(comb_ls)))





	def paKnumb(self):
		"""counts how many packets are in the capture"""

		self.pack_num.setText(str(len(self.l)))







 
	def stringing(self,pkt):
		"""trunes a packet into a string containing its most valiable information for the user"""

		if pkt.src_ip!="":
			if pkt.dns_name!="":
				return "Sender IP: "+pkt.src_ip+"\nRiciver IP: "+pkt.des_ip+"\nRiciver location: "+pkt.des_city+"-"+pkt.des_country+"\nURL: "+pkt.dns_name
			else:
				return "Sender IP: "+pkt.src_ip+"\nRiciver IP: "+pkt.des_ip+"\nRiciver location: "+pkt.des_city+"-"+pkt.des_country






	def printer(self,pks):
		"""turns a list of packets into a string"""
		s=""
		for x in pks:
			s+=self.stringing(x)+" \n \n \n"
		return s





	def selectCombo(self,pks):
		"""filters the packets being desplaed in the dispaly aria, acording to what has been selleckted in the dorpdown menue""" 
		s=""
		for x in pks:
			if x.src_ip == self.comboBox.currentText():
				s+=self.stringing(x)+" \n \n \n"
				self.display.setText(s)






	def only_web(self, paks):
		"""takes a list of packets, and reterns a list with only packets that have a DNS host name"""
		webl=[]
		for x in range(0,len(paks)):
			if paks[x].dns_name != "":
				webl.append(paks[x])

		return webl




	def themes(self):
		"""sets the style of the GUI"""
		with open('SpyBot.css') as myfile:
			styles = myfile.read()
		self.setStyleSheet(styles)

		
#main
app = QApplication([])
window = MainWindow()
window.show()
app.exec()
		
	














