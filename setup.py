from setuptools import setup


setup(
    name='nose_runnable_test_names',
    keywords="nose,test,plugins",
    version='0.1',
    author='Colin Deasy',
    author_email='coldeasy+nose@gmail.com',
    url="https://github.com/coldeasy/nose-runnable-test-names",
    description=(
        'Changes the nose test descriptions so that you can copy and paste '
        'a test to the nose runner'
    ),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python",
        "Topic :: Software Development :: Testing"
    ],
    install_requires=['nose'],
    py_modules=['nose_runnable_test_names'],
    entry_points={
        'nose.plugins.0.10': [
            'runnable-test-names = nose_runnable_test_names:RunnableTestNames'
        ]
    },
)
