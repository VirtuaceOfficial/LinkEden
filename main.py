import dearpygui.dearpygui as dpg
import ctypes

# Get the screen dimensions
user32 = ctypes.windll.user32
screen_width = user32.GetSystemMetrics(0)
screen_height = user32.GetSystemMetrics(1)

# Set the window dimensions
window_width = int(screen_width * 0.30)  # Adjusted to 30% of the screen width
window_height = int(screen_height * 0.40)

# Create the Dear PyGui context
dpg.create_context()

# Create the main window
with dpg.window(label="Log In", width=window_width, height=window_height, tag="main_window", no_move=True, no_resize=True, no_close=True, no_title_bar=True):
    with dpg.font_registry():
        default_font_size = int(window_height * 0.05)  # Adjust the initial font size to be 5% of the window height
        default_font = dpg.add_font("C:/Windows/Fonts/Verdana.ttf", default_font_size)
    dpg.bind_font(default_font)
    dpg.add_text("Welcome To LinkEden! The only useful job finding tool to exist.", tag="welcome_text", pos=(10, 10))
    
    # Add text fields for user input
    dpg.add_input_text(label="Client ID", hint="Enter your Client ID", pos=(10, 50), width=window_width - 20, align=dpg.mvAlign_Center)
    dpg.add_input_text(label="Client Secret", hint="Enter your Client Secret", pos=(10, 90), width=window_width - 20, align=dpg.mvAlign_Center)
    dpg.add_input_text(label="Access Token", hint="Enter your Access Token", pos=(10, 130), width=window_width - 20, align=dpg.mvAlign_Center)

# Create the viewport
dpg.create_viewport(title='LinkEden', width=window_width, height=window_height, resizable=False)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
