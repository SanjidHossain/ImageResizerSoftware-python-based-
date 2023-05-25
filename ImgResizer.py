import os
from PIL import Image
from tkinter import Entry   
import tkinter as tk
from tkinter import filedialog

def resize_images(input_dir, output_dir, new_size):
    # Create the output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Get the list of image files in the input directory
    image_files = [f for f in os.listdir(input_dir) if os.path.isfile(os.path.join(input_dir, f))]

    for file in image_files:
        # Open the image file
        image_path = os.path.join(input_dir, file)
        image = Image.open(image_path)

        # Resize the image
        resized_image = image.resize(new_size)

        # Save the resized image to the output directory
        output_path = os.path.join(output_dir, file)
        resized_image.save(output_path)

        print(f"Resized and saved {file}.")

def browse_input_dir():
    input_dir = filedialog.askdirectory()
    input_entry.delete(0, tk.END)
    input_entry.insert(0, input_dir)

def browse_output_dir():
    output_dir = filedialog.askdirectory()
    output_entry.delete(0, tk.END)
    output_entry.insert(0, output_dir)

def resize_images_gui():
    input_dir = input_entry.get()
    output_dir = output_entry.get()
    width = int(width_entry.get())
    height = int(height_entry.get())
    new_size = (width, height)
    resize_images(input_dir, output_dir, new_size)

# Create the Tkinter window
window = tk.Tk()
window.title("Image Resizer")

# Input Directory
input_label = tk.Label(window, text="Input Directory:")
input_label.pack()
input_entry = tk.Entry(window, width=50)
input_entry.pack()
input_button = tk.Button(window, text="Browse", command=browse_input_dir)
input_button.pack()

# Output Directory
output_label = tk.Label(window, text="Output Directory:")
output_label.pack()
output_entry = tk.Entry(window, width=50)
output_entry.pack()
output_button = tk.Button(window, text="Browse", command=browse_output_dir)
output_button.pack()

# Image Size
size_label = tk.Label(window, text="Image Size (Width x Height):")
size_label.pack()
size_frame = tk.Frame(window)
size_frame.pack()
width_entry = tk.Entry(size_frame, width=10)
width_entry.pack(side=tk.LEFT)
height_entry = tk.Entry(size_frame, width=10)
height_entry.pack(side=tk.LEFT)

# Resize Button
resize_button = tk.Button(window, text="Resize Images", command=resize_images_gui)
resize_button.pack()

# Run the Tkinter event loop
window.mainloop()
