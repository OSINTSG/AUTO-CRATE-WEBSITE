import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def generate_css():
    css_code = "* {\n\tmargin: 0;\n\tpadding: 0;\n\tbox-sizing: border-box;\n}\n\n"
    css_code += "html, body {\n\theight: 100%;\n\twidth: 100%;\n}\n\n"
    css_code += generate_paragraph_css()
    css_code += generate_div_css()
    css_code += generate_navbar_css()
    css_code += generate_animation_css()

    try:
        with open("style.css", "w") as css_file:
            css_file.write(css_code)
        messagebox.showinfo("Success", "CSS code generated and saved successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to write CSS code to file: {str(e)}")

def generate_paragraph_css():
    font_size = paragraph_font_size_entry.get()
    font_color = paragraph_font_color_entry.get()
    header_size = paragraph_header_size_entry.get()

    css_code = f"h1 {{\n\tcolor: {font_color};\n\tfont-size: {header_size}px;\n\tfont-family: 'Courier New', Courier, monospace;\n\tfont-weight: 800;\n}}\n\n"
    css_code += f"p {{\n\tfont-size: {font_size}px;\n\tcolor: {font_color};\n}}\n\n"
    return css_code

def generate_div_css():
    box_width = div_width_entry.get()
    box_height = div_height_entry.get()
    box_bg_color = div_bg_color_entry.get()
    box_margin_top = div_margin_top_entry.get()
    box_margin_left = div_margin_left_entry.get()
    box_padding_left = div_padding_left_entry.get()

    css_code = f"#box {{\n\theight: {box_height}px;\n\twidth: {box_width}px;\n\tbackground-color: {box_bg_color};\n\tmargin-left: {box_margin_left}px;\n\tmargin-top: {box_margin_top}px;\n\tmargin-bottom: auto;\n\tpadding-left: {box_padding_left}px;\n}}\n\n"
    return css_code

def generate_navbar_css():
    navbar_bg_color = navbar_bg_color_entry.get()
    navbar_font_color = navbar_font_color_entry.get()
    navbar_font_size = navbar_font_size_entry.get()
    navbar_padding = navbar_padding_entry.get()

    css_code = f".navbar {{\n\tbackground-color: {navbar_bg_color};\n\tcolor: {navbar_font_color};\n\tfont-size: {navbar_font_size}px;\n\tpadding: {navbar_padding}px;\n}}\n\n"
    return css_code

def generate_animation_css():
    animation_name = animation_name_entry.get()
    animation_duration = animation_duration_entry.get()
    animation_timing_function = animation_timing_function_entry.get()

    css_code = f"@keyframes {animation_name} {{\n"
    css_code += "\t0% {\n\t\ttransform: rotateY(0deg);\n\t}\n"
    css_code += "\t100% {\n\t\ttransform: rotateY(360deg);\n\t}\n"
    css_code += f"}}\n\n"
    css_code += f"#animatedBox {{\n\tanimation: {animation_name} {animation_duration}s {animation_timing_function} infinite;\n}}\n\n"
    return css_code

# GUI setup
root = tk.Tk()
root.title("CSS Code Generator")

main_frame = ttk.Frame(root, padding="20")
main_frame.grid(row=0, column=0)

# Paragraph Function
paragraph_frame = ttk.LabelFrame(main_frame, text="Paragraph Function")
paragraph_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

paragraph_font_size_label = ttk.Label(paragraph_frame, text="Font Size:")
paragraph_font_size_label.grid(row=0, column=0, sticky="w")

paragraph_font_size_entry = ttk.Entry(paragraph_frame, width=10)
paragraph_font_size_entry.grid(row=0, column=1, sticky="w")

paragraph_font_color_label = ttk.Label(paragraph_frame, text="Font Color:")
paragraph_font_color_label.grid(row=1, column=0, sticky="w")

paragraph_font_color_entry = ttk.Entry(paragraph_frame, width=10)
paragraph_font_color_entry.grid(row=1, column=1, sticky="w")

paragraph_header_size_label = ttk.Label(paragraph_frame, text="Header Size:")
paragraph_header_size_label.grid(row=2, column=0, sticky="w")

paragraph_header_size_entry = ttk.Entry(paragraph_frame, width=10)
paragraph_header_size_entry.grid(row=2, column=1, sticky="w")

