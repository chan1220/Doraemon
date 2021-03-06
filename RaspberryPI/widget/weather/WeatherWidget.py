from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import os

class WeatherWidget(QWidget):
	def __init__(self, parent):
		super(WeatherWidget, self).__init__(parent)
		self.path = os.getcwd() + "/widget/weather/"
		self.horizontalLayout_2 = QHBoxLayout(self)
		self.horizontalLayout_2.setObjectName("horizontalLayout_2")
		self.gridLayout = QGridLayout()
		self.gridLayout.setObjectName("gridLayout")
		self.line_6 = QFrame(self)
		self.line_6.setFrameShape(QFrame.HLine)
		self.line_6.setFrameShadow(QFrame.Sunken)
		self.line_6.setObjectName("line_6")
		self.gridLayout.addWidget(self.line_6, 3, 1, 1, 8)
		self.tmax_tomorrow = QLabel(self)
		self.tmax_tomorrow.setStyleSheet("font: 14pt \"HY헤드라인M\";")
		self.tmax_tomorrow.setAlignment(Qt.AlignCenter)
		self.tmax_tomorrow.setObjectName("tmax_tomorrow")
		self.gridLayout.addWidget(self.tmax_tomorrow, 9, 5, 1, 1)
		self.label_23 = QLabel(self)
		font = QFont()
		font.setFamily("Agency FB")
		font.setPointSize(50)
		self.label_23.setFont(font)
		self.label_23.setStyleSheet("image: url(" + self.path + "dust.png);")
		self.label_23.setText("")
		self.label_23.setObjectName("label_23")
		self.gridLayout.addWidget(self.label_23, 5, 4, 1, 1)
		self.label_19 = QLabel(self)
		self.label_19.setStyleSheet("image: url(" + self.path + "high.png);")
		self.label_19.setText("")
		self.label_19.setObjectName("label_19")
		self.gridLayout.addWidget(self.label_19, 2, 4, 1, 1)
		self.asdasdad = QLabel(self)
		self.asdasdad.setStyleSheet("image: url(" + self.path + "high.png);")
		self.asdasdad.setText("")
		self.asdasdad.setObjectName("asdasdad")
		self.gridLayout.addWidget(self.asdasdad, 9, 4, 1, 1)
		self.label_4 = QLabel(self)
		self.label_4.setStyleSheet("font: 10pt \"HY헤드라인M\";")
		self.label_4.setAlignment(Qt.AlignCenter)
		self.label_4.setObjectName("label_4")
		self.gridLayout.addWidget(self.label_4, 1, 4, 1, 2)
		self.label_13 = QLabel(self)
		self.label_13.setStyleSheet("font: 10pt \"HY헤드라인M\";")
		self.label_13.setAlignment(Qt.AlignCenter)
		self.label_13.setObjectName("label_13")
		self.gridLayout.addWidget(self.label_13, 8, 4, 1, 2)
		self.label_18 = QLabel(self)
		self.label_18.setStyleSheet("font: 10pt \"HY헤드라인M\";")
		self.label_18.setAlignment(Qt.AlignCenter)
		self.label_18.setObjectName("label_18")
		self.gridLayout.addWidget(self.label_18, 4, 4, 1, 2)
		self.tmax_today = QLabel(self)
		self.tmax_today.setStyleSheet("font: 14pt \"HY헤드라인M\";")
		self.tmax_today.setAlignment(Qt.AlignCenter)
		self.tmax_today.setObjectName("tmax_today")
		self.gridLayout.addWidget(self.tmax_today, 2, 5, 1, 1)
		self.dust = QLabel(self)
		self.dust.setStyleSheet("font: 14pt \"HY헤드라인M\";")
		self.dust.setAlignment(Qt.AlignCenter)
		self.dust.setObjectName("dust")
		self.gridLayout.addWidget(self.dust, 5, 5, 1, 1)
		self.label_10 = QLabel(self)
		self.label_10.setStyleSheet("font: 10pt \"HY헤드라인M\";")
		self.label_10.setAlignment(Qt.AlignCenter)
		self.label_10.setObjectName("label_10")
		self.gridLayout.addWidget(self.label_10, 4, 1, 1, 2)
		self.asdads = QLabel(self)
		self.asdads.setStyleSheet("image: url(" + self.path + "low.png);")
		self.asdads.setText("")
		self.asdads.setObjectName("asdads")
		self.gridLayout.addWidget(self.asdads, 2, 7, 1, 1)
		self.tmin_tomorrow = QLabel(self)
		self.tmin_tomorrow.setStyleSheet("font: 14pt \"HY헤드라인M\";")
		self.tmin_tomorrow.setAlignment(Qt.AlignCenter)
		self.tmin_tomorrow.setObjectName("tmin_tomorrow")
		self.gridLayout.addWidget(self.tmin_tomorrow, 9, 8, 1, 1)
		self.line_5 = QFrame(self)
		self.line_5.setFrameShape(QFrame.VLine)
		self.line_5.setFrameShadow(QFrame.Sunken)
		self.line_5.setObjectName("line_5")
		self.gridLayout.addWidget(self.line_5, 8, 6, 2, 1)
		self.sky_name_today = QLabel(self)
		self.sky_name_today.setStyleSheet("font: 14pt \"HY헤드라인M\";")
		self.sky_name_today.setAlignment(Qt.AlignCenter)
		self.sky_name_today.setObjectName("sky_name_today")
		self.gridLayout.addWidget(self.sky_name_today, 2, 2, 1, 1)
		self.label_12 = QLabel(self)
		self.label_12.setStyleSheet("font: 10pt \"HY헤드라인M\";")
		self.label_12.setAlignment(Qt.AlignCenter)
		self.label_12.setObjectName("label_12")
		self.gridLayout.addWidget(self.label_12, 8, 1, 1, 2)
		self.sky_name_tomorrow = QLabel(self)
		self.sky_name_tomorrow.setStyleSheet("font: 14pt \"HY헤드라인M\";")
		self.sky_name_tomorrow.setAlignment(Qt.AlignCenter)
		self.sky_name_tomorrow.setObjectName("sky_name_tomorrow")
		self.gridLayout.addWidget(self.sky_name_tomorrow, 9, 2, 1, 1)
		self.label_14 = QLabel(self)
		self.label_14.setStyleSheet("font: 10pt \"HY헤드라인M\";")
		self.label_14.setAlignment(Qt.AlignCenter)
		self.label_14.setObjectName("label_14")
		self.gridLayout.addWidget(self.label_14, 8, 7, 1, 2)
		self.label_2 = QLabel(self)
		self.label_2.setStyleSheet("font: 10pt \"HY헤드라인M\";")
		self.label_2.setAlignment(Qt.AlignCenter)
		self.label_2.setObjectName("label_2")
		self.gridLayout.addWidget(self.label_2, 1, 1, 1, 2)
		self.temp_current = QLabel(self)
		self.temp_current.setStyleSheet("font: 14pt \"HY헤드라인M\";")
		self.temp_current.setAlignment(Qt.AlignCenter)
		self.temp_current.setObjectName("temp_current")
		self.gridLayout.addWidget(self.temp_current, 5, 2, 1, 1)
		self.label = QLabel(self)
		self.label.setStyleSheet("font: 11pt \"HY헤드라인M\";\n"
"color : rgb(24, 136, 255);\n"
"border : 1px solid rgb(24, 136, 255);\n"
"background-color: qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(255, 255, 0, 69), stop:0.375 rgba(255, 255, 0, 69), stop:0.423533 rgba(251, 255, 0, 145), stop:0.45 rgba(247, 255, 0, 208), stop:0.477581 rgba(255, 244, 71, 130), stop:0.518717 rgba(255, 218, 71, 130), stop:0.55 rgba(255, 255, 0, 255), stop:0.57754 rgba(255, 203, 0, 130), stop:0.625 rgba(255, 255, 0, 69), stop:1 rgba(255, 255, 0, 69));")
		self.label.setObjectName("label")
		self.gridLayout.addWidget(self.label, 0, 1, 1, 8, Qt.AlignLeft)
		self.dust_str = QLabel(self)
		self.dust_str.setStyleSheet("font: 14pt \"HY헤드라인M\";")
		self.dust_str.setAlignment(Qt.AlignCenter)
		self.dust_str.setObjectName("dust_str")
		self.gridLayout.addWidget(self.dust_str, 5, 7, 1, 2)
		self.label_8 = QLabel(self)
		self.label_8.setStyleSheet("font: 10pt \"HY헤드라인M\";")
		self.label_8.setAlignment(Qt.AlignCenter)
		self.label_8.setObjectName("label_8")
		self.gridLayout.addWidget(self.label_8, 4, 7, 1, 2)
		self.label_11 = QLabel(self)
		self.label_11.setStyleSheet("font: 11pt \"HY헤드라인M\";\n"
"color : rgb(24, 136, 255);\n"
"border : 1px solid rgb(24, 136, 255);\n"
"background-color: qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(255, 255, 0, 69), stop:0.375 rgba(255, 255, 0, 69), stop:0.423533 rgba(251, 255, 0, 145), stop:0.45 rgba(247, 255, 0, 208), stop:0.477581 rgba(255, 244, 71, 130), stop:0.518717 rgba(255, 218, 71, 130), stop:0.55 rgba(255, 255, 0, 255), stop:0.57754 rgba(255, 203, 0, 130), stop:0.625 rgba(255, 255, 0, 69), stop:1 rgba(255, 255, 0, 69));")
		self.label_11.setObjectName("label_11")
		self.gridLayout.addWidget(self.label_11, 7, 1, 1, 8, Qt.AlignLeft)
		self.label_3 = QLabel(self)
		self.label_3.setStyleSheet("font: 10pt \"HY헤드라인M\";")
		self.label_3.setAlignment(Qt.AlignCenter)
		self.label_3.setObjectName("label_3")
		self.gridLayout.addWidget(self.label_3, 1, 7, 1, 2)
		self.line = QFrame(self)
		self.line.setFrameShadow(QFrame.Raised)
		self.line.setLineWidth(5)
		self.line.setFrameShape(QFrame.HLine)
		self.line.setObjectName("line")
		self.gridLayout.addWidget(self.line, 6, 1, 1, 8)
		self.line_3 = QFrame(self)
		self.line_3.setFrameShape(QFrame.VLine)
		self.line_3.setFrameShadow(QFrame.Sunken)
		self.line_3.setObjectName("line_3")
		self.gridLayout.addWidget(self.line_3, 1, 6, 2, 1)
		self.label_22 = QLabel(self)
		self.label_22.setStyleSheet("image: url(" + self.path + "low.png);")
		self.label_22.setText("")
		self.label_22.setObjectName("label_22")
		self.gridLayout.addWidget(self.label_22, 9, 7, 1, 1)
		self.tmin_today = QLabel(self)
		self.tmin_today.setStyleSheet("font: 14pt \"HY헤드라인M\";")
		self.tmin_today.setAlignment(Qt.AlignCenter)
		self.tmin_today.setObjectName("tmin_today")
		self.gridLayout.addWidget(self.tmin_today, 2, 8, 1, 1)
		self.label_9 = QLabel(self)
		self.label_9.setStyleSheet("image: url(" + self.path + "high.png);")
		self.label_9.setText("")
		self.label_9.setAlignment(Qt.AlignCenter)
		self.label_9.setObjectName("label_9")
		self.gridLayout.addWidget(self.label_9, 5, 1, 1, 1)
		self.sky_today = QLabel(self)
		font = QFont()
		font.setFamily("Agency FB")
		font.setPointSize(70)
		self.sky_today.setFont(font)
		self.sky_today.setText("")
		self.sky_today.setObjectName("sky_today")
		self.gridLayout.addWidget(self.sky_today, 2, 1, 1, 1)
		self.sky_tomorrow = QLabel(self)
		font = QFont()
		font.setFamily("Agency FB")
		font.setPointSize(70)
		self.sky_tomorrow.setFont(font)
		self.sky_tomorrow.setText("")
		self.sky_tomorrow.setObjectName("sky_tomorrow")
		self.gridLayout.addWidget(self.sky_tomorrow, 9, 1, 1, 1)
		self.line_4 = QFrame(self)
		self.line_4.setFrameShape(QFrame.VLine)
		self.line_4.setFrameShadow(QFrame.Sunken)
		self.line_4.setObjectName("line_4")
		self.gridLayout.addWidget(self.line_4, 8, 3, 2, 1)
		self.line_7 = QFrame(self)
		self.line_7.setFrameShape(QFrame.VLine)
		self.line_7.setFrameShadow(QFrame.Sunken)
		self.line_7.setObjectName("line_7")
		self.gridLayout.addWidget(self.line_7, 4, 3, 2, 1)
		self.line_2 = QFrame(self)
		self.line_2.setFrameShape(QFrame.VLine)
		self.line_2.setFrameShadow(QFrame.Sunken)
		self.line_2.setObjectName("line_2")
		self.gridLayout.addWidget(self.line_2, 1, 3, 2, 1)
		self.line_8 = QFrame(self)
		self.line_8.setFrameShape(QFrame.VLine)
		self.line_8.setFrameShadow(QFrame.Sunken)
		self.line_8.setObjectName("line_8")
		self.gridLayout.addWidget(self.line_8, 4, 6, 2, 1)
		self.horizontalLayout_2.addLayout(self.gridLayout)

		# set text
		self.tmax_tomorrow.setText("20 도")
		self.label_4.setText("최고온도")
		self.label_13.setText("최고온도")
		self.label_18.setText("미세먼지")
		self.tmax_today.setText("20 도")
		self.dust.setText("36m")
		self.label_10.setText("현재온도")
		self.tmin_tomorrow.setText("11도")
		self.sky_name_today.setText("맑음")
		self.label_12.setText("하늘")
		self.sky_name_tomorrow.setText("맑음")
		self.label_14.setText("최저온도")
		self.label_2.setText("구름")
		self.temp_current.setText("15 도")
		self.label.setText("   [오늘의 날씨]   ")
		self.dust_str.setText("보통")
		self.label_8.setText("미세먼지 지수")
		self.label_11.setText("   [내일의 날씨]   ")
		self.label_3.setText("최저온도")
		self.tmin_today.setText("11 도")


	def render(self, info_dict):
		self.sky_today.setStyleSheet("image: url({}.PNG);".format(self.path + info_dict['sky_code']))
		
		self.sky_name_today.setText(info_dict['sky_name'])
		self.tmax_today.setText("{}℃".format(info_dict['t_max']))
		self.tmin_today.setText("{}℃".format(info_dict['t_min']))

		self.temp_current.setText("{}℃".format(info_dict['t_temp']))
		self.dust.setText("{}㎍/㎥".format(info_dict['dust']))
		self.dust_str.setText(info_dict['dust_str'])

		self.sky_tomorrow.setStyleSheet("image: url({}.PNG);".format(self.path + info_dict['tomorrow']['sky_code']))
		self.sky_name_tomorrow.setText(info_dict['tomorrow']['sky_name'])
		self.tmax_tomorrow.setText("{}℃".format(format(info_dict['tomorrow']['t_max'])))
		self.tmin_tomorrow.setText("{}℃".format(format(info_dict['tomorrow']['t_min'])))