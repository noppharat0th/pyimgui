from imgui_bundle import imgui as ImGui, immapp

def gui():
    ImGui.style_colors_dark()
    ImGui.show_demo_window()

def render():
    immapp.run(gui_function=gui, window_title="Hello ImGui Bundle", window_size=(400, 300))

if __name__ == "__main__":
    render();