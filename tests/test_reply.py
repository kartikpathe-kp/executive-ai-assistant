import pytest

from eaia.main.reply import answer


def test_plain_text_is_a_response():
    assert answer("Thursday 1pm works") == {"type": "response", "args": "Thursday 1pm works"}


def test_a_structured_item_in_a_list_is_unwrapped():
    assert answer([{"type": "accept", "args": None}]) == {"type": "accept", "args": None}


def test_structured_item_passes_through():
    item = {"type": "edit", "args": {"args": {"content": "x"}}}
    assert answer(item) == item


@pytest.mark.parametrize("word,kind", [("accept", "accept"), (" Ignore ", "ignore")])
def test_a_bare_keyword_means_that_action(word, kind):
    assert answer(word) == {"type": kind, "args": None}


def test_empty_answer_is_still_a_response():
    assert answer("") == {"type": "response", "args": ""}
