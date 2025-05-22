import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu
import requests

st.set_page_config(layout="wide")

# Option Menu
selected = option_menu(
    menu_title=None,
    options=["About", "Education", "Experience", "Projects"],
    icons=["person-circle", "mortarboard", "briefcase", "code-slash"],
    default_index=0,
    orientation="horizontal",
    styles={
        "container": {
            "margin": "2",
            "padding": "5px",
            "background-color": "#1c1c1e",  # Near black, slightly softer
            "border-radius": "10px",
        },
        "nav-link": {
            "font-size": "18px",
            "font-weight": "600",
            "color": "#E0E0E0",  # Light gray text
            "text-align": "center",
            "--hover-color": "#333333",  # Dark gray hover background
        },
        "nav-link-selected": {
            "background-color": "#D3D3D3",  # Standout orange-red for selection
            "color": "black",  # Selected text color
        },
    },
)

if selected == "About":
    col1,col2, col3 = st.columns([2, 3, 2])

    with col1:
        st.markdown(
            "<div style='text-align: center;border-right:2px solid #ccc;'>"
            "<h2>Alwin V J</h2>"
            "<h5>AI/ML Engineer</h5>"
            "<button style='width: 100%; max-width: 300px; background-color:#333333; color: white; padding: 10px 20px;border-radius: 6px;margin-bottom: 10px'>My Resume</button>"
            "<button style='width: 100%; max-width: 300px; background-color:#222222; color: white; padding: 10px 20px;border-radius: 6px;'>Hire Me</button>"
            "</div>",
            unsafe_allow_html=True,
        )
    
    with col2:
        st.header("Hi, I'm _Alwin V J_")
        aboutme = """<p style='text-align: justify;'>
            "I am an AI/ML Engineer with a solid foundation in developing and deploying intelligent systems that solve real-world problems. Over the past year, I have worked on impactful projects involving machine learning, deep learning, and data-driven automation—ranging from predictive analytics to natural language processing and computer vision. I enjoy turning complex data into actionable insights and building end-to-end AI solutions from research to production. Passionate about continuous learning and staying current with the latest in AI advancements, I take pride in writing clean, efficient code and collaborating across disciplines to bring innovative ideas to life. I am proficient in Python and SQL, which has enabled me to efficiently manage data, develop models, and ensure quality through unit testing. Beyond my technical abilities, my adaptability, multitasking, and leadership skills drive my continuous learning and success in dynamic team environments."
        </p>"""
        
        st.markdown(aboutme, unsafe_allow_html=True)
        
        # Custom CSS for card styling
        st.markdown("""
        <h4>TECHNOLOGIES I USE:</h4>
        <style>
            .card {
            background-color: #1A1A1A;
            padding: 20px;
            border-radius: 12px;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
            margin-bottom: 20px;
            text-align: center;
            justify-content: center;
            align-items: center;
            height: 125px;
            }
            .card img {
            height: 40px;
            margin-bottom: 10px;
            }
            .card h5 {
            text-align: center;
            margin-left: 10px;
            margin-righ: 10px;
            margin-top: 0;
            margin-bottom: 0;
            font-size: 10x;
        }
        </style>
        """, unsafe_allow_html=True)

        # Technologies I use data
        tools = [
        {"name": "Python", "icon": "https://img.icons8.com/color/48/000000/python.png"},
        {"name": "Dart", "icon": "https://img.icons8.com/color/48/000000/dart.png"},
        {"name": "R", "icon": "https://www.r-project.org/logo/Rlogo.png"},
        {"name": "Django", "icon":"https://static.djangoproject.com/img/logos/django-logo-negative.png"},
        {"name":"Flask", "icon":"https://logo.svgcdn.com/l/flask.png"},
        {"name": "Flutter", "icon": "https://img.icons8.com/color/48/000000/flutter.png"},
        {"name": "Streamlit", "icon": "https://streamlit.io/images/brand/streamlit-logo-primary-colormark-darktext.png"},
        ]

        #Layout: 4 columns per row
        cols = st.columns(4)

        for idx, tool in enumerate(tools):
            with cols[idx % 4]:
                st.markdown(f"""
                <div class="card">
                <img src="{tool['icon']}" alt="{tool['name']} logo">
                <h5>{tool['name']}</h5>
                </div>
                """, unsafe_allow_html=True)


    # Load Lottie animation from URL
    def load_lottie_url(url):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()

    lottie_robot = load_lottie_url(
        "https://lottie.host/f3c2f2f6-0f76-4bc2-b3dd-f8d844c418bc/4iNdtj9xwW.json"
    )

    # Display it
    with col3:
        st_lottie(lottie_robot, height=400, width=500, key="robot")
        
    # Footer
    st.markdown("""
        <style>
          .footer {
            position: fixed;
            bottom: 0;
            width: 100%;
            color: white;
            background-color: #0E1117;
            text-align: center;
            padding: 10px;
            font-size: 14px;
        }
        </style>
        <div class="footer">
        Made with ❤️ by Alwin | © 2025
        </div>
    """, unsafe_allow_html=True)
    
    

