import streamlit as st

st.title("تطبيق صحة الكلى")
st.subheader("حاسبة معدل الفلترة الكبيبي التقديري (eGFR)")

# إدخال البيانات
age = st.number_input("أدخل العمر:", min_value=1, max_value=120, value=30)
creatinine = st.number_input("أدخل مستوى الكرياتينين في الدم (mg/dL):", min_value=0.1, max_value=20.0, value=1.0)
gender = st.selectbox("الجنس:", ["ذكر", "أنثى"])

# معادلة بسيطة للحساب (ملاحظة: هذه نسخة أولية للمناقشة)
if st.button("احسب eGFR"):
    # معادلة تجريبية مبسطة
    if gender == "ذكر":
        egfr = 141 * (min(creatinine/0.9, 1)**-0.411) * (max(creatinine/0.9, 1)**-1.209) * (0.993**age)
    else:
        egfr = 141 * (min(creatinine/0.7, 1)**-0.329) * (max(creatinine/0.7, 1)**-1.209) * (0.993**age) * 1.018
    
    st.success(f"معدل الفلترة الكبيبي التقديري هو: {egfr:.2f} mL/min/1.73m²")
