import streamlit as st

st.set_page_config(page_title="صحة الكلى", page_icon="腎")

st.title("تطبيق صحة الكلى التفاعلي")
st.subheader("حاسبة eGFR وتصنيف الحالة")

# إدخال البيانات
age = st.number_input("العمر:", min_value=1, max_value=120, value=30)
creatinine = st.number_input("مستوى الكرياتينين (mg/dL):", min_value=0.1, max_value=20.0, value=1.0)
gender = st.selectbox("الجنس:", ["ذكر", "أنثى"])

if st.button("احسب eGFR وقيّم الحالة"):
    # حساب eGFR
    if gender == "ذكر":
        egfr = 141 * (min(creatinine/0.9, 1)**-0.411) * (max(creatinine/0.9, 1)**-1.209) * (0.993**age)
    else:
        egfr = 141 * (min(creatinine/0.7, 1)**-0.329) * (max(creatinine/0.7, 1)**-1.209) * (0.993**age) * 1.018
    
    st.success(f"معدل الفلترة الكبيبي التقديري: {egfr:.2f} mL/min/1.73m²")
    
    # تصنيف الحالة طبياً
    st.write("### التقييم الطبي:")
    if egfr >= 90:
        st.write("✅ الحالة: وظائف الكلى طبيعية أو مرتفعة.")
    elif 60 <= egfr < 90:
        st.write("⚠️ الحالة: انخفاض طفيف في وظائف الكلى (المرحلة 2).")
    elif 30 <= egfr < 60:
        st.write("🟠 الحالة: قصور كلوي متوسط (المرحلة 3). يُنصح بمراجعة الطبيب.")
    elif 15 <= egfr < 30:
        st.write("🔴 الحالة: قصور كلوي شديد (المرحلة 4).")
    else:
        st.write("🚨 الحالة: فشل كلوي (المرحلة 5). يجب مراجعة الطبيب فوراً.")

st.markdown("---")
st.info("ملاحظة: هذه الحاسبة لأغراض تعليمية وتوعوية فقط، ولا تغني عن استشارة الطبيب المختص.")
