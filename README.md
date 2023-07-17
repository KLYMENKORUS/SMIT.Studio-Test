<h1>Тестовое задание на позицию Python разработчика</h1>

  <h2><a href="https://docs.google.com/document/d/1ET0V9ZsLNsdwkaZQ-M3nC6Kkvx2KS75UUROg3kc68UA/edit">Задание</a></h2>
  <h2>Инструкция к API</h2>
<ol>
  <li>Эндпоинты:</li>
    <ul>
      <li><code>POST "/api/v1/insurance/create"</code> Создание тарифов</li>
      <li><code>POST "/api/v1/insurance/calculate"</code> Расчет страховки</li>
      <li><code>GET "/api/v1/insurance/all_by_cargo_type"</code> Выдает все тарифы по данному грузу</li>
      <li><code>GET "/api/v1/insurance/all"</code> Выдает все тарифы в бд</li>
    </ul>
</ol>
  <h2>Технологии</h2>
  <div>
    <img src="https://img.shields.io/badge/Python-blue?style=for-the-badge&logo=python&logoColor=white&color=9cf" alt="Python Badge"/>
    <img src="https://img.shields.io/badge/FastAPI-blue?style=for-the-badge&logo=fastapi&logoColor=white&color=brightgreen" alt="FastAPI Badge"/>
    <img src="https://img.shields.io/badge/Postgres-green?style=for-the-badge&logo=postgresql&logoColor=white&color=informational" alt="Postgresql Badge"/>
    <img src="https://img.shields.io/badge/Tortoise-green?style=for-the-badge&logo=tortoise-orm&logoColor=white&color=informational" alt="Tortoise Badge"/>
    <img src="https://img.shields.io/badge/Docker-blue?style=for-the-badge&logo=docker&logoColor=white&color=blue" alt="Docker Badge"/>
    <img src="https://img.shields.io/badge/Pytest-blue?style=for-the-badge&logo=pytest&logoColor=white&color=brightgreen" alt="Pytest Badge"/>
    <img src="https://img.shields.io/badge/Aerich-blue?style=for-the-badge&logo=aerich&logoColor=white&color=red" alt="Aerich Badge"/>
  </div>
  <h2>Запуск проекта</h2>
  <ul>
  <li>Скачать и установить <a href='https://docs.docker.com/get-docker/'>Docker</a></li>
  <li>Клонировать репозиторий: <code> git clone https://github.com/KLYMENKORUS/SMIT.Studio-Test.git</code></li>
  <li>Установить зависимости: <code>pip install -r requirements.txt</code></li>
  <li>На уровне с корневой директорией <code>src</code> создать файл .env и заполнить его по примеру .env.example</li>
  <li>Выполнить команду <code>docker compose -f docker-compose.yaml up -d</code></li>
  <li>Запустить тесты <code>pytest tests</code></li>
  <li>Выполнить команду <code>aerich upgrade</code></li>
  <li>Запустить сервер: <code>uvicorn app:create_app --reload</code></li>
  </ul>
