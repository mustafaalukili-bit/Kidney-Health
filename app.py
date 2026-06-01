import streamlit as st

# إعداد الصفحة
st.set_page_config(page_title="نظام صحة الكلى", layout="centered")

# تهيئة حالة الجلسة (Session State) لحفظ بيانات المستخدم
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'user_info' not in st.session_state:
    st.session_state.user_info = {}

# القائمة الجانبية
st.sidebar.title("نظام إدارة صحة الكلى")

if not st.session_state.logged_in:
    # صفحة تسجيل الدخول
    st.title("تسجيل الدخول")
    name = st.text_input("اسم المستخدم:")
    age = st.number_input("العمر:", 1, 100)
    gender = st.selectbox("الجنس:", ["ذكر", "أنثى"])
    
    if st.button("دخول"):
        st.session_state.logged_in = True
        st.session_state.user_info = {"name": name, "age": age, "gender": gender}
        st.rerun() # تحديث الصفحة لدخول النظام
else:
    # واجهة البرنامج الرئيسية
    st.sidebar.write(f"مرحباً بك، {st.session_state.user_info['name']}")
    if st.sidebar.button("خروج"):
        st.session_state.logged_in = False
        st.rerun()

    menu = st.sidebar.radio("الخيارات", ["حاسبة eGFR", "النصائح الطبية"])

    if menu == "حاسبة eGFR":
        st.title("🫘 حاسبة الوظائف الكلوية")
        creatinine = st.number_input("مستوى الكرياتينين (mg/dL):", 0.1, 20.0, 1.0)
        
        if st.button("احسب النتيجة"):
            # استخدام بيانات المستخدم المخزنة
            age = st.session_state.user_info['age']
            gender = st.session_state.user_info['gender']
            
            if gender == "ذكر":
                egfr = 141 * (min(creatinine/0.9, 1)**-0.411) * (max(creatinine/0.9, 1)**-1.209) * (0.993**age)
            else:
                egfr = 141 * (min(creatinine/0.7, 1)**-0.329) * (max(creatinine/0.7, 1)**-1.209) * (0.993**age) * 1.018
            
            st.metric("معدل الفلترة (eGFR)", f"{egfr:.2f}")
            
            if egfr >= 90:
                st.success("وظائف الكلى طبيعية.")
            else:
                st.warning("يُنصح بمراجعة الطبيب لمناقشة هذه النتيجة.")

    elif menu == "النصائح الطبية":
        st.title("🍎 الدليل الغذائي")
        st.write("بناءً على بياناتك يا " + st.session_state.user_info['name'] + "، ننصحك بالآتي:")
        st.info("الالتزام بشرب الماء وتجنب الأملاح.")
