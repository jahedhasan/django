# Basic Git & GitHub Setup

## 1. Install Git

### Windows
- Download Git from [git-scm.com](https://git-scm.com/downloads)
- Run the installer and follow the default settings

### macOS
- Install using Homebrew:
  ```sh
  brew install git
  ```

### Linux (Debian/Ubuntu)
- Install using apt:
  ```sh
  sudo apt update
  sudo apt install git
  ```

## 2. Configure Git
```sh
# Set your username
git config --global user.name "Your Name"

# Set your email (should match your GitHub email)
git config --global user.email "your-email@example.com"
```

## 3. Verify Installation
```sh
git --version
```

## 4. Generate SSH Key and Connect to GitHub
```sh
ssh-keygen -t rsa -b 4096 -C "your-email@example.com"
```
- Press `Enter` to save the key
- Copy the SSH key:
  ```sh
  cat ~/.ssh/id_rsa.pub
  ```
- Add it to GitHub: 
  - Go to **GitHub > Settings > SSH and GPG keys**
  - Click **New SSH key**, paste the key, and save
- Test the connection:
  ```sh
  ssh -T git@github.com
  ```

## 5. Clone a Repository
```sh
git clone git@github.com:username/repository.git
```

## 6. Basic Git Commands
```sh
# Check repository status
git status

# Stage files
git add .

# Commit changes
git commit -m "Your commit message"

# Push changes to GitHub
git push origin main
```

## 7. Pull Changes from GitHub
```sh
git pull origin main
```

## 8. Create and Switch Branches
```sh
# Create a new branch
git branch new-feature

# Switch to the new branch
git checkout new-feature

# Push new branch to GitHub
git push -u origin new-feature
