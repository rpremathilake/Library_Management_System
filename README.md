<div align="center">

  <h1>📚 Library Management System 📚</h1>

  <p>A Python-based Command-Line Library Management System developed using Object-Oriented Programming (OOP) principles.

The system allows a university library to manage different types of educational resources, including Books, Magazines, Educational DVDs, and Lecture CDs. Users can add, remove, search, lend, return, and monitor the availability of resources through a simple command-line interface.</p>

  <div>
    <img src="https://img.shields.io/badge/-Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
    <img src="https://img.shields.io/badge/-OOP-007ACC?style=for-the-badge&logo=visual-studio-code&logoColor=white" alt="OOP" />
  </div>

</div>

---


# Table of Contents

1. [Overview](#overview)  
2. [Library Resources](#library-resources)  
3. [Features](#features)  
4. [Usage](#usage)  
5. [Technologies Used](#technologies-used)  
6. [Future Improvements](#future-improvements)  
7. [Author](#author)  
8. [License](#license)  

## Overview

This project is a **command-line Python program** designed to manage a university library’s resources. The system supports four types of resources: **Books, Magazines, Educational DVDs, and Lecture CDs**.

The program allows users to add, remove, view, lend, and update resources with details such as subject, format, rental price, and availability.

---

## Library Resources

| Resource Type    | Attributes                                                                                     | Example                                                                                      | Available Subjects/Formats                                    |
|------------------|------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------|--------------------------------------------------------------|
| **Book**         | ISBN number, title, format, subject, rental price per day, number of copies                    | `[ISBN1234, The Solar System, Hardcover, Science, 15.00, 5]`                                 | Formats: Hardcover, Paperback<br>Subjects: Science, History, Literature |
| **Magazine**     | Magazine number, title, color or black & white print, subject, rental price per day, copies   | `[01, History of Cricket, color, Sports, 5.00, 7]`                                           | Subjects: Science, Technology, Sports                         |
| **Educational DVD** | DVD number, title, subject, rental price per day, number of copies                            | `[10, Birth of the Solar System, Astronomy, 2.50, 10]`                                       | Subjects: Astronomy, Math, Technology                         |
| **Lecture CD**   | CD number, title, subject, rental price per day, number of copies                              | `[21, Basics of Western Music, Music, 1.50, 11]`                                             | Subjects: Music, Math, Foreign Languages                      |

---

## Features

- **Add a new resource** to the system.
- **Remove an existing resource** from the system.
- **View available resources** by resource type.
- **View unavailable resources** by resource type.
- **Filter and view all resources** by subject across all types.
- **Lend a resource** to students.
- **Update resources** when returned.

---

## Usage

The program runs entirely in the command line with simple prompts to perform actions such as adding, lending, or viewing resources.

---

## Technologies Used

- Python 3.x
- Object-oriented programming principles

---

## Future Improvements

- Implement a GUI interface for improved usability.
- Add student user accounts with borrowing history.
- Support for reservations and overdue fines.

---

## Author

 **Name:** Dulanjalee Gamage  
 **Role:** Software Engineering Undergraduate  
 **GitHub:** [@dulaagamage](https://github.com/dulaagamage)  
 **LinkedIn:** [Dulanjalee Gamage](https://www.linkedin.com/in/dulanjalee-gamage-01a7aa207/)  
 **Email:** dulaagamage123@gmail.com  

---

## License

This project was created as part of academic coursework.  
Licensed under the [MIT License](LICENSE).  

You are free to use and modify this project for educational and non-commercial purposes, with attribution to the original author.
