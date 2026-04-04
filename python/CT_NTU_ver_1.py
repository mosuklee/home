# *********************************
# *TOWER DEMAND (NTU) CALCULATION *
# *********************************

# -------------
# [lib install]
# -------------
import psychrolib
psychrolib.SetUnitSystem(psychrolib.IP)


# ------------
# [Input Data]
# ------------

# Air side
# [Design Tower Data]
alt_feet_design = 0
air_DBT_design = 85.82
air_WBT_design = 80.60
water_mass_flow_design = 2410  # GPM
air_mass_flow_design = 9227    # Lb/min
approch_design = 9.0

# [New Tower Data]
alt_feet_new = 0
air_DBT_new = 9/5*(2)+32
air_WBT_new = 9/5*(0.46)+32
water_mass_flow_new = 1513  # GPM
air_mass_flow_new = 9227    # Lb/min

# alt_feet_new = 0
# air_DBT_new = 9/5*(6.58)+32
# air_WBT_new = 9/5*(4.73)+32
# water_mass_flow_new = 1513  #GPM
# air_mass_flow_new = 9227    # Lb/min

# Water side
# [Design Tower Data]
hot_water_temperature_design = 98.60
cold_water_temperature_design = air_WBT_design + approch_design

# [New Tower Data]
hot_water_temperature_new = 9/5*(14.325)+32
#cold_water_temperature_new = air_WBT_new + approch_new

# Tower
tower_m = -0.8

# SPLASH FILL의 경우 : - 0.5 ~ -0.6
# FILM FILL의   경우 :  -0.7 ~ -0.8



# *********************************
# *TOWER DEMAND (NTU) CALCULATION *
# *********************************

# [Input Data]
# ------------

# Air side
# [Design Tower Data]
alt_feet_design = 0
air_DBT_design = 85.82
air_WBT_design = 80.60
water_mass_flow_design = 2410  # GPM
air_mass_flow_design = 9227    # Lb/min
approch_design = 9.0

# [New Tower Data]
alt_feet_new = 0
air_DBT_new = 9/5*(2)+32
air_WBT_new = 9/5*(0.46)+32
water_mass_flow_new = 1513  # GPM
air_mass_flow_new = 9227    # Lb/min

# alt_feet_new = 0
# air_DBT_new = 9/5*(6.58)+32
# air_WBT_new = 9/5*(4.73)+32
# water_mass_flow_new = 1513  #GPM
# air_mass_flow_new = 9227    # Lb/min

# Water side
# [Design Tower Data]
hot_water_temperature_design = 98.60
cold_water_temperature_design = air_WBT_design + approch_design

# [New Tower Data]
hot_water_temperature_new = 9/5*(14.325)+32
#cold_water_temperature_new = air_WBT_new + approch_new

# Tower
tower_m = -0.8

# SPLASH FILL의 경우 : - 0.5 ~ -0.6
# FILM FILL의   경우 :  -0.7 ~ -0.8
# Calculation
# -----------

l_g_ratio_design = water_mass_flow_design * (500/60) / air_mass_flow_design
l_g_ratio_new = water_mass_flow_new * (500/60) / air_mass_flow_new
heat_load_design = water_mass_flow_design * \
    (500/60) * (hot_water_temperature_design-cold_water_temperature_design)
cooling_range_design = hot_water_temperature_design - cold_water_temperature_design
cooling_range_new = heat_load_design/(water_mass_flow_new*(500/60))

# print(cooling_range_design,cooling_range_new)


