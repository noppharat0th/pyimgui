from imgui_bundle import imgui as ImGui, immapp

def gui():
    style = ImGui.get_style()
    ImGui.style_colors_dark()

    style.window_rounding = 10.0

    ImGui.set_next_window_size(ImGui.ImVec2(700, 500))
    ImGui.begin("window", None, ImGui.WindowFlags_.no_title_bar | ImGui.WindowFlags_.no_resize)
    ImGui.end()

def render():
    immapp.run(gui_function=gui, window_title="Hello ImGui Bundle", window_size=(400, 300))

if __name__ == "__main__":
    render();