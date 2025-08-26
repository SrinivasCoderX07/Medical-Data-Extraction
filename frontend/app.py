import streamlit as st
import requests
from pdf2image import convert_from_bytes
import ast
import time
import json

POPPLER_PATH = r"C:\poppler-25.07.0\Library\bin"
URL = "http://127.0.0.1:8000/{}"

# 🎯 Title with emoji
st.title("🩺 Medical Data Extractor 👩‍⚕️📄")

# 📂 Upload section
st.markdown("### 📂 Upload your medical document (PDF)")
file = st.file_uploader("Drop a file here 👇", type="pdf")

# Selection row
col3, col4 = st.columns(2)
with col3:
    file_format = st.radio(
        label="📝 Select type of document", 
        options=["💊 Prescription", "👤 Patient Details"], 
        horizontal=True
    )

with col4:
    if file and st.button("🚀 Upload PDF", type="primary"):
        bar = st.progress(50)
        time.sleep(2)
        bar.progress(100)

        payload = {'file_format': file_format.lower().replace("💊 ", "").replace("👤 ", "")}
        files = [('file', file.getvalue())]

        response = requests.post(URL.format('extract_from_doc'), data=payload, files=files)
        dict_str = response.content.decode("UTF-8")
        data = ast.literal_eval(dict_str)

        if data:
            st.session_state.update(data)
            st.success("✅ Data extracted successfully!")

# 📄 Show file + details side by side
if file:
    pages = convert_from_bytes(file.getvalue(), poppler_path=POPPLER_PATH)

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("📄 Uploaded File Preview")
        st.image(pages[0], caption="First page of your PDF")

    with col2:
        if st.session_state:
            st.subheader("📋 Extracted Details")

            if "prescription" in file_format.lower():
                name = st.text_input("👤 Name", value=st.session_state.get("patient_name", ""))
                address = st.text_input("🏠 Address", value=st.session_state.get("patient_address", ""))
                medicines = st.text_input("💊 Medicines", value=st.session_state.get("medicines", ""))
                directions = st.text_input("📖 Directions", value=st.session_state.get("directions", ""))
                refill = st.text_input("🔄 Refill", value=st.session_state.get("refill", ""))

            elif "patient" in file_format.lower():
                name = st.text_input("👤 Name", value=st.session_state.get("patient_name", ""))
                phone = st.text_input("📞 Phone No.", value=st.session_state.get("phone_no", ""))
                vacc_status = st.text_input("💉 Hepatitis B Vaccination Status", value=st.session_state.get("vaccination_status", ""))
                med_problems = st.text_input("🩺 Medical Problems", value=st.session_state.get("medical_problems", ""))
                has_insurance = st.text_input("💳 Insurance Status", value=st.session_state.get("has_insurance", ""))

            # Submit button
            if st.button("✅ Submit", type="primary"):
                if "patient" in file_format.lower():
                    response = requests.post(
                        URL.format("patient_details"), 
                        data={'name': name,
                              'phone': phone,
                              'vacc_status': vacc_status,
                              'med_problems': med_problems,
                              'has_insurance': has_insurance})
                else:
                    response = requests.post(
                        URL.format("prescription"), 
                        data={'name': name,
                              'address': address,
                              'medicines': medicines,
                              'directions': directions,
                              'refill': refill})

                resp = json.loads(response.content.decode("UTF-8"))
                if resp:
                    st.balloons()  # 🎈 celebratory animation
                    st.success("🎉 Details successfully recorded in database!")
                else:
                    st.error("⚠️ Error saving data into Database")

                # Clear state
                for key in list(st.session_state.keys()):
                    del st.session_state[key]
