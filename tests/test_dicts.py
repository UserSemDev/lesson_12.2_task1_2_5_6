import pytest
from utils import dicts


@pytest.mark.parametrize('data, key, default, excepted',
                         [({'vcs': 'mercurial'}, 'vcs', None, "mercurial"),
                          ({'vcs': 'mercurial'}, 'vcs', 'git', "mercurial"),
                          (None, 'vcs', 'git', "git"),
                          (None, 'vcs', 'bazaar', "bazaar")])
def test_get_val(data, key, default, excepted):
    assert dicts.get_val(data, key, default) == excepted
