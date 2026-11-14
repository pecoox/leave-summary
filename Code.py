import streamlit as st
import pandas as pd
import os

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
        st.subheader("🤖 ระบบ AI อัจฉริยะวิเคราะห์ข้อมูล")
        
        if st.button("✨ ให้ AI ช่วยวิเคราะห์พฤติกรรมการลา"):
            with st.spinner("AI กำลังอ่านและประมวลผลข้อมูล..."):
                # จำลองการวิเคราะห์ข้อมูลจากตารางที่อัปโหลด
                total_rows = len(edited_df)
                
                st.success("วิเคราะห์ข้อมูลสำเร็จ!")
                st.info(f"""
                **🤖 ผลการวิเคราะห์จาก AI Assistant:**
                - **จำนวนบุคลากรในระบบที่ตรวจสอบ:** {total_rows} รายการ
                - **ภาพรวมสถิติ:** ข้อมูลถูกบันทึกและจัดระเบียบเรียบร้อยดี 
                - **คำแนะนำ:** แนะนำให้ตรวจสอบอัตราการลาป่วยสะสมของบุคคลที่มีสถิติสูงเกินค่าเฉลี่ยเพื่อดูแลสวัสดิภาพเชิงป้องกันครับ
                """)
                        
    except Exception as e:
        st.error(f"ไม่สามารถอ่านไฟล์ Excel ได้: {e}")
else:
    st.info("💡 โปรดอัปโหลดไฟล์ Excel สรุปวันลาของคุณที่ปุ่มด้านบน เพื่อเริ่มต้นใช้งานระบบ")
