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

**SSE (Server-Sent Events)** és una tecnologia web que permet que un servidor envie dades al navegador del client en temps real mitjançant una connexió HTTP unidireccional i persistent:

- El servidor envia dades de forma contínua al client
- Basat en HTTP, no cal cap protocol especial com WebSockets
- El client escolta, però no pot respondre per aquest canal
- Ideal per xats, dashboards, notificacions o actualitzacions en temps real

**Avantatges d'SSE**

- Senzill d’implementar (només HTML + Flask)
- No cal obrir cap connexió especial ni configurar WebSockets
- Manté una connexió viva de llarga durada per enviar dades

Pel que fa a **Flask** és un microframework web per a Python que permet crear aplicacions web de manera ràpida, senzilla i flexible.

## Com pots provar-lo

1. **Clona el repositori**:

```bash
git clone https://github.com/iesbillenguatges/xat-pub-sub.git
cd xat-pub-sub
```

2. **Executa amb Docker Compose**:

```bash
docker-compose up --build
```

3. **Obre el navegador**:

```
http://localhost:5000
```
