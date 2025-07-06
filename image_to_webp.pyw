from tkinterdnd2 import DND_FILES, TkinterDnD
import tkinter as tk
from tkinter import messagebox
from PIL import Image
import os
import traceback

def get_unique_output_path(base_path):
	dirname, basename = os.path.split(base_path)
	name, ext = os.path.splitext(basename)
	counter = 1
	new_path = base_path
	while os.path.exists(new_path):
		new_name = f"{name}-{counter}{ext}"
		new_path = os.path.join(dirname, new_name)
		counter += 1
	return new_path

def convert_files(file_list):
	try:
		output = []
		for file in file_list:
			if file.lower().endswith((".jpg", ".jpeg", ".png")):
				try:
					img = Image.open(file)
					output_path = os.path.splitext(file)[0] + ".webp"
					output_path = get_unique_output_path(output_path)
					img.save(output_path, format="webp")
					output.append(f"✅ {os.path.basename(file)} → {os.path.basename(output_path)}")
				except Exception as e:
					output.append(f"❌ {os.path.basename(file)} failed: {str(e)}")
			else:
				output.append(f"⚠️ Skipped: {os.path.basename(file)} (unsupported format)")
		output_text.set("\n".join(output))
	except Exception:
		messagebox.showerror("Unexpected Error", f"A fatal error occurred:\n\n{traceback.format_exc()}")
		output_text.set("❌ Conversion failed.")

def handle_drop(event):
	try:
		files = root.tk.splitlist(event.data)
		output_text.set("⏳ Converting...")
		root.update_idletasks()
		root.after(100, lambda: convert_files(files))
	except Exception:
		messagebox.showerror("Drop Error", f"Something went wrong:\n\n{traceback.format_exc()}")
		output_text.set("❌ Drop failed.")

# GUI setup
root = TkinterDnD.Tk()
root.title("Drag-and-Drop WebP Converter")
root.geometry("400x300")
root.resizable(False, False)

drop_label = tk.Label(
	root,
	text="🎯 Drag and drop image files here (.jpg/.png)",
	bg="#e0e0e0",
	relief="ridge",
	borderwidth=3,
	font=("Segoe UI", 12),
	wraplength=360,
	justify="center"
)
drop_label.pack(expand=True, fill="both", padx=10, pady=10)

output_text = tk.StringVar()
output_label = tk.Label(root, textvariable=output_text, wraplength=380, justify="left", fg="darkgreen")
output_label.pack(pady=(0, 10))

drop_label.drop_target_register(DND_FILES)
drop_label.dnd_bind('<<Drop>>', handle_drop)

try:
	root.mainloop()
except Exception:
	messagebox.showerror("Fatal Error", f"The application crashed:\n\n{traceback.format_exc()}")
