import setuptools

__version__ = "0.0.0"

REPO_NAME = "HealthLlama-AI-Medical-Helper"
AUTHOR_USER_NAME = "45-Hrishi"
SRC_REPO = "healthllama"
AUTHOR_EMAIL = "hrishikeshkothawade1@gmail.com"
LONG_DESCRIPTION = """This application provides answers to health-related questions using Meta’s 
Llama 2 model fine-tuned for medical interactions, referred to as HealthLlama. 
Users can ask about diseases, medicines, symptoms, and general healthcare, and the chatbot 
delivers accurate, informative responses based on medical data. The system efficiently retrieves and 
processes relevant medical information to guide users, making it an intuitive tool for health 
assistance. The responses are tailored to the user's inquiries and help with quick decision-making or 
understanding health conditions. All interactions and responses can be logged in a file for future 
reference or analysis.
"""
DESCRIPTION = """
HealthLlama - AI Medical Helper
"""


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)