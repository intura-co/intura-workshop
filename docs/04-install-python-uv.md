# 🐍 Install Python with uv

## What is Python?
Python is a popular and easy-to-learn programming language. Great for beginners because of its simple and readable syntax.

## What is uv?
uv is a modern tool for managing Python and packages. Faster than pip and conda, with better dependency resolver.

## How to Install Python and uv

### Step 1: Install Python
1. Go to [python.org](https://python.org)
2. Click "Download Python" (latest version)
3. Run the installer
4. **Important**: Check "Add Python to PATH" during installation
5. Click "Install Now"

### Step 2: Verify Python Installation
Open Command Prompt and run:
```cmd
python --version
```
You should see Python version (e.g., Python 3.11.0)

### Step 3: Install pipx
pipx is a tool to install Python applications in isolated environments.

#### Install pipx on Windows:
```cmd
python -m pip install --user pipx
python -m pipx ensurepath
```

#### Install pipx on Linux/macOS:
```bash
python3 -m pip install --user pipx
python3 -m pipx ensurepath
```

### Step 4: Install uv with pipx
Now install uv using pipx:
```cmd
pipx install uv
```

### Step 5: Verify uv Installation
Run this command to make sure uv is installed:
```cmd
uv --version
```
If version appears, installation is successful!

### Step 6: Install Python with uv
uv will automatically install latest Python:
```cmd
uv python install
```

### Step 7: Check Python Version
```cmd
uv python list
```
This will show available Python versions.

## Create Your First Python Project

### Step 1: Create New Project
```bash
uv init my-first-project
cd my-first-project
```

### Step 2: Project Structure
After `uv init`, this will be created:
```
my-first-project/
├── pyproject.toml    # Project configuration
├── src/             # Folder for code
│   └── my_first_project/
│       └── __init__.py
└── tests/           # Folder for testing
    └── __init__.py
```

### Step 3: Install Packages
To add packages (libraries):
```bash
uv add requests
uv add pytest --dev
```

### Step 4: Run Project
```bash
uv run python main.py
```

## Useful uv Commands

### Package Management:
```bash
uv add package_name        # Install package
uv add package_name --dev  # Install package for development
uv remove package_name     # Remove package
uv sync                    # Install all dependencies
```

### Python Management:
```bash
uv python install          # Install Python
uv python list            # View Python versions
uv python remove 3.11     # Remove specific Python version
```

### Project Management:
```bash
uv init project_name      # Create new project
uv run python script.py   # Run script
uv run pytest            # Run tests
```

## uv Advantages:
1. **Faster** - Install packages faster than pip
2. **Dependency resolver** - Automatically solve dependency conflicts
3. **Lock file** - Ensure consistent package versions
4. **Virtual environment** - Automatically manage separate environments
5. **Modern** - Use latest Python standards

## Tips for Beginners:
1. **Use uv for all projects** - More consistent
2. **Always use virtual environment** - Avoid package conflicts
3. **Update uv regularly** - `uv self update`
4. **Backup lock file** - Commit `uv.lock` to git

## Troubleshooting

### Windows
**Python not found:**
```cmd
# Check if Python is installed
python --version

# If not found, install Python from python.org
# Make sure to check "Add Python to PATH" during installation
```

**pipx command not found:**
```cmd
# Install pipx
python -m pip install --user pipx
python -m pipx ensurepath

# Restart Command Prompt after installation
```

**uv command not found:**
```cmd
# Install uv with pipx
pipx install uv

# Or reinstall if needed
pipx reinstall uv

# Check PATH environment variable
echo %PATH%
```

**Permission denied:**
```cmd
# Run Command Prompt as Administrator
# Right-click Command Prompt → "Run as administrator"

# Or install pipx with user flag
python -m pip install --user pipx
```

**Network error:**
1. Check internet connection
2. Disable antivirus temporarily
3. Check proxy settings
4. Use VPN if needed

### Linux
**Python not found:**
```bash
# Check if Python is installed
python3 --version

# If not found, install Python
sudo apt update
sudo apt install python3 python3-pip
```

**pipx command not found:**
```bash
# Install pipx
python3 -m pip install --user pipx
python3 -m pipx ensurepath

# Restart shell
source ~/.bashrc
```

**uv command not found:**
```bash
# Install uv with pipx
pipx install uv

# Or reinstall if needed
pipx reinstall uv

# Check PATH
echo $PATH
```

**Permission denied:**
```bash
# Fix permissions
sudo chown -R $USER:$USER ~/.local
sudo chmod -R 755 ~/.local

# Or install pipx with user flag
python3 -m pip install --user pipx
```

**Dependencies can't be installed:**
```bash
# Update system
sudo apt update && sudo apt upgrade

# Install build tools
sudo apt install build-essential python3-dev
```

### macOS
**Python not found:**
```bash
# Check if Python is installed
python3 --version

# If not found, install Python via Homebrew
brew install python
```

**pipx command not found:**
```bash
# Install pipx
python3 -m pip install --user pipx
python3 -m pipx ensurepath

# Restart shell
source ~/.zshrc
```

**uv command not found:**
```bash
# Install uv with pipx
pipx install uv

# Or reinstall if needed
pipx reinstall uv

# Check PATH
echo $PATH
```

**Permission denied:**
```bash
# Fix permissions
sudo chown -R $USER ~/.local
chmod -R 755 ~/.local

# Or install pipx with user flag
python3 -m pip install --user pipx
```

**Xcode command line tools missing:**
```bash
# Install Xcode command line tools
xcode-select --install

# Or update
softwareupdate --all --install --force
```

### Environment Variables

#### Windows
**Add pipx to PATH:**
```cmd
# Check pipx location
where pipx

# Add to PATH (usually already done by pipx ensurepath)
setx PATH "%PATH%;%USERPROFILE%\.local\bin"
```

#### Linux/macOS
**Add pipx to PATH:**
```bash
# Temporary
export PATH="$HOME/.local/bin:$PATH"

# Permanent (add to ~/.bashrc or ~/.zshrc)
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc
```

### Common Issues

**SSL Certificate errors:**
```bash
# Update certificates
uv self update

# Or set environment variable
export SSL_CERT_FILE=/path/to/cert.pem
```

**Slow installation:**
1. Use nearest mirror repository
2. Check internet connection
3. Disable antivirus temporarily
4. Use VPN if needed

**Version conflicts:**
```bash
# List installed Python versions
uv python list

# Remove specific version
uv python remove 3.10

# Install specific version
uv python install 3.11
```

## Next Steps:
After Python and uv are ready, continue to package installation guide!

## 📧 Contact Person

For additional support or questions:
- **Email**: rama@intura.co
- **Subject**: Python and uv Installation Help