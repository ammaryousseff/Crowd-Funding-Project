# 🚀 Crowd-Funding Console App

A Python-based command-line application that allows users to register, login, and manage fundraising campaigns. This project demonstrates the use of **File Handling (JSON)**, **Modular Programming**, **Authentication Logic**, and **Input Validation**.

## ✨ Features

### 🔐 Authentication System
* **Register:** Users can create an account with strict validations:
    * **First/Last Name:** Must be letters only (no numbers).
    * **Email:** Validated using Regex; checks for duplicates to prevent double registration.
    * **Password:** Secure hidden input (shows `****`) with confirmation check.
    * **Mobile Phone:** Must be a valid Egyptian number (starts with 010, 011, 012, 015).
* **Login:** Secure login system that grants access to the project dashboard.

### 📂 Project Management
* **Create Project:** Users can start a campaign with Title, Details, Target, and Dates.
    * *Smart Date Logic:* Automatically checks that the End Date is after the Start Date.
* **View Projects:** Lists all campaigns from all users.
* **Search Projects:** Find campaigns that start on a specific date.
* **Edit Projects:** Users can edit **only their own** projects.
    * Includes a sub-menu to select specific fields (Title, Details, Target, Dates) to update.
* **Delete Projects:** Users can delete **only their own** projects.

### 💾 Data Persistence
* All data is stored in structured **JSON files** (`users.json` & `projects.json`).
* Data remains saved even after the program is closed.

---

## 🛠️ Installation & Setup

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/ammaryousseff/Crowd-Funding-Project.git](https://github.com/ammaryousseff/Crowd-Funding-Project.git)
    cd Crowd-Funding-Project
    ```

2.  **Install Dependencies:**
    This project uses `pwinput` to mask passwords.
    ```bash
    pip install pwinput
    ```

3.  **Run the Application:**
    ```bash
    python main.py
    ```

---

## 📂 File Structure

This project follows a modular architecture to keep code clean and organized:

```text
Crowd Funding/
│
├── main.py                  # 🏁 Entry Point: The main loop (Login/Register Menu)
├── projects_menu.py         # 🎮 Dashboard: The menu for logged-in users
│
├── 🔐 Authentication
│   ├── register.py          # Logic for creating new accounts
│   ├── login.py             # Logic for user authentication
│
├── 🚀 Features
│   ├── create_project.py    # Logic to add a new campaign
│   ├── view_projects.py     # Logic to list all campaigns
│   ├── edit_project.py      # Logic to update existing campaigns
│   ├── delete_project.py    # Logic to remove a campaign
│   └── search_project.py    # Logic to search campaigns by date
│
├── 🛠️ Helpers & Utils
│   ├── read_write_json.py   # Shared functions to Load/Save JSON data
│   └── validate_date.py     # Shared function to validate date formats
│
├── 💾 Database
│   ├── users.json           # Stores registered user data
│   └── projects.json        # Stores project campaign data
│
└── .gitignore               # Specifies files to be ignored by Git