def ntu(water_mass_flow, air_mass_flow, hot_water_temperature, cold_water_temperature, alt_feet, air_DBT, air_WBT, id):

    chk = 0
    # [Design Tower Calculation]

    l_g_ratio = water_mass_flow * (500/60) / air_mass_flow
    cooling_range = hot_water_temperature - cold_water_temperature
    vap_press = psychrolib.GetStandardAtmPressure(alt_feet)
    HumRatio = psychrolib.GetHumRatioFromTWetBulb(air_DBT, air_WBT, vap_press)

    tw0 = cold_water_temperature
    # print(tw0,cooling_range)
    tw1 = tw0+0.1 * cooling_range
    tw2 = tw0+0.4 * cooling_range
    tw3 = tw0+0.6 * cooling_range
    tw4 = tw0+0.9 * cooling_range

    hw0 = psychrolib.GetSatAirEnthalpy(tw0, vap_press)
    hw1 = psychrolib.GetSatAirEnthalpy(tw1, vap_press)
    hw2 = psychrolib.GetSatAirEnthalpy(tw2, vap_press)
    hw3 = psychrolib.GetSatAirEnthalpy(tw3, vap_press)
    hw4 = psychrolib.GetSatAirEnthalpy(tw4, vap_press)

    ha0 = psychrolib.GetMoistAirEnthalpy(air_DBT, HumRatio)
    ha1 = ha0 + 0.1*l_g_ratio*cooling_range
    ha2 = ha0 + 0.4*l_g_ratio*cooling_range
    ha3 = ha0 + 0.6*l_g_ratio*cooling_range
    ha4 = ha0 + 0.9*l_g_ratio*cooling_range

    hw1_ha1 = hw1-ha1
    hw2_ha2 = hw2-ha2
    hw3_ha3 = hw3-ha3
    hw4_ha4 = hw4-ha4

    if hw1_ha1 > 0 and hw2_ha2 > 0 and hw3_ha3 > 0 and hw4_ha4 > 0:
        chk = 1

    div_hw1_ha1 = 1/(hw1_ha1)
    div_hw2_ha2 = 1/(hw2_ha2)
    div_hw3_ha3 = 1/(hw3_ha3)
    div_hw4_ha4 = 1/(hw4_ha4)
    sum_div_hw_ha = div_hw1_ha1+div_hw2_ha2+div_hw3_ha3+div_hw4_ha4
    ntu = cooling_range / 4 * (1/hw1_ha1+1/hw2_ha2+1/hw3_ha3+1/hw4_ha4)

    if id == 1:
        ntu_print(alt_feet, hot_water_temperature, air_WBT, cold_water_temperature, water_mass_flow, l_g_ratio, air_mass_flow, cooling_range,
                  tw1, hw1, ha1, hw1_ha1, div_hw1_ha1, tw2, hw2, ha2, hw2_ha2, div_hw2_ha2, tw3, hw3, ha3, hw3_ha3, div_hw3_ha3,
                  tw4, hw4, ha4, hw4_ha4, div_hw4_ha4, sum_div_hw_ha, ntu)

    return ntu, chk


