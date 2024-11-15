import click

import just_count.square


@click.command()
@click.argument("x", type=int)
def main(x):
    """Calculates the square of a number."""
    print(just_count.square.square(x))


if __name__ == "__main__":
    main()
