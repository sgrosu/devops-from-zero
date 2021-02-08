from hello import tokenize
from click.testing import CliRunner
#from sync import cli
from prompt import PROMPT as prompt


def test_hello():
    runner = CliRunner()
    inp = "Who let the doge out"
    #result = runner.invoke(prompt, input="Who let the doge out")
    result = runner.invoke(tokenize, ['--phrase', inp])
    assert not result.exception
    assert result.output == "tokenized phrase: ['Who', 'let', 'the', 'doge', 'out']\n"
    #assert ["Who", "let", "the", "doge", "out"] == runner.invoke("tokenize", ["--phrase", "Who let the doge out"]).output