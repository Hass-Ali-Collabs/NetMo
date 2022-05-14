import building as bl
from PyQt5.QtWidgets import*
from PyQt5.QtCore import*
from PyQt5.QtGui import*
from Layout import Ui_MainWindow
import folium
import webbrowser
import pandas as pd





class MainWindow(QMainWindow, Ui_MainWindow):


	
#initializing the GUI

	def __init__(self, parent=None):
		super(MainWindow, self).__init__(parent)
		self.setupUi(self)
		
		self.btn_web_filter.clicked.connect(self.clicker)
		self.themes()
		self.btn_browse.clicked.connect(lambda: self.st_browse_path(self.lineEdit, 'pcapng'))
		self.pushButton.clicked.connect(lambda: self.st_browse_path(self.lineEdit_2, 'html'))
		self.comboBox.currentTextChanged.connect(lambda:self.selectCombo(self.l))
		self.btn_import.clicked.connect(self.importer)
		self.Resetbtn.clicked.connect(lambda:self.screanShow(self.l))


#create an html file to stor the map in 
	def create_map_first(self):	
		global m
		m = folium.Map(location=[0, 0], zoom_start=3)
		m.save(self.lineEdit_2.text())




#	opens the map in web browser
	def clicker(self):

		url = self.lineEdit_2.text()

		webbrowser.open(url,new=2)
		



#grabs the path of the chosen file 
	def st_browse_path(self, lineEd, typ):
		if typ == 'pcapng':	
			s=QFileDialog.getOpenFileName(self, 'Open a file', '','All Files (*.{})'.format(typ))
			lineEd.setText(s[0])
		else:
			s=QFileDialog.getSaveFileName(self, 'Save a file', '','All Files (*.{})'.format(typ))
			lineEd.setText(s[0])




#prompts the program to go threw the runing proccess 
	def importer(self):
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




#collect the logitude and latitude in a form the plotting needs 
	def maping(self,pks):
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




#plots the latitude and logitue on the map
	def plotting(self,ds):
		self.create_map_first()
		for i in range(0,len(ds)):
			folium.Marker(
			location=[ds.iloc[i]['lat'], ds.iloc[i]['lon']],
			popup=ds.iloc[i]['name'],
			).add_to(m)
		m.save(self.lineEdit_2.text())
		



#fills the drop down menue with distincet soruce ip adresses 
	def combo(self):
		comb_ls=[]
		for x in self.l:
			if x.src_ip not in comb_ls and x.src_ip!="":
				self.comboBox.addItem(str(x.src_ip))
				comb_ls.append(x.src_ip)






#prints the final result into the comand line for troubleshooting purpeces 
	def test(self,ls):
		print(self.printer(self.l))
		# for x in range(0,len(ls)):

		# 	if ls[x].src_ip !="":
		# 		print(self.stringing(ls[x]))
		# 		print()




#sets a string into the display aria 
	def screanShow(self,ls):
		self.display.setText(self.printer(ls))
		




#counts the number of packets with a DNS host name 
	def web_numb(self):
		self.web_num.setText(str(len(self.only_web(self.l))))







#counts the number of destinct source IP addresses are in the capture
	def ip_numb(self):#combine with the function combo
		comb_ls=[]
		for x in self.l:
			if x.src_ip not in comb_ls and x.src_ip!="":
				comb_ls.append(x.src_ip)
		self.ip_num.setText(str(len(comb_ls)))




#counds how many packets are in the capture
	def paKnumb(self):

		self.pack_num.setText(str(len(self.l)))







#trunes a packet into a string containing its most valiable information for the user 
	def stringing(self,pkt):

		if pkt.src_ip!="":
			if pkt.dns_name!="":
				return "Sender IP: "+pkt.src_ip+"\nRiciver IP: "+pkt.des_ip+"\nRiciver location: "+pkt.des_city+"-"+pkt.des_country+"\nURL: "+pkt.dns_name
			else:
				return "Sender IP: "+pkt.src_ip+"\nRiciver IP: "+pkt.des_ip+"\nRiciver location: "+pkt.des_city+"-"+pkt.des_country





#turns a list of packets into a string
	def printer(self,pks):
		s=""
		for x in pks:
			s+=self.stringing(x)+" \n \n \n"
		return s




#filters the packets being desplaed in the dispaly aria, acording to what has been selleckted in the dorpdown menue 
	def selectCombo(self,pks):
		s=""
		for x in pks:
			if x.src_ip == self.comboBox.currentText():
				s+=self.stringing(x)+" \n \n \n"
				self.display.setText(s)





#takes a list of packets, and reterns a list with only packets that have a DNS host name
	def only_web(self, paks):
		webl=[]
		for x in range(0,len(paks)):
			if paks[x].dns_name != "":
				webl.append(paks[x])

		return webl



#sets the style of the GUI
	def themes(self):
		with open('SpyBot.css') as myfile:
			styles = myfile.read()
		self.setStyleSheet(styles)

		
#main
app = QApplication([])
window = MainWindow()
window.show()
app.exec()
		
	














