import requests
import pytest

host = 'https://api.pokemonbattle.me:9104'

def test_status_code():
    response = requests.get(f'{host}/trainers')
    assert response.status_code == 200


def test_piece_body():
    response = requests.get(f'{host}/trainers', params = {'trainer_id' : '3543' })
    assert response.json()['trainer_name'] == 'DIDI'

