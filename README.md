# File Organizer

<div align="center">
<img src="./assets/img/Sample Page.png"/>
</div>

A simple desktop file organizer built with **Python**, **CustomTkinter**, and a collection of custom JSON themes from **CTkThemesPack**.

The application lets you select a source folder and a destination folder, then automatically sorts files into category-based folders according to their file extensions.

## ✨ Features

- Select a **Source Folder** containing files to organize.
- Select a **Destination Folder** where organized files will be placed.
- Automatically categorize files by extension.
- Create category folders automatically when needed.
- Handle duplicate filenames by generating unique names such as `file_1.txt`, `file_2.txt`, etc.
- Display organization progress with a progress bar.
- Show the number of files organized and skipped.
- Prevent the application from using selected protected Windows system folders.
- Prevent using the same folder as both source and destination.
- Modern GUI built with CustomTkinter.
- Light/Dark appearance toggle.
- Theme selector with multiple custom color themes.
- Supports running from a normal Python environment or a PyInstaller bundle.

## 🗂️ File Categories

The application currently recognizes the following categories:

| Category      | Examples of supported extensions                                                                                                                                                                                              |
| ------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Documents     | `.pdf`, `.docx`, `.doc`, `.txt`, `.md`, `.rtf`, `.odt`, `.tex`, `.pages`, `.wps`, `.wpd`, `.xps`, `.djvu`                                                                                                                     |
| Spreadsheets  | `.xls`, `.xlsx`, `.ods`, `.csv`, `.tsv`, `.numbers`                                                                                                                                                                           |
| Presentations | `.ppt`, `.pptx`, `.odp`, `.pps`, `.key`                                                                                                                                                                                       |
| Images        | `.jpg`, `.jpeg`, `.png`, `.gif`, `.bmp`, `.tiff`, `.webp`, `.svg`, `.ico`, `.psd`, `.ai`, `.eps`, `.heic`, `.heif`, `.avif`, `.raw`, `.cr2`, `.nef`, `.arw`                                                                   |
| Audio         | `.mp3`, `.wav`, `.aac`, `.ogg`, `.flac`, `.m4a`, `.wma`, `.opus`, `.aiff`, `.aif`, `.mid`, `.midi`                                                                                                                            |
| Video         | `.mp4`, `.avi`, `.mkv`, `.mov`, `.wmv`, `.flv`, `.webm`, `.mpg`, `.mpeg`, `.3gp`, `.m4v`, `.ogv`, `.ts`, `.m2ts`, `.vob`                                                                                                      |
| Archives      | `.zip`, `.rar`, `.7z`, `.tar`, `.gz`, `.bz2`, `.xz`, `.cab`, `.iso`, `.img`, `.zst`, `.tgz`                                                                                                                                   |
| Code          | `.py`, `.js`, `.ts`, `.java`, `.c`, `.cpp`, `.h`, `.hpp`, `.cs`, `.go`, `.rs`, `.rb`, `.php`, `.swift`, `.kt`, `.sh`, `.bat`, `.html`, `.css`, `.xml`, `.json`, `.sql`, `.lua`, `.pl`, `.r`, `.scala`, `.vue`, `.jsx`, `.tsx` |
| Executables   | `.exe`, `.msi`, `.bat`, `.cmd`, `.com`, `.apk`, `.app`, `.bin`, `.jar`, `.deb`, `.rpm`                                                                                                                                        |
| Fonts         | `.ttf`, `.otf`, `.woff`, `.woff2`, `.eot`                                                                                                                                                                                     |
| E-Books       | `.epub`, `.mobi`, `.azw`, `.azw3`, `.cbr`, `.cbz`                                                                                                                                                                             |
| Design        | `.psd`, `.ai`, `.sketch`, `.fig`, `.xd`, `.indd`, `.afdesign`, `.afphoto`, `.blend`, `.3ds`, `.max`                                                                                                                           |
| Data          | `.json`, `.xml`, `.yaml`, `.yml`, `.ini`, `.cfg`, `.config`, `.dat`, `.db`, `.sqlite`, `.parquet`                                                                                                                             |
| Others        | Files whose extensions are not listed above                                                                                                                                                                                   |

## 🚀 How It Works

