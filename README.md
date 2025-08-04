# 💬 Xat Pub/Sub amb Redis i Flask – `chat-pubsub-final`

Un xat en temps real implementat amb **Flask**, **Redis** i el patró **Publish/Subscribe (Pub/Sub)**. Aquest projecte mostra com crear una arquitectura lleugera de missatgeria sense connexions directes entre clients.

## 📌 Què és Pub/Sub?

**Pub/Sub** (Publish/Subscribe) és un patró on:

- Els **publishers** envien missatges a un canal
- Els **subscribers** escolten aquest canal
- Cap dels dos no ha de conèixer l'altre

Això fa que el sistema sigui:
- Escalable
- Flexible
- Desacoblat

Aquest projecte és un exemple pràctic d'això, usant **Redis com a sistema de pub/sub** i **Flask com a servidor web**.

## ⚙️ Tecnologies utilitzades

- 🐍 Python 3.11
- 🔥 Flask
- 🧠 Redis
- 🐳 Docker + Docker Compose
- 🌐 HTML + JavaScript (SSE - Server-Sent Events)

## 🧱 Arquitectura del sistema

Usuari navegador
     ↓         ↑
  [ HTML + JS ] (SSE + POST)
       ↓         ↑
   Flask (app.py) ←→ Redis Pub/Sub

## ▶️ Com executar

1. **Clona el repositori**:

```bash
git clone https://github.com/el-teu-usuari/chat-pubsub-final.git
cd chat-pubsub-final
```

2. **Executa amb Docker Compose**:

```bash
docker-compose up --build
```

3. **Obre el navegador**:

```
http://localhost:5000
```

## 🔄 Exemple amb Redis CLI (manual)

Obre dues terminals al contenidor Redis:

**1. Subscriu-te al canal**:
```bash
docker exec -it chat-pubsub-final-redis-1 redis-cli
> SUBSCRIBE chat
```

**2. Publica un missatge**:
```bash
docker exec -it chat-pubsub-final-redis-1 redis-cli
> PUBLISH chat "Hola des de Redis CLI!"
```
