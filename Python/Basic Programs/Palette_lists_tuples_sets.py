# creating palette list with 5 colours
palette = ["pink", "orange", "blue", "yellow", "purple"]

# remove a colo9ur and add a different one
palette.remove("pink")
palette.append("turquoise")
print(palette)

# converting palette list to a tuple
locked_palette = tuple(palette)

# creating a extra palette
extra_colours = ("brown", "blue", "white")

# combining to make full palette
full_palette = tuple(locked_palette + extra_colours)
print(full_palette)

# turning into editable palette and appending
editable_palette = list(full_palette)
editable_palette.append("bronze")
print(editable_palette)

# converting to a set to remove duplicates
unique_colours = set(editable_palette)

theme_colours = {"blue", "orange", "yellow"}
common_colours = set(unique_colours & theme_colours)
print(common_colours)