1. Choose the folder containing the files you want to organize.
2. Choose the destination folder.
3. Select a visual theme if desired.
4. Click **Organize Files**.
5. The application determines each file's category from its extension.
6. A category folder is created inside the destination when required.
7. The file is moved into the appropriate category folder.
8. If a file with the same name already exists, a unique filename is generated.
9. The progress bar and status label show the operation's progress.

For example:

```text
Destination/
├── Documents/
│   ├── report.pdf
│   └── notes.txt
├── Images/
│   ├── photo.jpg
│   └── logo.png
├── Videos/
│   └── movie.mp4
├── Archives/
│   └── backup.zip
└── Others/
    └── unknown.xyz
```

## 🎨 Themes

The application uses **CustomTkinter** for its graphical interface and loads additional JSON color palettes from **CTkThemesPack**.

Available theme names configured in the application include:

- Default
- Breeze
- Coffee
- Orange
- Midnight
- Violet
- Autumn
- Metal
- Cherry
- Red
- Patina
- Yellow
- Marsh
- Rose
- Pink
- Lavender
- Carrot
- Rime
- Sky

The application stores these theme files in the `themes` directory and loads the selected JSON file with CustomTkinter's `set_default_color_theme()` functionality.

The appearance toggle switches between Light and Dark modes.

## 📁 Project Structure

A typical project structure is:

```text
File Organizer/
├── file_organizer.py
├── README.md
├── assets/
│   └── logo.ico
└── themes/
    ├── breeze.json
    ├── coffee.json
    ├── orange.json
    ├── midnight.json
    ├── violet.json
    ├── autumn.json
    ├── metal.json
    ├── cherry.json
    ├── red.json
    ├── patina.json
    ├── yellow.json
    ├── marsh.json
    ├── rose.json
    ├── pink.json
    ├── lavender.json
    ├── carrot.json
    ├── rime.json
    └── sky.json
```

## 📦 Requirements

The main third-party Python GUI dependency used by the application is:

```bash
pip install customtkinter
```

The project also uses Python's standard-library modules including:

- `os`
- `sys`
- `shutil`
- `tkinter`

## 🛡️ Safety Checks

The application contains checks intended to prevent selecting several protected Windows locations, including:

```text
C:\
C:\Windows
C:\Program Files
C:\Program Files (x86)
C:\Users
```

It also checks that:

- The source folder exists.
- The destination folder exists.
- The selected folders are not blocked.
- Source and destination are not the same folder.
- The source contains files before organization begins.

## 🔄 Duplicate Files

When a destination already contains a file with the same name, the application does not overwrite it.

For example:

```text
report.pdf
report_1.pdf
report_2.pdf
report_3.pdf
```

This is handled by the application's unique filename logic.

## 🙏 Credits & Third-Party Libraries

### CustomTkinter

The graphical interface is built using **CustomTkinter**, a modern and customizable Python UI library based on Tkinter.

- Project: [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter)
- Documentation: [Docs](https://customtkinter.tomschimansky.com/)

### CTkThemesPack

The custom color themes used by this project are based on **[CTkThemesPack](https://github.com/a13xe/CTkThemesPack)**, created by **[a13xe](https://github.com/a13xe)**.

CTkThemesPack provides JSON color palettes designed for CustomTkinter applications. This project uses those theme files through CustomTkinter's `set_default_color_theme()` mechanism.

- Repository: https://github.com/a13xe/CTkThemesPack

**Credit:**

> Custom themes are provided by **[CTkThemesPack](https://github.com/a13xe/CTkThemesPack)** by **[a13xe](https://github.com/a13xe)**. Thank you to the author for creating and sharing the theme collection for CustomTkinter applications.

Please review the original repository's license and attribution requirements when redistributing the theme files.

## 📜 License

This README documents the application based on its current source code. Add the project's own license here if you have selected one.

Third-party components and theme files remain subject to their respective licenses and terms.

## 👤 Author


<a href="https://github.com/neeradian">
<img src="https://github.com/neeradian.png" width="50" height="50" style="border-radius:50%;">
</a>

Created and developed by [Nimesh Mandal](https://github.com/neeradian)


A lightweight desktop utility for organizing files by type using a modern CustomTkinter interface.
