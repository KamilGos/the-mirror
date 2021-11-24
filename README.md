<!-- image -->
<div align="center" id="top"> 
  <img src=images/themirror.jpg width="300" />
  &#xa0;
</div>

<h1 align="center"> the-mirror </h1>
<h2 align="center"> Robot that repeat human facial expression </h2>

<!-- https://shields.io/ -->
<p align="center">
  <img alt="Top language" src="https://img.shields.io/badge/Language-Python-yellow?style=for-the-badge&logo=python">
  <img alt="Status" src="https://img.shields.io/badge/Status-done-green?style=for-the-badge">
  <img alt="Code size" src="https://img.shields.io/github/languages/code-size/KamilGos/the-mirror?style=for-the-badge">
</p>

<!-- table of contents -->
<p align="center">
  <a href="#dart-about">About</a> &#xa0; | &#xa0;
  <a href="#package-content">Content</a> &#xa0; | &#xa0;
  <a href="#checkered_flag-starting">Starting</a> &#xa0; | &#xa0;
  <a href="#eyes-implementation">Implementation</a> &#xa0; | &#xa0;
  <a href="#microscope-tests">Tests</a> &#xa0; | &#xa0;
  <a href="#memo-license">License</a> &#xa0; | &#xa0;
  <a href="#technologist-author">Author</a> &#xa0; | &#xa0;
</p>

<br>

## :dart: About ##
The Mirror is a robot that uses image processing to transform human facial expressions into the corresponding movement of servos mounted on the model. 


## :package: Content
 * []()
 * []()

## :checkered_flag: Starting ##
```bash
# Clone this project
$ git clone https://github.com/KamilGos/the-mirror

# Access
$ cd the-mirror

# Run the project
$ sudo python3 main.py
```

## :eyes: Implementation ##
The "opencv" and "dlib" libraries were used as part of the image processing algorithm. The image is taken from a webcam, then a face is detected in the image. The next step is to add 68 characteristic points to the detected face (search for: "Face landmarks"). The last module of the algorithm focuses on using trigonometric relationships and proportions to determine the level of smile and whether the person's eyes are open or closed at a given moment. Then the results are mapped and sent via Serial (Virtual COM) to the STM32 microcontroller (the so-called "Blue pill"). There, the values are remapped to be able to use the PWM signal to control the servos. 

<h2>Mechanical part</h2>
Robot was designed using Autodesc Inventor. The neccesery parts were 3D printed or cut from plexiglass.

<h2>Presentation</h2>




## :microscope: Tests ##

## :memo: License ##

This project is under license from MIT.

## :technologist: Author ##

Made with :heart: by <a href="https://github.com/KamilGos" target="_blank">Kamil Goś</a>

&#xa0;

<a href="#top">Back to top</a>



<!-- ADDONS -->
<!-- images -->
<!-- <h2 align="left">1. Mechanics </h2>
<div align="center" id="inventor"> 
  <img src=images/model_1.png width="230" />
  <img src=images/model_2.png width="236" />
  <img src=images/model_3.png width="228" />
  &#xa0;
</div> -->

<!-- one image -->
<!-- <h2 align="left">2. Electronics </h1>
<div align="center" id="electronics"> 
  <img src=images/electronics.png width="500" />
  &#xa0;
</div> -->


<!-- project dockerized -->
<!-- <div align="center" id="status"> 
  <img src="https://www.docker.com/sites/default/files/d8/styles/role_icon/public/2019-07/Moby-logo.png" alt="simulator" width="75" style="transform: scaleX(-1);"/>
   <font size="6"> Project dockerized</font> 
  <img src="https://www.docker.com/sites/default/files/d8/styles/role_icon/public/2019-07/Moby-logo.png" alt="simulator" width="75"/>
  &#xa0;
</div>
<h1 align="center"> </h1> -->