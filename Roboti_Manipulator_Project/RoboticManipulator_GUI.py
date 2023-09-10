import dearpygui.dearpygui as dpg

check_name = "admin"
check_pass = "password"

def Check_Login(sender):
    pass #da completare con il controllo

dpg.create_context()

with dpg.window(label = "Robotic Manipulator Control Environment"):
    
    #Check Login:
    dpg.add_text(label = "Please Insert ID and Password")
    dpg.add_input_text(label = "ID")
    dpg.add_input_text(label = "Password")
    dpg.add_button(label = "Login", callback = Check_Login)



dpg.create_viewport(title = "Robotic Manipulator GUI!", width = 700, height = 700)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()