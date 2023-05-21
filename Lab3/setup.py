from setuptools import setup

setup(
    name="json_xml_serializer",
    version="0.1.1",
    description="Library for python (de)serialization in Json and Xml",
    url="https://github.com/YanPreskurel/Labs_1-4_4sem_IGI/tree/lab3",
    author="Yan",
    author_email="yanpresfoot@mail.ru",
    license="MIT",
    classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent"
    ],
    packages=["serializers"],
    include_package_data=True,
    install_requires=["regex"]
)