import setuptools


with open("README.md") as fp:
    long_description = fp.read()


setuptools.setup(
    name="rekognition_video_processor",
    version="0.0.1",

    description="A CDK Python app for demonstration purposes",
    long_description="Video processing based on S3 trigger",
    long_description_content_type="text/markdown",

    author="Agus Rivero",

    package_dir={"": "rekognition_video_processor"},
    packages=setuptools.find_packages(where="rekognition_video_processor"),

    python_requires=">=3.7",

    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: JavaScript",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Software Development :: Code Generators",
        "Topic :: Utilities",
        "Typing :: Typed",
    ],
)
