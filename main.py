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
	l=bl.infile("C:/Users/HP/Desktop/test.pcapng")





	def combo(self):
		comb_ls=[]
		for x in self.l:
			if x.src_ip not in comb_ls and x.src_ip!="":
				self.comboBox.addItem(str(x.src_ip))
				comb_ls.append(x.src_ip)
		# return comb_ls


	
	def test(self,ls):
		for x in range(0,len(ls)):

			if ls[x].src_ip !="":
				print(ls[x].src_ip)

		



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
		
	














