import asyncio

from eaia.main.reflect import reflect


class Runs:
    def __init__(self, err=None):
        self.err, self.calls = err, []

    async def create(self, thread, graph, input):
        self.calls.append((thread, graph, input))
        if self.err:
            raise self.err


class Client:
    def __init__(self, err=None):
        self.runs = Runs(err)


def test_reflect_starts_the_run():
    c = Client()
    assert asyncio.run(reflect(c, {"a": 1})) is True
    assert c.runs.calls == [(None, "multi_reflection_graph", {"a": 1})]


def test_reflect_swallows_a_missing_server():
    assert asyncio.run(reflect(Client(TypeError("'NoneType' object is not callable")), {})) is False
