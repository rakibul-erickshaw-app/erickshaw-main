
import streamlit as st
import pandas as pd
from streamlit_gsheets import GSheetsConnection

# ১. গুগল শিট কানেকশন
conn = st.connection("gsheets", type=GSheetsConnection)

# ২. ভাষা পরিবর্তনের মেনু (এখানে আপনি আরও ভাষা যোগ করতে পারেন)
languages = {
    "English": {"title": "E-Rickshaw Registration", "name": "Driver Name", "phone": "Phone Number", "btn": "Register", "success": "Registered successfully!"},
    "বাংলা": {"title": "ই-রিকশা রেজিস্ট্রেশন", "name": "চালকের নাম", "phone": "ফোন নম্বর", "btn": "রেজিস্ট্রেশন করুন", "success": "সফলভাবে রেজিস্ট্রেশন হয়েছে!"},
    "অসমীয়া": {"title": "ই-ৰিক্সা পঞ্জীয়ন", "name": "চালকৰ নাম", "phone": "ফোন নম্বৰ", "btn": "পঞ্জীয়ন কৰক", "success": "সফলভাৱে পঞ্জীয়ন হ’ল!"},
    "हिन्दी": {"title": "ई-रिक्शा पंजीकरण", "name": "चालक का नाम", "phone": "फ़ोन नंबर", "btn": "पंजीकरण करें", "success": "पंजीकरण सफल रहा!"}
}

# সাইডবারে ভাষা নির্বাচনের অপশন
selected_lang = st.sidebar.selectbox("Choose Language / ভাষা নির্বাচন করুন", list(languages.keys()))
text = languages[selected_lang]

# ৩. অ্যাপ ইন্টারফেস (ইউজারের ভাষা অনুযায়ী পরিবর্তন হবে)
st.title(text["title"])
st.write("Please fill the form / অনুগ্রহ করে ফর্মটি পূরণ করুন।")

name = st.text_input(text["name"])
phone = st.text_input(text["phone"])

# ৪. ডাটা সেভ করার লজিক
if st.button(text["btn"]):
    if name and phone:
        # নতুন ডাটা তৈরি
        new_data = pd.DataFrame([{"Name": name, "Phone": phone}])
        
        # গুগল শিটে সরাসরি সেভ হবে
        conn.create(data=new_data)
        st.success(f"{text['success']} - {name}")
    else:
        st.error("Please fill all fields / সব ঘর পূরণ করুন")
