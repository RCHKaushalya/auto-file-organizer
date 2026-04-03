# 🗂 Auto File Organizer

Automatically organize files into folders by type (Images, Docs, Videos, Music, Archives, Code, Executables).  
Built with Python using `os` and `shutil` modules. Includes both a **standalone GUI** and a **command-line automation script**.

---

## ✨ Features
- Organizes files into predefined categories
- Handles duplicate files safely (renames instead of overwriting)
- Generates a summary report after organizing
- **Standalone GUI** with folder picker and popup report
- **Automation-ready** script for scheduled runs (Downloads folder, etc.)

---

## 📂 Project Structure
```
auto-file-organizer/
│
├── organizer.py   # Core automation script (CLI)
├── gui.py         # Standalone GUI version
└── README.md      # Documentation
```

---

## 🚀 Usage

### 1. Command-Line Script
Run manually:
```bash
python organizer.py
```
Enter the folder path when prompted. Files will be organized automatically.

### 2. GUI Version
Run with:
```bash
python gui.py
```
Select a folder using the file picker. A popup will show the summary report.

---

## ⚙️ Automation Setup

You can schedule the script (`organizer.py`) to run automatically on your **Downloads folder**.

### Windows (Task Scheduler)
1. Open **Task Scheduler**.
2. Create a new task → *Run program*.
3. Program/script:  
   ```bash
   python
   ```
4. Add arguments:  
   ```bash
   C:\path\to\organizer.py
   ```
5. Set trigger: *Daily* or *At logon*.
6. Save → Your Downloads folder will be organized automatically.

---

### macOS (Cron / Launchd)

#### Using Cron:
1. Open Terminal.
2. Edit cron jobs:
   ```bash
   crontab -e
   ```
3. Add:
   ```bash
   0 * * * * python3 /path/to/organizer.py /Users/<username>/Downloads
   ```
   (Runs every hour)

#### Using Launchd (preferred):
- Create a `.plist` file in `~/Library/LaunchAgents/`.
- Point it to run `organizer.py` daily.

---

### Linux (Cron)
1. Open Terminal.
2. Edit cron jobs:
   ```bash
   crontab -e
   ```
3. Add:
   ```bash
   0 * * * * python3 /home/<username>/auto-file-organizer/organizer.py /home/<username>/Downloads
   ```
   (Runs every hour)

---