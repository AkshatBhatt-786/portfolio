import streamlit as st

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

# About Me Section
st.title("About Me")
st.write(
    """
    Hey there! I'm **Akshat Bhatt**, a Web and Desktop Developer who loves solving problems and building software that makes life easier.  
    My journey started during my diploma at **SIR BPTI College** under **GTU**, where I realized how much I enjoy turning ideas into working solutions.

    ### Here’s what I’m all about:
    - I built **Brainy Studio**, a tool to help teachers create and manage exam papers effortlessly.  
    - I’m currently working on **Last Bite**, an app to help people reduce food waste by transforming leftovers into amazing recipes.  
    - I have a solid grasp of **Python** and experience with libraries like **Pandas**, **Streamlit**, and **CustomTkinter**. I’ve even integrated cloud features with tools like **Dropbox API**.

    What I enjoy most about development is solving technical puzzles and creating software that’s easy to use and truly helpful.  
    Outside of coding, I’m always curious about exploring new tech, learning new skills, and working on projects that make an impact.
    """
)

# Contact Info
st.write("If any of this sounds interesting, feel free to [reach out](mailto:akshatbhatt0786@gmail.com) or check out my projects below!")

st.write(
    """
    ---
    Curious about what I’ve built?  
    Check out my **[Projects](projects)** and see how I bring ideas to life!
    """
)