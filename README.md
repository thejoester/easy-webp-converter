# Easy WebP Converter

![GitHub release](https://img.shields.io/github/v/release/thejoester/easy-webp-converter?label=latest%20release)
![GitHub](https://img.shields.io/github/license/thejoester/easy-webp-converter)

Convert your image files to `.webp` with a simple drag-and-drop interface.  
No terminal. No install. No bloat. Just WebP magic.

---

##  Features

- Drag and drop one or more images
- Supports `.jpg`, `.jpeg`, `.png`, `.bmp`, `.tiff`, `.gif`, etc.
- Converts to `.webp` using Python and Pillow
- Prevents overwrites by auto-renaming (`image-1.webp`, `image-2.webp`)
- Windows-native `.exe` — no Python needed
- Open-source and offline-friendly

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

### Install Dependencies

`pip install pillow tkinterdnd2 pyinstaller`

### Build the Executable

`pyinstaller --noconsole --onefile --icon=ewc.ico --name EasyWebPConverter --version-file=version.txt image_to_webp.pyw`

### Optional: Clean Build

`pyinstaller --clean ...`

### License

MIT License.
Do whatever you want — just don’t pretend you wrote it first.