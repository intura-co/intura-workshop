# 📦 Install Packages

## What are Packages?
Packages are code that other developers have created that you can use. Like plugins or add-ons that add features to your project.

## How to Install Packages with uv

### Step 1: Enter Project
```bash
cd your_project_name
```

### Step 2: Install Package
```bash
uv add package_name
```

### Example Install Popular Packages:
```bash
# Web Development
uv add flask          # Simple web framework
uv add django         # Complete web framework
uv add fastapi        # Modern API framework

# Data Science
uv add pandas         # Data analysis
uv add numpy          # Numerical computing
uv add matplotlib     # Data visualization

# Machine Learning
uv add scikit-learn   # Machine learning
uv add tensorflow     # Deep learning
uv add torch          # PyTorch

# Utilities
uv add requests       # HTTP requests
uv add beautifulsoup4 # Web scraping
uv add pillow         # Image processing
```

## Packages for Development

### Install Development Packages:
```bash
uv add pytest --dev        # Testing framework
uv add black --dev         # Code formatter
uv add flake8 --dev        # Linter
uv add mypy --dev          # Type checker
```

### Useful Development Packages:
- **pytest** - For testing code
- **black** - Automatic code formatting
- **flake8** - Check style and errors
- **mypy** - Check data types
- **pre-commit** - Hook before commit

## Manage Dependencies

### View Installed Packages:
```bash
uv tree
```

### Update Packages:
```bash
uv sync --upgrade
```

### Remove Package:
```bash
uv remove package_name
```

### Install from requirements.txt:
```bash
uv pip install -r requirements.txt
```

## Configuration Files

### pyproject.toml
This file contains project configuration:
```toml
[project]
name = "my-project"
version = "0.1.0"
dependencies = [
    "requests>=2.28.0",
    "pandas>=1.5.0",
]

[project.optional-dependencies]
dev = [
    "pytest>=7.0.0",
    "black>=22.0.0",
]
```

### uv.lock
This file locks package versions for consistency:
- **Don't edit manually** - Created automatically by uv
- **Commit to git** - For team consistency
- **Update with `uv sync`** - To update dependencies

## Best Practices

### 1. Use Virtual Environment
uv automatically creates virtual environment:
```bash
uv init project_name
cd project_name
uv add package_name
```

### 2. Specify Package Versions
```bash
uv add requests==2.28.0    # Specific version
uv add pandas>=1.5.0       # Minimum version
uv add flask~=2.3.0        # Compatible release
```

### 3. Group Dependencies
```bash
uv add requests            # Production dependency
uv add pytest --dev        # Development dependency
uv add mypy --dev          # Development dependency
```

### 4. Regular Updates
```bash
uv sync --upgrade          # Update all packages
uv sync --upgrade-package requests  # Update specific package
```

## Troubleshooting

### Windows
**uv command not found:**
```powershell
# Restart terminal after installing uv
# Or restart computer

# Check PATH
echo $env:PATH

# Reinstall uv if needed
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

**Permission denied:**
```powershell
# Run PowerShell as Administrator
# Or set execution policy
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
```

**Package can't be installed:**
```bash
# Check internet connection
# Disable antivirus temporarily
# Check proxy settings

# Clear cache
uv cache clean

# Install with verbose output
uv add package_name --verbose
```

**SSL Certificate errors:**
```bash
# Update certificates
uv self update

# Or set environment variable
$env:SSL_CERT_FILE="C:\path\to\cert.pem"
```

### Linux
**uv command not found:**
```bash
# Reinstall uv
curl -LsSf https://astral.sh/uv/install.sh | sh

# Restart shell
source ~/.bashrc

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

**Package can't be installed:**
```bash
# Update system
sudo apt update && sudo apt upgrade

# Install build tools
sudo apt install build-essential python3-dev

# Clear cache
uv cache clean
```

**Dependencies not found:**
```bash
# Check correct package name
uv search package_name

# Install from PyPI with different name
uv add package-name

# Check available versions
uv search package_name --all-versions
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

**Xcode command line tools missing:**
```bash
# Install Xcode command line tools
xcode-select --install

# Or update
softwareupdate --all --install --force
```

**Package can't be installed:**
```bash
# Install Homebrew if not installed
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Clear cache
uv cache clean

# Install with verbose output
uv add package_name --verbose
```

### Common Issues

**Dependency Conflicts:**
```bash
# uv will automatically solve conflicts
uv sync

# If still error, check compatible versions
uv tree

# Force resolve conflicts
uv sync --reinstall
```

**Package not found:**
```bash
# Check correct package name
uv search package_name

# Install from PyPI with different name
uv add package-name

# Check if package exists on PyPI
curl https://pypi.org/pypi/package_name/json
```

**Slow installation:**
1. Use nearest mirror repository
2. Check internet connection
3. Disable antivirus temporarily
4. Use VPN if needed

**Version conflicts:**
```bash
# List installed packages
uv tree

# Remove specific package
uv remove package_name

# Install specific version
uv add package_name==1.2.3
```

**Environment Variables:**
```bash
# Set proxy if needed
export HTTP_PROXY=http://proxy:port
export HTTPS_PROXY=http://proxy:port

# Set timeout
export UV_TIMEOUT=300

# Set cache directory
export UV_CACHE_DIR=/path/to/cache
```

## Tips for Beginners:
1. **Start with popular packages** - More documentation available
2. **Read documentation** - Each package has different usage
3. **Use virtual environment** - Avoid conflicts
4. **Update regularly** - For security and bug fixes
5. **Backup lock file** - Commit `uv.lock` to repository

## Next Steps:
Now you're ready to start coding! Try creating your first project with installed packages.

## 📧 Contact Person

For additional support or questions:
- **Email**: rama@intura.co
- **Subject**: Package Installation Help