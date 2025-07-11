<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>

<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->

  [![Python][python-shield]][python-url]
  [![Apache 2.0 License][license-shield]][license-url]
  [![PyPI - Format](https://img.shields.io/pypi/format/filtertext?style=for-the-badge)][pypi-url]
  [![PyPI - Status](https://img.shields.io/pypi/status/filtertext?style=for-the-badge)][pypi-url]
  [![LinkedIn][linkedin-shield]][linkedin-url]




<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/michagrandel/filtertext">
    <img src="https://github.com/michagrandel/filtertext/blob/main/doc/images/logo.png?raw=True" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Filter Text</h3>

  <p align="center">
    Command line tool to filter text and save result to file or print to output!
    <br />
    <a href="https://github.com/michagrandel/filtertext/wiki"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/michagrandel/filtertext/issues">Report Bug</a>
    ·
    <a href="https://github.com/michagrandel/filtertext/issues">Request Feature</a>
  </p>
</div>

> [!IMPORTANT]
>
> Please note that this project will be merged into my new general purpose python toolset <a href="https://github.com/michagrandel/plywoodpirate">"plywoodpirate"</a>.
> New features will be introduce only after the merge has been finished.
>
> The merge will take place during 2025.
> This repository will be available until 1st Feburary 2026. After that, it will be deleted.

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About Filter Text</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#installation">Installation</a>
    </li>
    <li>
      <a href="#usage">Usage</a>
      <ul>
        <li><a href="#command-line-script">Command line script</a></li>
        <li><a href="#python-library">Python Library</a></li>
      </ul>
    </li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

<!--[![Product Name Screen Shot][product-screenshot]](https://example.com)-->

**text_filter.py** is a simple commandline tool to filter text using predefined filters
and save the result in a new file.

You can use it for:
* Removing lines with whitespaces only in a text file
* Remove duplicated lines in a text file
* Extend the functionality by creating your own custom filters


<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

This is a simple command line tool written in native python 3, no additional dependencies.

Complete list of dependencies:

<table>
<tr style="padding:0; margin:0">
  <td style="padding:0; margin:0; vertical-align:center"> <img src="https://github.com/michagrandel/filtertext/blob/main/doc/images/python.png?raw=True" height="20" /> </td>
  <td style="padding:0; padding-left:5px; margin:0; vertical-align:center"> <a href="https://python.org">Python 3.x</a> </td></tr>
</table>

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Installation

Install via pip:

```bash
pip install filtertext
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->
## Usage

### Command line script

#### Installation Directory

pip will install a command line script that you can use.
To find the installation directory of that script, you can run this code:

```bash
python -m site --user-base
```
Inside of that folder, you will find a folder structure similar to `Python312\Scripts` or `Python312\bin`.
In this folder, there is a script file `filter_text.py`.

You can add this folder (`../Scripts` or `../bin`) to your **environment variables**,
so you can run the script without navigating to the folder again.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

#### Run the command line script

You can run the script **filter_text.py** with some command line arguments:

```bash
filter_text.py [-h] [-w] [-d] [-l LIST_FILE] [-D OUTPUT_PATH] [-o OUTPUT_FILE] FILE [FILE ...]

Filter
  -w    Remove lines that only contain whitespace
  -d    Remove duplicate lines

Input
  FILE: files to filter
  -f    LIST_FILE: Input file with list of files to filter, one file per line

Output
  -D    OUTPUT_PATH: Output directory (if it exists, it will be deleted first)
  -o    OUTPUT_FILE: Output file path (if it exists, it will be deleted first)
```
<br>

_For more examples, please refer to the [Documentation][doc-url]_

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Python Library

```python
from filtertext import *

file_path = "example.txt"
remove_whitespace = RemoveWhitespaceLinesTextFilter.from_file(file_path)
remove_whitespace.filter()

print(remove_filter.text)
```

_For more examples, please refer to the [Documentation][doc-url]_

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- CONTRIBUTING -->
## Contributing

Thank you for your interest in contributing! Any contributions you make are **greatly appreciated**.

Please make sure to follow our [Code of Conduct](CODE_OF_CONDUCT.md).

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue, if you prefer.
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

**Copyright 2024 Micha Grandel**
    
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at
    
http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

See [LICENSE.md](LICENSE.md) for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Micha Grandel<br>
[![LinkedIn][linkedin-shield]][linkedin-url]
[![Email][email-shield]][author-email]

Project Link: [https://github.com/michagrandel/filtertext][project-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* [Code of Conduct][codeofconduce-url]
* [Best README Template][readme-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[python-icon]: https://github.com/michagrandel/filtertext/blob/main/doc/images/python.png

[python-shield]: https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=white
[contributors-shield]: https://img.shields.io/github/contributors/michagrandel/filtertext.svg?style=for-the-badge
[github-release-version]: https://img.shields.io/github/v/release/michagrandel/filtertext.svg?style=for-the-badge
[forks-shield]: https://img.shields.io/github/forks/michagrandel/filtertext.svg?style=for-the-badge
[stars-shield]: https://img.shields.io/github/stars/michagrandel/filtertext.svg?style=for-the-badge
[issues-shield]: https://img.shields.io/github/issues/michagrandel/filtertext.svg?style=for-the-badge
[license-shield]: https://img.shields.io/github/license/michagrandel/filtertext.svg?style=for-the-badge
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[email-shield]: https://img.shields.io/badge/mail-D14836?style=for-the-badge&logo=email&logoColor=white

[product-screenshot]: https://github.com/michagrandel/filtertext/blob/main/doc/images/screenshot.png

[pypi-url]: https://pypi.org/project/filtertext/
[python-url]: https://python.org/
[issues-url]: https://github.com/michagrandel/filtertext/issues
[license-url]: https://github.com/michagrandel/filtertext/blob/master/LICENSE.md
[linkedin-url]: https://linkedin.com/in/michagrandel/en

[project-url]: https://github.com/michagrandel/filtertext
[codeofconduce-url]: https://opensource.guide/code-of-conduct/
[readme-url]: https://github.com/othneildrew/filtertext?search=1
[author-email]: mailto:hello@michagrandel.de
[doc-url]: https://github.com/michagrandel/filtertext/wiki
