import streamlit as st
from PIL import Image
# Page Config
st.set_page_config(page_title="Akshat Bhatt Portfolio", layout="wide")

# Custom CSS for styling
st.markdown("""
    <style>
        /* Background gradient */
        body {
            background: linear-gradient(135deg, #6e7c7c, #3e4c4c);
            font-family: 'Arial', sans-serif;
        }

        /* Header section */
        .header {
            text-align: center;
            padding-top: 100px;
            color: #fff;
            font-size: 3em;
            animation: fadeIn 2s ease-in-out;
        }

        /* Subheader animation */
        .subheader {
            text-align: center;
            color: #c2c2c2;
            font-size: 1.5em;
            margin-top: 20px;
            animation: fadeIn 3s ease-in-out;
        }
        
        /* Button animation */
        .btn {
            display: block;
            width: 200px;
            margin: 30px auto;
            padding: 10px;
            background-color: #FFD700;
            border: none;
            font-size: 1.2em;
            cursor: pointer;
            color: white;
            border-radius: 5px;
            animation: fadeIn 4s ease-in-out;
        }

        .btn:hover {
            background-color: #ffcc00;
        }

        /* Animation for fadeIn effect */
        @keyframes fadeIn {
            0% { opacity: 0; }
            100% { opacity: 1; }
        }
    

        /* For responsiveness */
        @media (max-width: 768px) {
            .header {
                font-size: 2.5em;
            }
            .subheader {
                font-size: 1.2em;
            }
            .btn {
                width: 150px;
                font-size: 1em;
            }
        }
    </style>
""", unsafe_allow_html=True)

with st.sidebar:
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

col1, col2 = st.columns([1, 2])
with col1:
    st.image("assets/profile.JPG", caption="Akshat Bhatt", width=150, use_container_width=True)
with col2:
    st.markdown('<div class="header">Welcome to My Portfolio</div>', unsafe_allow_html=True)
    st.markdown('<div class="subheader">A passionate Web & Desktop Developer</div>', unsafe_allow_html=True)
    st.write("""
        As a **Web and Desktop Developer**, I build software that is both **efficient** and **user-friendly**. 
        With a strong foundation in **Python** and solid experience in **Java**, I’m able to create solutions across various platforms. 
        I am focused on building software that is **practical**, **efficient**, and easy for users to interact with. 
        I enjoy solving **technical challenges** and turning **ideas** into working solutions that meet real needs.
""")

st.subheader("What I Can Do")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown('<div class="skill-card fade-in">', unsafe_allow_html=True)
    st.write(
        """
        **Python**:
        - I work with **Core Python** and use libraries like **Pandas**, **NumPy**, and **Matplotlib** for data analysis and visualization.
        - I've built web apps using **Streamlit** and desktop apps with **Tkinter**/**CustomTkinter**. I'm also exploring **PyQt5** for more advanced GUIs.
        - I like enhancing command-line tools with **Rich**, **Colorama**, and **Tabulate**, and use **Icecream** and **Logging** to make debugging easier.
        - I've also integrated services like **Dropbox** to add extra functionality to my projects.
        """
    )
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="skill-card fade-in">', unsafe_allow_html=True)
    st.write(
        """
        **Java**:
        - I have intermediate experience with **Java**, focusing on building object-oriented applications.
        - I'm comfortable using **Java** for both backend development and GUI-based desktop applications.
        - I've worked with frameworks like **Spring** to build scalable web services and enjoy writing clean, maintainable code.
        """
    )
    st.markdown('</div>', unsafe_allow_html=True)

with col3:
    st.markdown('<div class="skill-card fade-in">', unsafe_allow_html=True)
    st.write(
        """
        **PHP**:
        - I have basic experience with **PHP**, mainly for building dynamic websites and web applications.
        - I've worked with **PHP** to integrate front-end features and connect to databases, creating simple yet functional web solutions.
        """
    )
    st.markdown('</div>', unsafe_allow_html=True)

# Add a last row with the full-stack development skill
st.markdown('<div class="skill-card fade-in">', unsafe_allow_html=True)
st.write(
    """
    **Software Development**:
    - I focus on creating practical, efficient, and maintainable software solutions.
    - I’m experienced in both **full-stack development** and **desktop applications**, with an emphasis on clean code and scalability.
    - I enjoy solving complex problems and developing software that meets real-world needs.
    """
)
st.markdown('</div>', unsafe_allow_html=True)

st.subheader("Recent Projects")

with st.expander("Brainy Studio - Exam Paper Management Software"):
    st.write(
        """
        **Brainy Studio** is a powerful software tool designed for educators to easily create, manage, and publish exam papers. It provides an intuitive interface for customizing exam questions, setting instructions, and integrating with cloud storage services like **Dropbox** for easy access and sharing.

        **Technologies Used**:
        - Python (Core Python, Tkinter, CustomTkinter)
        - Dropbox API for cloud storage integration
        - File Handling & Error Handling in Python
        - GUI Development using Tkinter and CustomTkinter
        - Logging & Debugging with Python's built-in logging module

        **Key Features**:
        - **Customizable Exam Creation**: Create multiple types of exam questions like MCQs, True/False, and more.
        - **Cloud Integration**: Integration with **Dropbox** for secure storage and easy sharing.
        - **User Access Control**: Generate unique access codes and passwords for students.
        - **Simple and Efficient**: Designed with ease of use in mind for both teachers and students.

        Currently, the **Cloud Exam Software** is still in progress (80% complete), and **Brainy Studio** is fully functional and available for use.

        Check out the full project and code on [GitHub](https://github.com/AkshatBhatt-786/brainy-studio).
        """
    )

with st.expander("Last Bite - Reduce Food Waste, One Recipe at a Time"):
    st.write(
        """
        **Last Bite** is an innovative app designed to combat food waste by empowering users to make the most of their ingredients. Whether it's leftovers or items about to expire, **Last Bite** helps transform them into delicious meals.

        ### Key Features:
        - **Ingredient Input**: Enter ingredients you're about to discard.
        - **Recipe Suggestions**: Get creative meal ideas tailored to the ingredients you have.
        - **Waste Reduction**: Reduce food waste by giving new life to leftovers.
        - **User-Friendly Design**: Simple and intuitive interface for seamless use.

        ### Technologies Used:
        - **Python**: Backend processing and logic.
        - **Streamlit**: Interactive web app development.
        - **Third-party APIs**: Recipe generation and suggestions.
        - **Data Handling**: Efficient management of ingredient inputs and recipe outputs.

        **Mission**:
        - To promote sustainability and reduce food waste.
        - To inspire creativity in the kitchen by making the most of available ingredients.

        Check out the full project and code on [GitHub](https://github.com/AkshatBhatt-786/last-bite).
        """
    )


# Contact Section
st.subheader("Contact Me")
st.write(
    """
    Feel free to reach out to me for collaborations, project inquiries, or just to connect!

    - Email: [akshatbhatt0786@gmail.com](mailto:your.akshatbhatt0786@gmail.com)
    - LinkedIn: [www.linkedin.com/in/akshat-bhatt-60a78a276](www.linkedin.com/in/akshat-bhatt-60a78a276)
    """
)

# Footer
st.markdown(
    "<div style='text-align: center; color: white; padding: 20px;'>© 2025 Akshat Bhatt. All rights reserved.</div>",
    unsafe_allow_html=True
)
