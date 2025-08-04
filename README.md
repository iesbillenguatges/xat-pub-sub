# 💬 Xat Pub/Sub amb Redis i Flask – iesbi_np

Un xat en temps real implementat amb **Flask**, **Redis** i el patró **Publish/Subscribe (Pub/Sub)**. Aquest projecte mostra com crear una arquitectura lleugera de missatgeria sense connexions directes entre clients.

## Què és Pub/Sub?

**Pub/Sub** (Publish/Subscribe) és un patró on:

- Els **publishers** envien missatges a un canal
- Els **subscribers** escolten aquest canal
- A cap dels dos li cal conèixer l'altre

Això fa que el sistema siga:
- Escalable
- Flexible
- Desacoblat

Aquest projecte és un exemple pràctic d'això, usant **Redis com a sistema de pub/sub** i **Flask com a servidor web**.

## Tecnologies utilitzades

- Python 3.11
- Flask
- Redis
- Docker + Docker Compose
- HTML + JavaScript (SSE - Server-Sent Events)

SSE (Server-Sent Events) és una tecnologia web que permet que un servidor envie dades al navegador del client en temps real mitjançant una connexió HTTP unidireccional i persistent:

- El servidor envia dades de forma contínua al client
- Basat en HTTP, no cal cap protocol especial com WebSockets
- El client escolta, però no pot respondre per aquest canal
- Ideal per xats, dashboards, notificacions o actualitzacions en temps real

**Com funciona:**

    El client fa una petició HTTP:

const evtSource = new EventSource('/stream');

El servidor respon amb dades en format especial:

data: Nou missatge!

data: Una altra actualització!

El navegador executa automàticament el codi associat:

    evtSource.onmessage = function(event) {
      console.log("Missatge rebut:", event.data);
    };

🆚 Comparat amb WebSockets:
Característica	SSE	WebSockets
Direcció	Unidireccional (server → client)	Bidireccional
Protocol	HTTP	Protocol WebSocket (ws://)
Suport navegadors	Excel·lent (excepte IE11)	Bo, però menys universal
Fàcil d'implementar	✅ Sí	❌ Més complex
Ideal per...	Notificacions, xats simples	Jocs, videotrucades, xats complexos
✅ Avantatges d'SSE

    Senzill d’implementar (només HTML + Flask)

    No cal obrir cap connexió especial ni configurar WebSockets

    Manté una connexió viva de llarga durada per enviar dades

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
