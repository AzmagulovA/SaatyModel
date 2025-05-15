import ollama

# Конфигурация
MODEL_NAME = "saati-mistral"  # Название вашей модели в Ollama


def ask_model(prompt: str) -> str:
    """Отправляет запрос к модели и возвращает её ответ."""
    response = ollama.generate(model=MODEL_NAME, prompt=prompt)
    return response['response'].strip()


def interactive_test() -> None:
    """Интерактивный режим для ввода данных пользователем."""
    print("Введите текст для тестирования модели или 'exit' для выхода.")

    while True:
        user_input = input("Текст: ")

        if user_input.lower() == "exit":
            break

        model_answer = ask_model(user_input)
        print(f"Ответ модели: {model_answer}")


if __name__ == "__main__":
    interactive_test()
