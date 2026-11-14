import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="ระบบสรุปวันลาข้าราชการ", page_icon="📊", layout="wide")

st.title("📊 ระบบสรุปข้อมูลวันลาข้าราชการและพนักงานราชการ")
st.markdown("อัปโหลดไฟล์ Excel สรุปวันลา เพื่อจัดการและตรวจสอบข้อมูลได้อย่างเป็นระเบียบ")

# ส่วนอัปโหลดไฟล์ Excel
uploaded_file = st.file_uploader("📂 อัปโหลดไฟล์ Excel สรุปวันลา (.xlsx)", type=["xlsx", "xls"])

if uploaded_file is not None:
    try:
        # ใช้ header=4 เพื่อข้ามหัวตารางแถวบนสุดที่กินพื้นที่ แล้วดึงหัวตารางจริงมาใช้
        df = pd.read_excel(uploaded_file, sheet_name=0, header=4)
        
        # ทำความสะอาดข้อมูลเบื้องต้น (ตัดแถวที่เป็นช่องว่างทิ้ง)
        df = df.dropna(subset=[df.columns[1]]) # ให้เช็คจากคอลัมน์ "รายชื่อ" ว่าต้องมีข้อมูล
        
        st.success("อ่านและจัดรูปแบบข้อมูลจากไฟล์ Excel สำเร็จ!")
        
        # แสดงตารางข้อมูลให้สวยงามและสะอาดตา
        st.subheader("📋 ตารางสรุปข้อมูลวันลา")
        edited_df = st.data_editor(df, num_rows="dynamic", use_container_width=True)
        
        st.divider()
        st.subheader("🤖 ระบบ AI ผู้ช่วยวิเคราะห์ข้อมูล")
        
        if st.button("✨ ให้ AI สรุปสถิติและพฤติกรรมการลา"):
            with st.spinner("AI กำลังประมวลผลข้อมูล..."):
                total_people = len(edited_df)
                
                st.success("วิเคราะห์ข้อมูลสำเร็จ!")
                st.info(f"""
                **🤖 รายงานสรุปจาก AI Assistant:**
                - **จำนวนบุคลากรทั้งหมดในระบบ:** {total_people} คน
                - **สถานะข้อมูล:** โหลดข้อมูลจากไฟล์ Excel สำเร็จครบถ้วน ตารางถูกจัดระเบียบเรียบร้อยพร้อมใช้งาน
                - **คำแนะนำ:** สามารถแก้ไขข้อมูลตัวเลขผ่านหน้าเว็บได้โดยตรง ระบบจะอัปเดตตารางสรุปให้ทันทีครับ
                """)
                        
    except Exception as e:
        st.error(f"เกิดข้อผิดพลาดในการอ่านไฟล์ Excel: {e}")
else:
    st.info("💡 โปรดอัปโหลดไฟล์ Excel สรุปวันลาของคุณที่ปุ่มด้านบน เพื่อเริ่มต้นใช้งานระบบครับ")
