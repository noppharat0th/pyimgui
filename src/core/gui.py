from imgui_bundle import ImColor, imgui

class Gui():
    def draw():
        draw = imgui.get_window_draw_list()
        pos = imgui.get_cursor_screen_pos()

        red_color = imgui.get_color_u32((1.0, 0.0, 0.0, 1.0))
        draw.add_rect_filled(pos, imgui.ImVec2(pos.x + 20, pos.y + 20), red_color)