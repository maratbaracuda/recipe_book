class RecipeBook:
    def __init__(self):
        self._recipes = []
        self._last_recipe = None

    def add_recipe(self, recipe_dict):
        """Добавляет рецепт в книгу."""
        self._recipes.append(recipe_dict)
        self._last_recipe = recipe_dict

    def remove_recipe(self, name):
        """Удаляет рецепт по названию."""
        self._recipes = [r for r in self._recipes if r['name'] != name]
        if self._last_recipe and self._last_recipe['name'] == name:
            self._last_recipe = None

    def find_by_ingredient(self, ingredient):
        """Ищет рецепты по ингредиенту."""
        return [r for r in self._recipes if ingredient.lower() in [i.lower() for i in r['ingredients']]]

    @property
    def recipes_count(self):
        """Возвращает количество рецептов (только чтение)."""
        return len(self._recipes)

    @property
    def last_recipe(self):
        """Возвращает последний добавленный рецепт."""
        return self._last_recipe

    @last_recipe.setter
    def last_recipe(self, recipe_dict):
        """Устанавливает последний рецепт (если он есть в книге)."""
        if recipe_dict in self._recipes:
            self._last_recipe = recipe_dict