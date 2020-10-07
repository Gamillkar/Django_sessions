from django.shortcuts import render, redirect
from random import randint
from game.forms import GameForm
from game.models import Player, Game, PlayerGameInfo


def show_home(request, *args, **kwargs):
    success_attempt = None
    data_player = Player.objects
    games = Game.objects
    number = randint(0, 11)
    players = list(data_player.values())
    session = request.session.items()

    #если игрок уже завершил игру в сесcии
    try:
        if request.session['gameover'] == True:
            request.session.delete()
    except:
        pass

    # определения кто загадывает, кто отгадывает
    #добавление в DB и определение данных сессии
    if  str(session) == 'dict_items([])':
        if str(players) == '[]':
            first_player = Player.objects.create(player_id=1)
            first_player.save()
            first_game = Game.objects.create(game_id=1, number=number)
            first_game.save()
            Membership = PlayerGameInfo.objects.create(game=first_game, player=first_player)
            request.session['player'] = 1
            request.session['number'] = number

        else:
            player_id = players[-1]['id']
            if player_id == 1:
                second_player = Player.objects.create(player_id=player_id+1)
                second_player.save()
                game = games.all()[0]
                Membership = PlayerGameInfo.objects.create(game=game, player=second_player)
                request.session['player'] = 2
                number_result = games.values()[0]['number']
                request.session['number'] = number_result
                request.session['attempt'] = 0

            # для последующих игроко добавление DB и сохранения сессии
            if player_id % 2 == 0 and player_id > 1:
                primary_player = player_id + 1
                player = Player.objects.create(player_id=primary_player)
                player.save()
                game_info_id = list(games.values())[-1]['id'] + 1
                game = Game.objects.create(game_id=game_info_id, number=number)
                game.save()
                Membership = PlayerGameInfo.objects.create(game=game, player=player)
                request.session['player'] = primary_player
                request.session['number'] = number

            elif player_id % 2 != 0 and player_id > 1:
                second_player = player_id + 1
                player = Player.objects.create(player_id=second_player)
                player.save()
                game_info_id = (list(games.values())[-1]["id"])
                game = games.all().filter(id = game_info_id)[0]
                Membership = PlayerGameInfo.objects.create(game=game, player=player)
                games.values()
                number_result = list(games.values())[-1]['number']
                request.session['player'] = second_player
                request.session['number'] = number_result
                request.session['attempt'] = 0

    #определение создателя и второго игрока
    id_user = list(session)[0][1]

    if id_user % 2 != 0 or id_user == 1:
        user = 1
        for item in data_player.values():
            if int(item['player_id']) == int(request.session['player']) and item['success_attempt'] != None:
                request.session['gameover'] = True
    else:
        user = 2

    number_result = list(session)[1][1]
    form = GameForm
    context = {
        'form': form,
        'id': user,
        'number': number_result,
        'success_attempt': success_attempt,
    }

    if request.method == 'POST':
        form = GameForm(request.POST)
        print(form)
        if form.is_valid():
            request.session['attempt'] += 1
            example_number = request.POST['example_number']
            #нахождение и отправка уведомление 1 игроку
            if int(example_number) == int(number_result):
                search_game = Game.objects.values()
                for game in search_game:
                    if game['number'] == int(number_result):
                        game_id = game['id']
                        for player in PlayerGameInfo.objects.values():
                            if player['game_id'] == game_id and request.session['player'] != player['player_id']:
                                first_player = data_player.get(player_id=player['player_id'])
                                first_player.success_attempt = int(request.session['attempt'])
                                first_player.save()
                                request.session['gameover'] = True
            context = {
                'form': form,
                'id': user,
                'number': int(number_result),
                'example_number': int(example_number)
            }

    return render(
        request,
        'home.html',
        context
        )






