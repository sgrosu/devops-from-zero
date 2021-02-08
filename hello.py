import click

@click.command()
@click.option(
    "--phrase",
    prompt="Enter a phrase",
    help="Enter a phrase the program will then tokenize"
)
def tokenize(phrase):
    '''
    This tool will transform a phrase into a list of words
    '''
    click.echo(
        click.style(f'tokenized phrase: {phrase.split()}', bg="yellow", fg="blue")
    )

if __name__ == "__main__":
    tokenize()