import face_recognition
import test
from models.faces import Faces
import telebot
import os
import os.path

TOKEN = '470340551:AAHWbCr5tRh4Eo8zNL8iDaUJ-_nOVBGwMQ8' # токен вашего бота, полученный от @BotFather

NAME = ''
NO_FACES = 0
PROBABLY_FACE = ''
def find(image , path):
    faces = face_recognition.load_image_file(path)
    known_image = face_recognition.face_encodings(faces)
    size = len(face_recognition.face_encodings(image))
    print(size)
    if (size > 0):
        unknown_image = face_recognition.face_encodings(image)[0]

        print(face_recognition.face_distance(known_image, unknown_image)[0] )
        distance =face_recognition.face_distance(known_image, unknown_image)[0]
        if(distance >= 0.435 and distance < 0.499):
            global PROBABLY_FACE
            PROBABLY_FACE = path
        if (distance < 0.435):
            return True
        else:
            return False
        return (face_recognition.compare_faces(known_image, unknown_image)[0])
    else:
        global NO_FACES
        NO_FACES = 1
        print("array size is equal to 0")
        return False


def recognize(image):
    paths = test.getPaths()

    for path in paths:

        if(NO_FACES == 1):
            break
        global NAME

        if(os.path.exists(path)):
            continue

        if( find(image , path)):

            NAME = (test.getNameByPath(path))
            return True
        else:
            global PROBABLY_FACE
            if(PROBABLY_FACE!=''):
                NAME = (test.getNameByPath(path))
                return True
    return False

def getImagePathById(message):
    raw = message.photo[-1].file_id
    path = '/pictures/' + raw + ".jpg"
    file_info = bot.get_file(raw)
    downloaded_file = bot.download_file(file_info.file_path)
    try:
        with open(path, 'wb') as new_file:
            new_file.write(downloaded_file)
        if not os.path.exists(path):
            return None
        image = face_recognition.load_image_file(path)
        if countFaces( image ) == 1 :
            return path
        elif countFaces(image) == 0 :
            bot.send_message(message.chat.id , "Sorry this is image is invalid, no faces found!")
        else:
            bot.send_message(message.chat.id , "Too many faces in one image!")
    except Exception as e:
        print("Error: " + str(e))

    os.remove(path)
    return None


def countFaces(image):

    size = len(face_recognition.face_encodings(image))
    print(size)
    if size > 0:
        return size
    else:
        return 0

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=["help"])
def handle_help(message):
    bot.send_message(message.chat.id,"Я могу делать много чего интересного но это в будущем! Пока что ты можешь говорить мне 'привет' и 'пока'")

@bot.message_handler(commands=["register_user"])
def handle_register_user(message):
    msg = bot.send_message(message.chat.id , "Введите полное имя человека:")
    bot.register_next_step_handler(msg , enterName)

def enterName(message):
    if message.text.lower() == '':
        bot.send_message(message.chat.id, "Error")
    else:
        global NAME
        NAME = message.text
        msg = bot.send_message(message.chat.id , "GREAT! Send me photo of that user! I am waiting!")
        bot.register_next_step_handler(msg , getImage)

def getImage(message):
    if message.photo!=None:
        path = getImagePathById(message)
        if(path!=None):
            a = Faces(1 , NAME, path , 1)
            test.add_face(a)
            bot.send_message(message.chat.id , 'SuccessFully added')
        else:
            print("Problem happened")
    else:
        print("This is not photo")

@bot.message_handler(commands=["start"])
def handle_start(message):
    bot.send_message(message.chat.id,
                     "Hey man! My name is Kasya.")
    user_markup = telebot.types.ReplyKeyboardMarkup(True , False)
    user_markup.row('/start' , '/stop' , '/register_user')
    user_markup.row('привет' ,'аудио' ,'фото')
    print(message.from_user.id)
    bot.send_message(message.from_user.id , 'Добро пожаловать..', reply_markup=user_markup)
    bot.send_message(message.from_user.id , 'Скиньте свое фото..', reply_markup=user_markup)


@bot.message_handler(content_types=["text"])
def handle_all_text(message):
    if(message.text.lower() is "привет"):
        bot.send_message(message.chat.id , "Привет ! Я бот Кася")
    elif (message.text.lower() == "пошел"):
        bot.send_message(message.chat.id, "Ты?!!")
    else:
        bot.send_message(message.chat.id , "Я не понимаю данную команду (")



@bot.message_handler(content_types=["photo"])
def handle_photo(message):
    bot.send_message(message.chat.id, "В обработке...Ожидайте)")
    raw = message.photo[-1].file_id
    path = raw + ".jpg"
    file_info = bot.get_file(raw)
    downloaded_file = bot.download_file(file_info.file_path)
    try:
        with open(path, 'wb') as new_file:
            new_file.write(downloaded_file)
        print(path)
        im = face_recognition.load_image_file(path)
        if(recognize(im)):
            global PROBABLY_FACE
            if(PROBABLY_FACE==''):
                bot.send_message(message.chat.id , 'This is ' + NAME )
            else:
                bot.send_message(message.chat.id, 'Maybe this is ' + NAME)
                PROBABLY_FACE = ''
        else:
            global NO_FACES
            if(NO_FACES == 1):
                NO_FACES = 0
                bot.send_message(message.chat.id , 'No faces in this photo')
            else:
                bot.send_message(message.chat.id , "Don't found!")
        os.remove(path)
    except Exception as e:
        print(e)
        print("Problems!")
        raise

#recognize(message.photo)


bot.polling(none_stop=True, interval=0)