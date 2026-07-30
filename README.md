# 📚 Library Management System

A **Python-based Command-Line Library Management System** designed to efficiently manage university library resources.

**Python | OOP | CLI Application**

---

## 📋 Table of Contents

* [Overview](#overview)
* [Library Resources](#library-resources)
* [Features](#features)
* [Project Structure](#project-structure)
* [Technologies Used](#technologies-used)
* [How to Run](#how-to-run)
* [Usage](#usage)
* [OOP Concepts](#oop-concepts)
* [Future Improvements](#future-improvements)
* [Author](#author)
* [License](#license)

---

## 📖 Overview

The **Library Management System** is a command-line Python application developed to manage resources in a university library.

The system supports four types of resources:

* 📚 Books
* 📰 Magazines
* 💿 Educational DVDs
* 💿 Lecture CDs

The application allows users to **add, remove, view, search, lend, and return resources** while automatically tracking the number of available copies.

This project was developed using **Object-Oriented Programming (OOP)** principles to create a structured, reusable, and maintainable application.

---

## 📚 Library Resources

| Resource Type          | Main Attributes                                                       | Available Subjects / Formats                                            |
| ---------------------- | --------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| 📖 **Book**            | ISBN, title, format, subject, rental price/day, copies                | Formats: Hardcover, Paperback<br>Subjects: Science, History, Literature |
| 📰 **Magazine**        | Magazine number, title, print type, subject, rental price/day, copies | Subjects: Science, Technology, Sports                                   |
| 💿 **Educational DVD** | DVD number, title, subject, rental price/day, copies                  | Subjects: Astronomy, Math, Technology                                   |
| 💿 **Lecture CD**      | CD number, title, subject, rental price/day, copies                   | Subjects: Music, Math, Foreign Languages                                |

---

## ✨ Features

* ➕ Add a new resource
* 🗑️ Remove an existing resource
* 📚 View available resources
* ❌ View unavailable resources
* 🔎 Search resources by subject
* 📤 Lend resources to students
* 📥 Return borrowed resources
* 📊 Automatically update available copy counts
* 📋 View all library resources
* 🖥️ Interactive command-line menu

---

## 📂 Project Structure

```text
LibraryManagementSystem/
│
├── main.py
├── library.py
├── resources.py
├── README.md
└── LICENSE
```

### `main.py`

Contains the main application, command-line menu, user input handling, and program execution.

### `library.py`

Contains the `Library` class responsible for managing resources, including:

* Adding resources
* Removing resources
* Searching resources
* Lending resources
* Returning resources
* Viewing resources

### `resources.py`

Contains the resource class hierarchy:

```text
Resource
│
├── Book
├── Magazine
├── EducationalDVD
└── LectureCD
```

---

## 🛠️ Technologies Used

* **Python 3.x**
* **Object-Oriented Programming (OOP)**
* **Abstract Base Classes**
* **Python Lists**
* **Command-Line Interface (CLI)**

No external Python packages are required.

---

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/library-management-system.git
```

### 2. Navigate to the project directory

```bash
cd library-management-system
```

### 3. Run the application

```bash
python main.py
```

---

## 💻 Usage

After running the application, the following menu will be displayed:

```text
=============================================
       UNIVERSITY LIBRARY SYSTEM
=============================================

1. Add New Resource
2. Remove Resource
3. View Available Resources
4. View Unavailable Resources
5. Search Resources by Subject
6. Lend Resource
7. Return Resource
8. View All Resources
9. Exit

=============================================

Enter your choice:
```

### 📤 Lending a Resource

Enter the resource number or ISBN.

Example:

```text
========== LEND RESOURCE ==========

Enter resource number / ISBN: ISBN1234

Resource 'The Solar System' has been lent successfully.
Remaining copies: 4
```

The system automatically decreases the available copy count.

### 📥 Returning a Resource

Enter the resource number or ISBN.

Example:

```text
========== RETURN RESOURCE ==========

Enter resource number / ISBN: ISBN1234

Resource 'The Solar System' has been returned successfully.
Available copies: 5
```

The system automatically increases the available copy count.

### ❌ Unavailable Resources

When the number of available copies reaches `0`, the resource is automatically considered unavailable.

```text
Copies: 0
Status: Unavailable
```

---

## 🧱 OOP Concepts

This project demonstrates the following Object-Oriented Programming concepts.

### Abstraction

The `Resource` class is implemented as an abstract base class and defines common functionality for all resources.

### Inheritance

The resource classes inherit from the common `Resource` class:

```text
Resource
   │
   ├── Book
   ├── Magazine
   ├── EducationalDVD
   └── LectureCD
```

### Encapsulation

Resource attributes and related operations are grouped within their respective classes.

### Polymorphism

Each resource class implements its own `display()` method, allowing different resource types to be handled through a common interface.

---

## 🎯 Learning Objectives

Through this project, I practiced:

* Python programming
* Object-Oriented Programming
* Class and object design
* Inheritance
* Abstraction
* Encapsulation
* Polymorphism
* Data management using lists
* Input validation
* CLI application development
* Modular programming

---

## 🔮 Future Improvements

* 🌐 Develop a web-based version
* 🖥️ Add a graphical user interface
* 👤 Add student account management
* 🔐 Implement authentication and user roles
* 📚 Add student borrowing history
* 📅 Add borrowing due dates
* 💰 Implement overdue fine calculation
* 📌 Add resource reservation functionality
* 💾 Add SQLite or MySQL database support
* 🧪 Add unit and integration testing

---

## 👨‍💻 Author

**Bhagya Premathilake**

Software Engineering Undergraduate

* GitHub: `YOUR-GITHUB-USERNAME`
* LinkedIn: `YOUR-LINKEDIN-USERNAME`
* Email: `YOUR-EMAIL@example.com`

---

## 📄 License

This project was created as part of **academic coursework**.

Licensed under the **MIT License**.

See the [LICENSE](LICENSE) file for more information.
