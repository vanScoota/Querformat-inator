# Querformat-inator

This GIMP Python-Fu script adds horizontal borders to all portrait format images in a directory so that they become square.

## How to Use

1. Copy the file `Querformat-inator.py` to the following directory:  
   `C:\Users\<user>\AppData\Roaming\GIMP\2.10\plug-ins`
1. Launch GIMP.
1. Find the script here: `File` → `Create` → `Querformat-inator`
1. Select a directory, a border color and enter an image width maximum.
1. The script will create copies of all JPG and JPEG files in that directory.  
   If an image is in portrait format, the script will add colored borders to the left and right.
   All images wider than the entered maximum will be scaled to that width.
   
## Changelog

### [1.1.0] - 2021-04-17

#### Added
- Images wider than a entered maximum get scaled to that width.

### [1.0.0] - 2021-03-29

#### Added
- Initial release.
- Support for JPG and JPEG.
- Portrait format images get squared by adding a colored border.
