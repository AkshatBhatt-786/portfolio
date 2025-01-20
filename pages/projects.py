import streamlit as st

# Page Config
st.set_page_config(page_title="My Projects", page_icon="🛠️", layout="wide")

with st.sidebar: # Optionally add a profile picture
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
    st.link_button("Linkedin", url="https://www.linkedin.com/in/akshat-bhatt-60a78a276", icon=":material/link:", use_container_width=True)
    st.link_button("Github", url="https://github.com/AkshatBhatt-786", icon=":material/link:", use_container_width=True)
    st.link_button("Email", url="mailto:akshatbhatt0786@gmail.com", icon=":material/mail:", use_container_width=True)
    st.markdown("---")
    st.markdown("### About Me")
    st.write("I am a passionate web and desktop developer skilled in Python, Java, and PHP. I enjoy building efficient software and solving complex problems.")


# Header
st.title("My Projects")
st.write("Here are some of the projects I've worked on, demonstrating my skills in software development, web apps, and problem-solving.")

# Project 1: Brainy Studio
with st.expander("Brainy Studio - Exam Paper Management Software"):
    st.write(
        """
        **Brainy Studio** is a powerful software tool designed for educators to easily create, manage, and publish exam papers. It provides an intuitive interface for customizing exam questions, setting instructions, and integrating with cloud storage services like **Dropbox** for easy access and sharing.

        ### Key Features:
        - Customizable exam question types (MCQs, True/False, etc.)
        - Secure cloud integration for paper storage and sharing
        - Intuitive user interface for educators

        ### Technologies Used:
        - Python (Tkinter, CustomTkinter)
        - Dropbox API for cloud integration
        - File Handling & Error Handling

        **Check it out**: [GitHub Repo](https://github.com/AkshatBhatt-786/brainy-studio)
        """
    )

# Project 2: Last Bite
with st.expander("Last Bite - Reduce Food Waste, One Recipe at a Time"):
    st.write(
        """
        **Last Bite** is an app designed to combat food waste by helping users creatively use leftover ingredients. Input what you have, and get recipes to make every bite count.

        ### Key Features:
        - Ingredient-based recipe suggestions
        - Reduces food waste by inspiring creative cooking
        - Simple, intuitive user experience

        ### Technologies Used:
        - Python (Streamlit for web app development)
        - APIs for recipe suggestions
        - Data handling for ingredient input and output

        **Check it out**: [GitHub Repo](https://github.com/AkshatBhatt-786/last-bite)
        """
    )

# Divider for readability
st.markdown("---")

# Add more projects as needed
st.write("More projects coming soon!")
