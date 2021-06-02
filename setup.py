import setuptools

setuptools.setup(
    name="streamlit-nav",
    version="0.0.1",
    author="Clément LABRUGERE",
    author_email="<clement.labrugere@gmail.com",
    description="Custom Streamlit module for multiplage apps navigation",
    long_description="Custom Streamlit module for multiplage apps navigation",
    long_description_content_type="text/plain",
    url="https://github.com/clabrugere/streamlit-nav",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[],
    python_requires=">=3.6",
    install_requires=[
        "streamlit >= 0.63",
    ],
)