elif selected == "Education":
    col1, col2 = st.columns([2, 6])

    with col1:
        st.markdown(
            "<div style='text-align: center;border-right:2px solid #ccc;'>"
            "<h2>Alwin V J</h2>"
            "<h5 style>AI/ML Engineer</h5>"
            "<button style='width: 100%; max-width: 300px; background-color:#333333; color: white; padding: 10px 20px;border-radius: 6px;margin-bottom: 10px'>My Resume</button>"
            "<button style='width: 100%; max-width: 300px; background-color:#222222; color: white; padding: 10px 20px;border-radius: 6px;'>Hire Me</button>"
            "</div>",
            unsafe_allow_html=True,
        )

    with col2:
        st.header("Education page")
    
    # Footer
    st.markdown("""
        <style>
          .footer {
            position: fixed;
            bottom: 0;
            width: 100%;
            color: white;
            background-color: #0E1117;
            text-align: center;
            padding: 10px;
            font-size: 14px;
        }
        </style>
        <div class="footer">
        Made with ❤️ by Alwin | © 2025
        </div>
    """, unsafe_allow_html=True)

elif selected == "Experience":
    col1, col2 = st.columns([2, 6])

    with col1:
        st.markdown(
            "<div style='text-align: center;border-right:2px solid #ccc;'>"
            "<h2>Alwin V J</h2>"
            "<h5 style>AI/ML Engineer</h5>"
            "<button style='width: 100%; max-width: 300px; background-color:#333333; color: white; padding: 10px 20px;border-radius: 6px;margin-bottom: 10px'>My Resume</button>"
            "<button style='width: 100%; max-width: 300px; background-color:#222222; color: white; padding: 10px 20px;border-radius: 6px;'>Hire Me</button>"
            "</div>",
            unsafe_allow_html=True,
        )

    with col2:
        st.header("Experience page")
    
    # Footer
    st.markdown("""
        <style>
          .footer {
            position: fixed;
            bottom: 0;
            width: 100%;
            color: white;
            background-color: #0E1117;
            text-align: center;
            padding: 10px;
            font-size: 14px;
        }
        </style>
        <div class="footer">
        Made with ❤️ by Alwin | © 2025
        </div>
    """, unsafe_allow_html=True)

elif selected == "Projects":
    col1, col2 = st.columns([2, 6])

    with col1:
        st.markdown(
            "<div style='text-align: center;border-right:2px solid #ccc;'>"
            "<h2>Alwin V J</h2>"
            "<h5 style>AI/ML Engineer</h5>"
            "<button style='width: 100%; max-width: 300px; background-color:#333333; color: white; padding: 10px 20px;border-radius: 6px;margin-bottom: 10px'>My Resume</button>"
            "<button style='width: 100%; max-width: 300px; background-color:#222222; color: white; padding: 10px 20px;border-radius: 6px;'>Hire Me</button>"
            "</div>",
            unsafe_allow_html=True,
        )

    with col2:
        st.header("Projects page")
    
    # Footer
    st.markdown("""
        <style>
          .footer {
            position: fixed;
            bottom: 0;
            width: 100%;
            color: white;
            background-color: #0E1117;
            text-align: center;
            padding: 10px;
            font-size: 14px;
        }
        </style>
        <div class="footer">
        Made with ❤️ by Alwin | © 2025
        </div>
    """, unsafe_allow_html=True)
