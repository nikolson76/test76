import requests
import time

BASE_URL = "https://petstore.swagger.io/v2/"

test_pet = {
    "id": 6556,
    "name": "Frank",
    "status": "available"
}

def test_post_order():
    response = requests.post(f"{BASE_URL}pet", json=test_pet)
    assert response.status_code == 200
    print("Питомец добавлен")
    return response.json()

def test_get_order():
    time.sleep(1)  # Задержка для обработки на сервере
    response = requests.get(f"{BASE_URL}pet/6556")
    assert response.status_code == 200
    print("Питомец найден")

def test_put_order():
    updated_pet = {
        "id": 6556,
        "name": "Franke",
        "status": "sold"
    }
    response = requests.put(f"{BASE_URL}pet", json=updated_pet)
    assert response.status_code == 200
    print("Питомец обновлен")

def test_delete_order():
    response = requests.delete(f"{BASE_URL}pet/6556")
    assert response.status_code == 200
    print("Питомец удален")

def test_order_not_found():
    time.sleep(1)  # Задержка для обработки удаления
    response = requests.get(f"{BASE_URL}pet/6556")
    assert response.status_code == 404
    print("Питомец не найден")

print("\n===Начало тестирования===")
test_post_order()
test_get_order()
test_put_order()
test_delete_order()
test_order_not_found()
print("===Тестирование завершено===")

