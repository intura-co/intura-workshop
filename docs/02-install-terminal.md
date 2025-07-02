# 💻 Install Terminal

## What is a Terminal?
A terminal is a text-based interface to interact with your computer. Here you can run commands to install programs, run code, and manage files.

## Terminal on Windows

### 1. Windows Terminal (RECOMMENDED)
Windows Terminal is a modern terminal that's better than the regular Command Prompt.

#### How to Install Windows Terminal:
1. Open **Microsoft Store** on Windows
2. Search for "Windows Terminal"
3. Click "Install" or "Get"
4. Wait for installation to complete
5. Open from Start Menu

#### Windows Terminal Advantages:
- More modern and beautiful display
- Can open multiple tabs
- Supports various shells (PowerShell, Command Prompt, WSL)
- Customizable themes and colors

### 2. PowerShell (Already Installed)
PowerShell is already available on Windows 10/11:
1. Press `Windows + X`
2. Select "Windows PowerShell" or "Terminal"
3. Terminal is ready to use!

### 3. Command Prompt (CMD)
Also already installed on Windows:
1. Press `Windows + R`
2. Type `cmd`
3. Press Enter

## Basic Terminal Commands

### Navigation:
```bash
dir                    # View folder contents
cd folder_name        # Enter folder
cd ..                 # Go back to previous folder
cd \                  # Go back to main drive
```

### File Management:
```bash
mkdir folder_name     # Create new folder
del file_name         # Delete file
copy file1 file2      # Copy file
move file1 folder     # Move file
```

### System Information:
```bash
systeminfo            # System info
ipconfig              # Network info
whoami                # Current username
```

## Tips for Beginners:
1. **Don't be afraid to make mistakes** - Terminal won't break if you type wrong
2. **Use Tab** - For auto-complete file/folder names
3. **Copy-paste** - Right-click to paste in terminal
4. **Ctrl+C** - To cancel running command

## Terminal in VS Code
VS Code has built-in terminal:
1. Open VS Code
2. Press `Ctrl + `` (backtick)
3. Terminal will appear at bottom

## Troubleshooting

### Windows
**Command Prompt won't open:**
1. Press `Windows + R`, type `cmd`, press Enter
2. If it doesn't work, restart computer
3. Check if Windows is installed correctly

**PowerShell execution policy error:**
```powershell
# Open PowerShell as Administrator
Set-ExecutionPolicy RemoteSigned
# Type 'Y' to confirm
```

**Windows Terminal won't install:**
1. Update Windows to latest version
2. Install from Microsoft Store website
3. Or download manually from GitHub releases

**Command not recognized:**
1. Restart terminal after installing new program
2. Check PATH environment variable
3. Install program with "Add to PATH" option

### Linux
**Terminal won't open:**
```bash
# Open terminal with keyboard shortcut
Ctrl + Alt + T

# Or from Applications menu
# Or install new terminal
sudo apt install gnome-terminal
```

**Permission denied:**
```bash
# Fix file permissions
sudo chmod +x file_name
sudo chown $USER:$USER file_name

# Fix directory permissions
sudo chmod 755 folder_name
```

**Command not found:**
```bash
# Update package list
sudo apt update

# Install missing package
sudo apt install package_name

# Check PATH
echo $PATH
```

### macOS
**Terminal won't open:**
1. Applications → Utilities → Terminal
2. Or Spotlight (`Cmd + Space`) → type "Terminal"
3. Install iTerm2 as alternative: `brew install --cask iterm2`

**Permission denied:**
```bash
# Fix permissions
chmod +x file_name
chown $USER file_name

# Fix quarantine attribute
xattr -d com.apple.quarantine file_name
```

**Command not found:**
```bash
# Install Homebrew if not installed
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install missing package
brew install package_name

# Check PATH
echo $PATH
```

### Environment Variables

#### Windows
**Set PATH variable:**
1. System Properties → Environment Variables
2. Edit Path variable
3. Add new directory path
4. Restart terminal

**Via Command Line:**
```cmd
setx PATH "%PATH%;C:\path\to\program"
```

#### Linux/macOS
**Add to PATH:**
```bash
# Temporary (current session)
export PATH=$PATH:/path/to/program

# Permanent (add to ~/.bashrc or ~/.zshrc)
echo 'export PATH=$PATH:/path/to/program' >> ~/.bashrc
source ~/.bashrc
```

## Next Steps:
After terminal is ready, continue to GitHub account creation guide!

## 📧 Contact Person

For additional support or questions:
- **Email**: rama@intura.co
- **Subject**: Terminal Installation Help