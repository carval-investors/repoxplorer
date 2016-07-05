from unittest import TestCase

from repoxplorer import index
from repoxplorer.index.commits import Commits


class TestCommits(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.con = index.Connector(index='repoxplorertest')
        cls.c = Commits(cls.con)
        cls.commits = [
            {
                'sha': '3597334f2cb10772950c97ddf2f6cc17b184',
                'author_date': 1410456005,
                'committer_date': 1410456005,
                'author_name': 'Nakata Daisuke',
                'committer_name': 'Nakata Daisuke',
                'author_email': 'n.suke@joker.org',
                'committer_email': 'n.suke@joker.org',
                'projects': [
                    'https://github.com/nakata/monkey.git:monkey:master', ],
                'line_modifieds': 10,
                'merge_commit': False,
                'commit_msg': 'Add init method',
            },
            {
                'sha': '3597334f2cb10772950c97ddf2f6cc17b185',
                'author_date': 1410457005,
                'committer_date': 1410457005,
                'author_name': 'Keiko Amura',
                'committer_name': 'Keiko Amura',
                'author_email': 'keiko.a@joker.org',
                'committer_email': 'keiko.a@joker.org',
                'projects': [
                    'https://github.com/amura/kotatsu.git:kotatsu:master', ],
                'line_modifieds': 100,
                'merge_commit': True,
                'commit_msg': 'Merge "Fix sanity unittest"',
            },
            {
                'sha': '3597334f2cb10772950c97ddf2f6cc17b186',
                'author_date': 1410458005,
                'committer_date': 1410458005,
                'author_name': 'Jean Bon',
                'committer_name': 'Jean Bon',
                'author_email': 'jean.bon@joker.org',
                'committer_email': 'jean.bon@joker.org',
                'projects': [
                    'https://github.com/nakata/monkey.git:monkey:master', ],
                'line_modifieds': 200,
                'merge_commit': False,
                'commit_msg': 'Add request customer feature 19',
            },
            {
                'sha': '3597334f2cb10772950c97ddf2f6cc17b187',
                'author_date': 1410459005,
                'committer_date': 1410459005,
                'author_name': 'Jean Bon',
                'committer_name': 'Jean Bon',
                'author_email': 'jean.bon@joker.org',
                'committer_email': 'jean.bon@joker.org',
                'projects': [
                    'https://github.com/nakata/monkey.git:monkey:master', ],
                'line_modifieds': 300,
                'merge_commit': False,
                'commit_msg': 'Add request customer feature 20',
            },
            {
                'sha': '3597334f2cb10772950c97ddf2f6cc17b188',
                'author_date': 1410460005,
                'committer_date': 1410460005,
                'author_name': 'Jean Bon',
                'committer_name': 'Jean Bon',
                'author_email': 'jean.bon@joker.org',
                'committer_email': 'jean.bon@joker.org',
                'projects': [
                    'https://github.com/amura/kotatsu.git:kotatsu:master',
                    'https://github.com/amura/kotatsu.git:kotatsu:devel'],
                'line_modifieds': 400,
                'merge_commit': False,
                'commit_msg': 'Add request customer feature 21',
            },
            {
                'sha': '3597334f2cb10772950c97ddf2f6cc17b189',
                'author_date': 1410461005,
                'committer_date': 1410461005,
                'author_name': 'Jean Bon',
                'committer_name': 'Jean Bon',
                'author_email': 'jean.bon@joker.org',
                'committer_email': 'jean.bon@joker.org',
                'projects': [
                    'https://github.com/amura/kotatsu.git:kotatsu:devel', ],
                'line_modifieds': 400,
                'merge_commit': False,
                'commit_msg': 'Add request customer feature 22',
            },
            {
                'sha': '3597334f2cb10772950c97ddf2f6cc17b190',
                'author_date': 1410491005,
                'committer_date': 1410491005,
                'author_name': 'Jean Bon',
                'committer_name': 'Jean Bon',
                'author_email': 'jean.bon@joker.org',
                'committer_email': 'jean.bon@joker.org',
                'projects': [
                    'https://github.com/amura/kotatsu.git:kotatsu:devel', ],
                'line_modifieds': 400,
                'merge_commit': False,
                'commit_msg': 'Add request customer feature 23',
            }
        ]
        cls.c.add_commits(cls.commits)

    @classmethod
    def tearDownClass(cls):
        cls.con.ic.delete(index=cls.con.index)

    def test_get_commit(self):
        ret = self.c.get_commit('3597334f2cb10772950c97ddf2f6cc17b188')
        self.assertEqual(ret['commit_msg'], 'Add request customer feature 21')

    def test_get_commits(self):
        ret = self.c.get_commits(mails=['n.suke@joker.org'])
        self.assertEqual(ret[1], 1)
        self.assertEqual(ret[2][0]['commit_msg'], 'Add init method')

        ret = self.c.get_commits(mails=['jean.bon@joker.org'])
        self.assertEqual(ret[1], 5)
        self.assertEqual(ret[2][0]['commit_msg'],
                         'Add request customer feature 23')

        ret = self.c.get_commits(
            projects=['https://github.com/amura/kotatsu.git:kotatsu:master'])
        self.assertEqual(ret[1], 2)
        self.assertEqual(ret[2][0]['commit_msg'],
                         'Add request customer feature 21')

        ret = self.c.get_commits(
            projects=['https://github.com/nakata/monkey.git:monkey:master'],
            mails=['jean.bon@joker.org'])
        self.assertEqual(ret[1], 2)
        self.assertEqual(ret[2][0]['commit_msg'],
                         'Add request customer feature 20')

        ret = self.c.get_commits(
            projects=['https://github.com/nakata/monkey.git:monkey:master'])
        self.assertEqual(ret[1], 3)

        ret = self.c.get_commits(
            projects=['https://github.com/nakata/monkey.git:monkey:master'],
            fromdate=1410456000,
            todate=1410458010,)
        self.assertEqual(ret[1], 2)
        self.assertEqual(ret[2][0]['commit_msg'],
                         'Add request customer feature 19')

        ret = self.c.get_commits(
            projects=['https://github.com/amura/kotatsu.git:kotatsu:devel',
                      'https://github.com/amura/kotatsu.git:kotatsu:master'])
        self.assertEqual(ret[1], 4)

    def test_get_commits_based_on_merge_info(self):
        ret = self.c.get_commits(mails=['keiko.a@joker.org'],
                                 merge_commit=False)
        self.assertEqual(ret[1], 0)
        ret = self.c.get_commits(mails=['keiko.a@joker.org'],
                                 merge_commit=True)
        self.assertEqual(ret[1], 1)
        # When merge_commit at None either merge commit or not
        # are returned
        ret = self.c.get_commits(mails=['keiko.a@joker.org'],
                                 merge_commit=None)
        self.assertEqual(ret[1], 1)

    def test_get_commits_amount(self):
        ret = self.c.get_commits_amount(
            ['n.suke@joker.org'])
        self.assertEqual(ret, 1)

        ret = self.c.get_commits_amount(
            ['n.suke@joker.org',
             'jean.bon@joker.org'])
        self.assertEqual(ret, 6)

        ret = self.c.get_commits_amount(
            ['n.suke@joker.org',
             'jean.bon@joker.org'],
            fromdate=1410456000,
            todate=1410456010)
        self.assertEqual(ret, 1)

        ret = self.c.get_commits_amount(
            projects=['https://github.com/nakata/monkey.git:monkey:master'])
        self.assertEqual(ret, 3)

        ret = self.c.get_commits_amount(
            ['n.suke@joker.org'],
            projects=['https://github.com/nakata/monkey.git:monkey:master'])
        self.assertEqual(ret, 1)

        ret = self.c.get_commits_amount(
            ['jean.bon@joker.org'],
            projects=['https://github.com/nakata/monkey.git:monkey:master'])
        self.assertEqual(ret, 2)

        ret = self.c.get_commits_amount(
            ['jean.bon@joker.org'],
            projects=['https://github.com/nakata/monkey.git:monkey:master',
                      'https://github.com/amura/kotatsu.git:kotatsu:master'])
        self.assertEqual(ret, 3)

        ret = self.c.get_commits_amount(
            ['jean.bon@joker.org', 'keiko.a@joker.org'],
            projects=['https://github.com/nakata/monkey.git:monkey:master',
                      'https://github.com/amura/kotatsu.git:kotatsu:master'])
        self.assertEqual(ret, 4)

    def test_get_line_modifieds_amount(self):
        ret = self.c.get_line_modifieds_stats(
            ['n.suke@joker.org'])
        self.assertDictEqual(ret[1], {u'avg': 10.0, u'min': 10.0,
                                      u'count': 1, u'max': 10.0,
                                      u'sum': 10.0})

        ret = self.c.get_line_modifieds_stats(
            ['jean.bon@joker.org'],
            projects=['https://github.com/nakata/monkey.git:monkey:master',
                      'https://github.com/amura/kotatsu.git:kotatsu:master'])
        self.assertDictEqual(ret[1], {u'avg': 300.0, u'min': 200.0,
                                      u'max': 400.0, u'count': 3,
                                      u'sum': 900.0})

    def test_get_top_authors(self):
        ret = self.c.get_top_authors(
            projects=['https://github.com/nakata/monkey.git:monkey:master'])
        self.assertDictEqual(ret[1],
                             {u'jean.bon@joker.org': (2, 'Jean Bon'),
                              u'n.suke@joker.org': (1, u'Nakata Daisuke')})

        ret = self.c.get_top_authors(
            projects=['https://github.com/nakata/monkey.git:monkey:master',
                      'https://github.com/amura/kotatsu.git:kotatsu:master'])
        self.assertDictEqual(ret[1],
                             {u'jean.bon@joker.org': (3, 'Jean Bon'),
                              u'keiko.a@joker.org': (1, 'Keiko Amura'),
                              u'n.suke@joker.org': (1, 'Nakata Daisuke')})

    def test_get_top_projects(self):
        ret = self.c.get_top_projects(
            ['jean.bon@joker.org'])
        self.assertDictEqual(ret[1], {
            u'https://github.com/amura/kotatsu.git:kotatsu:devel': 3,
            u'https://github.com/amura/kotatsu.git:kotatsu:master': 1,
            u'https://github.com/nakata/monkey.git:monkey:master': 2})

    def test_get_commits_histo(self):
        ret = self.c.get_commits_histo(
            ['jean.bon@joker.org'])
        self.assertDictEqual(ret[1][0], {u'key': 1410393600000,
                                         u'doc_count': 4,
                                         u'key_as_string': u'2014-09-11'})
        self.assertDictEqual(ret[1][1], {u'key': 1410480000000,
                                         u'doc_count': 1,
                                         u'key_as_string': u'2014-09-12'})
        ret = self.c.get_commits_histo(
            ['jean.bon@joker.org'],
            projects=['https://github.com/amura/kotatsu.git:kotatsu:devel'])
        self.assertDictEqual(ret[1][0], {u'key': 1410393600000,
                                         u'doc_count': 2,
                                         u'key_as_string': u'2014-09-11'})
        self.assertDictEqual(ret[1][1], {u'key': 1410480000000,
                                         u'doc_count': 1,
                                         u'key_as_string': u'2014-09-12'})

    def test_get_top_authors_by_lines(self):
        ret = self.c.get_top_authors_by_lines(
            projects=['https://github.com/nakata/monkey.git:monkey:master'])
        self.assertDictEqual(ret[1], {u'n.suke@joker.org': 10.0,
                                      u'jean.bon@joker.org': 500.0})
