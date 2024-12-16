# Todo App

Welcome to the Todo App! This web application is designed to help you manage your tasks efficiently. Built using modern technologies, it offers a clean, responsive interface and robust functionality.

## Features

- Create new tasks by entering a title and description.
- Update tasks to mark them as completed or edit their details.
- Delete tasks that are no longer needed.
- Search for tasks by title or description.
- Responsive design for seamless use on both desktop and mobile devices.

## Technologies Used

### 1. Flask - Python Web Framework

Flask is a lightweight and flexible web framework for Python. It handles routing, request processing, and rendering dynamic web pages using templates.

### 2. Jinja2 - Templating Engine

Jinja2 allows for dynamic generation of HTML with Python-like logic. It is used to render dynamic content, such as displaying tasks and handling user input. Reusable templates (e.g., `base.html`) maintain a consistent design.

### 3. SQLite - Relational Database

SQLite is a lightweight, serverless database management system used to store and manage tasks. It tracks task details like title, description, and status. Its simplicity makes it ideal for small-scale applications.

### 4. Bootstrap - Front-End Framework

Bootstrap ensures the app is responsive and visually appealing. It provides pre-designed components like buttons, forms, and navigation bars, enabling a modern and user-friendly UI.

### 5. Other Tools and Technologies

- **HTML5 & CSS3:** For structuring and styling web pages.
- **JavaScript:** For basic client-side interactions.
- **SQLAlchemy (optional):** As an ORM for interacting with SQLite (if preferred over raw SQL queries).

## How It Works

The Todo App operates as follows:

1. **Create Tasks:** Users can create new tasks by providing a title and description.
2. **Update Tasks:** Tasks can be marked as completed or updated with new details.
3. **Delete Tasks:** Unnecessary tasks can be removed.
4. **Search Tasks:** Search functionality helps users quickly find tasks by title or description.

Flask handles HTTP requests and responses. When users interact with the app, the backend updates the SQLite database, and the changes are dynamically reflected on the frontend, styled with Bootstrap.

## Why These Technologies?

This combination of technologies ensures simplicity, speed, and scalability:

- **Flask:** Provides a minimal yet powerful backend framework.
- **Jinja2:** Enables dynamic and reusable HTML templates.
- **SQLite:** Offers a simple and reliable database solution.
- **Bootstrap:** Guarantees a polished, responsive design.

Together, these tools allow for the development of a modern web app with a clean interface and robust functionality, all without unnecessary complexity.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/todo-app.git
   ```
2. Navigate to the project directory:
   ```bash
   cd todo-app
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the app:
   ```bash
   python app.py
   ```
5. Open your browser and go to `http://127.0.0.1:5000`.

## Demo

You can try a live demo of the Todo App <a href="https://ajitchoudhary.pythonanywhere.com/" target="_blank">here</a>.

## Contributing

Contributions are welcome! Feel free to submit a pull request or open an issue for suggestions or bug reports.

## License

This project is licensed under the [MIT License](LICENSE).