def ntu_new_calc(water_mass_flow, air_mass_flow, hot_water_temperature, cold_water_temperature, alt_feet, air_DBT, air_WBT, id):

    chk = 0
    # [Design Tower Calculation]

    l_g_ratio = water_mass_flow * (500/60) / air_mass_flow
    cooling_range = hot_water_temperature - cold_water_temperature
    vap_press = psychrolib.GetStandardAtmPressure(alt_feet)
    HumRatio = psychrolib.GetHumRatioFromTWetBulb(air_DBT, air_WBT, vap_press)

    #print("air_wet_temp :", air_WBT)
    tw0 = air_WBT_new

    # print(tw0,cooling_range)

    tw1 = air_WBT_new + approch + 0.1 * cooling_range
    tw2 = air_WBT_new + approch + 0.4 * cooling_range
    tw3 = air_WBT_new + approch + 0.6 * cooling_range
    tw4 = air_WBT_new + approch + 0.9 * cooling_range
    # print(tw1,tw2,tw3,tw4)

    hw1 = psychrolib.GetSatAirEnthalpy(tw1, vap_press)
    hw2 = psychrolib.GetSatAirEnthalpy(tw2, vap_press)
    hw3 = psychrolib.GetSatAirEnthalpy(tw3, vap_press)
    hw4 = psychrolib.GetSatAirEnthalpy(tw4, vap_press)
    # print(hw1,hw2,hw3,hw4)

    ha0 = psychrolib.GetMoistAirEnthalpy(air_DBT, HumRatio)
    ha1 = ha0 + 0.1*l_g_ratio*cooling_range
    ha2 = ha0 + 0.4*l_g_ratio*cooling_range
    ha3 = ha0 + 0.6*l_g_ratio*cooling_range
    ha4 = ha0 + 0.9*l_g_ratio*cooling_range
    # print(ha1,ha2,ha3,ha4)

    hw1_ha1 = hw1-ha1
    hw2_ha2 = hw2-ha2
    hw3_ha3 = hw3-ha3
    hw4_ha4 = hw4-ha4

    if hw1_ha1 > 0 and hw2_ha2 > 0 and hw3_ha3 > 0 and hw4_ha4 > 0:
        chk = 1

    div_hw1_ha1 = 1/(hw1_ha1)
    div_hw2_ha2 = 1/(hw2_ha2)
    div_hw3_ha3 = 1/(hw3_ha3)
    div_hw4_ha4 = 1/(hw4_ha4)
    sum_div_hw_ha = div_hw1_ha1+div_hw2_ha2+div_hw3_ha3+div_hw4_ha4
    ntu = cooling_range / 4 * (1/hw1_ha1+1/hw2_ha2+1/hw3_ha3+1/hw4_ha4)
    # print(ntu)
    # print("id:",id)
    if id == 1:
        ntu_new_1_print(alt_feet, hot_water_temperature, air_WBT, cold_water_temperature,
                        water_mass_flow, l_g_ratio, air_mass_flow, cooling_range)
        ntu_new_2_print(tw1, hw1, ha1, hw1_ha1, div_hw1_ha1, tw2, hw2, ha2, hw2_ha2, div_hw2_ha2, tw3, hw3, ha3, hw3_ha3, div_hw3_ha3,
                        tw4, hw4, ha4, hw4_ha4, div_hw4_ha4, sum_div_hw_ha, ntu)

    return ntu, chk


def ntu_print(alt_feet, hot_water_temperature, air_WBT, cold_water_temperature, water_mass_flow, l_g_ratio, air_mass_flow, cooling_range,
              tw1, hw1, ha1, hw1_ha1, div_hw1_ha1, tw2, hw2, ha2, hw2_ha2, div_hw2_ha2, tw3, hw3, ha3, hw3_ha3, div_hw3_ha3,
              tw4, hw4, ha4, hw4_ha4, div_hw4_ha4, sum_div_hw_ha, ntu):

    print('TOWER DEMAND (NTU) CLACULATION')
    print('====================================================================================================')
    print('Altitude (feet)                 {0:6.2f}                    Hot Water Temperature  (F)       {1:6.2f}   '.format(
        alt_feet, hot_water_temperature))
    print('Wet Bulb Temperature@inlet(F)   {0:6.2f}                    Cold Water Temperature (F)       {1:6.2f}   '.format(
        air_WBT, cold_water_temperature))
    print('Water Flow Rate (gpm)           {0:6.0f}                    L/G Ratio                        {1:6.4f}   '.format(
        water_mass_flow, l_g_ratio))
    print('Air Mass Flow Rate (Lb/min)     {0:6.0f}                    Cooling Range (F)                {1:6.2f}   '.format(
        air_mass_flow, cooling_range))
    print('                                                          Approch (F)                      {0:6.2f}   '.format(
        cold_water_temperature-air_WBT))
    print('----------------------------------------------------------------------------------------------------')
    print('              WATER SIDE                                    AIR SIDE                ENTHALPY DIFF')
    print('----------------------------------------------------------------------------------------------------')
    print('            DESCRIPTIONS       tw(F)  hw(BTU/LB)         DESCRIPTIONS     ha(BTU/Lb) hw-ha 1/(hw-ha)')
    print('----------------------------------------------------------------------------------------------------')
    #        WBT + Approch + 0.1 x Range  {0:6.2f}   {1:6.4f}    ha1 + 0.1 x L/G x Range  {2:7.4f}  {3:7.4f}  {4:1.4f} '
    print('       tw1 + 0.1 x Range      {0:6.2f}   {1:6.4f}    ha1 + 0.1 x L/G x Range   {2:7.4f} {3:7.4f}  {4:1.4f} '.format(
        tw1, hw1, ha1, hw1_ha1, div_hw1_ha1))
    print('       tw1 + 0.4 x Range      {0:6.2f}   {1:6.4f}    ha1 + 0.4 x L/G x Range   {2:7.4f} {3:7.4f}  {4:1.4f} '.format(
        tw2, hw2, ha2, hw2_ha2, div_hw2_ha2))
    print('       tw1 + 0.6 x Range      {0:6.2f}   {1:6.4f}    ha1 + 0.6 x L/G x Range   {2:7.4f} {3:7.4f}  {4:1.4f} '.format(
        tw3, hw3, ha3, hw3_ha3, div_hw3_ha3))
    print('       tw1 + 0.9 x Range      {0:6.2f}   {1:6.4f}    ha1 + 0.9 x L/G x Range   {2:7.4f} {3:7.4f}  {4:1.4f} '.format(
        tw4, hw4, ha4, hw4_ha4, div_hw4_ha4))
    print('----------------------------------------------------------------------------------------------------')
    print(
        '              Sum of 1/ (hw - ha)  ..................................  {0:1.4f}    '.format(sum_div_hw_ha))
    print(
        '              Tower Demand (NTU) = sum of 1/(hw-ha)/4 * Range........  {0:1.4f}    '.format(ntu))
    print('====================================================================================================')


