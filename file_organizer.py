import os
import sys
import shutil
import customtkinter as ctk
from tkinter import filedialog, messagebox


# ============================================================
# FILE CATEGORIES
# ============================================================

FILE_CATEGORIES = {
    "Documents": [
        ".pdf",
        ".docx",
        ".doc",
        ".txt",
        ".srt",
        ".pdf",
        ".odt",
        ".rtf",
        ".md",
        ".tex",
        ".pages",
        ".wps",
        ".wpd",
        ".xps",
        ".djvu",
    ],
    "Spreadsheets": [
        ".xls",
        ".xlsx",
        ".ods",
        ".csv",
        ".tsv",
        ".numbers",
    ],
    "Presentations": [
        ".ppt",
        ".pptx",
        ".odp",
        ".pps",
        ".key",
    ],
    "Images": [
        ".jpg",
        ".jpeg",
        ".png",
        ".gif",
        ".bmp",
        ".tiff",
        ".tif",
        ".webp",
        ".svg",
        ".ico",
        ".psd",
        ".ai",
        ".eps",
        ".heic",
        ".heif",
        ".avif",
        ".raw",
        ".cr2",
        ".nef",
        ".arw",
    ],
    "Audio": [
        ".mp3",
        ".wav",
        ".aac",
        ".ogg",
        ".flac",
        ".m4a",
        ".wma",
        ".opus",
        ".aiff",
        ".aif",
        ".mid",
        ".midi",
    ],
    "Video": [
        ".mp4",
        ".avi",
        ".mkv",
        ".mov",
        ".wmv",
        ".flv",
        ".webm",
        ".mpg",
        ".mpeg",
        ".3gp",
        ".m4v",
        ".ogv",
        ".ts",
        ".m2ts",
        ".vob",
    ],
    "Archives": [
        ".zip",
        ".rar",
        ".7z",
        ".tar",
        ".gz",
        ".bz2",
        ".xz",
        ".cab",
        ".iso",
        ".img",
        ".zst",
        ".tgz",
    ],
    "Code": [
        ".py",
        ".js",
        ".ts",
        ".java",
        ".c",
        ".cpp",
        ".h",
        ".hpp",
        ".cs",
        ".go",
        ".rs",
        ".rb",
        ".php",
        ".swift",
        ".kt",
        ".sh",
        ".bat",
        ".html",
        ".css",
        ".xml",
        ".json",
        ".sql",
        ".lua",
        ".pl",
        ".r",
        ".scala",
        ".vue",
        ".jsx",
        ".tsx",
    ],
    "Executables": [
        ".exe",
        ".msi",
        ".bat",
        ".cmd",
        ".com",
        ".apk",
        ".app",
        ".bin",
        ".jar",
        ".deb",
        ".rpm",
    ],
    "Fonts": [
        ".ttf",
        ".otf",
        ".woff",
        ".woff2",
        ".eot",
    ],
    "E-Books": [
        ".epub",
        ".mobi",
        ".azw",
        ".azw3",
        ".cbr",
        ".cbz",
    ],
    "Design": [
        ".psd",
        ".ai",
        ".sketch",
        ".fig",
        ".xd",
        ".indd",
        ".afdesign",
        ".afphoto",
        ".blend",
        ".3ds",
        ".max",
    ],
    "Data": [
        ".json",
        ".xml",
        ".yaml",
        ".yml",
        ".ini",
        ".cfg",
        ".config",
        ".dat",
        ".db",
        ".sqlite",
        ".parquet",
    ],
    "Others": [],
}


# ============================================================
# BLOCKED FOLDERS
# ============================================================

BLOCKED_FOLDERS = [
    "C:\\",
    "C:\\Windows",
    "C:\\Program Files",
    "C:\\Program Files (x86)",
    "C:\\Users",
]


# ============================================================
# THEME DIRECTORY
# ============================================================

THEME_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "themes")


# ============================================================
# CTK THEMES PACK
# ============================================================

THEMES = {
    "Default": None,
    "Breeze": "breeze.json",
    "Coffee": "coffee.json",
    "Orange": "orange.json",
    "Midnight": "midnight.json",
    "Violet": "violet.json",
    "Autumn": "autumn.json",
    "Metal": "metal.json",
    "Cherry": "cherry.json",
    "Red": "red.json",
    "Patina": "patina.json",
    "Yellow": "yellow.json",
    "Marsh": "marsh.json",
    "Rose": "rose.json",
    "Pink": "pink.json",
    "Lavender": "lavender.json",
    "Carrot": "carrot.json",
    "Rime": "rime.json",
    "Sky": "sky.json",
}