# Div Function
div_frame = ttk.LabelFrame(main_frame, text="Div Function")
div_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

div_width_label = ttk.Label(div_frame, text="Width:")
div_width_label.grid(row=0, column=0, sticky="w")

div_width_entry = ttk.Entry(div_frame, width=10)
div_width_entry.grid(row=0, column=1, sticky="w")

div_height_label = ttk.Label(div_frame, text="Height:")
div_height_label.grid(row=1, column=0, sticky="w")

div_height_entry = ttk.Entry(div_frame, width=10)
div_height_entry.grid(row=1, column=1, sticky="w")

div_bg_color_label = ttk.Label(div_frame, text="Background Color:")
div_bg_color_label.grid(row=2, column=0, sticky="w")

div_bg_color_entry = ttk.Entry(div_frame, width=10)
div_bg_color_entry.grid(row=2, column=1, sticky="w")

div_margin_top_label = ttk.Label(div_frame, text="Margin Top:")
div_margin_top_label.grid(row=3, column=0, sticky="w")

div_margin_top_entry = ttk.Entry(div_frame, width=10)
div_margin_top_entry.grid(row=3, column=1, sticky="w")

div_margin_left_label = ttk.Label(div_frame, text="Margin Left:")
div_margin_left_label.grid(row=4, column=0, sticky="w")

div_margin_left_entry = ttk.Entry(div_frame, width=10)
div_margin_left_entry.grid(row=4, column=1, sticky="w")

div_padding_left_label = ttk.Label(div_frame, text="Padding Left:")
div_padding_left_label.grid(row=5, column=0, sticky="w")

div_padding_left_entry = ttk.Entry(div_frame, width=10)
div_padding_left_entry.grid(row=5, column=1, sticky="w")

# Navigation Bar Function
navbar_frame = ttk.LabelFrame(main_frame, text="Navigation Bar Function")
navbar_frame.grid(row=0, column=2, padx=10, pady=10, sticky="nsew")

navbar_bg_color_label = ttk.Label(navbar_frame, text="Background Color:")
navbar_bg_color_label.grid(row=0, column=0, sticky="w")

navbar_bg_color_entry = ttk.Entry(navbar_frame, width=10)
navbar_bg_color_entry.grid(row=0, column=1, sticky="w")

navbar_font_color_label = ttk.Label(navbar_frame, text="Font Color:")
navbar_font_color_label.grid(row=1, column=0, sticky="w")

navbar_font_color_entry = ttk.Entry(navbar_frame, width=10)
navbar_font_color_entry.grid(row=1, column=1, sticky="w")

navbar_font_size_label = ttk.Label(navbar_frame, text="Font Size:")
navbar_font_size_label.grid(row=2, column=0, sticky="w")

navbar_font_size_entry = ttk.Entry(navbar_frame, width=10)
navbar_font_size_entry.grid(row=2, column=1, sticky="w")

navbar_padding_label = ttk.Label(navbar_frame, text="Padding:")
navbar_padding_label.grid(row=3, column=0, sticky="w")

navbar_padding_entry = ttk.Entry(navbar_frame, width=10)
navbar_padding_entry.grid(row=3, column=1, sticky="w")

# Animation Function
animation_frame = ttk.LabelFrame(main_frame, text="Animation Function")
animation_frame.grid(row=0, column=3, padx=10, pady=10, sticky="nsew")

animation_name_label = ttk.Label(animation_frame, text="Animation Name:")
animation_name_label.grid(row=0, column=0, sticky="w")

animation_name_entry = ttk.Entry(animation_frame, width=10)
animation_name_entry.grid(row=0, column=1, sticky="w")

animation_duration_label = ttk.Label(animation_frame, text="Duration (s):")
animation_duration_label.grid(row=1, column=0, sticky="w")

animation_duration_entry = ttk.Entry(animation_frame, width=10)
animation_duration_entry.grid(row=1, column=1, sticky="w")

animation_timing_function_label = ttk.Label(animation_frame, text="Timing Function:")
animation_timing_function_label.grid(row=2, column=0, sticky="w")

animation_timing_function_entry = ttk.Entry(animation_frame, width=10)
animation_timing_function_entry.grid(row=2, column=1, sticky="w")

generate_button = ttk.Button(main_frame, text="Generate CSS", command=generate_css)
generate_button.grid(row=1, columnspan=4)

root.mainloop()
