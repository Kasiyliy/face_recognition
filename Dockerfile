FROM yuiti/python-dlib

RUN mkdir /face_recognition
COPY ./ /face_recognition

WORKDIR /face_recognition

RUN pip install face_recognition
RUN pip install pyTelegramBotAPI
RUN pip install --upgrade pyTelegramBotAPI

CMD ["python", "starter.py"]