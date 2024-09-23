 
from PySide6.QtWidgets import QWidget, QPushButton
from PySide6.QtCore import QEvent
from ui_widget import Ui_widget
import webbrowser

class Widget(QWidget, Ui_widget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Gas Bill Calculator")
        self.setMaximumHeight(500)
        self.setMaximumWidth(800)

        # Connect the "Calculate" button to the gasCal 
        self.pushCalculate.clicked.connect(self.gasCal)

        # Connect the "OnlineBill" button to the onlineBill 
        self.pushOnlineBill.clicked.connect(self.onlineBill)

        # Connect keypad buttons
        self.push_0.clicked.connect(self.keypad)
        self.push_1.clicked.connect(self.keypad)
        self.push_2.clicked.connect(self.keypad)
        self.push_3.clicked.connect(self.keypad)
        self.push_4.clicked.connect(self.keypad)
        self.push_5.clicked.connect(self.keypad)
        self.push_6.clicked.connect(self.keypad)
        self.push_7.clicked.connect(self.keypad)
        self.push_8.clicked.connect(self.keypad)
        self.push_9.clicked.connect(self.keypad)
        self.push_c.clicked.connect(self.keypad)
        self.push_dot.clicked.connect(self.keypad)

        # Set focus handlers for input fields
        self.preReading.installEventFilter(self)
        self.curReading.installEventFilter(self)
        self.factor.installEventFilter(self)
        self.gcv.installEventFilter(self)
        self.fixCharg.installEventFilter(self)
        self.meterRent.installEventFilter(self)

    # Variables to track active input fields
        self.active_field = None  

    def eventFilter(self, source, event):
        if event.type() == QEvent.FocusIn:  
            if source == self.preReading:
                self.active_field = 'preReading'
            elif source == self.curReading:
                self.active_field = 'curReading'
            elif source == self.factor:
                self.active_field = 'factor'
            elif source == self.gcv:
                self.active_field = 'gcv'
            elif source == self.fixCharg:
                self.active_field = 'fixCharg'
            elif source == self.meterRent:
                self.active_field = 'meterRent'

        return super(Widget, self).eventFilter(source, event)

    def keypad(self):
        button = self.sender()

        # Connect Clear button
        if button.text() == "C":
            self.preReading.setText("")
            self.curReading.setText("")
            self.factor.setText("")
            self.gcv.setText("")
            self.fixCharg.setText("")
            self.meterRent.setText("")
         

    # Enter data to the active field.
        if self.active_field == 'preReading':
            current_text_pre = self.preReading.text()
            self.preReading.setText(current_text_pre + button.text())

        elif self.active_field == 'curReading':
            current_text_cur = self.curReading.text()
            self.curReading.setText(current_text_cur + button.text())

        elif self.active_field == 'factor':
            current_text_fac = self.factor.text()
            self.factor.setText(current_text_fac + button.text())

        elif self.active_field == 'gcv':
            current_text_gcv = self.gcv.text()
            self.gcv.setText(current_text_gcv + button.text())

        elif self.active_field == 'fixCharg':
            current_text_fixCharg = self.fixCharg.text()
            self.fixCharg.setText(current_text_fixCharg + button.text())

        elif self.active_field == 'meterRent':
            current_text_rent = self.meterRent.text()
            self.meterRent.setText(current_text_rent + button.text())



# Gas Bill Calculation 

    def gasCal(self):
        try:
            # Input readings from the form
            previous_reading = int(self.preReading.text())
            current_reading = int(self.curReading.text())
            difference = current_reading - previous_reading

            # Input factors from the form
            factor = float(self.factor.text())
            gcv = float(self.gcv.text())
            fix = float(self.fixCharg.text())
            meter_rent = float(self.meterRent.text())

            # Calculate hm3 and mmbtu
            hm3 = (difference * factor) / 100000
            mmbtu = (hm3 * gcv) / 281.7385

            # Gas Tarif slabs for Islamabad Region
            s1 = 500 / 0.25
            s2 = 850 / 0.60
            s3 = 1250 / 1.0
            s4 = 1450 / 1.5
            s5 = 1900 / 2.0
            s6 = 3300 / 3.0
            s7 = 3800 / 4.0
            s8 = 4200

            # Rate based on mmbtu slab
            if hm3 <= 0.25:
                rate = s1
            elif 0.25 < hm3 <= 0.60:
                rate = s2
            elif 0.60 < hm3 <= 1.0:
                rate = s3
            elif 1.0 < hm3 <= 1.5:
                rate = s4
            elif 1.5 < hm3 <= 2.0:
                rate = s5
            elif 2.0 < hm3 <= 3.0:
                rate = s6
            elif 3.0 < hm3 <= 4.0:
                rate = s7
            else:
                rate = s8

            # Calculate GST based on 18%
            gst = (rate + meter_rent + fix) * 0.18  

            # Calculate final amount
            final_amount = rate + meter_rent + fix + gst

            # Output the results in the PlainTextEdit widget
            self.totAmount.setPlainText(f"Gas charges: {rate}\nGST: {gst}\nFinal Amount: {final_amount}")
        
        except ValueError:
            self.totAmount.setPlainText("Invalid input! Please enter numeric values.")

    def onlineBill(self):
        # Open the online bill webpage
        webbrowser.open("https://www.sngpl.com.pk/login.jsp?mdids=85")
        