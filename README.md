# Easy WebP Converter

![GitHub release](https://img.shields.io/github/v/release/thejoester/easy-webp-converter?label=latest%20release)
![GitHub](https://img.shields.io/github/license/thejoester/easy-webp-converter)

Convert your image files to `.webp` with a simple drag-and-drop interface.  
No terminal. No install. No bloat. Just WebP magic.

![image](https://github.com/user-attachments/assets/e37e1087-5565-42a5-871e-d34efacf2834) 

### Drag folders and convert all supported files recursively! 
![EasyWebPConverter_KGcBddYoMi](https://github.com/user-attachments/assets/ce4c9dd2-e2ad-42f2-83fc-4b43a467492d)

### Size comparison of my Steam Screenshots folder as an example
<img width="722" height="509" alt="image" src="https://github.com/user-attachments/assets/02e3d48f-ed8e-42ec-97cf-b4a21f8138f6" />


---

##  Features

- Drag and drop one or more images  — or entire folders!
- Recursively converts supported images in subfolders
- Supports `.jpg`, `.jpeg`, `.png`, `.bmp`, `.tiff`, `.gif`, etc.
- Converts to `.webp` using Python and Pillow
- Prevents overwrites by auto-renaming (`image-1.webp`, `image-2.webp`)
- Windows-native `.exe` — no Python needed
- Open-source and offline-friendly, no telemetry, no nonsense

## Add to Start menu
- Right-click .exe and select "Pin to Start"

---

## Download

Grab the latest `.exe` from [GitHub Releases](https://github.com/thejoester/easy-webp-converter/releases/latest)

No installer. Just double-click and drop in your images.

---

## Build Instructions (for developers)

Want to build it yourself or contribute? Here's how:

### Requirements

- Python 3.12+
- Git
- Windows (this app is Windows-only for now)

### Clone the Repo

```bash
git clone https://github.com/thejoester/easy-webp-converter.git
cd easy-webp-converter
```
### Install Dependencies

```bash
pip install pillow tkinterdnd2 pyinstaller
```

### Build the Executable

```bash
pyinstaller --noconsole --onefile --icon=ewc.ico --name EasyWebPConverter --version-file=version.txt image_to_webp.pyw
```

### Optional: Clean Build

```bash
pyinstaller --clean ...
```

### License

MIT License.
Do whatever you want — just don’t pretend you wrote it first.
