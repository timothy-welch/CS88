test = {
  'name': 'Problem 2',
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> woz_reviews = [make_review('Wozniak Lounge', 4.0),
          ...                make_review('Wozniak Lounge', 3.0),
          ...                make_review('Wozniak Lounge', 5.0)]
          >>> woz = make_restaurant('Wozniak Lounge', [127.0, 0.1],
          ...                       ['Restaurants', 'Pizza'],
          ...                       1, woz_reviews)
          >>> restaurant_num_scores(woz)
          3
          >>> restaurant_mean_score(woz) # should be a decimal
          4.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> import abstractions
      >>> from abstractions import *
      """,
      'teardown': '',
      'type': 'doctest'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> woz_reviews = [make_review('Wozniak Lounge', 4),
          ...                make_review('Wozniak Lounge', 3),
          ...                make_review('Wozniak Lounge', 5)]
          >>> woz = make_restaurant('Wozniak Lounge', [127.0, 0.1],
          ...                       ['Restaurants', 'Pizza'],
          ...                       1, woz_reviews)
          >>> restaurant_num_scores(woz)
          3
          >>> restaurant_mean_score(woz) # should be a decimal
          4.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> import abstractions
      >>> import tests.test_functions as test
      >>> test.swap_implementations(abstractions, rest_two=False) # don't violate abstraction!
      >>> make_user, make_review, make_restaurant = abstractions.make_user, abstractions.make_review, abstractions.make_restaurant
      >>> restaurant_num_scores = abstractions.restaurant_num_scores
      >>> restaurant_mean_score = abstractions.restaurant_mean_score
      """,
      'teardown': r"""
      >>> test.restore_implementations(abstractions)
      """,
      'type': 'doctest'
    }
  ]
}
