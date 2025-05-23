import streamlit as st
from streamlit_option_menu import option_menu
import requests

st.set_page_config(layout="wide")

hide_streamlit_style = """
    <style>
        /* Hide the hamburger menu (with share and GitHub icons) */
        #MainMenu {visibility: hidden;}
"""

st.markdown(hide_streamlit_style, unsafe_allow_html=True)

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

# Page contents starts here
# About page
if selected == "About":
    col1, col2 = st.columns([2, 6])

    with col1:
        st.markdown("""
             <style>
             .essential-details {
                 text-align: center;
                 border-right: 2px solid #ccc;
                 padding: 1rem;
             }
             
             .resumebutton{
                 width: 100%; max-width: 300px; 
                 background-color:#333333; 
                 color: white; 
                 padding: 10px 20px;
                 border-radius: 6px;
                 margin-bottom: 10px
             }
             
             .hiremebutton{
                 width: 100%; 
                 max-width: 300px; 
                 background-color:#222222; 
                 color: white; 
                 padding: 10px 20px;
                 border-radius: 6px;
             }
         
             /* Remove border on tablet and mobile (≤ 1024px) */
             @media screen and (max-width: 1024px) {
                 .essential-details {
                     border-right: none !important;
                 }
                 
                 .resumebutton{
                     width:45%;
                     margin-right: 5px;
                 }
                 
                 .hiremebutton{
                     width:45%;
                 }
                 
                 
             }
             </style>
             """, unsafe_allow_html=True)
        st.markdown(
            "<div class='essential-details'>"
            "<h2>Alwin V J</h2>"
            "<h5 style>AI/ML Engineer</h5>"
            "<h6 style='display: center; align-items: center; gap: 8x; color: white;'>"
            "<svg xmlns='http://www.w3.org/2000/svg' fill='white' width='20' height='20' viewBox='0 0 24 24'>"
            "<path d='M12 13.065L1.5 6.75V17.25H22.5V6.75L12 13.065ZM12 11.25L22.5 4.5H1.5L12 11.25Z'/>"
            "</svg>"
            "&nbsp;&nbsp;alwinvj5@gmail.com</h6>"
            "<div style='margin: 10px 0;'>"
            "<a href='https://github.com/AlwinVJ' target='_blank' style='margin: 0 10px;'>"
            "<img src='https://img.icons8.com/?size=100&id=3tC9EQumUAuq&format=png&color=FFFFFF' alt='GitHub' style='width: 24px; height: 24px;'>"
            "</a>"
            "<a href='https://www.linkedin.com/in/alwinvj' target='_blank' style='margin: 0 10px;'>"
            "<img src='https://img.icons8.com/?size=100&id=8808&format=png&color=FFFFFF' alt='LinkedIn' style='width: 24px; height: 24px;'>"
            "</a>"
            "</div>"
            "<br>"
            "<button class = 'resumebutton'>My Resume</button>"
            "<button class = 'hiremebutton'>Hire Me</button>"
            "</div>"
            "<br>",
            unsafe_allow_html=True,
        )

    with col2:
        st.header("Hi, I'm _Alwin V J_")
        aboutme = """<p style='text-align: justify; padding:10px'>
            "I am an AI/ML Engineer with a solid foundation in developing and deploying intelligent systems that solve real-world problems. Over the past year, I have worked on impactful projects involving machine learning, deep learning, and data-driven automation—ranging from predictive analytics to natural language processing and computer vision. I enjoy turning complex data into actionable insights and building end-to-end AI solutions from research to production. Passionate about continuous learning and staying current with the latest in AI advancements, I take pride in writing clean, efficient code and collaborating across disciplines to bring innovative ideas to life. I am proficient in Python and SQL, which has enabled me to efficiently manage data, develop models, and ensure quality through unit testing. Beyond my technical abilities, my adaptability, multitasking, and leadership skills drive my continuous learning and success in dynamic team environments."
        </p>"""

        st.markdown(aboutme, unsafe_allow_html=True)

        # Technologies I use layout
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
        """,
            unsafe_allow_html=True,
        )

        # Technologies I use data
        tools = [
            {
                "name": "Python",
                "icon": "https://img.icons8.com/color/48/000000/python.png",
            },
            {"name": "Dart", "icon": "https://img.icons8.com/color/48/000000/dart.png"},
            {"name": "R", "icon": "https://www.r-project.org/logo/Rlogo.png"},
            {
                "name": "Django",
                "icon": "https://img.icons8.com/?size=100&id=AksudKrBQryM&format=png&color=40C057",
            },
            {"name": "Flask", "icon": "https://img.icons8.com/?size=100&id=AqYCfGyGXlO7&format=png&color=FFFFFF"},
            {
                "name": "Flutter",
                "icon": "https://img.icons8.com/color/48/000000/flutter.png",
            },
            {
                "name": "Streamlit",
                "icon": "https://img.icons8.com/?size=100&id=Rffi8qeb2fK5&format=png&color=000000",
            },
            {
                "name": "TensorFlow",
                "icon": "https://upload.wikimedia.org/wikipedia/commons/2/2d/Tensorflow_logo.svg",
            },
            {
                "name": "PyTorch",
                "icon": "https://upload.wikimedia.org/wikipedia/commons/1/10/PyTorch_logo_icon.svg",
            },
            {
                "name": "Scikit-learn",
                "icon": "https://upload.wikimedia.org/wikipedia/commons/0/05/Scikit_learn_logo_small.svg",
            },
            {
                "name": "NumPy",
                "icon": "https://upload.wikimedia.org/wikipedia/commons/3/31/NumPy_logo_2020.svg",
            },
            {
                "name": "Pandas",
                "icon": "data:image/png;base64,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",
            },
            {
                "name": "FastAPI",
                "icon": "data:image/png;base64,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",
            },
            {
                "name": "OpenCV",
                "icon": "https://upload.wikimedia.org/wikipedia/commons/3/32/OpenCV_Logo_with_text_svg_version.svg",
            },
            {
                "name": "ZenML",
                "icon": "data:image/png;base64,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",
            },
            {
                "name": "LangChain",
                "icon": "data:image/png;base64,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",
            },
        ]

        # Layout: 4 columns per row
        cols = st.columns(4)

        for idx, tool in enumerate(tools):
            with cols[idx % 4]:
                st.markdown(
                    f"""
                <div class="card">
                <img src="{tool['icon']}" alt="{tool['name']} logo">
                <h5>{tool['name']}</h5>
                </div>
                """,
                    unsafe_allow_html=True,
                )
        # Apps I use layout
        st.markdown("""
        <h4>APPLICATIONS I USE:</h4>
        <style>
            @media screen and (max-width: 1024px) {
                .card-applications{
                    display: flex;
                    align-items:center;
                }
            }
            .card-applications {
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
            .card-applications img {
            height: 40px;
            margin-bottom: 10px;
            }
            .card-applications h5 {
            text-align: center;
            margin-left: 10px;
            margin-righ: 10px;
            margin-top: 0;
            margin-bottom: 0;
            font-size: 13.5px;
        }
        </style>
        """,
            unsafe_allow_html=True,
        )

        # Technologies I use data
        tools = [
            {
                "name": "VS Code",
                "icon": "https://cdn-icons-png.flaticon.com/512/906/906324.png",
            },
            {"name": "Google Colab", "icon": "https://img.icons8.com/?size=100&id=lOqoeP2Zy02f&format=png&color=000000"},
            {"name": "Jupyter Notebook", "icon": "https://img.icons8.com/?size=100&id=J0SgMWzAxqFj&format=png&color=000000"},
            {
                "name": "Postman",
                "icon": "https://img.icons8.com/?size=100&id=EPbEfEa7o8CB&format=png&color=000000",
            },
            {"name": "Figma", "icon": "https://img.icons8.com/?size=100&id=zfHRZ6i1Wg0U&format=png&color=000000"},
            {
                "name": "Slack",
                "icon": "https://img.icons8.com/?size=100&id=OXVeOEj6qZqX&format=png&color=000000",
            },
            {
                "name": "Jira",
                "icon": "https://img.icons8.com/?size=100&id=oROcPah5ues6&format=png&color=000000",
            },
            {
                "name": "Power BI",
                "icon": "https://img.icons8.com/?size=100&id=Ny0t2MYrJ70p&format=png&color=000000",
            },
            {
                "name": "Tableau",
                "icon": "https://img.icons8.com/?size=100&id=9Kvi1p1F0tUo&format=png&color=000000",
            },
            {
                "name": "Google Sheets",
                "icon": "https://img.icons8.com/?size=100&id=30461&format=png&color=000000",
            },
            {
                "name": "MS EXcel",
                "icon": "https://img.icons8.com/?size=100&id=UECmBSgBOvPT&format=png&color=000000",
            },
            {
                "name": "Google Sites",
                "icon": "https://img.icons8.com/?size=100&id=Jan95WujfAel&format=png&color=000000",
            },
        ]

        # Layout: 4 columns per row
        cols = st.columns(6)

        for idx, tool in enumerate(tools):
            with cols[idx % 6]:
                st.markdown(
                    f"""
                <div class="card-applications">
                <img src="{tool['icon']}" alt="{tool['name']} logo">
                <h5>{tool['name']}</h5>
                </div>
                """,
                    unsafe_allow_html=True,
                )

    # Footer
    st.markdown(
        """
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
    """,
        unsafe_allow_html=True,
    )

# Education Page
elif selected == "Education":
    col1, col2 = st.columns([2, 6])

    with col1:
        st.markdown("""
             <style>
             .essential-details {
                 text-align: center;
                 border-right: 2px solid #ccc;
                 padding: 1rem;
             }
         
             /* Remove border on tablet and mobile (≤ 1024px) */
             @media screen and (max-width: 1024px) {
                 .essential-details {
                     display:none;
                 }
             }
             </style>
             """, unsafe_allow_html=True)
        st.markdown(
            "<div class='essential-details'>"
            "<h2>Alwin V J</h2>"
            "<h5 style>AI/ML Engineer</h5>"
            "<h6 style='display: center; align-items: center; gap: 8x; color: white;'>"
            "<svg xmlns='http://www.w3.org/2000/svg' fill='white' width='20' height='20' viewBox='0 0 24 24'>"
            "<path d='M12 13.065L1.5 6.75V17.25H22.5V6.75L12 13.065ZM12 11.25L22.5 4.5H1.5L12 11.25Z'/>"
            "</svg>"
            "&nbsp;&nbsp;alwinvj5@gmail.com</h6>"
            "<div style='margin: 10px 0;'>"
            "<a href='https://github.com/AlwinVJ' target='_blank' style='margin: 0 10px;'>"
            "<img src='https://img.icons8.com/?size=100&id=3tC9EQumUAuq&format=png&color=FFFFFF' alt='GitHub' style='width: 24px; height: 24px;'>"
            "</a>"
            "<a href='https://www.linkedin.com/in/alwinvj' target='_blank' style='margin: 0 10px;'>"
            "<img src='https://img.icons8.com/?size=100&id=8808&format=png&color=FFFFFF' alt='LinkedIn' style='width: 24px; height: 24px;'>"
            "</a>"
            "</div>"
            "<br>"
            "<button style='width: 100%; max-width: 300px; background-color:#333333; color: white; padding: 10px 20px;border-radius: 6px;margin-bottom: 10px'>My Resume</button>"
            "<button style='width: 100%; max-width: 300px; background-color:#222222; color: white; padding: 10px 20px;border-radius: 6px;'>Hire Me</button>"
            "</div>"
            "<br>",
            unsafe_allow_html=True,
        )

    with col2:
        st.markdown(
        """
        <style>
        @media screen and (max-width: 1024px) {
        .content h4 {
            margin: 0;
            padding: 0;
            text-align: left;
            font-size: 12px;}
        .content h5{
            margin: 0;
            padding-top: 10px;
            text-align: left;
            padding-bottom: 0.5px;
            font-size: 11px;}
        .content h6{
            margin: 0;
            padding: 0;
            font-size: 10px;
        }
        .container{
            padding:5px 20px;
            margin: 0;
        }
        .content{
            padding:0;
            text-align: left;
        }
        }
        
        
        .timeline {
          position: relative;
          max-width: 800px;
          margin: auto;
        }
        
        .timeline::after {
          content: '';
          position: absolute;
          width: 4px;
          background-color:yellow;
          top: 0;
          bottom: 0;
          left: 50%;
          height: 100%;
          margin-left: -2px;
        }
        
        .container {
          padding: 10px 40px;
          position: relative;
          background-color:inherit;
          width: 50%;
        }
        
        .container::after {
          content: '';
          position: absolute;
          width: 20px;
          height: 20px;
          right: -10px;
          background-color: #000;
          border: 4px solid yellow;
          top: 15px;
          border-radius: 50%;
          z-index: 1;
        }
        
        .left {
          left: 0;
        }
        
        .right {
          left: 50%;
        }
        
        .right::after {
          left: -10px;
        }
        
        .content {
          padding: 10px;
          background-color: #222;
          color: white;
          border-radius: 6px;
        }
        .left-container-arrow{
            height:0;
            widht: 0;
            position: absolute;
            top: -10 px; /* moves the arrow above the container */
            right: 28px;
            z-index: 1;
            border-top: 15px solid transparent;
            border-bottom: 15px solid transparent;
            border-left: 15px solid #222;
        }
        .right-container-arrow{
            height:0;
            widht: 0;
            position: absolute;
            top: -10 px; /* moves the arrow above the container */
            left: 28px;
            z-index: 1;
            border-top: 15px solid transparent;
            border-bottom: 15px solid transparent;
            border-right: 15px solid #222;
        }
        .footer {
                position: fixed;
                justify-content: center;
                bottom: 0;
                width: 100%;
                color: white;
                background-color: #0E1117;
                text-align: center;
                padding: 10px;
                font-size: 14px;
            }
        </style>
        <br>
        <br>
        <div class="timeline">
        
          <div class="container left">
            <div class="content">
            <span class = "left-container-arrow"></span>
              <h4>Indian Institute of Technology, Madras (IITM)</h4>
              <h5>BS in Data Science and its applications</h5>
              <h6>2024 - Pursuing</h6>
            </div>
          </div>
        
          <div class="container right">
            <div class="content">
             <span class = "right-container-arrow"></span>
              <h4>National Council for Technology and Training</h4>
              <h5>Diploma in Android Flutter App Development</h5>
              <h6>2023 - 2024</h6>
            </div>
          </div>
        
          <div class="container left">
            <div class="content">
            <span class = "left-container-arrow"></span>
              <h4>The Indian Institute of Chartered Accountants of India</h4>
              <h5>CA - Intermediate</h5>
            </div>
          </div>
        </div>
        <div class="footer">
            Made with ❤️ by Alwin | © 2025
            </div>
        """,
            unsafe_allow_html=True,
        )

# Experience Page
elif selected == "Experience":
    col1, col2 = st.columns([2, 6])

    with col1:
        st.markdown("""
             <style>
             .essential-details {
                 text-align: center;
                 border-right: 2px solid #ccc;
                 padding: 1rem;
             }
         
             /* Remove border on tablet and mobile (≤ 1024px) */
             @media screen and (max-width: 1024px) {
                 .essential-details {
                     display:none;
                 }
             }
             </style>
             """, unsafe_allow_html=True)
        st.markdown(
            "<div class = 'essential-details'>"
            "<h2>Alwin V J</h2>"
            "<h5 style>AI/ML Engineer</h5>"
            "<h6 style='display: center; align-items: center; gap: 8x; color: white;'>"
            "<svg xmlns='http://www.w3.org/2000/svg' fill='white' width='20' height='20' viewBox='0 0 24 24'>"
            "<path d='M12 13.065L1.5 6.75V17.25H22.5V6.75L12 13.065ZM12 11.25L22.5 4.5H1.5L12 11.25Z'/>"
            "</svg>"
            "&nbsp;&nbsp;alwinvj5@gmail.com</h6>"
            "<div style='margin: 10px 0;'>"
            "<a href='https://github.com/AlwinVJ' target='_blank' style='margin: 0 10px;'>"
            "<img src='https://img.icons8.com/?size=100&id=3tC9EQumUAuq&format=png&color=FFFFFF' alt='GitHub' style='width: 24px; height: 24px;'>"
            "</a>"
            "<a href='https://www.linkedin.com/in/alwinvj' target='_blank' style='margin: 0 10px;'>"
            "<img src='https://img.icons8.com/?size=100&id=8808&format=png&color=FFFFFF' alt='LinkedIn' style='width: 24px; height: 24px;'>"
            "</a>"
            "</div>"
            "<br>"
            "<button style='width: 100%; max-width: 300px; background-color:#333333; color: white; padding: 10px 20px;border-radius: 6px;margin-bottom: 10px'>My Resume</button>"
            "<button style='width: 100%; max-width: 300px; background-color:#222222; color: white; padding: 10px 20px;border-radius: 6px;'>Hire Me</button>"
            "</div>"
            "<br>",
            unsafe_allow_html=True,
        )

    with col2:
        st.header("Experience page")

    # Footer
    st.markdown(
        """
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
    """,
        unsafe_allow_html=True,
    )

# Projects page
elif selected == "Projects":
    col1, col2 = st.columns([2, 6])

    with col1:
        st.markdown("""
             <style>
             .essential-details {
                 text-align: center;
                 border-right: 2px solid #ccc;
                 padding: 1rem;
             }
         
             /* Remove border on tablet and mobile (≤ 1024px) */
             @media screen and (max-width: 1024px) {
                 .essential-details {
                     display:none;
                 }
             }
             </style>
             """, unsafe_allow_html=True)
        st.markdown(
            "<div class = 'essential-details'>"
            "<h2>Alwin V J</h2>"
            "<h5 style>AI/ML Engineer</h5>"
            "<h6 style='display: center; align-items: center; gap: 8x; color: white;'>"
            "<svg xmlns='http://www.w3.org/2000/svg' fill='white' width='20' height='20' viewBox='0 0 24 24'>"
            "<path d='M12 13.065L1.5 6.75V17.25H22.5V6.75L12 13.065ZM12 11.25L22.5 4.5H1.5L12 11.25Z'/>"
            "</svg>"
            "&nbsp;&nbsp;alwinvj5@gmail.com</h6>"
            "<div style='margin: 10px 0;'>"
            "<a href='https://github.com/AlwinVJ' target='_blank' style='margin: 0 10px;'>"
            "<img src='https://img.icons8.com/?size=100&id=3tC9EQumUAuq&format=png&color=FFFFFF' alt='GitHub' style='width: 24px; height: 24px;'>"
            "</a>"
            "<a href='https://www.linkedin.com/in/alwinvj' target='_blank' style='margin: 0 10px;'>"
            "<img src='https://img.icons8.com/?size=100&id=8808&format=png&color=FFFFFF' alt='LinkedIn' style='width: 24px; height: 24px;'>"
            "</a>"
            "</div>"
            "<br>"
            "<button style='width: 100%; max-width: 300px; background-color:#333333; color: white; padding: 10px 20px;border-radius: 6px;margin-bottom: 10px'>My Resume</button>"
            "<button style='width: 100%; max-width: 300px; background-color:#222222; color: white; padding: 10px 20px;border-radius: 6px;'>Hire Me</button>"
            "</div>"
            "<br>",
            unsafe_allow_html=True,
        )

    with col2:
        st.header("Projects page")

    # Footer
    st.markdown(
        """
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
    """,
        unsafe_allow_html=True,
    )
