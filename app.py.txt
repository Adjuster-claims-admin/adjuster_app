import streamlit as st

# 1. Page Configuration
st.set_page_config(page_title="Adjuster Portal", page_icon="📋", layout="centered")

# 2. Simple Password Protection System
# We will securely move these to Streamlit Secrets in Phase 3
VALID_CREDENTIALS = {
    "adjuster1": "blue_sky_99",
    "adjuster2": "green_valley_44",
    "adjuster3": "rocky_road_11"
}

# Initialize session state for tracking login status
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "username" not in st.session_state:
    st.session_state.username = ""

# 3. Login Screen UI
if not st.session_state.logged_in:
    st.title("🔒 Claims Portal Login")
    st.write("Please enter your assigned credentials to access the claims system.")
    
    input_user = st.text_input("Username").strip()
    input_pass = st.text_input("Password", type="password").strip()
    
    if st.button("Log In"):
        if input_user in VALID_CREDENTIALS and VALID_CREDENTIALS[input_user] == input_pass:
            st.session_state.logged_in = True
            st.session_state.username = input_user
            st.rerun()
        else:
            st.error("Incorrect username or password. Please try again.")

# 4. Main App Content (Visible only after successful login)
else:
    # Sidebar with user info and logout button
    st.sidebar.title(f"👤 Welcome, {st.session_state.username}")
    if st.sidebar.button("Log Out"):
        st.session_state.logged_in = False
        st.session_state.username = ""
        st.rerun()

    # Main Dashboard
    st.title("📋 Adjuster Claims Dashboard")
    st.write("Secure workspace for managing and submitting active insurance claims.")
    
    # Placeholder for claims features
    st.info("Your application framework is officially ready! In future steps, we can add photo uploaders, estimation calculators, or claim databases here.")
