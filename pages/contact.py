import streamlit as st

st.set_page_config("Contact | Portfolio", layout="centered")

with st.sidebar:
    st.header("Akshat Bhatt")
    st.subheader("Web & Desktop Developer")
    st.markdown("---")
    st.markdown("### Navigation")
    st.page_link("app.py", label="Home", icon=":material/home:")
    st.page_link("pages/projects.py", label="Projects", icon=":material/folder_code:")
    st.page_link("pages/about.py", label="About Me", icon=":material/person:")
    st.page_link("pages/contact.py", label="Contact Me", icon=":material/contact_page:")
    st.markdown("---")
    st.markdown("### Connect with me")
    st.link_button("Linkedin", url="https://www.linkedin.com/in/akshatb786", icon=":material/link:", use_container_width=True)
    st.link_button("Github", url="https://github.com/AkshatBhatt-786", icon=":material/link:", use_container_width=True)
    st.link_button("Email", url="mailto:akshatbhatt0786@gmail.com", icon=":material/mail:", use_container_width=True)
    st.markdown("---")
    st.markdown("### About Me")
    st.write("I am a passionate web and desktop developer skilled in Python, Java, and PHP. I enjoy building efficient software and solving complex problems.")

st.title("Contact Me")
st.write(
    """
    Whether you’re looking to collaborate, have a project idea, or just want to say hi—I'd love to connect!  
    Feel free to reach out through any of the platforms below:
    """
)

st.markdown(
    """
    - 📧 Email: [akshatbhatt0786@gmail.com](mailto:akshatbhatt0786@gmail.com)  
    - 🌐 LinkedIn: [Akshat Bhatt](https://www.linkedin.com/in/akshatb786)  
    - 🖥️ GitHub: [AkshatBhatt-786](https://github.com/AkshatBhatt-786)
    """,
    unsafe_allow_html=True
)

st.write(
    """
    ---
    Let's connect and make something amazing together! 🚀
    """
)
