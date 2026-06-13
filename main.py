import streamlit as st
from PIL import Image
import cv2
import numpy as np

st.set_page_config(
    page_title="StreetScan",
    layout="wide"
)

st.title("StreetScan")
st.subheader("AI-Based Road Defect Detection and Risk Assessment")

uploaded_file = st.file_uploader(
    "Upload Road Image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file:

    image = Image.open(uploaded_file).convert("RGB")

    img = np.array(image)

    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

    blur = cv2.GaussianBlur(gray, (7, 7), 0)

    _, mask = cv2.threshold(
        blur,
        90,
        255,
        cv2.THRESH_BINARY_INV
    )

    kernel = np.ones((5, 5), np.uint8)

    mask = cv2.morphologyEx(
        mask,
        cv2.MORPH_OPEN,
        kernel
    )

    mask = cv2.morphologyEx(
        mask,
        cv2.MORPH_CLOSE,
        kernel
    )

    contours, _ = cv2.findContours(
        mask,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )

    result_img = img.copy()

    total_damage_area = 0

    for contour in contours:

        area = cv2.contourArea(contour)

        if area > 1000:

            total_damage_area += area

            x, y, w, h = cv2.boundingRect(contour)

            cv2.rectangle(
                result_img,
                (x, y),
                (x + w, y + h),
                (255, 0, 0),
                4
            )

            cv2.putText(
                result_img,
                "DEFECT",
                (x, y - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (255, 0, 0),
                2
            )

    image_area = img.shape[0] * img.shape[1]

    raw_damage = (
        total_damage_area / image_area
    ) * 100

    damage_score = min(
        round(raw_damage * 15, 2),
        100
    )

    if damage_score > 60:
        severity = "HIGH"
    elif damage_score > 25:
        severity = "MEDIUM"
    else:
        severity = "LOW"

    col1, col2 = st.columns([2, 1])

    with col1:

        st.image(
            image,
            caption="Uploaded Road Image",
            use_container_width=True
        )

    with col2:

        st.subheader("Analysis Results")

        st.metric(
            "Road Damage Score",
            f"{damage_score}%"
        )

        st.metric(
            "Severity Level",
            severity
        )

        st.progress(
            min(int(damage_score), 100)
        )

        if severity == "HIGH":

            st.error(
                "Critical road defect detected"
            )

        elif severity == "MEDIUM":

            st.warning(
                "Moderate road defect detected"
            )

        else:

            st.success(
                "Road condition appears acceptable"
            )

    st.divider()

    st.subheader("Detected Defect Regions")

    st.image(
        result_img,
        use_container_width=True
    )

    st.divider()

    st.subheader("Risk Assessment")

    if severity == "HIGH":

        st.write("""
- High risk for vehicles
- Potential safety hazard
- Immediate inspection required
- Maintenance should be prioritised
""")

    elif severity == "MEDIUM":

        st.write("""
- Moderate deterioration detected
- Monitoring required
- Maintenance recommended
""")

    else:

        st.write("""
- No significant damage detected
- Continue routine monitoring
- No immediate action required
""")

    st.divider()

    st.subheader("Maintenance Recommendation")

    if severity == "HIGH":

        st.info(
            "Recommended repair timeframe: Within 7 days."
        )

        st.write(
            "Priority Level: Critical Infrastructure Maintenance"
        )

    elif severity == "MEDIUM":

        st.info(
            "Recommended repair timeframe: Within 30 days."
        )

        st.write(
            "Priority Level: Scheduled Maintenance"
        )

    else:

        st.info(
            "Recommended repair timeframe: Routine inspection cycle."
        )

        st.write(
            "Priority Level: Monitoring Only"
        )

    st.divider()

    st.subheader("AI Insights")

    estimated_cost = int(damage_score * 25)

    st.write(
        f"Estimated Repair Complexity: {severity}"
    )

    st.write(
        f"Estimated Maintenance Cost Index: {estimated_cost}"
    )

    if severity == "HIGH":

        st.write(
            "Potential impact: Increased vehicle damage risk and reduced road safety."
        )

    elif severity == "MEDIUM":

        st.write(
            "Potential impact: Progressive deterioration if maintenance is delayed."
        )

    else:

        st.write(
            "Potential impact: Minimal infrastructure risk."
        )

    if st.button("Generate Inspection Report"):

        st.subheader("Road Inspection Report")

        st.write(f"Road Damage Score: {damage_score}%")
        st.write(f"Severity Level: {severity}")

        if severity == "HIGH":

            st.write(
                "Recommended Action: Immediate repair and safety inspection."
            )

        elif severity == "MEDIUM":

            st.write(
                "Recommended Action: Scheduled maintenance."
            )

        else:

            st.write(
                "Recommended Action: Routine monitoring."
            )

        st.write(
            f"Maintenance Cost Index: {estimated_cost}"
        )

        st.write(
            f"Estimated Repair Complexity: {severity}"
        )

        if severity == "HIGH":

            st.write(
                "Suggested Repair Timeframe: Within 7 days."
            )

        elif severity == "MEDIUM":

            st.write(
                "Suggested Repair Timeframe: Within 30 days."
            )

        else:

            st.write(
                "Suggested Repair Timeframe: Routine inspection cycle."
            )
            st.divider()

    st.subheader("Municipality Repair Dashboard")

    city = st.text_input(
        "Location",
        placeholder="Enter city or road name"
    )

    if severity == "HIGH":

        risk_index = 90
        priority = "CRITICAL"
        material = "Hot Mix Asphalt"

    elif severity == "MEDIUM":

        risk_index = 60
        priority = "MEDIUM"
        material = "Cold Asphalt Patch"

    else:

        risk_index = 20
        priority = "LOW"
        material = "Monitoring Only"

    st.metric(
        "Road Risk Index",
        f"{risk_index}/100"
    )

    st.metric(
        "Estimated Repair Cost",
        f"${estimated_cost}"
    )

    st.metric(
        "Repair Priority",
        priority
    )

    st.metric(
        "Recommended Material",
        material
    )

    st.divider()

    st.subheader("Municipality Report")

    report = f"""
Road Defect Assessment Report

Location: {city}

Severity Level: {severity}

Road Risk Index: {risk_index}/100

Repair Priority: {priority}

Recommended Material: {material}

Estimated Cost: ${estimated_cost}

Suggested Repair Timeframe:
{('Within 7 Days' if severity == 'HIGH'
else 'Within 30 Days' if severity == 'MEDIUM'
else 'Routine Monitoring')}
"""

    st.text_area(
        "Generated Report",
        report,
        height=250
    )
