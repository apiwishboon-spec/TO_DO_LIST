📝 To-Do List — README
Table of Contents

Project Overview

Features

Screenshots

Technologies Used

Installation

Usage

File Structure

Customization

License

Contributing

Acknowledgements

Future Improvements

Project Overview

Welcome to 📝 To-Do List, a next-level productivity web application built with Python, Flask, HTML, CSS, and JavaScript. This project is designed to help users manage tasks efficiently with a timer, audio alerts, speech notifications, and real-time task completion tracking.

The project emphasizes:

Clean UI with gradient backgrounds (light pink → light blue).

Easy-to-use interface for adding, editing, and completing tasks.

Audio and speech alerts to remind you about deadlines.

Task completion feedback with fun sounds and popups.

Local and browser-based notifications for productivity reinforcement.

Whether you're a student, freelancer, or anyone who needs hardcore task management, this To-Do List app is perfect for staying on top of your day.

Features

Add new tasks with optional deadlines (HH:MM).

Checkbox completion: Mark tasks as done and see how many are left.

Audio notifications:

alert.mp3 when task is due.

Text-to-speech announcing the task.

end_alert.mp3 after speech finishes.

congrats.mp3 if 0 tasks left.

multi_tasks.mp3 if multiple tasks remain.

Popup confirmations to delete tasks when due.

Responsive design with gradient backgrounds.

Copyright notice fixed at the bottom-right.

Fully client-side notifications (browser notifications).

Task timer checking every minute.

This app blends productivity + gamification to keep you motivated. ✅

Screenshots

Add your screenshots here with markdown syntax

![Home Screen](./screenshots/home.png)
![Task Reminder](./screenshots/reminder.png)
![Task Completed](./screenshots/completed.png)

Technologies Used

Backend: Python 3.13, Flask

Frontend: HTML5, CSS3, JavaScript (ES6), Web Speech API

Audio: MP3 files for alerting and celebration

Notifications: Web Notifications API

Fonts: Google Fonts – Inter

Version Control: Git + GitHub

Installation

Clone the repository

git clone https://github.com/YourUsername/todo_app.git
cd todo_app


Install dependencies

pip3 install flask


Run the app

python3 app.py


Open in browser

Go to http://127.0.0.1:5000

Usage

Enter your task in the New task… field.

Optional: Set a deadline using the time input.

Click Add. Task appears in the list with a checkbox.

When the task time arrives:

alert.mp3 plays.

Browser notification shows up.

Speech announces task: “You should finish the task … now!”

end_alert.mp3 plays.

Popup asks if you want to delete the task.

Checking the box manually deletes the task and plays either:

congrats.mp3 (0 tasks left)

multi_tasks.mp3 (>1 task left)

All completed tasks update the remaining task count.

File Structure
todo_app/
├─ app.py             # Flask backend
├─ LICENSE            # Apache License 2.0
├─ README.md          # This file
├─ templates/
│   └─ index.html     # Main HTML page
└─ static/
    ├─ alert.mp3
    ├─ end_alert.mp3
    ├─ congrats.mp3
    └─ multi_tasks.mp3

Customization

Change gradient colors: Modify background: linear-gradient(135deg, #ffc0cb, #add8e6) in CSS.

Add custom sounds: Replace MP3s in /static.

Change title or copyright: Update <h1> and .copyright.

Adjust notification frequency: Edit setInterval in JS.

License

This project is licensed under the Apache License 2.0. See LICENSE
 file for details.

© 2025 APIWISH ANUTARAVANICHKUL

Contributing

Contributions are welcome! Please follow these steps:

Fork this repository.

Create a new branch: git checkout -b feature-name.

Make your changes.

Commit your changes: git commit -m "Add new feature".

Push to your branch: git push origin feature-name.

Open a Pull Request.

Acknowledgements

Flask – Python web framework

Web Speech API – for TTS notifications

Google Fonts – Inter font family

Inspiration: Hardcore productivity apps

Future Improvements

Save tasks persistently using localStorage or a database

Allow editing tasks after creation

Mobile-friendly interface

Dark mode toggle

Custom notification sounds per task

Add priority levels and tags
