##StreetScan##

AI-Assisted Road Defect Detection and Maintenance Planning System

Track

Track 1: Smart Mobility & Infrastructure

##Problem##

Road defects such as potholes, cracks, and surface deterioration pose significant risks to drivers, increase vehicle maintenance costs, and create challenges for municipalities responsible for infrastructure maintenance.

Traditional road inspections are often time-consuming, expensive, and dependent on manual assessment.

StreetScan aims to provide a fast and accessible AI-assisted solution for identifying road defects and supporting maintenance decision-making.

##Solution##

StreetScan is a computer vision-based road infrastructure assessment system that analyses uploaded road images, detects potential defects, evaluates severity levels, estimates repair costs, and generates maintenance recommendations.

The system supports both road users and municipal authorities by providing actionable insights for infrastructure maintenance planning.

##Key Features##

* Road image upload and analysis
* Automated defect detection using computer vision
* Damage severity classification (Low, Medium, High)
* Visual defect highlighting
* Risk assessment generation
* Estimated damaged area calculation
* Estimated repair cost calculation
* Maintenance priority assessment
* Repair material recommendations
* Driver safety recommendations
* Location-based reporting (city and address)
* Automated inspection report generation

##AI Methodology##

StreetScan uses an AI-assisted computer vision pipeline:

1. Image preprocessing using OpenCV
2. Defect region segmentation
3. Defect area estimation
4. Damage score calculation
5. Severity classification
6. Infrastructure risk assessment
7. Maintenance recommendation generation
8. Repair cost estimation

The system combines computer vision techniques with rule-based infrastructure assessment logic to support maintenance planning and decision-making.

##Technologies Used##

* Python
* Streamlit
* OpenCV
* NumPy
* Pillow

##System Workflow##

1. Upload a road image.
2. The image is preprocessed.
3. Defect regions are detected.
4. Damage score is calculated.
5. Severity level is determined.
6. Repair cost is estimated.
7. Risk level is assessed.
8. Repair recommendations are generated.
9. Inspection report is produced.

##Severity Classification##

Damage Score	Severity
0–25	LOW
26–60	MEDIUM
61–100	HIGH

##Output Information##

StreetScan generates:

* Road Damage Score
* Severity Level
* Defect Visualisation
* Infrastructure Risk Assessment
* Estimated Damaged Area
* Estimated Repair Cost
* Recommended Repair Method
* Recommended Repair Material
* Driver Recommendations
* Municipal Maintenance Recommendations
* Inspection Report

##Potential Applications##

* Municipal road maintenance planning
* Smart city infrastructure management
* Road safety monitoring
* Transportation infrastructure assessment
* Infrastructure inspection support
* Public works prioritisation

##Future Development##

* Machine learning-based defect classification
* YOLO road defect detection
* GPS integration
* Real-time road monitoring
* Cloud deployment
* Mobile application
* Municipality dashboard integration
* Predictive maintenance analytics

##Installation##

pip install -r requirements.txt
streamlit run app.py

##Author##

Developed for the SmartScape AI Smart City Hackathon.

StreetScan demonstrates how AI-assisted computer vision can support road infrastructure assessment, maintenance planning, and smart city decision-making.
