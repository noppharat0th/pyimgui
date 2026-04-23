from imgui_bundle import imgui as ImGui, immapp

def gui():
    ImGui.show_demo_window()

def config():
    ImGui.style_colors_dark()

def render():
    config();
    immapp.run(gui_function=gui, window_title="Hello ImGui Bundle", window_size=(400, 300))

render();