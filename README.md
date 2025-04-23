# Git Basics for This Project

Hey!

Welcome to the projects repository!
We're going to use **Git** to collaborate smoothly and keep our code organized. Even if you've never used Git before—no worries! This guide is for **beginners**, with a focus on **just what you need** to contribute.

Let’s get started 💡

---

## 🤔 What is Git, and Why Use It?

Git is a **version control system**. It helps us:

- ✅ Save the history of our work
- ✅ Collaborate without overwriting each other’s code
- ✅ Backtrack if something breaks
- ✅ Understand who changed what and why

With Git, we don’t send each other files like `final_version_REALLY_final_THIS_ONE.tex`.  
Instead, we all share **one clean, organized project history**. Beautiful, right? 😄

---

## ⚙️ Setup Instructions

### ✅ If you're on **Linux/macOS**:
You're ready! Just open your terminal and go!

### ✅ If you're on **Windows**:
We recommend using **WSL (Windows Subsystem for Linux)** to work like you're on Linux.

To open WSL:

1. Press `Win + S` and type `wsl`
2. Open the WSL terminal (usually Ubuntu)

Once inside, you’re in a Linux environment and can use Git like the others.

---

## 🧰 Common Git Commands

Here are the essential Git commands you’ll need—with easy explanations and best practices.

### 1. 🔍 Check Your Project's Status
```bash
git status
```
Shows what's going on. Use this *often* to stay in the loop!

---

### 2. 🔄 Get the Latest Changes
```bash
git pull
```
Before you do anything: **always pull first**. This fetches updates from your teammates so you're working on the latest version.

> **✅ Best Practice**:  
> `git pull` BEFORE you start working  
> `git pull` BEFORE you push

---

### 3. ➕ Stage Your Changes
```bash
git add -p
```
Instead of adding *everything*, `-p` lets you pick what to include. This helps keep your commits clean and focused.

> Pro tip: You can still do `git add .` if you're sure you want everything.

---

### 4. 📝 Save Your Work with a Commit
```bash
git commit -m "Explain clearly what you did"
```
This saves your staged changes. The message should describe **why** you made the change.

> Think of commits like writing a diary entry for the project.

---

### 5. 🚀 Share Your Work
```bash
git push
```
Pushes your changes to the shared project. Only do this **after you've pulled** and resolved any conflicts.

> ❗ **NEVER** run `git push --force`. That can delete other people’s work.

---

### 6. 🔄 (Optional) Switch to Another Branch or File
```bash
git checkout branch-name
```
Or to undo changes in a file:
```bash
git checkout path/to/file
```
Useful if you want to switch branches or undo changes in a file before committing.
But be warned, restoring a file will delete all uncommited changes.
If you just want to see how the old file looked you can do a 
```bash
git show <branch/commit> <filename> > <new-file-name-for-temporary-save>
``

---

## ✅ Typical Workflow Example

Here’s a standard daily routine to follow:

```bash
# 1. Go to your project folder
cd my-project

# 2. Make sure you're on the right branch
git status

# 3. Pull the latest changes BEFORE anything
git pull

# 4. Work on your code...

# 5. Check what you've changed
git status

# 6. Add your changes selectively
git add -p

# 7. Save with a clear commit message
git commit -m "Add feature to greet the user"

# 8. Pull again in case someone else pushed changes
git pull

# 9. Push your work
git push
```

---

## 💬 A Few Final Tips

- 🧠 **Keep commits small & focused** (1 commit = 1 idea)
- 💥 **Never force push** – it can erase other people’s work
- 🔄 **Pull often** – especially before pushing or starting new work
- 🧪 **Experiment?** Use a branch! Ask if you want help with that.

---

## 🫶 You're Not Alone!

If you’re unsure, just ask your teammates. Git can feel weird at first, but soon it’ll be second nature.

> Happy coding and collaborating!  
> Let's build something awesome together 🚀

---

Let me know if you'd like me to generate this as a downloadable file, or want to include project-specific sections like cloning the repo, setting up remotes, or any branching strategy!
