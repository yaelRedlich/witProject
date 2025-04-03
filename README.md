Project Description in English:
wit - A CLI-Based Version Control System using Click

The "wit" project is a simple version control system inspired by Git, written in Python and using the Click library to provide a Command-Line Interface (CLI). It allows users to track file changes, commit updates, view version history, and revert to previous versions.

Key Features and Implementation Highlights:
Object-Oriented Programming (OOP) Approach:

The system is structured around a Repository class that manages the repository and a Commit class representing each commit.

OOP principles are used to maintain a clean and modular design.

File and Version Management:

A .wit directory is created to store version-related data, including commits and a staging area.

Each commit is stored in a separate directory, enabling version restoration.

Commit history is managed using a JSON file.

Utilization of Python Libraries for File Handling:

os and shutil are used for file management and directory operations.

json is used to store and retrieve commit data.

datetime provides timestamps for commits.

CLI Interaction with Click:

Commands such as wit init, wit add, wit commit, wit log, wit checkout, and wit status are implemented using Click, making the interface user-friendly.

The system ensures that commits only occur when changes are detected.

This project was designed with flexibility, scalability, and code readability in mind, focusing on OOP principles and an intuitive CLI interface.








