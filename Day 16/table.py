from prettytable import PrettyTable

pokemon_table = PrettyTable()
pokemon_table2 = PrettyTable()

print(pokemon_table)

pokemon_table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
pokemon_table.add_column("Type", ["Electric", "Water", "Fire"])
print(pokemon_table.align)

pokemon_table.align = "l"
print(pokemon_table)

# print("\n" * 5)

# pokemon_table2.field_names = ["Pokemon Name", "Type"]
# pokemon_table2.add_rows(
#     [
#         ["Pikachu", "Electric"],
#         ["Squirtle", "Water"],
#         ["Charmander", "Fire"],
#     ]
# )

# print(pokemon_table2)

