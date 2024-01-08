import sys

import cv2
import threading
import time

from PySide6.QtWidgets import QGridLayout, QVBoxLayout, QHBoxLayout, QLabel, QWidget
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtCore import QThread, Qt, Signal


class CameraBufferCleanerThread(threading.Thread):
    def __init__(self, camera, name='camera-buffer-cleaner-thread'):
        self.camera = camera
        self.thread_active = False
        self.last_frame = None
        super(CameraBufferCleanerThread, self).__init__()
        # self.start()

    def run(self, camera):
        while True:
            if self.thread_active:
                try:
                    ret, self.last_frame = camera.read()
                except:
                    print(camera)
                    pass


class CameraThread(QThread):
    ImageUpdate = Signal(QImage)

    def __init__(self, parent=None, cam_cleaner=None):
        super(CameraThread, self).__init__(parent)

        self.ThreadActive = False
        self.cam_cleaner = cam_cleaner
        self.frame_height, self.frame_width = 480, 640
        self.rect_width = int(self.frame_width * 0.3)
        self.rect_height = int(self.frame_height * 0.3)
        self.rect_x = (self.frame_width - self.rect_width) // 2
        self.rect_y = self.frame_height - self.rect_height
        self.cross_center_x = self.rect_x + self.rect_width // 2
        self.cross_center_y = self.rect_y + self.rect_height // 2
        self.current_x = self.cross_center_x
        self.current_y = self.cross_center_y

        # Rectangle settings
        self.rectangle_color = (0, 255, 0)  # Color of the rectangle (green in BGR format)
        self.thickness = 2

        # Cross settings
        self.cross_length = 5
        self.cross_thickness = 2

        self.label_font = cv2.FONT_HERSHEY_SIMPLEX
        self.label_scale = 0.5
        self.label_color = (0, 255, 0)  # Color of the labels (white in BGR format)
        self.label_thickness = 1

    def run(self):
        self.ThreadActive = True

        while True:
            if self.ThreadActive:
                if self.cam_cleaner.last_frame is not None:

                    image = cv2.cvtColor(self.cam_cleaner.last_frame, cv2.COLOR_BGR2RGB)
                    convertToQtFormat = QImage(image.data, image.shape[1], image.shape[0], QImage.Format_RGB888)
                    pic = convertToQtFormat.scaled(640, 480, Qt.KeepAspectRatio)
                    self.ImageUpdate.emit(pic)

    def disconnect_camera_thread(self):
        self.ThreadActive = False
        self.cam_cleaner.thread_active = False

    def connect_camera_thread(self):
        self.ThreadActive = True
        self.cam_cleaner.thread_active = True

    def display_rectangle(self, frame):
        cv2.rectangle(frame, (self.rect_x, self.rect_y),
                      (self.rect_x + self.rect_width, self.rect_y + self.rect_height),
                      self.rectangle_color, self.thickness)

    def display_cross(self,cross_position_x,cross_position_y ,frame):
        cv2.line(frame, (cross_position_x - self.cross_length, cross_position_y),
                 (cross_position_x + self.cross_length, cross_position_y), self.rectangle_color,
                 self.cross_thickness)
        cv2.line(frame, (cross_position_x, cross_position_y - self.cross_length),
                 (cross_position_x, cross_position_y + self.cross_length), self.rectangle_color,
                 self.cross_thickness)

    def updateCrossPosition(self, x, y):
        # Calculate the position of the cross based on x and y inputs
        self.current_x +=round(x/10)
        self.current_y -=round(y/20)

        if self.current_x < self.rect_x:
            self.current_x = self.rect_x
        elif self.current_x > self.rect_x + self.rect_width:
            self.current_x = self.rect_x + self.rect_width

        if self.current_y < self.rect_y:
            self.current_y = self.rect_y
        elif self.current_y > self.rect_y + self.rect_height:
            self.current_y = self.rect_y + self.rect_height
        print(self.current_x,self.current_y)


        # self.display_cross(self.current_x,self.current_y,self.cam_cleaner.last_frame)

    def dispplayLabel(self, frame):
        left_label_text = '-90'
        left_label_position = (self.rect_x - 40, self.rect_y + self.rect_height // 2 + 5)
        cv2.putText(frame, left_label_text, left_label_position, self.label_font, self.label_scale,
                    self.label_color,
                    self.label_thickness)

        # Label text and position for right side
        right_label_text = '+90'
        right_label_position = (self.rect_x + self.rect_width + 10, self.rect_y + self.rect_height // 2 + 5)
        cv2.putText(frame, right_label_text, right_label_position, self.label_font,
                    self.label_scale, self.label_color,
                    self.label_thickness)

    def updateDotPosition(self, x, y, frame_width, frame_height):
        # Calculate the position of the dot based on x and y inputs
        dot_x = int(frame_width * x)
        dot_y = int(frame_height * y)

        return dot_x, dot_y


class CameraWidget(QWidget):
    def __init__(self,initial_image=None):
        super(CameraWidget, self).__init__()
        self.image = initial_image
        try:
            self.camera = cv2.VideoCapture("http://25.59.215.144:8000/stream.mjpg")
        except:
            print("Camera not found")
            self.camera = None

        self.cam_cleaner = CameraBufferCleanerThread(self.camera)

        self.camera_thread = CameraThread(cam_cleaner=self.cam_cleaner)
        self.camera_thread.ImageUpdate.connect(self.ImageUpdateSlot)

        self.VBL = QVBoxLayout()
        self.video = QLabel()

        self.setContentsMargins(0, 0, 0, 0)

        self.pic = QPixmap("black.jpg")
        self.video.setPixmap(self.pic)
        self.VBL.addWidget(self.video)
        self.setLayout(self.VBL)
        self.show()
        # self.layout.addLayout(self.VBL, 1, 0)

        # self.cam_cleaner.start()
        # self.camera_thread.start()

    def ImageUpdateSlot(self, Image):
        self.video.setPixmap(QPixmap.fromImage(Image))

    def connect_camera(self):
        self.camera = cv2.VideoCapture("http://25.59.215.144:8000/stream.mjpg")
        self.camera_thread.connect_camera_thread()

    def disconnect_camera(self):
        self.video.setPixmap(self.pic)
        self.show()
        self.camera_thread.disconnect_camera_thread()
        self.camera = None


