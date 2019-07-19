import setuptools

with open("README.md", "r") as fh:

    long_description = fh.read()

setuptools.setup(

     name="your_package_name",  
     version='0.0.1',
     author="Your Name",
     author_email="your.email@email.com",
     description="describe your package",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/you/your_package_repo",
     packages=['your_package_name'],
     classifiers=[
         "Programming Language :: Python :: 3.7",
         "Operating System :: OS Independent",
     ],
 )
