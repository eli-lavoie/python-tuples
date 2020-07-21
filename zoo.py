zoo = ("fox", "rabbit", "panda", "kangaroo", "owl", "falcon", "liger", "narwhal", "jellyfish", "shark")

zoo.index("owl")
animal_to_find = "gator"
if animal_to_find in zoo:
    print(f'We found a {animal_to_find} in the zoo.')
else:
    print(f"We couldn't find the {animal_to_find} in the zoo.")

(first_animal, second_animal, third_animal, fourth_animal, fifth_animal, sixth_animal, seventh_animal, eighth_animal, ninth_animal, tenth_animal) = zoo

print(first_animal)
print(second_animal)
print(third_animal)
print(fourth_animal)
print(fifth_animal)
print(sixth_animal)
print(seventh_animal)
print(eighth_animal)
print(ninth_animal)
print(tenth_animal)

zoo_list = list(zoo)
new_animals = ["zebra", "coyote", "cat"]
zoo_list.extend(new_animals)

new_zoo = tuple(zoo_list)