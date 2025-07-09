import os
import sys
import threading
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from PIL import Image

# --- App Config ---
SUPPORTED_FORMATS = (".jpg", ".jpeg", ".png", ".bmp")

# --- Attempt tkinterdnd2 ---
try:
	import tkinterdnd2 as tkdnd
	root = tkdnd.TkinterDnD.Tk()
	dnd_available = True
except ImportError:
	root = tk.Tk()
	dnd_available = False

# --- GUI Setup ---
root.title("Easy WebP Converter")
root.geometry("500x450")
root.minsize(360, 450)
root.resizable(True, True)

# Drag area
drag_label = ttk.Label(
	root,
	text="🖼️ Drag and drop image files here (.jpg/.png/.bmp)" if dnd_available else
	"Drag-and-drop not available.\nInstall tkinterdnd2 for full functionality.",
	anchor="center",
	relief="solid",
	padding=10,
	font=("Segoe UI Emoji", 14) 
)
drag_label.pack(padx=10, pady=10, fill="both", expand=True, ipady=30)

# Output frame (initially hidden)
output_frame = ttk.Frame(root)

# Progress bar
progress_bar = ttk.Progressbar(output_frame, orient="horizontal", mode="determinate")
progress_bar.pack(fill="x", padx=10, pady=(0, 5))
progress_bar["maximum"] = 100
progress_bar["value"] = 0

# Header with ❌ button
output_header = ttk.Frame(output_frame)
output_header.pack(fill="x")

output_title = ttk.Label(output_header, text="✅ Conversion Log", anchor="w")
output_title.pack(side="left", padx=(5, 0), pady=2)

close_button = ttk.Button(output_header, text="❌", width=3, command=lambda: hide_output(clear=True))
close_button.pack(side="right", padx=5, pady=2)

# Scrollable text log
output_text_frame = ttk.Frame(output_frame)
output_text_frame.pack(fill="both", expand=True)

scrollbar = ttk.Scrollbar(output_text_frame)
scrollbar.pack(side="right", fill="y")

output_text = tk.Text(output_text_frame, wrap="word", height=10, yscrollcommand=scrollbar.set, state="disabled")
output_text.pack(side="left", fill="both", expand=True)

scrollbar.config(command=output_text.yview)

output_frame.pack_forget()

# --- Output Helpers ---
def show_output():
	output_frame.pack(padx=10, pady=(0, 10), fill="both", expand=True)

def hide_output(clear=False):
	output_frame.pack_forget()
	output_text.configure(state="normal")
	output_text.delete("1.0", tk.END)
	output_text.configure(state="disabled")
	if clear:
		progress_bar["value"] = 0

def write_output(message, replace_last=False):
	show_output()
	output_text.configure(state="normal")
	if replace_last:
		output_text.delete("end-2l", "end-1l")
	output_text.insert("end", message + "\n")
	output_text.configure(state="disabled")
	output_text.see("end")

def update_progress(current, total):
	percent = int((current / total) * 100)
	root.after(0, lambda: progress_bar.config(value=percent))

# --- Image Conversion ---
def convert_images(file_paths):
	success_count = 0
	total_files = len([f for f in file_paths if os.path.splitext(f)[1].lower() in SUPPORTED_FORMATS])
	processed = 0

	for file_path in file_paths:
		base, ext = os.path.splitext(file_path)
		if ext.lower() not in SUPPORTED_FORMATS:
			continue

		filename = os.path.basename(file_path)
		file_size = os.path.getsize(file_path)
		if file_size < 1_000_000:
			file_size_str = f"{round(file_size / 1024)} KB"
		else:
			file_size_str = f"{round(file_size / (1024 * 1024), 1)} MB"

		root.after(0, lambda f=filename, s=file_size_str: write_output(f"{f} ({s})...", False))

		try:
			img = Image.open(file_path).convert("RGB")

			# Ensure unique output filename
			out_path = base + ".webp"
			counter = 1
			while os.path.exists(out_path):
				out_path = f"{base}-{counter}.webp"
				counter += 1

			img.save(out_path, "webp")
			success_count += 1
			processed += 1

			root.after(0, lambda f=filename, o=os.path.basename(out_path): write_output(f"{f} → {o} ✅", True))
			update_progress(processed, total_files)

		except Exception as e:
			root.after(0, lambda f=filename, err=e: messagebox.showerror("Conversion Error", f"Error converting {f}:\n\n{err}"))

	if success_count == 0:
		root.after(0, lambda: write_output("⚠️ No supported files were converted."))
	else:
		root.after(0, lambda: write_output("✅ Finished!"))
		root.after(500, lambda: progress_bar.config(value=0))

# --- Threaded handler ---
def convert_in_background(files):
	try:
		convert_images(files)
	finally:
		root.after(0, lambda: drag_label.config(
			state="normal",
			text="🖼️ Drag and drop image files here (.jpg/.png/.bmp)"
		))

# --- Drag-and-drop handler ---
def drop_event_handler(event):
	files_or_dirs = root.tk.splitlist(event.data)
	if not files_or_dirs:
		return

	all_files = []
	for path in files_or_dirs:
		if os.path.isfile(path):
			all_files.append(path)
		elif os.path.isdir(path):
			for dirpath, _, filenames in os.walk(path):
				for filename in filenames:
					full_path = os.path.join(dirpath, filename)
					if os.path.splitext(full_path)[1].lower() in SUPPORTED_FORMATS:
						all_files.append(full_path)

	if not all_files:
		messagebox.showinfo("No Supported Images", "No supported image files found to convert.")
		return

	hide_output(clear=True)
	drag_label.config(state="disabled", text="⏳ Converting...")
	write_output("⏳ Converting...")

	progress_bar["value"] = 0
	threading.Thread(target=lambda: convert_in_background(all_files)).start()

# --- Bind drag-and-drop if available ---
if dnd_available:
	drag_label.drop_target_register(tkdnd.DND_FILES)
	drag_label.dnd_bind('<<Drop>>', drop_event_handler)

# --- Launch ---
if __name__ == "__main__":
	try:
		root.mainloop()
	except Exception as e:
		import traceback
		trace = traceback.format_exc()
		with open("easywebp-error.log", "w") as f:
			f.write(trace)
		messagebox.showerror("Startup Crash", f"{type(e).__name__}: {e}")