def ntu_new_1_print(alt_feet, hot_water_temperature, air_WBT, cold_water_temperature, water_mass_flow, l_g_ratio, air_mass_flow, cooling_range):

    print('TOWER DEMAND (NTU) CLACULATION')
    print('====================================================================================================')
    print('Altitude (feet)                 {0:6.2f}                    Hot Water Temperature  (F)       {1:6.2f}   '.format(
        alt_feet, hot_water_temperature))
    print('Wet Bulb Temperature@inlet(F)   {0:6.2f}                    Cold Water Temperature (F)       {1:6.2f}   '.format(
        air_WBT, cold_water_temperature))
    print('Water Flow Rate (gpm)           {0:6.0f}                    L/G Ratio                        {1:6.4f}   '.format(
        water_mass_flow, l_g_ratio))
    print('Air Mass Flow Rate (Lb/min)     {0:6.0f}                    Cooling Range (F)                {1:6.2f}   '.format(
        air_mass_flow, cooling_range))
    print('                                                          Approch (F)                      {0:6.2f}   '.format(
        cold_water_temperature-air_WBT))


def ntu_new_2_print(tw1, hw1, ha1, hw1_ha1, div_hw1_ha1, tw2, hw2, ha2, hw2_ha2, div_hw2_ha2, tw3, hw3, ha3, hw3_ha3, div_hw3_ha3,
                    tw4, hw4, ha4, hw4_ha4, div_hw4_ha4, sum_div_hw_ha, ntu):

    print('----------------------------------------------------------------------------------------------------')
    print('              WATER SIDE                                    AIR SIDE                ENTHALPY DIFF')
    print('----------------------------------------------------------------------------------------------------')
    print('            DESCRIPTIONS       tw(F)  hw(BTU/LB)         DESCRIPTIONS     ha(BTU/Lb) hw-ha 1/(hw-ha)')
    print('----------------------------------------------------------------------------------------------------')
    print(' WBT + Approch + 0.1 x Range  {0:6.2f}   {1:6.4f}    ha1 + 0.1 x L/G x Range  {2:7.4f}  {3:7.4f}  {4:1.4f} '.format(
        tw1, hw1, ha1, hw1_ha1, div_hw1_ha1))
    print(' WBT + Approch + 0.4 x Range  {0:6.2f}   {1:6.4f}    ha1 + 0.4 x L/G x Range  {2:7.4f}  {3:7.4f}  {4:1.4f} '.format(
        tw2, hw2, ha2, hw2_ha2, div_hw2_ha2))
    print(' WBT + Approch + 0.6 x Range  {0:6.2f}   {1:6.4f}    ha1 + 0.6 x L/G x Range  {2:7.4f}  {3:7.4f}  {4:1.4f} '.format(
        tw3, hw3, ha3, hw3_ha3, div_hw3_ha3))
    print(' WBT + Approch + 0.9 x Range  {0:6.2f}   {1:6.4f}    ha1 + 0.9 x L/G x Range  {2:7.4f}  {3:7.4f}  {4:1.4f} '.format(
        tw4, hw4, ha4, hw4_ha4, div_hw4_ha4))
    print('----------------------------------------------------------------------------------------------------')
    print(
        '              Sum of 1/ (hw - ha)  ..................................  {0:1.4f}    '.format(sum_div_hw_ha))
    print(
        '              Tower Demand (NTU) = sum of 1/(hw-ha)/4 * Range........  {0:1.4f}    '.format(ntu))
    print('====================================================================================================')


