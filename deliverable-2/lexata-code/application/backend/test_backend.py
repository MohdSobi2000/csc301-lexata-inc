from lexata import Lexata


def test_query_simple():
    lexata = Lexata()
    query = 'pollution'
    results = lexata.get_closest_to(query)
    print('Best: ', results)
    assert type(results) == dict
    assert len(results) == 1


def test_query_multiple_factors():
    lexata = Lexata()
    query = 'can changes in the global climate or extreme weather conditions affect my business'
    results = lexata.get_closest_to(query, 4, ['information Technology'])
    print('Best: ', results)
    assert type(results) == dict
    assert len(results) == 4
