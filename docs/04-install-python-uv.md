# 🐍 Install Python with uv

## What is Python?
Python is a popular and easy-to-learn programming language. Great for beginners because of its simple and readable syntax.

## What is uv?
uv is a modern tool for managing Python and packages. Faster than pip and conda, with better dependency resolver.

## How to Install Python with uv

### Step 1: Install uv
1. Open terminal (PowerShell or Command Prompt)
2. Run this command:
```bash
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```
3. Wait for installation to complete
4. Close and reopen terminal

### Step 2: Verify Installation
Run this command to make sure uv is installed:
```bash
uv --version
```
If version appears, installation is successful!

### Step 3: Install Python with uv
uv will automatically install latest Python:
```bash
uv python install
```

### Step 4: Check Python Version
```bash
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
uv run python src/my_first_project/__init__.py
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
**uv command not found:**
```powershell
# Restart terminal after install
# Or restart computer

# Check PATH environment variable
echo $env:PATH

# Reinstall if needed
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

**Permission denied:**
```powershell
# Run PowerShell as Administrator
# Or set execution policy
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
```

**Python not installed:**
```bash
# Install Python manually if uv fails
uv python install 3.11

# Or download from python.org
# Make sure to check "Add to PATH" during install
```

**Network error:**
1. Check internet connection
2. Disable antivirus temporarily
3. Check proxy settings
4. Use VPN if needed

### Linux
**uv command not found:**
```bash
# Reinstall uv
curl -LsSf https://astral.sh/uv/install.sh | sh

# Restart shell
source ~/.bashrc
# or
source ~/.zshrc

# Check PATH
echo $PATH
```

**Permission denied:**
```bash
# Fix permissions
sudo chown -R $USER:$USER ~/.cargo
sudo chmod -R 755 ~/.cargo

# Or install for user
curl -LsSf https://astral.sh/uv/install.sh | sh -s -- --no-modify-path
```

**Python not installed:**
```bash
# Install Python system-wide
sudo apt update
sudo apt install python3 python3-pip

# Or use uv
uv python install 3.11
```

**Dependencies can't be installed:**
```bash
# Update system
sudo apt update && sudo apt upgrade

# Install build tools
sudo apt install build-essential python3-dev
```

### macOS
**uv command not found:**
```bash
# Reinstall uv
curl -LsSf https://astral.sh/uv/install.sh | sh

# Restart shell
source ~/.zshrc

# Check PATH
echo $PATH
```

**Permission denied:**
```bash
# Fix permissions
sudo chown -R $USER ~/.cargo
chmod -R 755 ~/.cargo

# Or install for user
curl -LsSf https://astral.sh/uv/install.sh | sh -s -- --no-modify-path
```

**Python not installed:**
```bash
# Install Python via Homebrew
brew install python

# Or use uv
uv python install 3.11
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
**Add uv to PATH:**
```powershell
# Check uv location
where.exe uv

# Add to PATH (replace with actual path)
setx PATH "%PATH%;C:\Users\%USERNAME%\.cargo\bin"
```

#### Linux/macOS
**Add uv to PATH:**
```bash
# Temporary
export PATH="$HOME/.cargo/bin:$PATH"

# Permanent (add to ~/.bashrc or ~/.zshrc)
echo 'export PATH="$HOME/.cargo/bin:$PATH"' >> ~/.zshrc
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