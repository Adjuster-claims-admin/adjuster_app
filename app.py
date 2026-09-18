import streamlit as st
import os

# 1. Page Configuration
st.set_page_config(page_title="Adjuster Portal", page_icon="📋", layout="centered")

# 2. Secure Credentials Retrieval
VALID_CREDENTIALS = {}
if "credentials" in st.secrets:
    for key, value in st.secrets["credentials"].items():
        VALID_CREDENTIALS[key] = value
else:
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

    # Main Dashboard Title
    st.title("📋 Adjuster Claims Dashboard")
    st.write("Secure workspace for managing active insurance claims.")
    
    st.divider()
    
    # 📸 PHOTO UPLOADER TOOL SECTION
    st.header("📸 Photo Uploader & Auto-Namer")
    st.write("Upload claim images to automatically organize and rename them according to company standards.")
    
    # Text Input for Claim Number
    claim_number = st.text_input("1. Enter Claim Number (e.g., 2026-A405)").strip()
    
    # Dropdown for Damage Category
    damage_type = st.selectbox(
        "2. Select Damage Category",
        ["Roof", "Exterior_Siding", "Interior_Water", "Foundation", "Vehicle", "Other"]
    )
    
    # File Uploader Box (Accepts multiple PNG or JPG files)
    uploaded_files = st.file_uploader(
        "3. Choose claim photos", 
        type=["png", "jpg", "jpeg"], 
        accept_multiple_files=True
    )
    
    # If the user has actually uploaded files
    if uploaded_files:
        if not claim_number:
            st.warning("⚠️ Please enter a Claim Number above to see your formatted file names.")
        else:
            st.success(f"✅ Ready to process {len(uploaded_files)} photo(s)!")
            st.write("### 📋 Your Organized & Renamed Files:")
            
            # Loop through files and display their new standardized names
            for index, file in enumerate(uploaded_files, start=1):
                # Extract original extension (.jpg, .png, etc.)
                _, file_extension = os.path.splitext(file.name)
                
                # Create the clean, professional name
                new_filename = f"{claim_number}_{damage_type.upper()}_{index}{file_extension}"
                
                # Create a visual layout for each photo preview
                col1, col2 = st.columns([1, 3])
                with col1:
                    st.image(file, width=120)  # Displays a small thumbnail preview
                with col2:
                    st.code(new_filename, language="text")  # Shows the beautiful new name
                    # Add a simple button to let them download their freshly renamed file
                    st.download_button(
                        label=f"📥 Download {new_filename}",
                        data=file,
                        file_name=new_filename,
                        mime=file.type,
                        key=f"dl_{index}"
                    )

    
    
