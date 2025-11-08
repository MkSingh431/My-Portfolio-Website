import streamlit as st
import base64

# Set page configuration
st.set_page_config(
    page_title="Motilal Das Portfolio",
    page_icon="🌟",
    layout="wide"
)

# Function to load and encode CSS
def load_css(file_path):
    with open(file_path) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Load CSS files
load_css('css/bootstrap.min.css')
load_css('css/open-iconic-bootstrap.min.css')
load_css('css/animate.css')
load_css('css/owl.carousel.min.css')
load_css('css/owl.theme.default.min.css')
load_css('css/magnific-popup.css')
load_css('css/aos.css')
load_css('css/ionicons.min.css')
load_css('css/flaticon.css')
load_css('css/icomoon.css')
load_css('css/style.css')

# Custom CSS for project image zoom effect
st.markdown("""
<style>
.zoom-effect {
  overflow: hidden;
  transition: transform 0.3s ease-out;
}

.zoom-effect:hover {
  transform: scale(1.1);
}
</style>
""", unsafe_allow_html=True)

# Navigation Bar
st.markdown("""
<nav class="navbar navbar-expand-lg navbar-dark ftco_navbar ftco-navbar-light site-navbar-target" id="ftco-navbar">
    <div class="container">
        <a class="navbar-brand" href="index.html">Motilal Das</a>
        <button class="navbar-toggler js-fh5co-nav-toggle fh5co-nav-toggle" type="button" data-toggle="collapse" data-target="#ftco-nav" aria-controls="ftco-nav" aria-expanded="false" aria-label="Toggle navigation">
            <span class="oi oi-menu"></span> Menu
        </button>
        <div class="collapse navbar-collapse" id="ftco-nav">
            <ul class="navbar-nav nav ml-auto">
                <li class="nav-item"><a href="#home-section" class="nav-link"><span>Home</span></a></li>
                <li class="nav-item"><a href="#about-section" class="nav-link"><span>About</span></a></li>
                <li class="nav-item"><a href="#resume-section" class="nav-link"><span>Resume</span></a></li>
                <li class="nav-item"><a href="#project-section" class="nav-link"><span>Projects</span></a></li>
                <li class="nav-item"><a href="#contact-section" class="nav-link"><span>Contact</span></a></li>
            </ul>
        </div>
    </div>
</nav>
""", unsafe_allow_html=True)


# Home Section


st.markdown('<section id="home-section" class="hero">', unsafe_allow_html=True)


col1, col2 = st.columns([1, 1])


with col1:


    st.markdown('<div class="one-forth d-flex align-items-center ftco-animate" data-scrollax=" properties: { translateY: \'70%\' }">', unsafe_allow_html=True)


    st.markdown('<div class="text">', unsafe_allow_html=True)


    st.markdown('<span class="subheading">Hello!</span>', unsafe_allow_html=True)


    st.markdown("<h1 class=\"mb-4 mt-3\">I'm <span>Motilal Das</span></h1>", unsafe_allow_html=True)


    


    st.markdown('''

        <h2 id="typing-animation" style="margin-bottom: 1rem;"></h2>


        <script>


            const typingAnimationElement = document.getElementById('typing-animation');


            if (typingAnimationElement && !typingAnimationElement.hasAttribute('data-running')) {


                typingAnimationElement.setAttribute('data-running', 'true');


                const typingTexts = [


                    'Data Scientist',


                    'Data Analyst',


                    'Machine Learning Enthusiast',


                ];


                let textIndex = 0;


                let charIndex = 0;





                function type() {


                    if (charIndex < typingTexts[textIndex].length) {


                        typingAnimationElement.innerHTML += typingTexts[textIndex].charAt(charIndex);


                        charIndex++;


                        setTimeout(type, 120);


                    } else {


                        setTimeout(erase, 2000);


                    }


                }





                function erase() {


                    if (charIndex > 0) {


                        typingAnimationElement.innerHTML = typingTexts[textIndex].substring(0, charIndex - 1);


                        charIndex--;


                        setTimeout(erase, 80);


                    } else {


                        textIndex = (textIndex + 1) % typingTexts.length;


                        setTimeout(type, 500);


                    }


                }





                // Start the animation


                if (typingTexts.length) {


                    setTimeout(type, 1000);


                }


            }


        </script>


    ''', unsafe_allow_html=True)





    st.markdown('<p><a href="https://www.linkedin.com/in/motilal-das-42b4a9254/?lipi=urn%3Ali%3Apage%3Ad_flagship3_feed%3BLjI78pnlSA6l%2BuFnsx8F%2FA%3D%3D" class="btn btn-white btn-outline-white py-3 px-4">Linkedin</a> <a href="https://github.com/MkSingh431/MkSingh431" class="btn btn-white btn-outline-white py-3 px-4">My works</a></p>', unsafe_allow_html=True)


    st.markdown('</div>', unsafe_allow_html=True)


    st.markdown('</div>', unsafe_allow_html=True)




