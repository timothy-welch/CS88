test = {
  'name': 'Problem 0',
  'points': 4,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> square = lambda x: x * x
          >>> is_odd = lambda x: x % 2 == 1
          >>> map_and_filter([1, 2, 3, 4, 5], square, is_odd)
          [1, 9, 25]
          >>> map_and_filter(['hi', 'hello', 'hey', 'world'],
          ...                lambda x: x[4], lambda x: len(x) > 4)
          ['o', 'd']
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> key_of_min_value({1: 6, 2: 5, 3: 4})
          3
          >>> key_of_min_value({'a': 6, 'b': 5, 'c': 4})
          'c'
          >>> key_of_min_value({'hello': 'world', 'hi': 'there'})
          'hi'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> enumerate([6, 'one', 'a'], 3)[1]
          [4, 'one']
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from utils import *
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
