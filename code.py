import random
import click


def roll_dice(sides):
        roll = random.randint(1, sides)
        print("{} sided die rolled: {}".format(sides, roll))


@click.command()
@click.option("rolls", "--rolls", type=int, help="Number of times to roll.")
@click.option("sides", "--sides", type=int, help="Number of sides of dice.")
def main(rolls, sides):
    for x in range(rolls):
        roll_dice(sides)


if __name__ == "__main__":
    main()