def tower_c(ntu_design, l_g_ratio_design, tower_m):

    tower_c_design = ntu_design * (l_g_ratio_design)**(-tower_m)
    #print(' C = KaV/L x (LG1)^m  ..................................  {0:1.4f}    '.format(tower_c_design))
    return tower_c_design


def ntu_corr(water_mass_flow, air_mass_flow, tower_c, tower_m):
    l_g_ratio = water_mass_flow * (500/60) / air_mass_flow
    ntu1 = tower_c*(l_g_ratio)**tower_m
    return ntu1


print("[Design NTU Calculation]")
ntu_design, chk = ntu(water_mass_flow_design, air_mass_flow_design, hot_water_temperature_design,
                      cold_water_temperature_design, alt_feet_design, air_DBT_design, air_WBT_design, 1)
# print(ntu_design,chk)

tower_c_design = tower_c(ntu_design, l_g_ratio_design, tower_m)
print("C :", tower_c_design)
ntu_corr = ntu_corr(water_mass_flow_new, air_mass_flow_new,
                    tower_c_design, tower_m)
print("NTU_corr :", ntu_corr)

print("")
print("[NEW NTU Calculation]")

# ****************************
# *   MAIN NTU Calculation   *
# ****************************
#approch = 10.01
for i in range(1, 500000):
    approch = i*0.0001
    # print("app:",approch)

    cold_water_temperature_new = air_WBT_new + approch
    #hot_water_temperature_new = cold_water_temperature_new+cooling_range_new
    # print("temp:",hot_water_temperature_new)
    # print(water_mass_flow_new,air_mass_flow_new,hot_water_temperature_new,cold_water_temperature_new,alt_feet_new,air_DBT_new,air_WBT_new,1)
    ntu_new, chk = ntu_new_calc(water_mass_flow_new, air_mass_flow_new, hot_water_temperature_new,
                                cold_water_temperature_new, alt_feet_new, air_DBT_new, air_WBT_new, 0)
    # print(ntu_new,chk)
    if chk == 1 and ntu_new < ntu_corr:
        ntu_new, chk = ntu_new_calc(water_mass_flow_new, air_mass_flow_new, hot_water_temperature_new,
                                    cold_water_temperature_new, alt_feet_new, air_DBT_new, air_WBT_new, 1)
        break
print("")
print("[Calculation Check]")
print('Corr. NTU :  {0:1.4}     NEW NTU  : {1:1.4}   Error : {2:1.4}% '.format(
    ntu_corr, ntu_new, 100-(ntu_new/ntu_corr)*100))
print('Iteration :{0:7}'.format(i))
