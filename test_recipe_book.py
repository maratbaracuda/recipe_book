from recipe_book import RecipeBook


def test_recipe_book():
    # 1. Инициализация
    book = RecipeBook()

    # 2. Добавление рецептов
    omelet = {"name": "Омлет", "ingredients": ["яйца", "молоко"], "time": 10}
    salad = {"name": "Салат", "ingredients": ["помидоры", "огурцы"], "time": 15}
    book.add_recipe(omelet)
    book.add_recipe(salad)

    # 3. Проверка добавления
    assert book.recipes_count == 2, "Ошибка: неверное количество рецептов"
    assert book.last_recipe["name"] == "Салат", "Ошибка: last_recipe не обновляется"

    # 4. Поиск по ингредиенту
    found = book.find_by_ingredient("яйца")
    assert len(found) == 1 and found[0]["name"] == "Омлет", "Ошибка поиска по ингредиенту"

    # 5. Удаление
    book.remove_recipe("Омлет")
    assert book.recipes_count == 1, "Ошибка удаления"
    assert book.find_by_ingredient("яйца") == [], "Рецепт не удалился"

    print("✅ Все тесты прошли успешно!")


if __name__ == "__main__":
    test_recipe_book()