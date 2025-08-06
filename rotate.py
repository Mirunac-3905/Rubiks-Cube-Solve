"""
Rubik's Cube Rotation Functions
This module contains all the rotation functions for manipulating the Rubik's cube state
"""

import cv2
import numpy as np
from datetime import datetime
import time

def rotate_face_clockwise(face):
    """Rotate a 3x3 face clockwise"""
    face = np.array(face).reshape(3, 3)
    rotated = np.rot90(face, -1)  # -1 for clockwise
    return rotated.flatten()

def rotate_face_counterclockwise(face):
    """Rotate a 3x3 face counterclockwise"""
    face = np.array(face).reshape(3, 3)
    rotated = np.rot90(face, 1)  # 1 for counterclockwise
    return rotated.flatten()

def show_instruction(video, videoWriter, instruction_text, duration=2):
    """Display instruction on screen for specified duration"""
    start_time = datetime.now()
    while True:
        if (datetime.now() - start_time).total_seconds() > duration:
            break
        
        is_ok, bgr_image_input = video.read()
        if not is_ok:
            break
            
        bgr_image_input = cv2.putText(bgr_image_input, instruction_text, (50, 50), 
                                    cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 3)
        videoWriter.write(bgr_image_input)
        cv2.imshow("Output Image", bgr_image_input)
        
        key_pressed = cv2.waitKey(1) & 0xFF
        if key_pressed == 27 or key_pressed == ord('q'):
            break

def right_cw(video, videoWriter, up_face, right_face, front_face, down_face, left_face, back_face):
    """Perform R (Right clockwise) move"""
    show_instruction(video, videoWriter, "Rotate RIGHT face CLOCKWISE", 2)
    
    # Rotate the right face clockwise
    new_right_face = rotate_face_clockwise(right_face)
    
    # Move edge pieces
    temp = [up_face[2], up_face[5], up_face[8]]
    
    new_up_face = up_face.copy()
    new_up_face[2] = front_face[2]
    new_up_face[5] = front_face[5]
    new_up_face[8] = front_face[8]
    
    new_front_face = front_face.copy()
    new_front_face[2] = down_face[2]
    new_front_face[5] = down_face[5]
    new_front_face[8] = down_face[8]
    
    new_down_face = down_face.copy()
    new_down_face[2] = back_face[6]
    new_down_face[5] = back_face[3]
    new_down_face[8] = back_face[0]
    
    new_back_face = back_face.copy()
    new_back_face[0] = temp[2]
    new_back_face[3] = temp[1]
    new_back_face[6] = temp[0]
    
    return [new_up_face, new_right_face, new_front_face, new_down_face, left_face, new_back_face]

def right_ccw(video, videoWriter, up_face, right_face, front_face, down_face, left_face, back_face):
    """Perform R' (Right counterclockwise) move"""
    show_instruction(video, videoWriter, "Rotate RIGHT face COUNTER-CLOCKWISE", 2)
    
    # Rotate the right face counterclockwise
    new_right_face = rotate_face_counterclockwise(right_face)
    
    # Move edge pieces (opposite of clockwise)
    temp = [up_face[2], up_face[5], up_face[8]]
    
    new_up_face = up_face.copy()
    new_up_face[2] = back_face[6]
    new_up_face[5] = back_face[3]
    new_up_face[8] = back_face[0]
    
    new_back_face = back_face.copy()
    new_back_face[0] = down_face[8]
    new_back_face[3] = down_face[5]
    new_back_face[6] = down_face[2]
    
    new_down_face = down_face.copy()
    new_down_face[2] = front_face[2]
    new_down_face[5] = front_face[5]
    new_down_face[8] = front_face[8]
    
    new_front_face = front_face.copy()
    new_front_face[2] = temp[0]
    new_front_face[5] = temp[1]
    new_front_face[8] = temp[2]
    
    return [new_up_face, new_right_face, new_front_face, new_down_face, left_face, new_back_face]

