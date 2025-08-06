<<<<<<< HEAD
Rubiks-Solve 

This project concentrates on solving a unsolved Rubik's Cube. The program contains OpenCV libraries and when executed will show a live video from the webcam. When a unsolved Rubik's cube is shown in front of a camera, it will scan the faces of the Rubik's cube. These instructions will be displayed along with the live video in a text format. After a successful scan the program will start to give the instructions on the moves to be made using Augmented arrow on the cube in the live video. When these moves are followed we get the end product of a solved Rubik's Cube within 30 moves.

# RubiksCube
1.  Create an virtual environment using
	```
	$ python3 -m venv  virtual environment name.
	```
2.  Run 
	```
	$ pip3 install -r requirements.txt
	```
3.  Run
	```
	$ python3 main.py
	```
	
=======
# Rubik's Cube Solver

A computer vision-based Rubik's Cube solver that uses OpenCV for cube detection and a custom implementation of the Kociemba algorithm for solving.

## Features

- **Real-time Cube Detection**: Uses computer vision to detect and analyze Rubik's cube faces through webcam
- **Color Recognition**: Automatically identifies cube colors and face configurations
- **Hybrid Solver**: Combines Python and C++ implementations for optimal performance
- **Visual Guidance**: Provides on-screen instructions for cube rotations
- **Video Recording**: Records the solving process to an output video file

## Requirements

- Python 3.7+
- Webcam/Camera
- C++ compiler (optional, for performance optimization)

## Installation

### 1. Clone or Download the Project

```bash
cd RubiksCubeSolver
```

### 2. Create Virtual Environment

```bash
python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Optional: Install C++ Compiler

For better performance, install a C++ compiler:

**Windows:**
- Install Visual Studio Build Tools or MinGW

**macOS:**
```bash
xcode-select --install
```

**Linux (Ubuntu/Debian):**
```bash
sudo apt-get install build-essential
```

## Usage

### Basic Usage

1. **Connect your webcam** and ensure it's working
2. **Run the program**:
   ```bash
   python main.py
   ```

3. **Follow the on-screen instructions**:
   - Show each face of the cube to the camera when prompted
   - Hold the cube steady until the face is detected (9 squares should be highlighted)
   - Follow the sequence: Front → Top → Down → Right → Left → Back

4. **Cube solving**:
   - Once all faces are scanned, the algorithm will calculate the solution
   - Follow the on-screen rotation instructions
   - The program will guide you through each move

### Controls

- **ESC** or **Q**: Quit the program at any time
- **Camera view**: Shows the detected squares in yellow outlines
- **Text instructions**: Displayed at the top of the screen

## File Structure

```
RubiksCubeSolver/
├── main.py                 # Main program file
├── rotate.py              # Cube rotation functions
├── kociemba_solver.py     # Custom Kociemba algorithm implementation
├── requirements.txt       # Python dependencies
├── README.md             # This file
└── OUTPUT5.avi           # Generated video output (after running)
```

## How It Works

### 1. Face Detection (`detect_face` function)
- Converts camera input to grayscale
- Uses morphological operations to clean the image
- Applies adaptive thresholding
- Finds contours representing cube squares
- Analyzes color values (BGR) to identify cube colors

### 2. Color Classification
The system identifies 6 cube colors:
- **White**: High values in all BGR channels
- **Yellow**: High blue and green, lower red
- **Orange**: Highest in blue channel
- **Green**: Highest in green channel
- **Blue**: Highest in red channel, low green/blue
- **Red**: High red and blue, low green

### 3. Cube Solving Algorithm
- Uses a custom implementation of Kociemba's algorithm
- Attempts to use C++ solver for performance (falls back to Python)
- Generates move sequences: R, L, F, B, U, D (with ', 2 modifiers)

### 4. Move Execution
- Translates algorithm moves to physical rotations
- Provides visual guidance for each move
- Updates internal cube state representation

## Troubleshooting

### Camera Issues
- **"Cannot read video source"**: Check if webcam is connected and not used by another application
- **Poor detection**: Ensure good lighting and stable cube positioning
- **Wrong colors detected**: Adjust lighting conditions or cube positioning

### Installation Issues
- **OpenCV installation fails**: Try `pip install opencv-python-headless`
- **C++ compiler not found**: The program will work with Python-only solver
- **Permission errors**: Run terminal as administrator (Windows) or use `sudo` (Linux/macOS)

### Performance Issues
- **Slow detection**: Reduce camera resolution or improve lighting
- **Slow solving**: Ensure C++ compiler is available for performance optimization

## Cube Color Mapping

The program uses the following internal representation:
- 1: White
- 2: Yellow  
- 3: Orange
- 4: Green
- 5: Blue
- 6: Red

## Algorithm Details

The solver implements a simplified version of Kociemba's algorithm:

1. **Phase 1**: Cross formation
2. **Phase 2**: First Two Layers (F2L)
3. **Phase 3**: Orient Last Layer (OLL)
4. **Phase 4**: Permute Last Layer (PLL)

## Contributing

Feel free to contribute improvements:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## Known Limitations

- Lighting conditions significantly affect color detection
- Cube must be held steadily during face scanning
- Some color combinations may be difficult to distinguish
- C++ solver compilation may fail on some systems

## License

This project is open source. Feel free to use and modify as needed.

## Support

If you encounter issues:
1. Check the troubleshooting section above
2. Ensure all dependencies are properly installed
3. Verify your webcam is working with other applications
4. Check that you have proper lighting conditions

## Version History

- **v1.0**: Initial release with basic cube detection and solving
- **v1.1**: Added C++ solver integration for improved performance
- **v1.2**: Enhanced color detection and error handling
>>>>>>> 3bc2919 (Initial commit)
