# A sample use case of the Lexata Python module.
# Not for deployment purposes.
import pprint

from backend.lexata import Lexata


if __name__ == '__main__':
    lexata = Lexata()
    query = 'environment'
    results = lexata.get_closest_to(query, 3, ['Materials', 'Information technology'])
    pprint.pprint(results)
