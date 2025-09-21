from flask import Flask, render_template, send_file, abort
import os

app = Flask(__name__)


@app.route("/")
def index():
    # Data extracted and summarized from your resume
    # This can be later moved to a separate data file or a database
    profile = {
        "name": "Rishank Gautam",
        "tagline": "Data Scientist Specializing in AI-Driven Solutions",
        "email": "rishankgautam8@gmail.com",
        "linkedin": "https://www.linkedin.com/in/rishank-gautam-46284820a",
        "github": "https://github.com/Ris1103",
        "summary": (
            "I am an experienced Data Scientist with a passion for developing "
            "innovative AI-driven solutions to tackle real-world challenges. "
            "My work involves transforming complex data into actionable insights "
            "and building intelligent systems that automate and enhance business "
            "processes. From developing sophisticated contract extraction systems "
            "to designing dynamic conversational AI, I thrive on leveraging "
            "cutting-edge technology to deliver measurable impact."
        ),
    }

    skills = {
        "Languages": ["Python", "SQL"],
        "Data Analysis & Visualization": [
            "Pandas",
            "Numpy",
            "Seaborn",
            "Matplotlib",
            "PowerBI",
            "Tableau",
        ],
        "Technologies & Frameworks": [
            "Langchain",
            "LangGraph",
            "FastAPI",
            "Docker",
            "Tensorflow-Keras",
            "PyTorch",
            "Git/GitHub",
            "Azure",
            "OpenAI",
        ],
        "Domain Knowledge": [
            "Generative AI",
            "LLM",
            "NLP",
            "Deep Learning",
            "Computer Vision",
            "Statistical Modelling",
        ],
    }

    experiences = [
        {
            "role": "Associate Data Scientist",
            "company": "Emplay Analytics",
            "period": "July 2024 - Present",
            "location": "Bengaluru, KA",
            "description": [
                (
                    "Developed an AI-driven contract extraction system, automating the "
                    "processing of over <strong>2,000 contracts</strong> per run."
                ),
                (
                    "Built a Generative AI-based data extraction solution using LangChain, "
                    "OpenAI, and FastAPI to streamline information retrieval."
                ),
                (
                    "Designed an LLM-powered supplier evaluation bot, reducing manual "
                    "assessment effort by <strong>70%</strong>."
                ),
                (
                    "Transformed a rigid service bot into a dynamic, multi-turn "
                    "conversational experience to significantly improve user engagement."
                ),
            ],
        },
        {
            "role": "Data Science Intern",
            "company": "Emplay Analytics",
            "period": "Jan 2024 - July 2024",
            "location": "Bengaluru, KA",
            "description": [
                (
                    "Designed and implemented LLM-based solutions for advanced "
                    "information retrieval and automation."
                ),
                (
                    "Developed and deployed scalable FastAPI applications for AI-driven "
                    "data extraction, improving process speed by <strong>60%</strong>."
                ),
                (
                    "Built a Computer Adaptive Testing (CAT) simulation using Python, "
                    "Langchain, and Azure OpenAI."
                ),
            ],
        },
        {
            "role": "ML Engineering Intern",
            "company": "3DAILY",
            "period": "Sep 2023 - Nov 2023",
            "location": "Bengaluru, KA",
            "description": [
                "Developed and fine-tuned deep learning models for 3D modelling "
                "and super-resolution tasks.",
                "Improved 3D model visual fidelity by <strong>10%</strong> by extracting and "
                "imprinting intricate skin textures from 2D images.",
                (
                    "Utilised Python, Tensorflow, OpenCV, and PyTorch to streamline "
                    "3D modelling processes."
                ),
            ],
        },
    ]

    projects = [
        {
            "title": "Smart Legal Assistant (Smart-LA)",
            "description": (
                "An AI-powered legal assistant designed for Indian SMBs, utilizing a "
                "hybrid RAG + Agent system to provide contextual legal advice and "
                "automated contract generation."
            ),
            "technologies": ["ChromaDB", "pgVector", "Redis", "Celery", "RAG", "LLM"],
            "link": "https://github.com/Ris1103/Smart-Legal-Assistant",
            "image": (
                "https://images.unsplash.com/photo-1589829545856-d10d557cf95f?"
                "ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80"
            ),
            "image_alt": "AI Legal Assistant with documents and scales of justice",
        },
        {
            "title": "Store Item Demand Forecasting",
            "description": (
                "A comprehensive forecasting model to predict future sales for store inventory "
                "using historical sales data. Features extensive EDA, feature engineering, and "
                "XGBoost modeling with hyperparameter tuning for optimal performance."
            ),
            "technologies": [
                "Python",
                "XGBoost",
                "Pandas",
                "Scikit-learn",
                "Matplotlib",
                "Seaborn",
            ],
            "link": "https://github.com/Ris1103/Product-Forecasting",
            "image": (
                "https://images.unsplash.com/photo-1460925895917-afdab827c52f?"
                "ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80"
            ),
            "image_alt": "Data analytics dashboard with charts and graphs",
        },
        {
            "title": "Customer Churn Prediction",
            "description": (
                "A machine learning solution to predict customer churn with comprehensive model "
                "comparison. Random Forest achieved the best performance with high precision, "
                "recall, and F1-score for effective churn identification."
            ),
            "technologies": [
                "Python",
                "Random Forest",
                "XGBoost",
                "Scikit-learn",
                "Data Visualization",
            ],
            "link": "https://github.com/Ris1103/Customer-Churn-Analysis",
            "image": (
                "https://images.unsplash.com/photo-1551288049-bebda4e38f71?"
                "ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80"
            ),
            "image_alt": "Customer analytics and retention metrics visualization",
        },
        {
            "title": "Insurance Claim Prediction Model",
            "description": (
                "An advanced XGBoost model for predicting insurance claim outcomes using "
                "comprehensive customer and vehicle data. Features extensive preprocessing, "
                "hyperparameter tuning, and model optimization for accurate claim predictions."
            ),
            "technologies": ["Python", "XGBoost", "Scikit-learn", "Pandas", "GridSearchCV"],
            "link": "https://github.com/Ris1103/Insurance-Claim-Prediction-Model",
            "image": (
                "https://images.unsplash.com/photo-1450101499163-c8848c66ca85?"
                "ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80"
            ),
            "image_alt": "Insurance documents and car accident analysis",
        },
        {
            "title": "Football Tracking with YOLOv8",
            "description": (
                "A deep learning model trained to detect and track the movement of a "
                "football in video footage, enabling advanced game analysis with high accuracy."
            ),
            "technologies": ["YOLOv8", "Computer Vision", "PyTorch", "Object Detection"],
            "link": "https://github.com/Ris1103/Football-Tracking-Model",
            "image": (
                "https://images.unsplash.com/photo-1574629810360-7efbbe195018?"
                "ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80"
            ),
            "image_alt": "Football game analysis with computer vision overlay",
        },
    ]

    return render_template(
        "index.html", profile=profile, skills=skills, experiences=experiences, projects=projects
    )


@app.route("/download-resume")
def download_resume():
    """Download resume PDF file"""
    try:
        # Define the path to the resume file
        resume_path = os.path.join(app.root_path, "static", "resume.pdf")

        # Check if file exists
        if os.path.exists(resume_path):
            return send_file(
                resume_path,
                as_attachment=True,
                download_name="Rishank_Gautam_Resume.pdf",
                mimetype="application/pdf",
            )
        else:
            # If no resume file exists, create a placeholder response
            abort(
                404,
                description=("Resume file not found. Please contact me directly for my resume."),
            )
    except Exception:
        abort(500, description="Error downloading resume. Please try again later.")


if __name__ == "__main__":
    # Use environment variables for production
    port = int(os.environ.get("PORT", 5000))
    debug = os.environ.get("FLASK_ENV") != "production"
    app.run(host="0.0.0.0", port=port, debug=debug)
