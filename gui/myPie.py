from PyQt5 import QtGui , QtWidgets
from PyQt5.QtChart import QChart, QChartView, QPieSeries, QPieSlice
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QVBoxLayout 

class PieChart(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)

        self.widget = QWidget(self)
        self.widget.setObjectName("main")
        self.widget.setStyleSheet("""
                    QWidget#main{
                        border:1px solid #148CD2;
                        border-radius:10px;
                    }
        """)

        data = {"Social media": 50,"Educational": 20,"News": 10,"Other": 20,}
        
        self.create_piechart(data)

        layout = QVBoxLayout (self)        
        layout.addWidget(self.chartview)
        self.widget.setLayout(layout)
        self.widget.setFixedSize(500,400)


    def create_piechart(self,data):
        series = QPieSeries()

        for name, value in data.items():
            _slice = series.append(name, value)
            _slice.setLabelVisible(True) # can be removed if unnecessary
            #_slice.setBrush(color)
            
        chart = QChart()
        chart.legend().hide()
        chart.addSeries(series)
        chart.createDefaultAxes()
        chart.setAnimationOptions(QChart.SeriesAnimations)
        chart.setTitle("Categories")

        chart.legend().setVisible(True)
        chart.legend().setAlignment(Qt.AlignBottom)

        self.chartview = QChartView(chart)
        self.chartview.setRenderHint(QPainter.Antialiasing)