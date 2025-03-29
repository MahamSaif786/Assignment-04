import streamlit as st
import os
from PIL import Image

def main():
    st.set_page_config(page_title="CodeFusion Hub", page_icon="🚀", layout="wide")

    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["Home", "AI Insights", "About", "Contact"])

    if page == "Home":
        show_home()
    elif page == "AI Insights":
        show_ai_insights()
    elif page == "About":
        show_about()
    elif page == "Contact":
        show_contact()

def show_home():
    st.title("Welcome to CodeFusion Hub")
    st.write("### Your Gateway to Python and AI Knowledge!")
    
    image_path = "assests/pexels-tara-winstead-8386440.jpgz"
    if os.path.exists(image_path):
        image = Image.open(image_path)
        st.image(image, caption="Python & AI Innovation", use_container_width=True)
    else:
        st.warning("Image file not found! Please check the path.")
    
    st.markdown("""
    - Learn about the latest AI advancements
    - Explore Python development and machine learning
    - Connect with AI enthusiasts and experts
    """)
    
    st.button("Get Started", key="start")

def show_ai_insights():
    st.title("AI Insights")
    st.write("### Latest Trends and Developments in Artificial Intelligence")
    
    st.subheader("1. The Rise of Generative AI")
    st.write("Generative AI, like ChatGPT and DALL·E, is revolutionizing the way content is created, from text generation to image synthesis.")
    
    st.subheader("2. AI in Healthcare")
    st.write("AI-powered diagnostic tools are improving accuracy and efficiency in disease detection, making healthcare more accessible and effective.")
    
    st.subheader("3. Ethical AI and Bias Mitigation")
    st.write("As AI grows, addressing bias and ensuring fairness in algorithms is becoming a crucial topic in the AI industry.")
    
    st.subheader("4. The Future of AI and Automation")
    st.write("AI is transforming industries with automation, improving productivity while raising questions about job displacement and workforce adaptation.")

def show_about():
    st.title("About Us")
    st.write("### Empowering developers with Python & AI knowledge!")
    st.info("CodeFusion is a platform dedicated to making Python learning easy and engaging.")

def show_contact():
    st.title("Contact Us")
    name = st.text_input("Name")
    email = st.text_input("Email")
    message = st.text_area("Message")
    
    if st.button("Send Message"):
        st.success(f"Thanks, {name}! We'll get back to you at {email}.")

if __name__ == "__main__":
    main()
