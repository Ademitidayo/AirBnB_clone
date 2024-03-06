AirBnB Clone Project

Authors
Adedayo Adeniji
Ayoola Nuatin

Project Overview
Welcome to our AirBnB clone project! Our goal is to build a command-line interface (CLI) tool that allows users to manage AirBnB objects efficiently. This project is the first step towards creating a full-fledged web application, and it involves implementing various features such as object initialization, serialization, deserialization, and file storage.

Project Specifications
Background Context
Before diving into the implementation details, it's essential to understand the concept of AirBnB and the objectives of this project. Please refer to the AirBnB concept page for a detailed overview.

Command Interpreter
We will develop a command interpreter similar to the Unix Shell but tailored to manage AirBnB objects. This CLI tool will allow users to perform various operations, including creating new objects, retrieving objects from storage, updating object attributes, and more.

Learning Objectives
By the end of this project, we aim to achieve the following learning objectives:

Creation of a Python package
Implementation of a command interpreter in Python using the cmd module
Understanding and implementation of Unit testing in a large project
Serialization and deserialization of Class objects
Handling of JSON files for data storage
Efficient management of datetime objects
Utilization of UUID for unique identifiers
Understanding and application of *args and **kwargs in function arguments
Proper handling of named arguments in functions
Requirements
Python Scripts
All files should be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
Code should adhere to the pycodestyle (version 2.8.*) guidelines
All modules, classes, and functions must be properly documented
The project should include a README.md file providing an overview of the project, installation instructions, usage guide, and any additional information deemed necessary
Python Unit Tests
Unit tests should cover all modules, classes, and functions
Test files should be organized in a structured manner within the 'tests' directory
The unittest module should be used for writing and executing tests
All tests should be well-documented, covering edge cases and expected behavior comprehensively
GitHub
The project should be hosted on GitHub, with one repository per group
Collaborative development practices are encouraged, including proper branching, pull requests, and code reviews
Execution
The CLI tool should support both interactive and non-interactive modes of operation. Interactive mode allows users to input commands directly into the shell, while non-interactive mode accepts commands from standard input.

bash
Copy code
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
Non-interactive mode:

bash
Copy code
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
Conclusion
With this project, we aim to lay the foundation for building a robust AirBnB clone application. By adhering to the specified requirements and objectives, we strive to create a high-quality, scalable, and efficient solution that meets the needs of our users.