def left_cw(video, videoWriter, up_face, right_face, front_face, down_face, left_face, back_face):
    """Perform L (Left clockwise) move"""
    show_instruction(video, videoWriter, "Rotate LEFT face CLOCKWISE", 2)
    
    # Rotate the left face clockwise
    new_left_face = rotate_face_clockwise(left_face)
    
    # Move edge pieces
    temp = [up_face[0], up_face[3], up_face[6]]
    
    new_up_face = up_face.copy()
    new_up_face[0] = back_face[8]
    new_up_face[3] = back_face[5]
    new_up_face[6] = back_face[2]
    
    new_back_face = back_face.copy()
    new_back_face[2] = down_face[6]
    new_back_face[5] = down_face[3]
    new_back_face[8] = down_face[0]
    
    new_down_face = down_face.copy()
    new_down_face[0] = front_face[0]
    new_down_face[3] = front_face[3]
    new_down_face[6] = front_face[6]
    
    new_front_face = front_face.copy()
    new_front_face[0] = temp[0]
    new_front_face[3] = temp[1]
    new_front_face[6] = temp[2]
    
    return [new_up_face, right_face, new_front_face, new_down_face, new_left_face, new_back_face]

def left_ccw(video, videoWriter, up_face, right_face, front_face, down_face, left_face, back_face):
    """Perform L' (Left counterclockwise) move"""
    show_instruction(video, videoWriter, "Rotate LEFT face COUNTER-CLOCKWISE", 2)
    
    # Rotate the left face counterclockwise
    new_left_face = rotate_face_counterclockwise(left_face)
    
    # Move edge pieces (opposite of clockwise)
    temp = [up_face[0], up_face[3], up_face[6]]
    
    new_up_face = up_face.copy()
    new_up_face[0] = front_face[0]
    new_up_face[3] = front_face[3]
    new_up_face[6] = front_face[6]
    
    new_front_face = front_face.copy()
    new_front_face[0] = down_face[0]
    new_front_face[3] = down_face[3]
    new_front_face[6] = down_face[6]
    
    new_down_face = down_face.copy()
    new_down_face[0] = back_face[8]
    new_down_face[3] = back_face[5]
    new_down_face[6] = back_face[2]
    
    new_back_face = back_face.copy()
    new_back_face[2] = temp[2]
    new_back_face[5] = temp[1]
    new_back_face[8] = temp[0]
    
    return [new_up_face, right_face, new_front_face, new_down_face, new_left_face, new_back_face]

def front_cw(video, videoWriter, up_face, right_face, front_face, down_face, left_face, back_face):
    """Perform F (Front clockwise) move"""
    show_instruction(video, videoWriter, "Rotate FRONT face CLOCKWISE", 2)
    
    # Rotate the front face clockwise
    new_front_face = rotate_face_clockwise(front_face)
    
    # Move edge pieces
    temp = [up_face[6], up_face[7], up_face[8]]
    
    new_up_face = up_face.copy()
    new_up_face[6] = left_face[8]
    new_up_face[7] = left_face[5]
    new_up_face[8] = left_face[2]
    
    new_left_face = left_face.copy()
    new_left_face[2] = down_face[0]
    new_left_face[5] = down_face[1]
    new_left_face[8] = down_face[2]
    
    new_down_face = down_face.copy()
    new_down_face[0] = right_face[6]
    new_down_face[1] = right_face[3]
    new_down_face[2] = right_face[0]
    
    new_right_face = right_face.copy()
    new_right_face[0] = temp[0]
    new_right_face[3] = temp[1]
    new_right_face[6] = temp[2]
    
    return [new_up_face, new_right_face, new_front_face, new_down_face, new_left_face, back_face]

