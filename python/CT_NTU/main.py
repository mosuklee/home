import sys      
from PyQt5.QtWidgets import QApplication, QDialog, QTableWidgetItem
import pandas as pd
import enviro  # enviro.py파일을 읽어들인다.

# UI file을 불러와 사용
from PyQt5 import uic
form_class = uic.loadUiType('./UI_Files/scr_uifiles.ui')[0]

class MyWindow(QDialog, form_class):
    # input_data = []

    def __init__(self):  # 초기화 구문임
        super().__init__()  # 상위 클래스를 최기화하여 메서드를 가져오는데 super()로 실행시 실제 클래스이름 지정하지 않아도 됨
        self.setUI()
        self.input_data = [14.037, 3.439, 8.137, 73.502, 0.0, 0.885, 100000, 240, 40, 10, 2.5, 40, 20, 2.0, 5.0]
        self.text_label_1.clear()
        self.setTableWidgetData()
        self.item_comp.setColumnWidth(0, 130)

        # Input_data의 list를 메인메뉴의 입력상자에 각각 입력한다.
        self.text_input_1.setText(str(self.input_data[6]))
        self.text_input_2.setText(str(self.input_data[7]))
        self.text_input_3.setText(str(self.input_data[8]))
        self.text_input_4.setText(str(self.input_data[9]))
        self.text_input_5.setText(str(self.input_data[10]))
        self.text_input_6.setText(str(self.input_data[11]))
        self.text_input_7.setText(str(self.input_data[12]))
        # self.text_input_8.setText(str(self.input_data[13])) 희석수 유량을 별도로 게산하여 삭제함
        self.text_input_9.setText(str(self.input_data[13]))
        self.text_input_10.setText(str(self.input_data[14]))

    def setUI(self):
        self.setupUi(self)
        self.pushButton.clicked.connect(self.buttonClick)

    def setTableWidgetData(self):
        # input_data의 list를 table wedget spread sheet에 입력한다.
        self.item_comp.setItem(0, 0, QTableWidgetItem(str(self.input_data[0])))
        self.item_comp.setItem(1, 0, QTableWidgetItem(str(self.input_data[1])))
        self.item_comp.setItem(2, 0, QTableWidgetItem(str(self.input_data[2])))
        self.item_comp.setItem(3, 0, QTableWidgetItem(str(self.input_data[3])))
        self.item_comp.setItem(4, 0, QTableWidgetItem(str(self.input_data[4])))
        self.item_comp.setItem(5, 0, QTableWidgetItem(str(self.input_data[5])))

    def buttonClick(self):
        inlet_gas_composition = pd.DataFrame(
            [[0.00, 0.0, 0.0, 0.0, 0.0],
             [0.00, 0.0, 0.0, 0.0, 0.0],
             [0.00, 0.0, 0.0, 0.0, 0.0],
             [0.00, 0.0, 0.0, 0.0, 0.0],
             [0.00, 0.0, 0.0, 0.0, 0.0],
             [0.00, 0.0, 0.0, 0.0, 0.0],
             [0.00, 0.0, 0.0, 0.0, 0.0]],
            index=['O2', 'CO2', 'H2O', 'N2', 'SO2', 'AR', 'TOTAL'],
            columns=['W%', 'kg/mole', 'partial_weight', 'partial_mole', 'mol%'])

        # 1. SCR 입구조건
        # 1.1 배기가스 유량
        flow_rate_weight = float(self.text_input_1.toPlainText())

        # 1.2 가스조성입력 (w%)
        # 텍스트박스에 입력된 가스조성을 계산변수에 입력한다.
        inlet_gas_composition['W%']['O2'] = float(self.item_comp.item(0, 0).text())
        inlet_gas_composition['W%']['CO2'] = float(self.item_comp.item(1, 0).text())
        inlet_gas_composition['W%']['H2O'] = float(self.item_comp.item(2, 0).text())
        inlet_gas_composition['W%']['N2'] = float(self.item_comp.item(3, 0).text())
        inlet_gas_composition['W%']['SO2'] = float(self.item_comp.item(4, 0).text())
        inlet_gas_composition['W%']['AR'] = float(self.item_comp.item(5, 0).text())
        inlet_gas_composition['W%']['TOTAL'] = float(inlet_gas_composition['W%'].sum())

        # 1.3 입구 온도
        inlet_gas_temp = float(self.text_input_2.toPlainText())  # C

        # 2. 배기가스  NOx 농도
        # 2.1 SCR 입구농도
        Nox_inlet_concentra = float(self.text_input_3.toPlainText())  # 인입가스 : ppm(15)
        # 2.2 SCR 출구농도
        Nox_outlet_concentra = float(self.text_input_4.toPlainText())  # 출구가스 : ppm(15)

        # 3. 기    타
        # 3.1 SCR 열손실율
        heatloss_surface = float(self.text_input_5.toPlainText())
        # 3.2 당량비
        equiv_ratio = float(self.text_input_9.toPlainText())
        # 3.3 요소수 농도
        urea_concentra = float(self.text_input_6.toPlainText())
        # 3.4 희석수 온도
        inlet_water_temp = float(self.text_input_7.toPlainText())
        # 3.5 희석수 유량 (kg/h)
        # inlet_water_flowrate = float(self.text_input_8.toPlainText()) 희석수 유량을 별도로 계산하여 삭제함

        # 성분별 질량입력
        inlet_gas_composition['kg/mole']['O2'] = 32
        inlet_gas_composition['kg/mole']['CO2'] = 44.01
        inlet_gas_composition['kg/mole']['H2O'] = 18.016
        inlet_gas_composition['kg/mole']['N2'] = 28.02
        inlet_gas_composition['kg/mole']['SO2'] = 64.07
        inlet_gas_composition['kg/mole']['AR'] = 39.948
        inlet_gas_composition['kg/mole']['TOTAL'] = inlet_gas_composition['kg/mole']['O2'] + \
                                                    inlet_gas_composition['kg/mole']['CO2'] + \
                                                    inlet_gas_composition['kg/mole']['H2O'] + \
                                                    inlet_gas_composition['kg/mole']['N2'] + \
                                                    inlet_gas_composition['kg/mole']['SO2'] + \
                                                    inlet_gas_composition['kg/mole']['AR']

        # partial weight 계산
        inlet_gas_composition['partial_weight'] = inlet_gas_composition['W%'] * inlet_gas_composition['kg/mole'] / 100.0
        inlet_gas_composition['partial_weight']['TOTAL'] = inlet_gas_composition['partial_weight']['O2'] + \
                                                           inlet_gas_composition['partial_weight']['CO2'] + \
                                                           inlet_gas_composition['partial_weight']['H2O'] + \
                                                           inlet_gas_composition['partial_weight']['N2'] + \
                                                           inlet_gas_composition['partial_weight']['SO2'] + \
                                                           inlet_gas_composition['partial_weight']['AR']

        # partial mole 계산
        inlet_gas_composition['partial_mole'] = inlet_gas_composition['W%'] / inlet_gas_composition['kg/mole'] / 100.0
        inlet_gas_composition['partial_mole']['TOTAL'] = inlet_gas_composition['partial_mole']['O2'] + \
                                                         inlet_gas_composition['partial_mole']['CO2'] + \
                                                         inlet_gas_composition['partial_mole']['H2O'] + \
                                                         inlet_gas_composition['partial_mole']['N2'] + \
                                                         inlet_gas_composition['partial_mole']['SO2'] + \
                                                         inlet_gas_composition['partial_mole']['AR']

        # mol% 계산 (일반적으로 v%와 mol%는 같다.)
        inlet_gas_composition['mol%'] = inlet_gas_composition['partial_mole'] / inlet_gas_composition['partial_mole'][
            'TOTAL'] * 100
        inlet_gas_composition['mol%']['TOTAL'] = inlet_gas_composition['mol%']['O2'] + \
                                                 inlet_gas_composition['mol%']['CO2'] + \
                                                 inlet_gas_composition['mol%']['H2O'] + \
                                                 inlet_gas_composition['mol%']['N2'] + \
                                                 inlet_gas_composition['mol%']['SO2'] + \
                                                 inlet_gas_composition['mol%']['AR']

        # 체적유량 계산
        flow_rate_volume = flow_rate_weight / inlet_gas_composition['partial_weight']['TOTAL'] * 22.4
        # self.text_label_1.setText("체적유량 : " + str(flow_rate_volume) + "m3/h"+"\n")

        new_text = "체적유량      : " + str('%10.2f' % flow_rate_volume) + " Sm3/h" + "\n"
        exist_text = ""
        exist_text = exist_text + new_text

        # 열 및 물질수지 계산
        # 계산된 가스조성입력 (V%)
        # mol%와 Volume %는 동일하므로 mol%를 V%에 입력한다
        inlet_gas_composition['V%'] = inlet_gas_composition['mol%']
        inlet_gas_composition['V%']['O2'] = inlet_gas_composition['mol%']['O2']
        inlet_gas_composition['V%']['CO2'] = inlet_gas_composition['mol%']['CO2']
        inlet_gas_composition['V%']['H2O'] = inlet_gas_composition['mol%']['H2O']
        inlet_gas_composition['V%']['N2'] = inlet_gas_composition['mol%']['N2']
        inlet_gas_composition['V%']['SO2'] = inlet_gas_composition['mol%']['SO2']
        inlet_gas_composition['V%']['AR'] = inlet_gas_composition['mol%']['AR']

        inlet_gas_composition['V%']['TOTAL'] = inlet_gas_composition['mol%']['TOTAL']

        # partial gas volume을 계산한다.
        inlet_gas_composition['gas_volume'] = 0.0
        inlet_gas_composition['gas_volume']['O2'] = flow_rate_volume * inlet_gas_composition['V%']['O2'] / 100
        inlet_gas_composition['gas_volume']['CO2'] = flow_rate_volume * inlet_gas_composition['V%']['CO2'] / 100
        inlet_gas_composition['gas_volume']['H2O'] = flow_rate_volume * inlet_gas_composition['V%']['H2O'] / 100
        inlet_gas_composition['gas_volume']['N2'] = flow_rate_volume * inlet_gas_composition['V%']['N2'] / 100
        inlet_gas_composition['gas_volume']['SO2'] = flow_rate_volume * inlet_gas_composition['V%']['SO2'] / 100
        inlet_gas_composition['gas_volume']['AR'] = flow_rate_volume * inlet_gas_composition['V%']['AR'] / 100

        inlet_gas_composition['gas_volume']['TOTAL'] = inlet_gas_composition['gas_volume']['O2'] + \
                                                       inlet_gas_composition['gas_volume']['CO2'] + \
                                                       inlet_gas_composition['gas_volume']['H2O'] + \
                                                       inlet_gas_composition['gas_volume']['N2'] + \
                                                       inlet_gas_composition['gas_volume']['SO2'] + \
                                                       inlet_gas_composition['gas_volume']['AR']

        inlet_gas_composition['gas_volume_dry'] = 0.0
        inlet_gas_composition['gas_volume_dry']['O2'] = inlet_gas_composition['gas_volume']['O2']
        inlet_gas_composition['gas_volume_dry']['CO2'] = inlet_gas_composition['gas_volume']['CO2']
        inlet_gas_composition['gas_volume_dry']['H2O'] = 0.0
        inlet_gas_composition['gas_volume_dry']['N2'] = inlet_gas_composition['gas_volume']['N2']

        inlet_gas_composition['gas_volume_dry']['TOTAL'] = inlet_gas_composition['gas_volume_dry']['O2'] + \
                                                           inlet_gas_composition['gas_volume_dry']['CO2'] + \
                                                           inlet_gas_composition['gas_volume_dry']['N2']

        inlet_gas_composition['V%_dry'] = 0.0
        inlet_gas_composition['V%_dry']['O2'] = inlet_gas_composition['gas_volume_dry']['O2'] / \
                                                inlet_gas_composition['gas_volume_dry']['TOTAL'] * 100
        inlet_gas_composition['V%_dry']['CO2'] = inlet_gas_composition['gas_volume_dry']['CO2'] / \
                                                 inlet_gas_composition['gas_volume_dry']['TOTAL'] * 100
        inlet_gas_composition['V%_dry']['N2'] = inlet_gas_composition['gas_volume']['N2'] / \
                                                inlet_gas_composition['gas_volume_dry']['TOTAL'] * 100
        inlet_gas_composition['V%_dry']['TOTAL'] = inlet_gas_composition['V%_dry']['O2'] + \
                                                   inlet_gas_composition['V%_dry']['CO2'] + \
                                                   inlet_gas_composition['V%_dry']['N2']

        # ---------------------------------------------
        # 정적비열계산 제거부분
        # ---------------------------------------------
        # 화공약품 계산
        # 제거율
        NOx_inlet_ppm = Nox_inlet_concentra
        NOx_outlet_ppm = Nox_outlet_concentra
        NOx_elu_eff = (NOx_inlet_ppm - NOx_outlet_ppm) / NOx_inlet_ppm * 100

        new_text = '제거율        : ' + str('%10.2f' % NOx_elu_eff) + ' %' + "\n"
        exist_text = exist_text + new_text

        NOx_elu_volume = inlet_gas_composition['gas_volume_dry']['TOTAL'] * (NOx_inlet_ppm / 1000000.0) * (
                NOx_elu_eff / 100.0) * (21 - inlet_gas_composition['V%_dry']['O2']) / (21 - 15)

        new_text = '제거량        : ' + str('%10.2f' % NOx_elu_volume) + ' Sm3/h' + "\n"
        exist_text = exist_text + new_text

        urea_specific_gravity = 1.33
        urea_use_qty = NOx_elu_volume * 0.5 * 60 / 22.4 * equiv_ratio / (urea_concentra / 100) * urea_specific_gravity

        new_text = '당량비        : ' + str('%10.2f' % equiv_ratio) + "\n"
        exist_text = exist_text + new_text
        new_text = '요소수 사용량 : ' + str('%10.2f' % (urea_use_qty / urea_specific_gravity)) + ' kg/h   (@40% urea)' + "\n"
        exist_text = exist_text + new_text
        new_text = '요소수 사용량 : ' + str('%10.2f' % urea_use_qty) + ' lit/h  (@40% urea)' + "\n"
        exist_text = exist_text + new_text

        # 5% 요소수 공급시 물사용량
        spray_urea_concentra = float(self.text_input_10.toPlainText()) / 100.0
        water_spray_qty = (urea_use_qty / urea_specific_gravity) * (urea_concentra / 100) / spray_urea_concentra * (
                1 - spray_urea_concentra)

        new_text = 'Water Spray량 : ' + str('%10.2f' % water_spray_qty) + ' kg/h' + "\n"
        exist_text = exist_text + new_text

        # 열 및 물질수지 계산
        # 표면열손실율 : 2.5%

        # 정적비열 계산
        cp_fluegas = enviro.cp_g(0, inlet_gas_composition['V%']['N2'], inlet_gas_composition['V%']['O2'], 0,
                                 inlet_gas_composition['V%']['H2O'], inlet_gas_composition['V%']['CO2'], 0, 0,
                                 inlet_gas_temp)

        heat_inlet = flow_rate_volume * cp_fluegas * inlet_gas_temp
        heat_water_inlet = water_spray_qty * 1 * inlet_water_temp
        heat_inlet_total = heat_inlet + heat_water_inlet
        heat_outlet_surface = heat_inlet_total * heatloss_surface / 100

        # Flue Gas Temp
        temp_fluegas_outlet = heat_inlet_total - heat_outlet_surface
        cpg_tg = temp_fluegas_outlet / flow_rate_volume

        # water량등 추가 계산
        temp_fluegas_outlet = inlet_gas_temp
        for i in range(1, 5):
            temp_inlet = temp_fluegas_outlet
            cp_outlet = enviro.cp_g(0, inlet_gas_composition['V%']['N2'], inlet_gas_composition['V%']['O2'], 0,
                                    inlet_gas_composition['V%']['H2O'], inlet_gas_composition['V%']['CO2'], 0, 0,
                                    temp_fluegas_outlet)
            temp_fluegas_outlet = cpg_tg / cp_outlet
        new_text = 'SCR 출구온도  : ' + str('%10.2f' % temp_fluegas_outlet) + ' (℃)' + "\n"
        exist_text = exist_text + new_text

        # 계산된 값을 text_label_1에 나타낸다
        self.text_label_1.setText(exist_text)

    # < Calculation Module -END >


#####################
## 프로그램 실행 구문 ##
#####################
if __name__ == "__main__":
    # __main__은 자기자신이 호출할 경우 실행하라는 의미임
    # 만일 다른 프로그램에서 호출할 경우 실행되지 않음

    # 다음 실행은 app에서 app.exec()까지 무한 루프로 실행되는 구간임, 상단의 함수를 실행할 경우 여기에서 실행하면 됨
    # ----------------------------------------
    # 콘솔에 hello world를 출력한다.
    app = QApplication(sys.argv)
    myApp = MyWindow()
    myApp.show()
    app.exec_()
