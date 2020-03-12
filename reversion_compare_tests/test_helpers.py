import pytest

from reversion_compare.helpers import EFFICIENCY, SEMANTIC, dmp, html_diff


@pytest.mark.skipif(dmp is not None, reason='google "diff-match-patch" is available')
def test_difflib():
    """
    Test diffs if google "diff-match-patch" not available
    """
    html = html_diff(
        value1='one',
        value2='two',
    )
    assert html == (
        '<pre class="highlight">\n'
        '<del>- one</del>\n'
        '<ins>+ two</ins>\n'
        '</pre>'
    )

    html = html_diff(
        value1='aaa\nccc\nddd\n',
        value2='aaa\nbbb\nccc\n',
        cleanup=SEMANTIC
    )
    assert html == (
        '<pre class="highlight">\n'
        '  aaa\n'
        '<ins>+ bbb</ins>\n'
        '  ccc\n'
        '<del>- ddd</del>\n'
        '</pre>'
    )


@pytest.mark.skipif(dmp is None, reason='google "diff-match-patch" not available')
def test_diff_match_patch_no_cleanup():
    """
    Test diffs created by google "diff-match-patch" without cleanup
    """
    html = html_diff(
        value1='one',
        value2='two',
        cleanup=None
    )
    assert html == (
        '<pre class="highlight">\n'
        '<ins>+ tw</ins>\n'
        'o\n'
        '<del>- ne</del>\n'
        '</pre>'
    )

    html = html_diff(
        value1='aaa\nccc\nddd\n',
        value2='aaa\nbbb\nccc\n',
        cleanup=None
    )
    assert html == (
        '<pre class="highlight">\n'
        'aaa\n'
        '\n'
        '<ins>+ bbb\n'
        '</ins>\n'
        'ccc\n'
        '\n'
        '<del>- ddd\n'
        '</del>\n'
        '</pre>'
    )


@pytest.mark.skipif(dmp is None, reason='google "diff-match-patch" not available')
def test_diff_match_patch_efficiency():
    """
    Test diffs created by google "diff-match-patch" with "efficiency" cleanup
    """
    html = html_diff(
        value1='one',
        value2='two',
        cleanup=EFFICIENCY
    )
    assert html == (
        '<pre class="highlight">\n'
        '<ins>+ tw</ins>\n'
        'o\n'
        '<del>- ne</del>\n'
        '</pre>'
    )

    html = html_diff(
        value1='aaa\nccc\nddd\n',
        value2='aaa\nbbb\nccc\n',
        cleanup=EFFICIENCY
    )
    assert html == (
        '<pre class="highlight">\n'
        'aaa\n'
        '\n'
        '<ins>+ bbb\n'
        '</ins>\n'
        'ccc\n'
        '\n'
        '<del>- ddd\n'
        '</del>\n'
        '</pre>'
    )


@pytest.mark.skipif(dmp is None, reason='google "diff-match-patch" not available')
def test_diff_match_patch_semantic():
    """
    Test diffs created by google "diff-match-patch" with "semantic" cleanup
    """
    html = html_diff(
        value1='one',
        value2='two',
        cleanup=SEMANTIC
    )
    assert html == (
        '<pre class="highlight">\n'
        '<del>- one</del>\n'
        '<ins>+ two</ins>\n'
        '</pre>'
    )

    html = html_diff(
        value1='aaa\nccc\nddd\n',
        value2='aaa\nbbb\nccc\n',
        cleanup=SEMANTIC
    )
    assert html == (
        '<pre class="highlight">\n'
        'aaa\n'
        '\n'
        '<del>- ccc\n'
        '- ddd</del>\n'
        '<ins>+ bbb\n'
        '+ ccc</ins>\n'
        '\n'
        '\n'
        '</pre>'
    )
