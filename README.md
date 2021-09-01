# Photo Pixelator

Program that converts a .jpeg/.jpg image into pixel art.

The input image is broken into N x N squares, where N is the user input for pixel size. Within each square, the average RGB value is computed using the RGB values of the individual pixels. Using a predesigned color palette of RGB values, the program calculates the standard error between the average RGB value of a square and every RGB value in the palette. The color from the palette with the lowest error is used for the entire N x N square.

# Website
You can try out our program here: <br>
http://wlnguyen.pythonanywhere.com/

# Pixelation Examples

Original                   |  Pixel Size: 8
:-------------------------:|:-------------------------:
<img src="https://user-images.githubusercontent.com/52009450/131593165-25495d8e-fa46-4034-9c07-9dc47e1483b2.jpeg" width = "600">  |  <img src="https://user-images.githubusercontent.com/52009450/131593329-ca46744c-7d6c-4eb2-aa2c-57828f8e0faf.jpeg" width = "600">
**Pixel Size: 16**         |  **Pixel Size: 32**
<img src="https://user-images.githubusercontent.com/52009450/131595716-a25d87db-a455-4727-a862-41f1b137f043.jpeg" width = "600">  |  <img src="https://user-images.githubusercontent.com/52009450/131595736-b6ad7ffa-ee44-4dbb-b9fe-ce1c67a87657.jpeg" width = "600">

<br>

Original                   |  Pixel Size: 8
:-------------------------:|:-------------------------:
<img src="https://user-images.githubusercontent.com/52009450/131595886-21118755-af8d-4f57-ada7-4d4a5889ce73.jpeg" width = "600" >  |  <img src="https://user-images.githubusercontent.com/52009450/131595923-97d01f5b-665e-4bd3-9573-05615aa043d9.jpeg" width = "600">
**Pixel Size: 16**         |  **Pixel Size: 32**
<img src="https://user-images.githubusercontent.com/52009450/131595955-823a8424-0ec4-4d17-87b9-3728db5f1644.jpeg" width = "600" >  |  <img src="https://user-images.githubusercontent.com/52009450/131595975-22f6ac53-e3c5-4c0a-919b-546aeaed4340.jpeg" width = "600">

# Future Improvements
In the future, we would like to improve the Photo Pixelator by:
- Adding a loading icon
- Making pixelation more accurate
- Making the website mobile-friendly
- Allowing users to choose a color palette

# Creators
Jonny Tran and Wesley Nguyen
