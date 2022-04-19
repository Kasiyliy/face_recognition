FROM orgoro/dlib-opencv-python:3.7

RUN mkdir /face_recognition
COPY ./ /face_recognition

WORKDIR /face_recognition

RUN mkdir /pictures

RUN pip3 install face_recognition
RUN pip3 install pyTelegramBotAPI
RUN pip3 install --upgrade pyTelegramBotAPI

CMD ["python", "starter.py"]