│
├── client/ # Klient API do pobierania danych
│ ├── **init**.py
│ ├── config.py # Konfiguracja klienta (np. adres API, klucz API)
│ ├── api_client.py # Klasa klienta API
│ └── main.py # Punkt wejścia dla klienta
│
├── backend/ # Aplikacja backendowa
│ ├── **init**.py
│ ├── config.py # Konfiguracja backendu (np. port serwera)
│ ├── models.py # Modele danych (np. OdczytPogody, OdczytZanieczyszczenia)
│ ├── services/ # Usługi biznesowe (np. walidacja danych)
│ │ ├── **init**.py
│ │ └── validation.py # Walidacja danych
│ ├── views/ # Widoki (endpointy)
│ │ ├── **init**.py
│ │ └── weather_view.py # Widok dla odczytów pogody
│ ├── controllers/ # Kontrolery (logika biznesowa)
│ │ ├── **init**.py
│ │ └── weather_controller.py
│ ├── database/ # Persystencja (np. lista/słownik w pamięci)
│ │ ├── **init**.py
│ │ └── memory_db.py # Implementacja bazy danych w pamięci
│ └── main.py # Punkt wejścia dla backendu
│
└── README.md # Dokumentacja projektu
