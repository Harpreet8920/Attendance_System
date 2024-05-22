# Attendance_System
# Attendance System using Face Recognition

This project implements an attendance system using face recognition technology. The system captures video input from a webcam, recognizes known faces, and logs attendance with timestamps into a CSV file.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Files](#files)
- [Known Issues](#known-issues)
- [Future Improvements](#future-improvements)
- [Contributing](#contributing)

## Features

- Real-time face recognition using webcam input.
- Attendance logging with timestamps.
- CSV file generation for each day's attendance.
- Text overlay on the video feed indicating recognized individuals.

## Requirements

- Python 3.x
- `face_recognition` library
- `opencv-python` library
- `numpy` library

## Files

- `attendance_system.py`: Main script for running the attendance system.
- `faces/`: Directory containing images of known individuals.
- `README.md`: Documentation for the project.

## Known Issues

- The system may not recognize faces accurately in poor lighting conditions.
- The accuracy of face recognition may decrease with a larger number of known faces.

## Future Improvements

- Add support for more robust logging with additional details such as entry and exit times.
- Implement an interface for adding new faces dynamically.
- Improve face recognition accuracy by using advanced models and techniques.
- Add functionality to handle multiple cameras.

## Contributing

Contributions are welcome! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add some feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Open a pull request.
