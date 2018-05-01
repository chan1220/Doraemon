from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from util import scale, map_scale, map_value, str_scale


class NeedleGauge(QWidget):
    def __init__(self, parent, rpm=False):
        super(NeedleGauge, self).__init__(parent)
        self.rpm = rpm
        self.FONT_SIZE = 20

        if self.rpm:
            self.FONT_SIZE_NOTE = 13
        else:
            self.FONT_SIZE_NOTE = 10

        self.value = 0
        self.font = QFont()
        self.note_font = QFont()
        self.color = QColor(0x53B9E8)
        self.red_color = QColor(0xFF3643)
        self.brush = QBrush(self.color)
        self.pen = QPen(self.color)
        self.red_pen = QPen(self.red_color)
        self.font.setPixelSize(self.FONT_SIZE)
        self.note_font.setPixelSize(self.FONT_SIZE_NOTE)
        self.pen.setWidth(3)
        self.red_pen.setWidth(3)

        if self.rpm:
            s = scale(0, 5000, 1000)
        else:
            s = scale(0, 200, 20)

        self.angles = map_scale(s, 0, 270)

        if self.rpm:
            self.str_scale, self.multiplier = str_scale(s, 1000)
        else:
            self.str_scale, self.multiplier = str_scale(s, 1)

        self.red_angle = 270

        if self.rpm:
            self.red_angle = map_value(4000, 0, 5000, 0, 270)
        else:
            self.red_angle = map_value(150, 0, 200, 0, 270)

    def render(self, response):
        self.value = response
        self.update()

    def sizeHint(self):
        return QSize(350, 300)

    def paintEvent(self, e):
        r = min(self.width(), self.height()) / 2
        self.__text_r = r - (r / 10)   # radius of the text
        self.__tick_r = r - (r / 4)    # outer radius of the tick marks
        self.__tick_l = (r / 10)       # length of each tick, extending inwards
        self.__needle_l = (r / 5) * 3    # length of the needle

        painter = QPainter()
        painter.begin(self)
        painter.setFont(self.font)
        painter.setPen(self.pen)
        painter.setBrush(self.brush)
        painter.setRenderHint(QPainter.Antialiasing)

        self.draw_title(painter)
        self.draw_multiplier(painter)
        self.draw_numbers(painter)
        self.draw_marks(painter)
        self.draw_needle(painter)

        painter.end()

    def draw_marks(self, painter):
        painter.save()
        painter.translate(self.width() / 2, self.height() / 2)

        # draw the ticks
        end = self.__tick_r - self.__tick_l
        for a in self.angles:
            painter.save()
            painter.rotate(90 + 45 + a)

            if a > self.red_angle:
                painter.setPen(self.red_pen)

            painter.drawLine(self.__tick_r, 0, end, 0)
            painter.restore()

        # draw the arc
        p = -self.__tick_r
        d = 2 * self.__tick_r
        r = QRect(p, p, d, d)

        # arc angles are in 16th of degrees
        s = -(90 + 45) * 16
        l = -self.red_angle * 16
        painter.drawArc(r, s, l)
        painter.setPen(self.red_pen)
        s += l
        l = -(270 - self.red_angle) * 16
        painter.drawArc(r, s, l)
        painter.restore()

    def draw_numbers(self, painter):
        for a, v in zip(self.angles, self.str_scale):
            painter.save()

            if a > self.red_angle:
                painter.setPen(self.red_pen)

            painter.translate(self.width() / 2, self.height() / 2)
            painter.rotate(a)
            painter.rotate(-45)
            painter.translate(-self.__text_r, 0)
            painter.rotate(45)
            painter.rotate(-a)

            r_width = self.FONT_SIZE * len(v)
            r_height = self.FONT_SIZE
            r = QRect(-r_width / 2, -r_height / 2, r_width, r_height)
            painter.drawText(r, Qt.AlignHCenter | Qt.AlignVCenter, v)
            painter.restore()

    def draw_needle(self, painter):
        painter.save()
        painter.translate(self.width() / 2, self.height() / 2)
        if self.rpm:
            angle = map_value(self.value, 0, 5000, 0, 270)
        else:
            angle = map_value(self.value, 0, 200, 0, 270)
        angle = min(angle, 270)
        angle -= 90 + 45
        painter.rotate(angle)
        painter.drawEllipse(QPoint(0,0), 5, 5)
        painter.drawPolygon(QPolygon([QPoint(-2, 0),
                                      QPoint(0,   -self.__needle_l),
                                      QPoint(2,  0),
                                      QPoint(-2, 0)]))
        painter.restore()

    def draw_title(self, painter):
        painter.save()

        if self.rpm:
            r_height = self.FONT_SIZE + 100
        else:
            r_height = self.FONT_SIZE + 50

        r = QRect(0, self.height() - r_height, self.width(), r_height)

        if self.rpm:
            painter.drawText(r, Qt.AlignHCenter | Qt.AlignVCenter, 'RPM')
        else:
            painter.drawText(r, Qt.AlignHCenter | Qt.AlignVCenter, 'Speed')

        painter.restore()

    def draw_multiplier(self, painter):
        if self.multiplier > 1:
            painter.save()
            painter.setFont(self.note_font)
            s = 'x' + str(self.multiplier)
            r = QRect(0, -self.width() / 6, self.width(), self.height())
            painter.drawText(r, Qt.AlignHCenter | Qt.AlignVCenter, s)
            painter.restore()