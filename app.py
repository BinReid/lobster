from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'I_LOVE_TANYA'

users = {
    'ShadowedSeeker': '2#XgN9',
    'QuantumVoyage': '3^HjK7',
    'DreamingDruid': '1!pL8v',
    'VibrantMystic': '7@QzF4',
    'CelestialRover': '5#DkW2',
    'WhimsicalWanderer': '9!XwN1',
    'ElectricFable': '6$RjT5',
    'CuriousDynamo': '2^QmL3',
    'FrostyPathfinder': '8&FhK9',
    'EnigmaticWanderlust': '1!sT6v',
    'RadiantSaga': '4@JgN2',
    'TwilightRover': '3^WqF8',
    'CosmicDancer': '9#YtH1',
    'LuminousVoyager': '5!RzK7',
    'MythicSeeker': '2&dQm3',
    'SpiritedNomad': '8@XgJ5',
    'CuriousEcho': '1^HjT9',
    'VibrantJourney': '6#LwF2',
    'ShadowedExplorer': '3!KqN8',
    'QuantumDreamer': '4^YfR1',
    'EnchantedOdyssey': '9@TgK5',
    'CelestialQuest': '5&bJ3v',
    'WhimsicalSaga': '2^WmL6',
    'ElectricWanderer': '8#DkN9',
    'RadiantMystic': '1!pQ4j',
    'FrostedVoyager': '7@XhF2',
    'CosmicPioneer': '3^RzK1',
    'calphaks': 'FATASS@@@',
    'admin': 'password'
}

sports_events = [
   {
        'id': 1,
        'title': 'Футбольный матч',
        'date': '2024-05-01',
        'location': 'Стадион "Спартак"',
        'description': 'Приходите поддержать свою команду!',
        'image_url': 'https://s-cdn.sportbox.ru/images/styles/upload/fp_fotos/64/87/0264a3069f54eb6b9e7e056274a015a36675e72bc4236535251625.jpg'
    },
    {
        'id': 2,
        'title': 'Баскетбольный турнир',
        'date': '2024-06-15',
        'location': 'Спортзал "Олимп"',
        'description': 'Не пропустите захватывающие игры!',
        'image_url': 'https://www.ballgames.ru/img/basketball_tournament_h4.jpg'
    },
    {
        'id': 3,
        'title': 'Легкоатлетический забег',
        'date': '2024-07-20',
        'location': 'Парк "Солнечный"',
        'description': 'Присоединяйтесь к забегу на 5 км!',
        'image_url': 'https://img.five-sport.ru/files/1/6901/16677621/original/%D0%A1%D0%BE%D1%80%D0%B5%D0%B2%D0%BD%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F_%D0%BF%D0%BE_%D0%B1%D0%B5%D0%B3%D1%83.jpg'
    },
    {
        'id': 4,
        'title': 'Теннисный Турнир "Золотая Ракетка"',
        'date': '2024-09-17',
        'location': 'Теннисный корт "Балтийский"',
        'description': 'Турнир для игроков всех уровней, проводимый на местных теннисных кортах. Включает одиночные и парные соревнования.',
        'image_url': 'https://ss.sport-express.net/userfiles/materials/197/1977963/volga.jpg'
    },
    {
        'id': 5,
        'title': 'Зимний фестиваль "Лыжня России"',
        'date': '2024-01-22',
        'location': 'Ленинградская область, Санкт-Петербург, «Игора Драйв»',
        'description': 'Массовые лыжные гонки, проходящие в зимний период. Участники могут выбрать дистанцию от 5 до 25 км.',
        'image_url': 'https://fnpr.ru/upload/iblock/2f6/lp860dfccixq0z04wvr6a5vry3aa2bj8/2023_02_12_20_22_35.jpeg'
    },
    {
        'id': 6,
        'title': 'Чемпионат по плаванию "Золотая Рыбка"',
        'date': '2024-10-25',
        'location': 'Аквасфера',
        'description': 'Соревнования на разные дистанции для детей и взрослых. Проводится в местном бассейне.',
        'image_url': 'https://sportprimorsky.ru/uploads/posts/2024-02/1708996995_zolotaya-rybka-202400054.jpg'
    },
    {
        'id': 7,
        'title': 'Чемпионат по шахмат "Мозговой Штурм"',
        'date': '2024-05-15',
        'location': 'Ростех Арена',
        'description': 'Открытый шахматный турнир для игроков всех уровней. Проходит в культурном центре.',
        'image_url': 'https://tvtogliatti24.ru/userfiles/news/big/0_1700766653.jpg'
    }
]

@app.route('/profile')
def user_profile():
    # Пример данных в формате JSON
    user_data = {
        "username": "Иван Иванов",
        "role": "Спортсмен",
        "region": "Москва",
        "protocols": [
    "Итоговый протокол 2023 - Конкурс талантов",
    "Итоговый протокол 2023 - Спортивные достижения",
    "Итоговый протокол 2023 - Научные исследования"
],
        "participant_count": 150,
        "average_score": 85.5
    }
    
    return render_template('profile.html', **user_data)
    
    return render_template('profile.html', **user_data)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username] == password:
            session['username'] = username
            return redirect(url_for('events'))
        else:
            error = 'Неверное имя пользователя или пароль'
    return render_template('login.html', error=error)

@app.route('/events')
def events():
    if 'username' in session:
        return render_template ('events.html', username=session['username'], events=sports_events)
    return redirect(url_for('login'))

@app.route('/register/<int:event_id>', methods=['GET', 'POST'])
def register(event_id):
    if 'username' in session:
        return redirect(url_for('events'))
    return redirect(url_for('login'))

@app.route('/edit_profile', methods=['GET', 'POST'])
def edit_profile():
    # Your logic for editing the profile goes here
    return render_template('edit_profile.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('home'))

@app.route('/profile')
def profile():
    if 'username' in session:
        username = session['username']
        email = "user@example.com" 
        registration_date = "2024-01-01"
        return render_template('profile.html', username=username, email=email, registration_date=registration_date)
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)