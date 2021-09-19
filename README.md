# Photo Pixelator
A website for converting images into pixel art.

The input image is broken into squares of N x N pixels, where N is the pixel size provided by the user. Within each square, the average RGB value is computed using the RGB values of the individual pixels. From a predesigned color palette of 64 colors, the nearest color is found and assigned to each square. The result is a pixel art version of the original image.

# Website
You can check out our website here: <br>
https://wlnguyen.pythonanywhere.com

# Pixelation Examples
Original                   |  Pixel Size: 8
:-------------------------:|:-------------------------:
<img src="https://user-images.githubusercontent.com/61168867/132125796-b39cebf0-7804-468d-adbc-1caab2e8d0fd.jpg" width = "600">  |  <img src="https://user-images.githubusercontent.com/61168867/132125770-4ffcda56-52ca-48f2-9ebd-0c27c041d4f6.jpg" width = "600">
**Pixel Size: 16**         |  **Pixel Size: 32**
<img src="https://user-images.githubusercontent.com/61168867/132125818-4d8f5f62-773e-460e-a670-b018ee8d664e.jpg" width = "600">  |  <img src="https://user-images.githubusercontent.com/61168867/132125841-dafa7998-888c-4020-8bf6-d021ecf77914.jpg" width = "600">

<br>

Original                   |  Pixel Size: 8
:-------------------------:|:-------------------------:
<img src="https://user-images.githubusercontent.com/61168867/132125910-78e845e7-f61d-420f-8d8f-9395e11a22f9.jpg" width = "600">  |  <img src="https://user-images.githubusercontent.com/61168867/132125891-bff134a3-0617-49d6-8ed0-eff48c2536b7.jpg" width = "600">
**Pixel Size: 16**         |  **Pixel Size: 32**
<img src="https://user-images.githubusercontent.com/61168867/132125903-c9269ce8-2856-4ca6-a174-06bd4fa4f31a.jpg" width = "600">  |  <img src="https://user-images.githubusercontent.com/61168867/132125918-7fbbcf72-d1ee-4b87-b3a2-4894ca3c32c4.jpg" width = "600">

# Future Improvements
In the future, we would like to improve the Photo Pixelator by:
- Adding a loading animation
- Implementing drag-and-drop uploading
- Showing a before and after image comparison
- Giving users the option to choose from several color palettes

# Creators
Jonny Tran and Wesley Nguyen
