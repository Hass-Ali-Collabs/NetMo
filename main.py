import building as bl
from PyQt5.QtWidgets import*
from PyQt5.QtCore import*
from PyQt5.QtGui import*
from Layout import Ui_MainWindow
import folium
import pandas as pd





class MainWindow(QMainWindow, Ui_MainWindow):
	s=r"C:\Users\HP\Desktop\test.pcapng"

	l=bl.infile(r""+s)

	m = folium.Map(zoom_start=3)
	m.save('map.html')


	def __init__(self, parent=None):
		super(MainWindow, self).__init__(parent)
		self.setupUi(self)
		self.test(self.l)
		self.ip_numb()
		self.screanShow(self.l)
		self.combo()
		self.paKnumb()
		self.web_numb()
		self.plotting(self.maping(self.l))
		#self.btn_import.clicked.connect(self.importer)
		#self.fill(self.l)



	def importer(self):
		path=QFileDialog.getOpenFileName(self,'Open a file','','All Files(*.*)')
		#path=self.getfolderDir()


		self.l=bl.infile(r""+path)
		print(self.stringing(l))

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

	def plotting(self,ds):

			for i in range(0,len(ds)):
				folium.Marker(
				location=[ds.iloc[i]['lat'], ds.iloc[i]['lon']],
				popup=ds.iloc[i]['name'],
				).add_to(self.m)
			self.m.save('map.html')
		


	def combo(self):
		comb_ls=[]
		for x in self.l:
			if x.src_ip not in comb_ls and x.src_ip!="":
				self.comboBox.addItem(str(x.src_ip))
				comb_ls.append(x.src_ip)
		# return comb_ls

	# def fill(self,ls):
	# 	for x in ls:
	# 		self.scrollArea.addItem(self.stringing(x))
	
	def test(self,ls):
		print(self.printer(self.l))
		# for x in range(0,len(ls)):

		# 	if ls[x].src_ip !="":
		# 		print(self.stringing(ls[x]))
		# 		print()

	def screanShow(self,ls):
		self.display.setText(self.printer(ls))
		

	def web_numb(self):
		self.web_num.setText(str(len(self.only_web(self.l))))






	def ip_numb(self):#combine with the function combo
		comb_ls=[]
		for x in self.l:
			if x.src_ip not in comb_ls and x.src_ip!="":
				comb_ls.append(x.src_ip)
		self.ip_num.setText(str(len(comb_ls)))


	def paKnumb(self):

		self.pack_num.setText(str(len(self.l)))






	def stringing(self,pkt):

		if pkt.src_ip!="":
			if pkt.dns_name!="":
				return "Sender IP: "+pkt.src_ip+"\nRiciver IP: "+pkt.des_ip+"\nRiciver location: "+pkt.des_city+"-"+pkt.des_country+"\nURL: "+pkt.dns_name
			else:
				return "Sender IP: "+pkt.src_ip+"\nRiciver IP: "+pkt.des_ip+"\nRiciver location: "+pkt.des_city+"-"+pkt.des_country





	def IP_sorting(self, ip):
		global l
		ipl=[]
		for x in range(0,len(l)):
			if l[x].src_ip == ip:
				ipl.append(l[x])
			else:
				pass
		return ipl

	def printer(self,pks):
		s=""
		for x in pks:
			s+=self.stringing(x)+" \n \n \n"
		return s

	

	def only_web(self, paks):
		webl=[]
		for x in range(0,len(paks)):
			if paks[x].dns_name != "":
			    webl.append(paks[x])
	
		return webl

		

app = QApplication([])
window = MainWindow()
window.show()
app.exec()
		
	














