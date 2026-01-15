# Crowd-Funding Console App

A Python-based command-line application that allows users to register, login, and manage fundraising campaigns. This project demonstrates the use of **File Handling (JSON)**, **Modular Architecture**, **Tabular Data Views**, and **Advanced Search Logic**.

## Features

### Authentication System
* **Register:** Secure account creation with strict validations:
    * **Names:** Letters only.
    * **Email:** Regex validation & duplicate checking.
    * **Password:** Hidden input (`****`) with confirmation.
    * **Phone:** Egyptian number validation (010, 011, 012, 015).
* **Login:** Secure session management.

### Project Management
* **Create Project:** Add campaigns with Title, Details, Target, and Date Range.
    * *Smart Validation:* Ensures End Date is logically after Start Date.
* **View Projects (Table View):** Displays all campaigns in a professional **Grid Table** using `tabulate`.
* **Edit/Delete:** Users can only modify or remove their *own* projects.

### Advanced Search System
* **Flexible Criteria:** Users can search by **Start Date** or **End Date**.
* **Smart Date Matching:** Supports two modes:
    * **Exact Date:** `2025-01-01`
    * **Year Only:** `2025` (Finds all projects in that year).

### Data Persistence
* Data is stored in structured **JSON files** (`users.json`, `projects.json`).
* Changes are saved automatically.

---

## Installation & Setup

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/ammaryousseff/Crowd-Funding-Project.git](https://github.com/ammaryousseff/Crowd-Funding-Project.git)
    cd Crowd-Funding-Project
    ```

2.  **Install Dependencies:**
    This project uses `pwinput` for passwords and `tabulate` for tables.
    ```bash
    pip install pwinput tabulate
    ```

3.  **Run the Application:**
    ```bash
    python main.py
    ```

---

## File Structure

```text
Crowd Funding/
│
├── main.py                  # Entry Point: Main Login/Register Menu
├── projects_menu.py         # Dashboard: Menu for logged-in users
│
├── 🔐 Authentication
│   ├── register.py          # Account creation logic
│   ├── login.py             # Authentication logic
│
├── 🚀 Features
│   ├── create_project.py    # Add new campaign
│   ├── view_projects.py     # List all campaigns (Table view)
│   ├── edit_project.py      # Edit own campaigns
│   ├── delete_project.py    # Delete own campaigns
│   └── search_project.py    # Search by Start/End Date or Year
│
├── 🛠️ Utilities
│   ├── read_write_json.py   # Shared JSON Load/Save functions
│   └── validate_date.py     # Shared Date validation
│
└── 💾 Database
    ├── users.json           # User data
    └── projects.json        # Project data
