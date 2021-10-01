# Milk-Boiling-Detection-and-Alert-System
Developed a classical Computer Vision algorithm to detect the boiling status of milk and provide timely alerts so that the stove can be turned off before the milk overflows.
The algorithm is as follows:
1) Perform operations such as thresholding and median blur to get a binary image where the milk's white colour is predominant
2) Detect the white contour of the milk
3) Find the contour area of the milk portion
4) If contour area goes above a certain threshold (which is determined by trial and error), give alert to turn off the stove.
5) Give appropriate alert messages for other possible contour areas also.

This is the output for your reference. Cheers!



![Output as gif](https://user-images.githubusercontent.com/70104287/135690365-f62ade6c-d091-4371-8971-0bca6ed1f21f.gif)