def front_ccw(video, videoWriter, up_face, right_face, front_face, down_face, left_face, back_face):
    """Perform F' (Front counterclockwise) move"""
    show_instruction(video, videoWriter, "Rotate FRONT face COUNTER-CLOCKWISE", 2)
    
    # Rotate the front face counterclockwise
    new_front_face = rotate_face_counterclockwise(front_face)
    
    # Move edge pieces (opposite of clockwise)
    temp = [up_face[6], up_face[7], up_face[8]]
    
    new_up_face = up_face.copy()
    new_up_face[6] = right_face[0]
    new_up_face[7] = right_face[3]
    new_up_face[8] = right_face[6]
    
    new_right_face = right_face.copy()
    new_right_face[0] = down_face[2]
    new_right_face[3] = down_face[1]
    new_right_face[6] = down_face[0]
    
    new_down_face = down_face.copy()
    new_down_face[0] = left_face[2]
    new_down_face[1] = left_face[5]
    new_down_face[2] = left_face[8]
    
    new_left_face = left_face.copy()
    new_left_face[2] = temp[2]
    new_left_face[5] = temp[1]
    new_left_face[8] = temp[0]
    
    return [new_up_face, new_right_face, new_front_face, new_down_face, new_left_face, back_face]

def up_cw(video, videoWriter, up_face, right_face, front_face, down_face, left_face, back_face):
    """Perform U (Up clockwise) move"""
    show_instruction(video, videoWriter, "Rotate UP face CLOCKWISE", 2)
    
    # Rotate the up face clockwise
    new_up_face = rotate_face_clockwise(up_face)
    
    # Move edge pieces
    temp = [front_face[0], front_face[1], front_face[2]]
    
    new_front_face = front_face.copy()
    new_front_face[0] = right_face[0]
    new_front_face[1] = right_face[1]
    new_front_face[2] = right_face[2]
    
    new_right_face = right_face.copy()
    new_right_face[0] = back_face[0]
    new_right_face[1] = back_face[1]
    new_right_face[2] = back_face[2]
    
    new_back_face = back_face.copy()
    new_back_face[0] = left_face[0]
    new_back_face[1] = left_face[1]
    new_back_face[2] = left_face[2]
    
    new_left_face = left_face.copy()
    new_left_face[0] = temp[0]
    new_left_face[1] = temp[1]
    new_left_face[2] = temp[2]
    
    return [new_up_face, new_right_face, new_front_face, down_face, new_left_face, new_back_face]

def up_ccw(video, videoWriter, up_face, right_face, front_face, down_face, left_face, back_face):
    """Perform U' (Up counterclockwise) move"""
    show_instruction(video, videoWriter, "Rotate UP face COUNTER-CLOCKWISE", 2)
    
    # Rotate the up face counterclockwise
    new_up_face = rotate_face_counterclockwise(up_face)
    
    # Move edge pieces (opposite of clockwise)
    temp = [front_face[0], front_face[1], front_face[2]]
    
    new_front_face = front_face.copy()
    new_front_face[0] = left_face[0]
    new_front_face[1] = left_face[1]
    new_front_face[2] = left_face[2]
    
    new_left_face = left_face.copy()
    new_left_face[0] = back_face[0]
    new_left_face[1] = back_face[1]
    new_left_face[2] = back_face[2]
    
    new_back_face = back_face.copy()
    new_back_face[0] = right_face[0]
    new_back_face[1] = right_face[1]
    new_back_face[2] = right_face[2]
    
    new_right_face = right_face.copy()
    new_right_face[0] = temp[0]
    new_right_face[1] = temp[1]
    new_right_face[2] = temp[2]
    
    return [new_up_face, new_right_face, new_front_face, down_face, new_left_face, new_back_face]

def down_cw(video, videoWriter, up_face, right_face, front_face, down_face, left_face, back_face):
    """Perform D (Down clockwise) move"""
    show_instruction(video, videoWriter, "Rotate DOWN face CLOCKWISE", 2)
    
    # Rotate the down face clockwise
    new_down_face = rotate_face_clockwise(down_face)
    
    # Move edge pieces
    temp = [front_face[6], front_face[7], front_face[8]]
    
    new_front_face = front_face.copy()
    new_front_face[6] = left_face[6]
    new_front_face[7] = left_face[7]
    new_front_face[8] = left_face[8]
    
    new_left_face = left_face.copy()
    new_left_face[6] = back_face[6]
    new_left_face[7] = back_face[7]
    new_left_face[8] = back_face[8]
    
    new_back_face = back_face.copy()
    new_back_face[6] = right_face[6]
    new_back_face[7] = right_face[7]
    new_back_face[8] = right_face[8]
    
    new_right_face = right_face.copy()
    new_right_face[6] = temp[0]
    new_right_face[7] = temp[1]
    new_right_face[8] = temp[2]
    
    return [up_face, new_right_face, new_front_face, new_down_face, new_left_face, new_back_face]

