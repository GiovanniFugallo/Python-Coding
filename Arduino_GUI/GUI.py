import serial, time
import dearpygui.dearpygui as dpg

dpg.create_context()

def Start_Comunication(sender):
    arduino_comunication = serial.Serial("COM3", 9600)
    time.sleep(1)

def Phase1_Control(sender):
    value = dpg.get_value(sender)

    if (value == 1):
        arduino.write(value)
        print("Value for Phase_1 transmitted to Arduino.")

    else:
        print("Error during the comunication of the Phase_1 value!")

def Phase2_Control(sender):
    value = dpg.get_value(sender)

    if (value == 1):
        arduino.write(value)
        print("Value for Phase_2 transmitted to Arduino.")

    else:
        print("Error during the comunication of the Phase_2 value!")

def Phase3_Control(sender):
    value = dpg.get_value(sender)

    if (value == 1):
        arduino.write(value)
        print("Value for Phase_3 transmitted to Arduino.")

    else:
        print("Error during the comunication of the Phase_3 value!")

def Phase4_Control(sender):
    value = dpg.get_value(sender)

    if (value == 1):
        arduino.write(value)
        print("Value for Phase_4 transmitted to Arduino.")

    else:
        print("Error during the comunication of the Phase_4 value!")

with dpg.window(label = "Arduino Comunications", width = 700, heigth = 700):
    button_1 = dpg.add_button(label = "Start Arduino Comunication", callback = Start_Comunication)
    slider_phase1 = dpg.add_slider_int(label = "Phase 1", default_value = 0, max_value = 1, width = 100, callback = Phase1_Control)
    slider_phase2 = dpg.add_slider_int(label = "Phase 2", default_value = 0, max_value = 1, width = 100, callback = Phase2_Control)
    slider_phase3 = dpg.add_slider_int(label = "Phase 3", default_value = 0, max_value = 1, width = 100, callback = Phase3_Control)
    slider_phase4 = dpg.add_slider_int(label = "Phase 4", default_value = 0, max_value = 1, width = 100, callback = Phase4_Control)


dpg.create_viewport(title = "Arduino Simulation GUI!", width = 700, heigth = 700)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()