from imgui_bundle import imgui as ImGui, immapp
from core.state import SETTING



def gui():
    style = ImGui.get_style()
    ImGui.style_colors_dark()

    style.window_rounding = 10.0

    ImGui.set_next_window_size(ImGui.ImVec2(SETTING.window_width, SETTING.window_height))
    ImGui.begin("window", None, ImGui.WindowFlags_.no_title_bar | ImGui.WindowFlags_.no_resize)

    ImGui.text(SETTING.app_name)

    ImGui.end()

def render():
    immapp.run(gui_function=gui, window_title="Hello ImGui Bundle", window_size=(400, 300))

if __name__ == "__main__":
    render();