def down_ccw(video, videoWriter, up_face, right_face, front_face, down_face, left_face, back_face):
    """Perform D' (Down counterclockwise) move"""
    show_instruction(video, videoWriter, "Rotate DOWN face COUNTER-CLOCKWISE", 2)
    
    # Rotate the down face counterclockwise
    new_down_face = rotate_face_counterclockwise(down_face)
    
    # Move edge pieces (opposite of clockwise)
    temp = [front_face[6], front_face[7], front_face[8]]
    
    new_front_face = front_face.copy()
    new_front_face[6] = right_face[6]
    new_front_face[7] = right_face[7]
    new_front_face[8] = right_face[8]
    
    new_right_face = right_face.copy()
    new_right_face[6] = back_face[6]
    new_right_face[7] = back_face[7]
    new_right_face[8] = back_face[8]
    
    new_back_face = back_face.copy()
    new_back_face[6] = left_face[6]
    new_back_face[7] = left_face[7]
    new_back_face[8] = left_face[8]
    
    new_left_face = left_face.copy()
    new_left_face[6] = temp[0]
    new_left_face[7] = temp[1]
    new_left_face[8] = temp[2]
    
    return [up_face, new_right_face, new_front_face, new_down_face, new_left_face, new_back_face]

def turn_to_right(video, videoWriter, up_face, right_face, front_face, down_face, left_face, back_face):
    """Turn the entire cube to the right (for accessing back face)"""
    show_instruction(video, videoWriter, "Turn cube to RIGHT", 2)
    
    # Rotate the entire cube right: F->R, R->B, B->L, L->F
    new_front_face = left_face
    new_right_face = front_face
    new_back_face = right_face
    new_left_face = back_face
    
    return [up_face, new_right_face, new_front_face, down_face, new_left_face, new_back_face]

def turn_to_front(video, videoWriter, up_face, right_face, front_face, down_face, left_face, back_face):
    """Turn the entire cube back to front (opposite of turn_to_right)"""
    show_instruction(video, videoWriter, "Turn cube to FRONT", 2)
    
    # Rotate the entire cube left: F->L, L->B, B->R, R->F
    new_front_face = right_face
    new_right_face = back_face
    new_back_face = left_face
    new_left_face = front_face
    
    return [up_face, new_right_face, new_front_face, down_face, new_left_face, new_back_face]

def turn_to_left(video, videoWriter, up_face, right_face, front_face, down_face, left_face, back_face):
    """Turn the entire cube to the left"""
    show_instruction(video, videoWriter, "Turn cube to LEFT", 2)
    
    # Rotate the entire cube left: F->L, L->B, B->R, R->F
    new_front_face = right_face
    new_right_face = back_face
    new_back_face = left_face
    new_left_face = front_face
    
    return [up_face, new_right_face, new_front_face, down_face, new_left_face, new_back_face]

def turn_up(video, videoWriter, up_face, right_face, front_face, down_face, left_face, back_face):
    """Turn the entire cube up"""
    show_instruction(video, videoWriter, "Turn cube UP", 2)
    
    # Rotate the entire cube up: F->U, U->B, B->D, D->F
    new_up_face = front_face
    new_front_face = down_face
    new_down_face = back_face
    new_back_face = up_face
    
    return [new_up_face, right_face, new_front_face, new_down_face, left_face, new_back_face]

def turn_down(video, videoWriter, up_face, right_face, front_face, down_face, left_face, back_face):
    """Turn the entire cube down"""
    show_instruction(video, videoWriter, "Turn cube DOWN", 2)
    
    # Rotate the entire cube down: F->D, D->B, B->U, U->F
    new_up_face = back_face
    new_front_face = up_face
    new_down_face = front_face
    new_back_face = down_face
    
    return [new_up_face, right_face, new_front_face, new_down_face, left_face, new_back_face]