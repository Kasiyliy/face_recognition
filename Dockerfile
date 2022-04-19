FROM orgoro/dlib-opencv-python:3.7

RUN mkdir /face_recognition
COPY ./ /face_recognition

WORKDIR /face_recognition

RUN mkdir /pictures

RUN pip install face_recognition
RUN pip install pyTelegramBotAPI
RUN pip install --upgrade pyTelegramBotAPI

ENTRYPOINT ["tail", "-f", "/dev/null"]
