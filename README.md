# StreetScan

AI-Based Road Defect Detection and Risk Assessment System

## Overview

StreetScan is a lightweight computer vision application designed to automatically detect road defects from uploaded images and assess their severity.

The system analyses road surface conditions, identifies potential defects, estimates damage severity, and generates a maintenance recommendation report.

This solution can support municipalities, road maintenance teams, and infrastructure inspectors by providing a fast and accessible preliminary assessment tool.

---

## Features

- Road image upload
- Automated defect detection
- Damage severity classification
- Visual defect highlighting
- Risk assessment generation
- Inspection report generation
- User-friendly web interface

---

## Technologies Used

- Python
- Streamlit
- OpenCV
- NumPy
- Pillow

---

## System Workflow

1. Upload a road image.
2. Image preprocessing is performed.
3. Potential defect regions are identified.
4. Damage score is calculated.
5. Severity level is classified.
6. Risk assessment is generated.
7. Inspection report is produced.

---

## Severity Classification

| Damage Score | Severity |
|-------------|----------|
| 0–25% | LOW |
| 26–60% | MEDIUM |
| 61–100% | HIGH |

---

## Example Output

The system provides:

- Road Damage Score
- Severity Level
- Defect Visualisation
- Risk Assessment
- Maintenance Recommendation

---

## Potential Applications

- Road infrastructure monitoring
- Municipal maintenance planning
- Smart city initiatives
- Transportation safety analysis
- Infrastructure inspection support

---

## Future Improvements

- Machine Learning-based defect classification
- Real-time video analysis
- GPS integration
- Automated maintenance prioritisation
- Cloud deployment
- Mobile application support

---

## Author

Developed as part of the SmartScape Hackathon Project.

StreetScan demonstrates how computer vision can assist in road infrastructure monitoring and maintenance decision-making.