with col2:


    st.markdown('<div class="one-third js-fullheight order-md-last img" style="background-image:url(data:image/png;base64,{});">'.format(base64.b64encode(open("images/image1.png", "rb").read()).decode()), unsafe_allow_html=True)


    st.markdown('<div class="overlay"></div>', unsafe_allow_html=True)


    st.markdown('</div>', unsafe_allow_html=True)

st.markdown('</section>', unsafe_allow_html=True)


# About Section
st.markdown('<section class="ftco-about img ftco-section ftco-no-pb" id="about-section">', unsafe_allow_html=True)
st.markdown('<div class="container">', unsafe_allow_html=True)
st.markdown('<div class="row">', unsafe_allow_html=True)
st.markdown('<div class="row d-flex align-items-stretch">', unsafe_allow_html=True)
col1, col2 = st.columns([5, 7])
with col1:
    st.markdown('<div class="img-about img d-flex align-items-stretch">', unsafe_allow_html=True)
    st.markdown('<div class="overlay">', unsafe_allow_html=True)
    st.markdown('<div class="row">', unsafe_allow_html=True)
    st.markdown('<div class="col-sm-4 col-md-5">', unsafe_allow_html=True)
    st.markdown('<div class="about-img">', unsafe_allow_html=True)
    st.image("images/image4.png", use_column_width=True, clamp=True)
    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('<div class="col-sm-4 col-md-7">', unsafe_allow_html=True)
    st.markdown('<div class="about-info">', unsafe_allow_html=True)
    st.markdown('<p><span class="title-s">Name: </span> <span>Motilal Das</span></p>', unsafe_allow_html=True)
    st.markdown('<p><span class="title-s">Job Role: </span> <span> Data Scientist/Data Analyst </span></p>', unsafe_allow_html=True)
    st.markdown('<p><span class="title-s">Experience: </span> <span>Fresher</span></p>', unsafe_allow_html=True)
    st.markdown('<p><span class="title-s">Address: </span> <span>Gurgaon, India</span></p>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('<div class="skill-mf">', unsafe_allow_html=True)
    st.markdown('<p class="title-s">Skills</p>', unsafe_allow_html=True)
    st.markdown('<span>SQL</span> <span class="pull-right">95%</span>', unsafe_allow_html=True)
    st.progress(95)
    st.markdown('<span>PYTHON</span> <span class="pull-right">85%</span>', unsafe_allow_html=True)
    st.progress(85)
    st.markdown('<span>Data Visualization</span> <span class="pull-right">90%</span>', unsafe_allow_html=True)
    st.progress(90)
    st.markdown('<span>Statistical Analysis</span> <span class="pull-right">85%</span>', unsafe_allow_html=True)
    st.progress(85)
    st.markdown('<span>Machine Learning</span> <span class="pull-right">80%</span>', unsafe_allow_html=True)
    st.progress(80)
    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
with col2:
    st.markdown('<div class="row justify-content-start pb-3">', unsafe_allow_html=True)
    st.markdown('<div class="col-md-12 heading-section ftco-animate">', unsafe_allow_html=True)
    st.markdown('<h2 class="mb-4">About Me</h2>', unsafe_allow_html=True)
    st.markdown('<p>A highly analytical and driven Data Science Fresher eager to solve complex problems and drive quantifiable impact through data. Proficient in the entire machine learning pipeline, from data cleaning and feature engineering to building and deploying models. Expert in Python (including NumPy, Pandas, Scikit-learn, TensorFlow/PyTorch) and SQL, with hands-on experience in building predictive models, including classification and regression. Seeking an entry-level role where I can transform large datasets into actionable predictions and business strategies.</p>', unsafe_allow_html=True)
    st.markdown('<ul class="about-info mt-4 px-md-0 px-2">', unsafe_allow_html=True)
    st.markdown('<li class="d-flex"><span>Profile:</span> <span>Data Science &amp; Analytics</span></li>', unsafe_allow_html=True)
    st.markdown('<li class="d-flex"><span>Domain:</span> <span>E-commerce &amp; Retail </span></li>', unsafe_allow_html=True)
    st.markdown('<li class="d-flex"><span>Education:</span> <span>Bachelor of Computer Application</span></li>', unsafe_allow_html=True)
    st.markdown('<li class="d-flex"><span>Language:</span> <span>English, Hindi, </span></li>', unsafe_allow_html=True)
    st.markdown('<li class="d-flex"><span>BI Tools:</span> <span>Microsoft Power BI, Looker &amp; Tableau</span></li>', unsafe_allow_html=True)
    st.markdown('<li class="d-flex"><span>Other Skills:</span> <span>Cloud, PySpark, Excel, Git, Google Analytics &amp; Microsoft Azure</span></li>', unsafe_allow_html=True)
    st.markdown('<li class="d-flex"><span>Interest:</span> <span>Football </span></li>', unsafe_allow_html=True)
    st.markdown('</ul>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('<div class="counter-wrap ftco-animate d-flex mt-md-3">', unsafe_allow_html=True)
    st.markdown('<div class="text">', unsafe_allow_html=True)
    st.markdown('<p class="mb-4"><span class="number" data-number="30">0</span> <span>+</span> <span>&nbsp; Projects completed</span></p>', unsafe_allow_html=True)
    st.markdown('<p><a href="https://www.linkedin.com/in/motilal-das-42b4a9254/?lipi=urn%3Ali%3Apage%3Ad_flagship3_feed%3BLjI78pnlSA6l%2BuFnsx8F%2FA%3D%3D" class="btn btn-primary py-3 px-3">LinkedIn</a></p>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
st.markdown('</section>', unsafe_allow_html=True)

# Resume Section
st.markdown('<section class="ftco-section ftco-no-pb" id="resume-section">', unsafe_allow_html=True)
st.markdown('<div class="container">', unsafe_allow_html=True)
st.markdown('<div class="row justify-content-center pb-5">', unsafe_allow_html=True)
st.markdown('<div class="col-md-10 heading-section text-center ftco-animate">', unsafe_allow_html=True)
st.markdown('<h2 class="mb-4">Resume</h2>', unsafe_allow_html=True)
st.markdown('<p>A strong foundation in statistical modeling and data science principles. Highly proficient in Python (Pandas, Scikit-learn) and SQL for cleaning, manipulating, and extracting data from relational databases. Developed and validated several Machine Learning models (e.g., classification/regression) through capstone projects, and effectively communicated findings using compelling data visualizations (Matplotlib/Seaborn). Eager to apply analytical rigor to a dynamic business environment.</p>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
st.markdown('<div class="row">', unsafe_allow_html=True)
st.markdown('<h1 class="big-4">Experience</h1>', unsafe_allow_html=True)
st.markdown('<div class="underline"></div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
st.markdown('<br>', unsafe_allow_html=True)
st.markdown('<div class="row">', unsafe_allow_html=True)
col1, col2 = st.columns(2)
with col1:
    st.markdown('<div class="resume-wrap ftco-animate">', unsafe_allow_html=True)
    st.markdown('<span class="date">2025-Present</span>', unsafe_allow_html=True)
    st.markdown('<h2>Operation Executive</h2>', unsafe_allow_html=True)
    st.markdown('<span class="position">BAI Infosolutions Pvt. Ltd</span>', unsafe_allow_html=True)
    st.markdown('<p class="mt-4">BAI Infosolutions primarily concentrates on providing robust, end-to-end IT solutions across critical business functions. <ul><li>SAP Data Integration: Successfully performed ETL (Extract, Transform, Load) on large-scale SAP ERP (ECC/S/4HANA) data for reporting, ensuring data consistency and analytical readiness</li><li>BI Reporting & Dashboards: Designed and deployed interactive SAP Business Objects/Analytics Cloud (SAC) dashboards focused on Key Performance Indicators (KPIs) like sales variance and inventory turnover</li></ul></p>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
with col2:
    st.markdown('<div class="resume-wrap ftco-animate">', unsafe_allow_html=True)
    st.markdown('<span class="date">2022-2023</span>', unsafe_allow_html=True)
    st.markdown('<h2>Data Entry Scpecialist</h2>', unsafe_allow_html=True)
    st.markdown('<span class="position">Reliance E-Commerce </span>', unsafe_allow_html=True)
    st.markdown('<p><ul><li>Real-time Reporting: Developed real-time Business Intelligence (BI) dashboards using SAP Analytics Cloud (SAC) or Power BI integrated with SAP HANA to provide immediate insights into critical metrics (e.g., inventory levels, production output) for executive decision-making.</li><li>Analyse and monitor data management projects</li><li>Managing ERP data entry using SAP </li></ul></p>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
st.markdown('<br>', unsafe_allow_html=True)
st.markdown('<br>', unsafe_allow_html=True)
st.markdown('<div class="row">', unsafe_allow_html=True)
st.markdown('<h1 class="big-4">Education</h1>', unsafe_allow_html=True)
st.markdown('<div class="underline"></div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
st.markdown('<br>', unsafe_allow_html=True)
st.markdown('<div class="row">', unsafe_allow_html=True)
col1, col2 = st.columns(2)
with col1:
    st.markdown('<div class="resume-wrap ftco-animate">', unsafe_allow_html=True)
    st.markdown('<span class="date">2025-2026</span>', unsafe_allow_html=True)
    st.markdown('<h2>AI/Data Science</h2>', unsafe_allow_html=True)
    st.markdown('<span class="position">Ducat, Gurgaon</span>', unsafe_allow_html=True)
    st.markdown('<p class="mt-4">Grade: First class distinction.</p>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
with col2:
    st.markdown('''<div class="resume-wrap ftco-animate">
        <span class="date">2023-2026</span>
        <h2>Bachelor of Computer Application</h2>
        <span class="position">World College of Technology and Management</span>
        <p class="mt-4">Grade: First class distinction.</p>
    </div>''', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
st.markdown('<br>', unsafe_allow_html=True)
st.markdown('<div class="row">', unsafe_allow_html=True)
st.markdown('<div class="col-md-6">', unsafe_allow_html=True)
st.markdown('''<div class="resume-wrap ftco-animate">
    <span class="date">2020-2022</span>
    <h2>Higher Secondary School</h2>
    <span class="position">D.S College, Katihar (Bihar)</span>
    <p class="mt-4">Grade: First class distinction.</p>
</div>''', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
st.markdown('<div class="row justify-content-center mt-5">', unsafe_allow_html=True)
st.markdown('<div class="col-md-6 text-center ftco-animate">', unsafe_allow_html=True)
st.markdown('<p><a href="https://drive.google.com/file/d/10egkgW5KXZ3_hVEXAMW1gOhMhEhYkhyf/view?usp=drive_link" class="btn btn-primary py-3 px-3">Download CV</a></p>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
st.markdown('</section>', unsafe_allow_html=True)
    
# Projects Section
st.markdown('''<section class="ftco-section" id="project-section">
''', unsafe_allow_html=True)
st.markdown('''<div class="container">
''', unsafe_allow_html=True)
st.markdown('''<div class="row justify-content-center mb-5 pb-5">
''', unsafe_allow_html=True)
st.markdown('''<div class="col-md-7 heading-section text-center ftco-animate">
''', unsafe_allow_html=True)
st.markdown('''<h2 class="mb-4">Projects</h2>
''', unsafe_allow_html=True)
st.markdown('''<p>Below are the sample Data Analytics projects on SQL, Python, Power BI & ML.</p>
''', unsafe_allow_html=True)
st.markdown('''</div>
''', unsafe_allow_html=True)
st.markdown('''</div>
''', unsafe_allow_html=True)
st.markdown('''<div class="row d-flex">
''', unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown('''<div class="blog-entry justify-content-end">
''', unsafe_allow_html=True)
    st.markdown(f'<a href="https://github.com/MkSingh431/SQL_Music_Store_Analysis" class="block-20 zoom-effect" style="background-image: url(data:image/jpeg;base64,{base64.b64encode(open("images/proj_1.jpg", "rb").read()).decode()})"></a>', unsafe_allow_html=True)
    st.markdown('''<div class="text mt-3 float-right d-block">
''', unsafe_allow_html=True)
    st.markdown('''<h3 class="heading"><a href="https://github.com/MkSingh431/SQL_Music_Store_Analysis">Digital Music Store Data Analysis using SQL</a></h3>
''', unsafe_allow_html=True)
    st.markdown('''<p>Analyzed music store data using advanced SQL queires to identify gaps and increase the business growth.</p>
''', unsafe_allow_html=True)
    st.markdown('''</div>
''', unsafe_allow_html=True)
    st.markdown('''</div>
''', unsafe_allow_html=True)
with col2:
    st.markdown('''<div class="blog-entry justify-content-end">
''', unsafe_allow_html=True)
    st.markdown(f'<a href="https://github.com/MkSingh431/Python_Diwali_Sales_Analysis/blob/main/Diwali_Sales_Analysis.ipynb" class="block-20 zoom-effect" style="background-image: url(data:image/jpeg;base64,{base64.b64encode(open("images/proj_2.jpg", "rb").read()).decode()})"></a>', unsafe_allow_html=True)
    st.markdown('''<div class="text mt-3 float-right d-block">
''', unsafe_allow_html=True)
    st.markdown('''<h3 class="heading"><a href="https://github.com/MkSingh431/Python_Diwali_Sales_Analysis/blob/main/Diwali_Sales_Analysis.ipynb">Data Analysis using Python Project for Beginners</a></h3>
''', unsafe_allow_html=True)
    st.markdown('''<p>Performed exploratory data analysis on diwali sales data using Python to improve the customer experience.</p>
''', unsafe_allow_html=True)
    st.markdown('''</div>
''', unsafe_allow_html=True)
    st.markdown('''</div>
''', unsafe_allow_html=True)
with col3:
    st.markdown('''<div class="blog-entry">
''', unsafe_allow_html=True)
    st.markdown(f'<a href="https://github.com/MkSingh431/Flipkart-Sales-Data-Visualization/tree/main" class="block-20 zoom-effect" style="background-image: url(data:image/png;base64,{base64.b64encode(open("images/dashboard.png", "rb").read()).decode()})"></a>', unsafe_allow_html=True)
    st.markdown('''<div class="text mt-3 float-right d-block">
''', unsafe_allow_html=True)
    st.markdown('''<h3 class="heading"><a href="https://github.com/MkSingh431/Flipkart-Sales-Data-Visualization/tree/main">Power BI Sales dashboard Project for Beginners</a></h3>
''', unsafe_allow_html=True)
    st.markdown('''<p>Designed a power bi dashboard for Flipkart to track and analyze the online sales data acorss India.</p>
''', unsafe_allow_html=True)
    st.markdown('''</div>
''', unsafe_allow_html=True)
    st.markdown('''</div>
''', unsafe_allow_html=True)
st.markdown('''</div>
''', unsafe_allow_html=True)
st.markdown('''<br>
''', unsafe_allow_html=True)
st.markdown('''<div class="row d-flex justify-content-center">
''', unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown('''<div class="blog-entry justify-content-end">
''', unsafe_allow_html=True)
    st.markdown(f'<a href="https://github.com/MkSingh431/sales_forecasting" class="block-20 zoom-effect" style="background-image: url(data:image/jpeg;base64,{base64.b64encode(open("images/proj_4.jpg", "rb").read()).decode()})"></a>', unsafe_allow_html=True)
    st.markdown('''<div class="text mt-3 float-right d-block">
''', unsafe_allow_html=True)
    st.markdown('''<h3 class="heading"><a href="https://github.com/MkSingh431/sales_forecasting">Sales Forecast- Time Series Forecasting</a></h3>
''', unsafe_allow_html=True)
    st.markdown('''<p>Used multiple machine learning models to forecast sales (retail store) and performed time series analysis.</p>
''', unsafe_allow_html=True)
    st.markdown('''</div>
''', unsafe_allow_html=True)
    st.markdown('''</div>
''', unsafe_allow_html=True)
with col2:
    st.markdown('''<div class="blog-entry justify-content-end">
''', unsafe_allow_html=True)
    st.markdown(f'<a href="https://github.com/MkSingh431/tableau-projects-collection" class="block-20 zoom-effect" style="background-image: url(data:image/png;base64,{base64.b64encode(open("images/tableau.png", "rb").read()).decode()})"></a>', unsafe_allow_html=True)
    st.markdown('''<div class="text mt-3 float-right d-block">
''', unsafe_allow_html=True)
    st.markdown('''<h3 class="heading"><a href="https://github.com/MkSingh431/tableau-projects-collection">HR data to derive insights into the employee base</a></h3>
''', unsafe_allow_html=True)
    st.markdown('''<p>Designed a Tableau Dashboard for call centre &amp; provide insights into sales trends over time.</p>
''', unsafe_allow_html=True)
    st.markdown('''</div>
''', unsafe_allow_html=True)
    st.markdown('''</div>
''', unsafe_allow_html=True)
with col3:
    st.markdown('''<div class="blog-entry justify-content-end">
''', unsafe_allow_html=True)
    st.markdown(f'<a href="https://iplanalyst.streamlit.app/" class="block-20 zoom-effect" style="background-image: url(data:image/jpeg;base64,{base64.b64encode(open("images/ipl.jpg", "rb").read()).decode()})"></a>', unsafe_allow_html=True)
    st.markdown('''<div class="text mt-3 float-right d-block">
''', unsafe_allow_html=True)
    st.markdown('''<h3 class="heading"><a href="https://iplanalyst.streamlit.app/">IPL Analysis using Python</a></h3>
''', unsafe_allow_html=True)
    st.markdown('''<p>This project provides a detailed exploration of IPL matches and player performances over the years.</p>
''', unsafe_allow_html=True)
    st.markdown('''</div>
''', unsafe_allow_html=True)
    st.markdown('''</div>
''', unsafe_allow_html=True)
st.markdown('''</div>
''', unsafe_allow_html=True)
st.markdown('''</div>
''', unsafe_allow_html=True)
st.markdown('''</section>
''', unsafe_allow_html=True)

# Contact Section
st.markdown('''<section class="ftco-section contact-section ftco-no-pb" id="contact-section">
''', unsafe_allow_html=True)
st.markdown('''<div class="container">
''', unsafe_allow_html=True)
st.markdown('''<div class="row justify-content-center mb-5 pb-3">
''', unsafe_allow_html=True)
st.markdown('''<div class="col-md-7 heading-section text-center ftco-animate">
''', unsafe_allow_html=True)
st.markdown('''<h2 class="mb-4">Contact Me</h2>
''', unsafe_allow_html=True)
st.markdown('''<p>Below are the details to reach out to me!</p>
''', unsafe_allow_html=True)
st.markdown('''</div>
''', unsafe_allow_html=True)
st.markdown('''</div>
''', unsafe_allow_html=True)
st.markdown('''<div class="row d-flex contact-info mb-5">
''', unsafe_allow_html=True)
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.markdown('''<div class="align-self-stretch box p-4 text-center">
''', unsafe_allow_html=True)
    st.markdown('''<div class="icon d-flex align-items-center justify-content-center">
''', unsafe_allow_html=True)
    st.markdown('''<span class="icon-map-signs"></span>
''', unsafe_allow_html=True)
    st.markdown('''</div>
''', unsafe_allow_html=True)
    st.markdown('''<h3 class="mb-4">Address</h3>
''', unsafe_allow_html=True)
    st.markdown('''<p>Gurgaon, India</p>
''', unsafe_allow_html=True)
    st.markdown('''</div>
''', unsafe_allow_html=True)
with col2:
    st.markdown('''<div class="align-self-stretch box p-4 text-center">
''', unsafe_allow_html=True)
    st.markdown('''<div class="icon d-flex align-items-center justify-content-center">
''', unsafe_allow_html=True)
    st.markdown('''<span class="icon-phone2"></span>
''', unsafe_allow_html=True)
    st.markdown('''</div>
''', unsafe_allow_html=True)
    st.markdown('''<h3 class="mb-4">Contact Number</h3>
''', unsafe_allow_html=True)
    st.markdown('''<p><a href="">+91 9304236214</a></p>
''', unsafe_allow_html=True)
    st.markdown('''</div>
''', unsafe_allow_html=True)
with col3:
    st.markdown('''<div class="align-self-stretch box p-4 text-center">
''', unsafe_allow_html=True)
    st.markdown('''<div class="icon d-flex align-items-center justify-content-center">
''', unsafe_allow_html=True)
    st.markdown('''<span class="icon-paper-plane"></span>
''', unsafe_allow_html=True)
    st.markdown('''</div>
''', unsafe_allow_html=True)
    st.markdown('''<h3 class="mb-4">Email Address</h3>
''', unsafe_allow_html=True)
    st.markdown('''<p><a href="mailto:info@yoursite.com">mks465261@gmail.com</a></p>
''', unsafe_allow_html=True)
    st.markdown('''</div>
''', unsafe_allow_html=True)
with col4:
    st.markdown('''<div class="align-self-stretch box p-4 text-center">
''', unsafe_allow_html=True)
    st.markdown('''<div class="icon d-flex align-items-center justify-content-center">
''', unsafe_allow_html=True)
    st.markdown('''<span class="icon-globe"></span>
''', unsafe_allow_html=True)
    st.markdown('''</div>
''', unsafe_allow_html=True)
    st.markdown('''<h3 class="mb-4">Download Resume</h3>
''', unsafe_allow_html=True)
    st.markdown('''<p><a href="https://drive.google.com/file/d/1rohX3SabaHJ5NjqUHIehRHrV-n6TJoB6/view?usp=drive_link">Resume link</a></p>
''', unsafe_allow_html=True)
    st.markdown('''</div>
''', unsafe_allow_html=True)
st.markdown('''</div>
''', unsafe_allow_html=True)
st.markdown('''<div class="container">
''', unsafe_allow_html=True)
st.markdown('''<br>
''', unsafe_allow_html=True)
st.markdown('''<br>
''', unsafe_allow_html=True)
st.markdown('''<div class="row justify-content-center">
''', unsafe_allow_html=True)
st.markdown('''<div class="col-md-7 ftco-animate text-center">
''', unsafe_allow_html=True)
st.markdown('''<h2>Have a<span> Question?  </span> <a href="https://forms.office.com/Pages/ResponsePage.aspx?id=DQSIkWdsW0yxEjajBLZtrQAAAAAAAAAAAAO__SgL1qtUODdPT01NTVpOMVFWODYwUUdMT1ZTWUhFWS4u" class="btn btn-primary py-3 px-5">Click Here</a> </h2>
''', unsafe_allow_html=True)
st.markdown('''</div>
''', unsafe_allow_html=True)
st.markdown('''</div>
''', unsafe_allow_html=True)
st.markdown('''<br>
''', unsafe_allow_html=True)
st.markdown('''<ul class="ftco-footer-social list-unstyled d-flex justify-content-center align-items-center mb-0">
''', unsafe_allow_html=True)
st.markdown('''<li class="ftco-animate normal-txt">Find me on  </li>
''', unsafe_allow_html=True)
st.markdown('''<li class="ftco-animate"><a href="https://www.linkedin.com/in/motilal-das-42b4a9254/?lipi=urn%3Ali%3Apage%3Ad_flagship3_feed%3BLjI78pnlSA6l%2BuFnsx8F%2FA%3D%3D"><span class="icon-linkedin"></span></a></li>
''', unsafe_allow_html=True)
st.markdown('''<li class="ftco-animate"><a href="https://x.com/Mksingh431/photo"><span class="icon-twitter"></span></a></li>
''', unsafe_allow_html=True)
st.markdown('''<li class="ftco-animate"><a href="https://www.facebook.com/motilal.das.129357"><span class="icon-facebook"></span></a></li>
''', unsafe_allow_html=True)
st.markdown('''<li class="ftco-animate"><a href="https://www.instagram.com/mk_singh_431/"><span class="icon-instagram"></span></a></li>
''', unsafe_allow_html=True)
st.markdown('''</ul>
''', unsafe_allow_html=True)
st.markdown('''<br>
''', unsafe_allow_html=True)
st.markdown('''</div>
''', unsafe_allow_html=True)
st.markdown('''</div>
''', unsafe_allow_html=True)
st.markdown('''</section>
''', unsafe_allow_html=True)
# Footer
st.markdown("""
<footer class="ftco-footer ftco-section">
    <div class="container">
        <div class="row">
            <div class="col-md-12 text-center">
                <p>
                    Copyright &copy;<script>document.write(new Date().getFullYear());</script> All rights reserved | This template is made with <i class="icon-heart color-danger" aria-hidden="true"></i> by <a href="https://colorlib.com" target="_blank">Colorlib</a>
                </p>
            </div>
        </div>
    </div>
</footer>
""", unsafe_allow_html=True)

# Loader
st.markdown('<div id="ftco-loader" class="show fullscreen"><svg class="circular" width="48px" height="48px"><circle class="path-bg" cx="24" cy="24" r="22" fill="none" stroke-width="4" stroke="#eeeeee"/><circle class="path" cx="24" cy="24" r="22" fill="none" stroke-width="4" stroke-miterlimit="10" stroke="#F96D00"/></svg></div>', unsafe_allow_html=True)