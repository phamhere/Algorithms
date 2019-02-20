#!/usr/bin/python


def recipe_batches(recipe, ingredients):
    count = 0
    looping = True
    # while loop to continually subtract ingredients if they're available
    while looping:
        # looping through recipe dict
        for ing in recipe.keys():
            """if recipe requirements greater than ingredient amount, counteract
            count adding, make sure while loop and for loop exits"""
            if ing not in ingredients.keys() or recipe[ing] > ingredients[ing]:
                count -= 1
                looping = False
                break
            # if enough ingredients, subtract recipe requirements
            else:
                ingredients[ing] -= recipe[ing]
        count += 1
    return count


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
