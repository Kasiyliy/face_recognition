FROM m03geek/opencv-dlib:alpine-19.8


RUN mkdir /face_recognition
COPY ./ /face_recognition

WORKDIR /face_recognition

RUN mkdir /pictures

RUN pip3 install face_recognition
RUN pip3 install pyTelegramBotAPI
RUN pip3 install --upgrade pyTelegramBotAPI

CMD ["python", "starter.py"]