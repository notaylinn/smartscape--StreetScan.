# StreetScan

AI-Assisted Road Defect Detection and Municipal Maintenance Planning System

**Track:** Smart Mobility & Infrastructure

## Problem

Road defects such as potholes, cracks, and surface deterioration create safety risks for drivers...

## Solution

StreetScan is a computer vision-based application that analyses uploaded road images...

## Key Features

- Road image upload and analysis
- Automated road defect detection
- Damage severity classification

## AI Methodology

StreetScan uses an AI-assisted computer vision workflow:

1. Image preprocessing using OpenCV
2. Defect segmentation and contour detection
3. Damage area calculation

## Technologies Used

- Python
- Streamlit
- OpenCV
- NumPy
- Pillow

## System Workflow

1. Upload a road image.
2. Image preprocessing is performed.
3. Defect regions are detected.

## Severity Classification

| Damage Score | Severity |
|-------------|----------|
| 0–25 | LOW |
| 26–60 | MEDIUM |
| 61–100 | HIGH |

## Generated Outputs

StreetScan provides:

- Road Damage Score
- Severity Level
- Defect Visualisation

## Municipality Dashboard

The dashboard provides municipal authorities with:

- Road Risk Index
- Repair Priority Assessment
- Estimated Repair Cost

## Potential Applications

- Municipal road maintenance planning
- Smart city infrastructure management

## Future Development

- Machine learning-based defect classification
- YOLO road defect detection

## Installation

```bash
pip install -r requirements.txt
streamlit run app.py
