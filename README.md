<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->

<a name="readme-top"></a>

<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->

<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/SeifEleslam/AirBnB_clone">
    <img src="images/logo.png" alt="Logo" width="160" height="80">
  </a>

<h1 align="center">AirBnB Clone</h1>

  <p align="center">
    Cloning AirBnB website As Part of My full stack journey
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <!-- <li><a href="#license">License</a></li> -->
    <li><a href="#contact">Contact</a></li>
    <!-- <li><a href="#acknowledgments">Acknowledgments</a></li> -->
  </ol>
</details>

<!-- ABOUT THE PROJECT -->

## About The Project

The project is a clone of the AirBnB. It aims to help me practice all the full stack skills.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Built With

[![Python][Python]][Python-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->

## Getting Started

This project was built using python3. For everything to work correctly please install python in your machine

### Prerequisites

Make Sure you have Python3 installed in your machine

Python 3

```sh
python3 --version
```

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/SeifEleslam/AirBnB_clone.git
   ```
2. Go to repo directory
   ```sh
   cd AirBnB_clone
   ```
3. Run Console as root
   ```sh
   sudo ./console.py
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->

## Usage

The Frontend of the project is not available yet. For now you can play with the console to create, read, update, and delete data.

### Classes List

- **BaseModel**
- **User**
- **Amenity**
- **City**
- **Place**
- **Review**
- **State**

### Commands List

- **create** : Create Instance of a Class [args: class_name], examples:

  ```sh
  create User
  ```

  ```sh
  User.create()
  ```

- **count** : Count all existing Instances of a Class [args: class_name], examples:

  ```sh
  User.count()
  ```

- **all** : Show all created Instances of a Class or all classes [args?: class_name], examples:

  ```sh
  all
  ```

  ```sh
  User.all()
  ```

- **show** : Show an instance with id [args: class_name, id], examples:

  ```sh
  show User 123
  ```

  ```sh
  User.show(123)
  ```

- **destroy** : Destroy an instance with id [args: class_name, id], examples:

  ```sh
  destroy User 123
  ```

  ```sh
  User.destroy(123)
  ```

- **update** : Update an instance attribute value with id

  - Formula 1 [args: class_name, id, attribute_name, value], examples:

    ```sh
    update User 123 name "sa3d"
    ```

    ```sh
    User.update(123, name, "sa3d")
    ```

  - Formula 2 [args: class_name, id, dict], examples:

    ```sh
    User.update(123, {"name":"sa3d", "age": 89})
    ```

  <p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ROADMAP -->

## Roadmap

- Models : to implement project data structures
- Storage : to store data in JSON file
- Console : to play with data using shell commands **-- current --**
- Frontend: to interact with backend using well designed UI
- Backend : to add functionality to the models and handle them
- API : to create bridge between Frontend and Backend

See the [open issues](https://github.com/SeifEleslam/AirBnB_clone/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTRIBUTING -->

## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- LICENSE -->

## Contact

SeifEleslam Gouda - [@_SeifEleslam_](https://twitter.com/_SeifEleslam_) - seifeleslamgouda@gmail.com

Project Link: [https://github.com/SeifEleslam/AirBnB_clone](https://github.com/SeifEleslam/AirBnB_clone)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ACKNOWLEDGMENTS

## Acknowledgments

- []()
- []()
- []()

<p align="right">(<a href="#readme-top">back to top</a>)</p> -->

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[contributors-shield]: https://img.shields.io/github/contributors/SeifEleslam/AirBnB_clone.svg?style=for-the-badge
[contributors-url]: https://github.com/SeifEleslam/AirBnB_clone/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/SeifEleslam/AirBnB_clone.svg?style=for-the-badge
[forks-url]: https://github.com/SeifEleslam/AirBnB_clone/network/members
[stars-shield]: https://img.shields.io/github/stars/SeifEleslam/AirBnB_clone.svg?style=for-the-badge
[stars-url]: https://github.com/SeifEleslam/AirBnB_clone/stargazers
[issues-shield]: https://img.shields.io/github/issues/SeifEleslam/AirBnB_clone.svg?style=for-the-badge
[issues-url]: https://github.com/SeifEleslam/AirBnB_clone/issues
[license-shield]: https://img.shields.io/github/license/SeifEleslam/AirBnB_clone.svg?style=for-the-badge
[license-url]: https://github.com/SeifEleslam/AirBnB_clone/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/seifeleslam-gouda
[product-screenshot]: images/screenshot.png
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Python-url]: https://python.org/
[Python]: https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54
