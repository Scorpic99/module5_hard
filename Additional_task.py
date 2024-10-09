import time


class UrTube:
    users = []
    videos = []
    __passwords = {}
    current_user = None
    def __init__(self):
        pass
    def log_in(self, nickname, password):
        for i in self.users:
            if nickname == i:
                if hash(password) == self.__passwords.get(nickname):
                    self.current_user = nickname
                else:
                    print('Вы ввели не правельный пароль')
            else:
                print('Такого пользователя не существует')

    def register(self, obj_user, nickname, password, age):

        my_flag = False
        for i in self.users:
            if nickname == i:
                my_flag = True
                break
            else:
                my_flag = False

        if my_flag:
            print(f"Пользователь {nickname} уже существует")
        else:

            self.users.append(nickname)
            obj_user.nickname = nickname
            self.current_user = nickname
            self.__passwords[nickname] = password
            obj_user.password = hash(password)
            obj_user.age = age


    def log_out(self):
        self.current_user = None

    def add(self, *args):
        temp_movies = []
        for i in args:
            temp_movies.append(i.title)
        for i in self.videos:
            for j in temp_movies:
                if i == j:
                    temp_movies.remove(i)
        self.videos.extend(temp_movies)


    def get_videos(self, search_word):
        video_with_word = []
        for i in self.videos:
            if search_word.lower() in str(i.lower()):
                video_with_word.append(i)
        return video_with_word

    def watch_video(self,obj_user, title_video):
        if self.current_user is not None:
            if  obj_user.age > 18:
                for i in range(len(self.videos)):
                    if self.videos[i] == title_video:
                        for j in range(10):
                            time.sleep(1)
                            print(j, end=' ')
                        print('Конец видео')

            else:
                print("Вам нет 18 лет, пожалуйста покиньте страницу")
        else:
            print("Войдите в аккаунт, чтобы смотреть видео")

    def __str__(self):
        if self.current_user is not None:
            return self.current_user
        else:
            return 'Пользователь не найден'


class Video:
    title = None
    duration = None
    time_now = None
    adult_mode = None

    def __init__(self, title, duration = 0, time_now = 0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

class User:
    nickname = ''
    password = None
    age = 0


    def __str__(self):
        if not self.nickname:
            print('Пользователь не существует')
        else:
            return f"Имя пользователя: {self.nickname}\nВозраст: {self.age}"

ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)
us = User()

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video(us,'Для чего девушкам парень программист?')
ur.register(us,'vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video(us,'Для чего девушкам парень программист?')
ur.register(us,'urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video(us,'Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register(us,'vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video(us,'Лучший язык программирования 2024 года!')

