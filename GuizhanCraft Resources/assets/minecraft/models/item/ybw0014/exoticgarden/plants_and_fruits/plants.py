plant_template = """
{
    "parent": "item/handheld",
    "author": "ybw0014",
    "textures": {
        "layer0": "items/ybw0014/exoticgarden/plants_and_fruits/{{ fruit }}"
    },
    "display": {
        "thirdperson_righthand": {
            "rotation": [ 0, 0, 0 ],
            "translation": [ 0, 1, 0 ],
            "scale": [ 0.55, 0.55, 0.55 ]
        },
        "thirdperson_lefthand": {
            "rotation": [ 0, 0, 0 ],
            "translation": [ 0, 1, 0 ],
            "scale": [ 0.55, 0.55, 0.55 ]
        }
    }
}
"""

fruits = ['apple', 'apple_oak_sapling', 'blackberry', 'blackberry_bush', 'black_pepper', 'black_pepper_plant', 'blueberry', 'blueberry_bush', 'cabbage', 'cabbage_plant', 'cherry', 'cherry_sapling', 'cilantro', 'cilantro_plant', 'coconut', 'coconut_sapling', 'corn', 'corn_plant', 'cowberry', 'cowberry_bush', 'cranberry', 'cranberry_bush', 'curry_leaf', 'curry_leaf_plant', 'dragon_fruit', 'dragon_fruit_sappling', 'elderberry', 'elderberry_bush', 'garlic', 'garlic_plant', 'grape', 'grape_bush', 
'grass_seeds', 'lemon', 'lemon_sapling', 'lettuce', 'lettuce_plant', 'lime', 'lime_sapling', 'mustard_seed', 'mustard_seed_plant', 'onion', 'onion_plant', 'orange', 'orange_sapling', 'peach', 'peach_sapling', 'pear', 'pear_sapling', 'pineapple', 'pineapple_plant', 'plum', 'plum_sapling', 'pomegranate', 'pomegranate_sapling', 'raspberry', 'raspberry_bush', 'strawberry', 'strawberry_bush', 'sweet_potato', 'sweet_potato_plant', 'tea_leaf', 'tea_leaf_plant', 'tomato', 'tomato_plant'] 

for fruit in fruits:
    f = open(fruit + ".json", "w")
    f.write(plant_template.replace("{{ fruit }}", fruit))
    f.close()
