import streamlit as st
from predict import predict_message

st.set_page_config(page_title="Spam Message Filter", layout="centered")
st.title("📩 Spam Message Filter ")
st.markdown("🔍 *Enter a message below to detect if it's spam, its category, and reason.*")

user_input = st.text_area("✉ Enter a message to analyze:")

if st.button("Check Message"):
    if not user_input.strip():
        st.warning("⚠ Please enter a message before analyzing.")
    else:
        result = predict_message(user_input)

        if result["label"] == "Safe":
            st.success("✅ This message is likely: *Safe*")
        else:
            st.error("🚨 This message is likely: *Spam*")

            st.write(f"📂 Spam Category**: {result['category']}")
            st.write(f"🔑 Matched Keywords**: {', '.join(result['keywords']) or 'None'}")
            st.write(f"🧠 Explanation / Indicators**: {', '.join(result['explanation'])}")

            if result["urls"]:
                st.warning("⚠ *Suspicious URLs found in the message:*")
                for url in result["urls"]:
                    st.code(url)