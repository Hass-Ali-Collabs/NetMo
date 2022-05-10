import building as bl
from PyQt5.QtWidgets import*
from PyQt5.QtCore import*
from PyQt5.QtGui import*
from Layout import Ui_MainWindow






class MainWindow(QMainWindow, Ui_MainWindow):
	
	def __init__(self, parent=None):
		super(MainWindow, self).__init__(parent)
		self.setupUi(self)
		self.test(self.l)
		self.combo()
		# self.fill(self.l)
	l=bl.infile("C:/Users/HP/Desktop/test.pcapng")






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
		for x in range(0,len(ls)):

			if ls[x].src_ip !="":
				print(self.stringing(ls[x]))
				print()

	def web_num(self):
		return len(only_web(l))

	def ip_num(self):
		comb_ls=[]
		for x in self.l:
			if x.src_ip not in comb_ls and x.src_ip!="":
				comb_ls.append(x.src_ip)
		return len(comb_ls)

	def stringing(self,pkt):

		if pkt.src_ip!="":
			if pkt.dns_name!="":
				return "Sender IP: "+pkt.src_ip+" Riciver IP: "+pkt.des_ip+" Sender location: "+pkt.src_city+"-"+pkt.src_country+" Riciver location: "+pkt.des_city+"-"+pkt.des_country+" URL: "+pkt.dns_name
			else:
				return "Sender IP: "+pkt.src_ip+" Riciver IP: "+pkt.des_ip+" Sender location: "+pkt.src_city+"-"+pkt.src_country+" Riciver location: "+pkt.des_city+"-"+pkt.des_country


	def IP_sorting(self, ip):
		global l
		ipl=[]
		for x in xrange(0,len(l)):
			if l[x].src_ip == ip:
				ipl.append(l[x])
			else:
				pass
		return ipl
	

	def only_web(self, paks):
		webl
		for x in xrange(0,len(paks)):
			if paks.dns_name != "":
			    webl.append(paks[x])
	
		return webl

		

app = QApplication([])
window = MainWindow()
window.show()
app.exec()
		
	














