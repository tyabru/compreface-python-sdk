"""
    Copyright(c) 2021 the original author or authors

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        https: // www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
    or implied. See the License for the specific language governing
    permissions and limitations under the License.
 """


from setuptools import find_packages, setup


setup(
    name='compreface-sdk',
    packages=find_packages(where='compreface', include=['examples']),
    version='0.1.0',
    license='apache-2.0',
    description='CompreFace Python SDK makes face recognition into your application even easier.',
    author='Artsiom Liubymov aliubymov@exadel.com, Artsiom Khadzkou akhadzkou@exadel.com',
    author_email='aliubymov@exadel.com, akhadzkou@exadel.com',
    url='https://exadel.com/solutions/compreface/',
    download_url='https://github.com/exadel-inc/compreface-python-sdk/0.1.0.tar.gz',
    keywords=[
        "CompreFace",
        "Face Recognition",
        "Face Detection",
        "Face Verification",
        "Face Identification",
        "Computer Vision",
        "SDK"
    ],
    install_requires=[
        'requests-toolbelt==0.9.1'
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: Apache license 2.0',
        'Programming Language :: Python :: 3.7+',
    ],
)