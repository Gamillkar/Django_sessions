from django.db import models


class Game(models.Model):
    game_id = models.IntegerField()
    number = models.IntegerField()

    def __str__(self):
        return self.number


class Player(models.Model):
    player_id = models.IntegerField()
    game_info = models.ManyToManyField(Game, through='PlayerGameInfo', related_name='game_info')
    success_attempt = models.IntegerField(null=True)


class PlayerGameInfo(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)



