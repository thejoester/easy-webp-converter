import os
import sys
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from PIL import Image

# --- App Config ---
SUPPORTED_FORMATS = (".jpg", ".jpeg", ".png", ".bmp")

# --- Drag-and-drop Support ---
try:
	import tkinterdnd2 as tkdnd
	root = tkdnd.TkinterDnD.Tk()
	DND_ENABLED = True
except ImportError:
	root = tk.Tk()
	DND_ENABLED = False

root.title("Easy WebP Converter")
root.geometry("600x450")
root.resizable(True, True)

# --- Image Conversion ---
def convert_images(file_paths):
	success_count = 0
	for file_path in file_paths:
		try:
			base, ext = os.path.splitext(file_path)
			if ext.lower() not in SUPPORTED_FORMATS:
				continue

			img = Image.open(file_path).convert("RGB")

			# Ensure unique output filename (e.g. name-1.webp)
			out_path = base + ".webp"
			counter = 1
			while os.path.exists(out_path):
				out_path = f"{base}-{counter}.webp"
				counter += 1

			img.save(out_path, "webp")
			write_output(f"✅ {os.path.basename(file_path)} → {os.path.basename(out_path)}")
			success_count += 1
		except Exception as e:
			messagebox.showerror("Conversion Error", f"Error converting {file_path}:\n\n{e}")
	if success_count == 0:
		write_output("⚠️ No supported files were converted.")

# --- Drag-and-drop handler ---
def drop_event_handler(event):
	files = root.tk.splitlist(event.data)
	convert_images(files)

# --- Output Handling ---
def hide_output():
	output_frame.pack_forget()
	output_text.configure(state="normal")
	output_text.delete("1.0", tk.END)
	output_text.configure(state="disabled")

def show_output():
	output_frame.pack(padx=10, pady=(0, 10), fill="both", expand=True)

def write_output(message):
	show_output()
	output_text.configure(state="normal")
	output_text.insert("end", message + "\n")
	output_text.configure(state="disabled")
	output_text.see("end")

# --- Drag Label ---
drag_label = ttk.Label(
	root,
	text="🖼️ Drag and drop image files here (.jpg/.png/.bmp)",
	anchor="center",
	relief="solid",
	padding=40,
	font=("Segoe UI", 11)
)
drag_label.pack(padx=10, pady=10, fill="both", expand=True)

if DND_ENABLED:
	drag_label.drop_target_register(tkdnd.DND_FILES)
	drag_label.dnd_bind('<<Drop>>', drop_event_handler)
else:
	drag_label.config(text="Drag-and-drop not available.\nInstall tkinterdnd2 for full functionality.")

# --- Output Frame ---
output_frame = ttk.Frame(root)

# Header with ❌ button
output_header = ttk.Frame(output_frame)
output_header.pack(fill="x")

output_title = ttk.Label(output_header, text="✅ Conversion Log", anchor="w")
output_title.pack(side="left", padx=(5, 0), pady=2)

close_button = ttk.Button(output_header, text="❌", width=3, command=hide_output)
close_button.pack(side="right", padx=5, pady=2)

# Scrollable output
output_text_frame = ttk.Frame(output_frame)
output_text_frame.pack(fill="both", expand=True)

scrollbar = ttk.Scrollbar(output_text_frame)
scrollbar.pack(side="right", fill="y")

output_text = tk.Text(output_text_frame, wrap="word", height=10, yscrollcommand=scrollbar.set, state="disabled")
output_text.pack(side="left", fill="both", expand=True)

scrollbar.config(command=output_text.yview)

output_frame.pack_forget()

# --- Start GUI ---
if __name__ == "__main__":
	try:
		root.mainloop()
	except Exception as e:
		import traceback
		trace = traceback.format_exc()
		with open("easywebp-error.log", "w") as f:
			f.write(trace)
		messagebox.showerror("Startup Crash", f"{type(e).__name__}: {e}")
