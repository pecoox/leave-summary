import streamlit as st
import pandas as pd
import os
from google import genai

st.set_page_config(page_title="ระบบสรุปวันลาและ AI", page_icon="📊", layout="wide")

st.title("📊 ระบบสรุปข้อมูลวันลาข้าราชการและพนักงานราชการ")
st.markdown("อัปโหลดไฟล์ Excel สรุปวันลาของคุณเพื่อดูข้อมูล แก้ไข และให้ AI ช่วยวิเคราะห์ได้ทันที")

# ส่วนสำหรับอัปโหลดไฟล์ Excel
uploaded_file = st.file_uploader("📂 อัปโหลดไฟล์ Excel สรุปวันลา (.xlsx)", type=["xlsx", "xls"])

if uploaded_file is not None:
    try:
        # อ่านไฟล์ Excel ที่อัปโหลดเข้ามา (ดึงข้อมูลจาก Sheet แรก)
        df = pd.read_excel(uploaded_file, sheet_name=0)
        st.success("อัปโหลดและดึงข้อมูลจากไฟล์ Excel สำเร็จ!")
        
        # แสดงตารางข้อมูลแบบแก้ไขได้
        st.subheader("📋 ข้อมูลจากไฟล์ Excel")
        edited_df = st.data_editor(df, num_rows="dynamic", use_container_width=True)
        
        st.divider()
        st.subheader("🤖 ให้ AI ช่วยวิเคราะห์ข้อมูลจากตารางนี้")
        
        # ช่องใส่ API Key สำหรับเรียกใช้งาน AI
        api_key = st.text_input("กรอก Gemini API Key ของคุณ", type="password")

        if st.button("✨ ให้ AI วิเคราะห์พฤติกรรมการลา"):
            if not api_key:
                st.warning("กรุณากรอก API Key ก่อนใช้งาน AI ครับ")
            else:
                with st.spinner("AI กำลังอ่านและวิเคราะห์ข้อมูล..."):
                    try:
                        # แปลงข้อมูลตารางเป็นข้อความเพื่อให้ AI อ่าน
                        data_summary = edited_df.to_string(index=False)
                        
                        # เรียกใช้งาน Gemini API
                        client = genai.Client(api_key=api_key)
                        response = client.models.generate_content(
                            model="gemini-2.5-flash",
                            contents=f"คุณคือผู้ช่วยฝ่ายบุคคล ช่วยวิเคราะห์ข้อมูลสถิติการลาจากตารางนี้ให้หน่อย:\n{data_summary}\nสรุปจุดสังเกต ภาพรวม และให้คำแนะนำสั้นๆ เป็นภาษาไทย"
                        )
                        
                        st.success("วิเคราะห์สำเร็จ!")
                        st.markdown(response.text)
                    except Exception as e:
                        st.error(f"เกิดข้อผิดพลาดในการเชื่อมต่อ AI: {e}")
                        
    except Exception as e:
        st.error(f"ไม่สามารถอ่านไฟล์ Excel ได้: {e}")
else:
    st.info("💡 โปรดอัปโหลดไฟล์ Excel (เช่น ไฟล์สรุปวันลาของคุณ) ที่ปุ่มด้านบน เพื่อเริ่มต้นใช้งานระบบ")
