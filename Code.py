import streamlit as st
import pandas as pd
import os

# ตั้งค่าหน้าเว็บ
st.set_page_config(page_title="ระบบสรุปวันลาและ AI ผู้ช่วย", page_icon="📊", layout="wide")

# ไฟล์สำหรับเก็บข้อมูล (Database จำลองแบบไฟล์ CSV บน GitHub)
DATA_FILE = "leave_data.csv"

# ข้อมูลตัวเริ่มต้นถ้ายังไม่มีไฟล์
if not os.path.exists(DATA_FILE):
    initial_data = pd.DataFrame({
        "รายชื่อ": ["นายธเนศ วิริยะจิตต์", "นายทีฆายุ ศรีโต", "นายธรัณ โอศิริ"],
        "ประเภท": ["ข้าราชการ", "ข้าราชการ", "ข้าราชการ"],
        "ลาพักผ่อน_ครั้ง": [2, 2, 1],
        "ลาพักผ่อน_วัน": [0.0, 0.0, 0.0],
        "ลาป่วย_ครั้ง": [4, 4, 12],
        "ลาป่วย_วัน": [1.0, 1.0, 7.0],
        "มาสาย_ครั้ง": [0, 0, 1],
        "มาสาย_วัน": [0.0, 0.0, 18.0]
    })
    initial_data.to_csv(DATA_FILE, index=False)

# โหลดข้อมูล
df = pd.read_csv(DATA_FILE)

st.title("📊 ระบบสรุปข้อมูลการมาปฏิบัติงานและวันลา (Streamlit)")
st.markdown("จัดการข้อมูลวันลา บันทึก แก้ไข และให้ AI ช่วยวิเคราะห์ได้ทันทีผ่าน GitHub")

# แสดงตารางข้อมูลหลัก
st.subheader("📋 ตารางสรุปข้อมูลปัจจุบัน")
edited_df = st.data_editor(df, num_rows="dynamic", use_container_width=True)

# ปุ่มบันทึกข้อมูลที่แก้ไขบนตาราง
if st.button("💾 บันทึกการเปลี่ยนแปลงข้อมูล"):
    edited_df.to_csv(DATA_FILE, index=False)
    st.success("บันทึกข้อมูลลงระบบเรียบร้อยแล้ว!")
    st.rerun()

# ส่วนจำลอง AI วิเคราะห์ข้อมูล
st.divider()
st.subheader("🤖 AI ผู้ช่วยวิเคราะห์สถิตการลา")

if st.button("✨ ให้ AI วิเคราะห์พฤติกรรมการลาในระบบ"):
    with st.spinner("AI กำลังวิเคราะห์ข้อมูล..."):
        total_sick = edited_df["ลาป่วย_วัน"].sum()
        max_late_person = edited_df.loc[edited_df["มาสาย_วัน"].idxmax()]["รายชื่อ"] if not edited_df.empty else "-"
        
        # ผลวิเคราะห์จาก AI
        st.info(f"""
        **ผลการวิเคราะห์โดย AI Assistant:**
        - **ยอดรวมวันลาป่วยทั้งหมดในองค์กร:** {total_sick} วัน
        - **บุคลากรที่มีสถิติมาสายสูงสุด:** {max_late_person}
        - **คำแนะนำ:** ภาพรวมการลาพักผ่อนอยู่ในเกณฑ์ปกติ แต่อาจต้องติดตามสถิตลาป่วยในบางบุคคลเพื่อดูแลสุขภาพเชิงป้องกันครับ
        """)