# ============================================================
# DEFAULT CUSTOMTKINTER SETTINGS
# ============================================================

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

# ============================================================
# RESOURCE PATH FUNCTION FOR LOGO 
# ============================================================

def resource_path(relative_path):
    """Get the correct path for development and PyInstaller."""
    if getattr(sys, "frozen", False):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.dirname(os.path.abspath(__file__))

    return os.path.join(base_path, relative_path)


# ============================================================
# FILE ORGANIZER APP
# ============================================================


class FileOrganizerApp(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("File Organizer")
        self.geometry("700x500")
        self.minsize(600, 450)
        self.resizable(False, False)
        self.iconbitmap(resource_path("assets/logo.ico"))

        self.source_folder = ""
        self.destination_folder = ""

        self.create_widgets()

    # ========================================================
    # CREATE GUI
    # ========================================================

    def create_widgets(self):

        # ----------------------------------------------------
        # Main Frame
        # ----------------------------------------------------

        self.main_frame = ctk.CTkFrame(self, corner_radius=15)

        self.main_frame.pack(fill="both", expand=True, padx=25, pady=25)

        # ----------------------------------------------------
        # Header
        # ----------------------------------------------------

        self.header_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")

        self.header_frame.pack(fill="x", padx=25, pady=(20, 5))

        # ----------------------------------------------------
        # Title
        # ----------------------------------------------------

        self.title_label = ctk.CTkLabel(
            self.header_frame,
            text="File Organizer",
            font=ctk.CTkFont(size=28, weight="bold"),
        )

        self.title_label.pack(side="left")

        # ----------------------------------------------------
        # Theme Manager Icon
        # ----------------------------------------------------

        self.theme_button = ctk.CTkButton(
            self.header_frame,
            text="☾",
            width=40,
            height=35,
            corner_radius=10,
            font=ctk.CTkFont(size=20),
            command=self.toggle_theme,
        )

        self.theme_button.pack(side="right")

        # ----------------------------------------------------
        # Style Selector
        # ----------------------------------------------------

        self.style_selector = ctk.CTkOptionMenu(
            self.header_frame,
            values=list(THEMES.keys()),
            width=110,
            height=32,
            corner_radius=8,
            command=self.change_style,
        )

        self.style_selector.set("Default")

        self.style_selector.pack(side="right", padx=(0, 8))

        # ----------------------------------------------------
        # Subtitle
        # ----------------------------------------------------

        self.subtitle_label = ctk.CTkLabel(
            self.main_frame,
            text="Organize files automatically by their file type",
            font=ctk.CTkFont(size=14),
        )

        self.subtitle_label.pack(pady=(0, 25))

        # ====================================================
        # SOURCE FOLDER
        # ====================================================

        self.source_label = ctk.CTkLabel(
            self.main_frame,
            text="Source Folder",
            font=ctk.CTkFont(size=15, weight="bold"),
            anchor="w",
        )

        self.source_label.pack(fill="x", padx=40)

        self.source_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")

        self.source_frame.pack(fill="x", padx=40, pady=(5, 20))

        self.source_entry = ctk.CTkEntry(
            self.source_frame,
            placeholder_text="Select the folder containing your files...",
        )

        self.source_entry.pack(side="left", fill="x", expand=True, padx=(0, 10))

        self.source_button = ctk.CTkButton(
            self.source_frame,
            text="Browse",
            width=100,
            command=self.select_source_folder,
        )

        self.source_button.pack(side="right")

        # ====================================================
        # DESTINATION FOLDER
        # ====================================================

        self.destination_label = ctk.CTkLabel(
            self.main_frame,
            text="Destination Folder",
            font=ctk.CTkFont(size=15, weight="bold"),
            anchor="w",
        )

        self.destination_label.pack(fill="x", padx=40)

        self.destination_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")

        self.destination_frame.pack(fill="x", padx=40, pady=(5, 25))

        self.destination_entry = ctk.CTkEntry(
            self.destination_frame,
            placeholder_text="Select where organized files should be placed...",
        )

        self.destination_entry.pack(side="left", fill="x", expand=True, padx=(0, 10))

        self.destination_button = ctk.CTkButton(
            self.destination_frame,
            text="Browse",
            width=100,
            command=self.select_destination_folder,
        )

        self.destination_button.pack(side="right")

        # ====================================================
        # ORGANIZE BUTTON
        # ====================================================

        self.organize_button = ctk.CTkButton(
            self.main_frame,
            text="Organize Files",
            height=45,
            font=ctk.CTkFont(size=16, weight="bold"),
            command=self.organize_files,
        )

        self.organize_button.pack(fill="x", padx=40, pady=(0, 20))

        # ====================================================
        # PROGRESS BAR
        # ====================================================

        self.progress_bar = ctk.CTkProgressBar(self.main_frame, height=10)

        self.progress_bar.pack(fill="x", padx=40)

        self.progress_bar.set(0)

        # ====================================================
        # STATUS
        # ====================================================

        self.status_label = ctk.CTkLabel(
            self.main_frame, text="Ready", font=ctk.CTkFont(size=13)
        )

        self.status_label.pack(pady=10)

    # ========================================================
    # THEME MANAGER
    # ========================================================

    def toggle_theme(self):

        current_mode = ctk.get_appearance_mode()

        if current_mode == "Dark":

            ctk.set_appearance_mode("Light")

            self.theme_button.configure(text="☀")

        else:

            ctk.set_appearance_mode("Dark")

            self.theme_button.configure(text="☾")

    # ========================================================
    # CHANGE CTK THEME
    # ========================================================

    def change_style(self, selected_theme):
        theme_file = THEMES.get(selected_theme)

        if selected_theme == "Default":
            ctk.set_default_color_theme("blue")
        else:
            if not theme_file:
                return
            theme_path = os.path.join(THEME_DIR, theme_file).replace("\\", "/")
            if not os.path.exists(theme_path):
                messagebox.showerror(
                    "Theme Not Found", f"Theme not found:\n{theme_path}"
                )
                return
            try:
                # Load selected CTk theme
                ctk.set_default_color_theme(theme_path)
            except Exception as e:
                messagebox.showerror("Theme Error", str(e))
                return

        # ------------------------------------------------
        # Important:
        # Existing widgets may not automatically receive
        # the new theme in every CustomTkinter version.
        # Rebuild the interface to apply the palette.
        # ------------------------------------------------

        # Destroy all existing widgets
        for widget in self.winfo_children():
            widget.destroy()

        # Rebuild with the new theme
        self.create_widgets()

    # ========================================================
    # SELECT SOURCE FOLDER
    # ========================================================

    def select_source_folder(self):

        folder = filedialog.askdirectory(title="Select Source Folder")

        if not folder:
            return

        if self.is_blocked_folder(folder):

            messagebox.showerror(
                "Blocked Folder", "This folder is protected and cannot be used."
            )

            return

        self.source_folder = folder

        self.source_entry.delete(0, "end")

        self.source_entry.insert(0, folder)

        self.status_label.configure(text="Source folder selected")

    # ========================================================
    # SELECT DESTINATION FOLDER
    # ========================================================

    def select_destination_folder(self):

        folder = filedialog.askdirectory(title="Select Destination Folder")

        if not folder:
            return

        if self.is_blocked_folder(folder):

            messagebox.showerror(
                "Blocked Folder", "This folder is protected and cannot be used."
            )

            return

        self.destination_folder = folder

        self.destination_entry.delete(0, "end")

        self.destination_entry.insert(0, folder)

        self.status_label.configure(text="Destination folder selected")

    # ========================================================
    # CHECK BLOCKED FOLDER
    # ========================================================

    def is_blocked_folder(self, folder):

        folder = os.path.normcase(os.path.abspath(folder))

        for blocked in BLOCKED_FOLDERS:

            blocked_path = os.path.normcase(os.path.abspath(blocked))

            if folder == blocked_path:
                return True

        return False

    # ========================================================
    # GET FILE CATEGORY
    # ========================================================

    def get_file_category(self, filename):

        extension = os.path.splitext(filename)[1].lower()

        for category, extensions in FILE_CATEGORIES.items():

            if extension in extensions:
                return category

        return "Others"

    # ========================================================
    # ORGANIZE FILES
    # ========================================================

    def organize_files(self):

        source = self.source_entry.get().strip()
        destination = self.destination_entry.get().strip()

        # ----------------------------------------------------
        # Validate source
        # ----------------------------------------------------

        if not source:

            messagebox.showwarning("Source Folder", "Please select a source folder.")

            return

        if not os.path.isdir(source):

            messagebox.showerror(
                "Invalid Folder", "The selected source folder does not exist."
            )

            return

        if self.is_blocked_folder(source):

            messagebox.showerror(
                "Blocked Folder", "The selected source folder is protected."
            )

            return

        # ----------------------------------------------------
        # Validate destination
        # ----------------------------------------------------

        if not destination:

            messagebox.showwarning(
                "Destination Folder", "Please select a destination folder."
            )

            return

        if not os.path.isdir(destination):

            messagebox.showerror(
                "Invalid Folder", "The selected destination folder does not exist."
            )

            return

        if self.is_blocked_folder(destination):

            messagebox.showerror(
                "Blocked Folder", "The selected destination folder is protected."
            )

            return

        # ----------------------------------------------------
        # Same folder
        # ----------------------------------------------------

        if os.path.normcase(os.path.abspath(source)) == os.path.normcase(
            os.path.abspath(destination)
        ):

            messagebox.showerror(
                "Invalid Selection",
                "Source and destination folders cannot be the same.",
            )

            return

        # ----------------------------------------------------
        # Find files
        # ----------------------------------------------------

        try:

            files = []

            for filename in os.listdir(source):

                file_path = os.path.join(source, filename)

                if os.path.isfile(file_path):
                    files.append(filename)

        except PermissionError:

            messagebox.showerror(
                "Permission Denied", "You do not have permission to access this folder."
            )

            return

        if not files:

            messagebox.showinfo("No Files", "No files were found in the source folder.")

            return

        # ----------------------------------------------------
        # Disable controls
        # ----------------------------------------------------

        self.organize_button.configure(state="disabled", text="Organizing...")

        self.source_button.configure(state="disabled")

        self.destination_button.configure(state="disabled")

        self.style_selector.configure(state="disabled")

        self.progress_bar.set(0)

        moved_files = 0
        skipped_files = 0

        # ----------------------------------------------------
        # Organize
        # ----------------------------------------------------

        try:

            total_files = len(files)

            for index, filename in enumerate(files):

                source_path = os.path.join(source, filename)

                category = self.get_file_category(filename)

                category_folder = os.path.join(destination, category)

                os.makedirs(category_folder, exist_ok=True)

                destination_path = os.path.join(category_folder, filename)

                destination_path = self.get_unique_filename(destination_path)

                try:

                    shutil.move(source_path, destination_path)

                    moved_files += 1

                except (PermissionError, OSError):

                    skipped_files += 1

                # Progress
                progress = (index + 1) / total_files

                self.progress_bar.set(progress)

                self.status_label.configure(text=f"Organizing: {filename}")

                self.update_idletasks()

            # ------------------------------------------------
            # Complete
            # ------------------------------------------------

            self.status_label.configure(
                text=f"Completed — {moved_files} files organized"
            )

            messagebox.showinfo(
                "Organization Complete",
                f"Files organized: {moved_files}\n" f"Files skipped: {skipped_files}",
            )

        except Exception as error:

            messagebox.showerror("Error", f"An unexpected error occurred:\n\n{error}")

            self.status_label.configure(text="Organization failed")

        finally:

            self.organize_button.configure(state="normal", text="Organize Files")

            self.source_button.configure(state="normal")

            self.destination_button.configure(state="normal")

            self.style_selector.configure(state="normal")

    # ========================================================
    # HANDLE DUPLICATE FILES
    # ========================================================

    def get_unique_filename(self, filepath):

        if not os.path.exists(filepath):
            return filepath

        folder = os.path.dirname(filepath)

        filename = os.path.basename(filepath)

        name, extension = os.path.splitext(filename)

        counter = 1

        while True:

            new_filename = f"{name}_{counter}{extension}"

            new_filepath = os.path.join(folder, new_filename)

            if not os.path.exists(new_filepath):

                return new_filepath

            counter += 1


# ============================================================
# RUN APPLICATION
# ============================================================

if __name__ == "__main__":

    app = FileOrganizerApp()

    app.mainloop()
