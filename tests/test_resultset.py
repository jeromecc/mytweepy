from config import TweepyTestCase
from mytweepy.models import ResultSet


class NoIdItem:
    pass


class IdItem:
    def __init__(self, id):
        self.id = id


ids_fixture = [1, 10, 8, 50, 2, 100, 5]


class TweepyResultSetTests(TweepyTestCase):
    def setUp(self):
        self.results = ResultSet()
        for i in ids_fixture:
            self.results.append(IdItem(i))
            self.results.append(NoIdItem())

    def testids(self):
        ids = self.results.ids()
        self.assertListEqual(ids, ids_fixture)

    def testmaxid(self):
        self.assertEqual(self.results.max_id, 0)

    def testsinceid(self):
        self.assertEqual(self.results.since_id, 100)
