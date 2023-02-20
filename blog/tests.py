import pytest

from django.urls import reverse

from .models import HighScore
from .serializers import HighScoreSerializer
from rest_framework.test import APIRequestFactory

factory = APIRequestFactory()
request = factory.post('/score2/', {'player_name': 'new idea'})

@pytest.mark.django_db
def test_list_games(client):
    url = reverse('game_list')
    response = client.get(url)
    articles = HighScore.objects.all()
    expected_data = HighScoreSerializer(articles, many=True).data
    # import pdb; pdb.set_trace()
    assert response.status_code == 200
    assert response.data == expected_data