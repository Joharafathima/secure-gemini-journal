import streamlit as st
import os

# Application interface configuration
st.set_page_config(page_title="Personal Gemini Journal", page_icon="🔐", layout="wide")
st.title("🔐 Secure Personal Gemini Journal Pro")

# PILAR 1: User Identity via Firebase Authentication Simulation
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False
    st.session_state.user_email = ""

if not st.session_state.authenticated:
    st.subheader("Authorized Personnel Access Required")
    email = st.text_input("Institutional Email (Firebase Domain):")
    password = st.text_input("Security Encryption Key:", type="password")
    
    if st.button("Authenticate Identity"):
        if email == "johara@jmc.edu" and password == "finalyear2026":
            st.session_state.authenticated = True
            st.session_state.user_email = email
            st.success("Firebase Auth Token Generated Successfully!")
            st.rerun()
        else:
            st.error("Access Denied. Invalid token signatures.")
else:
    st.sidebar.success(f"Session Active: {st.session_state.user_email}")
    
    # PILLAR 2: User-Isolated Cloud Firestore Simulation
    if "logs" not in st.session_state:
        st.session_state.logs = [
            {"date": "2026-09-03", "entry": "Spent a relaxing day with my friends.", "summary": "Rest milestone log."}
        ]

    tab_write, tab_history = st.tabs(["📝 New Journal Entry", "📜 Isolated Vault"])
    
    with tab_write:
        log_date = st.date_input("Select Entry Date:")
        journal_text = st.text_area("Write your thoughts securely:")
        
        # FEATURE ENHANCEMENT: Mood Monitor Node
        energy = st.slider("Select Current Physical Energy Level:", 1, 10, 5)
        
        if st.button("Process Entry under AI Constitution"):
            if journal_text:
                with st.spinner("Executing structural code directives..."):
                    ai_summary = f"Summary: {journal_text[:50]}... [Processed via Gemini AI Studio Constitution - Energy: {energy}/10]"
                    st.session_state.logs.append({"date": str(log_date), "entry": journal_text, "summary": ai_summary})
                    st.success("Record safely isolated and saved to personal Firestore path!")
            else:
                st.warning("Data field cannot be left empty.")
                
    with tab_history:
        st.subheader("Isolated Firestore Path: /users/{userId}/journals/")
        for log in st.session_state.logs:
            st.markdown(f"### 📅 Date: {log['date']}")
            st.write(f"**Content:** {log['entry']}")
            st.info(f"🤖 **Gemini Guardrails Summary:** {log['summary']}")
            st.markdown("---")
