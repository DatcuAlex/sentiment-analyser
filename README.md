# Sentiment Analyser

Acesta este un proiect pentru a învăța cum să pun un model de AI într-un mediu propriu.

- Folosește un model de AI (DistilBERT) pentru a ghici sentimentul unui text.
- Expune modelul printr-un **API** creat cu FastAPI.
- Tot sistemul este „împachetat” în **Docker**, deci poate fi rulat oriunde fără instalări complicate.
- Include un server de **Prometheus** care monitorizează în timp real câte cereri procesează AI-ul.

## Tehnologii utilizate
- **Backend:** Python & FastAPI
- **AI:** HuggingFace (Transformers & PyTorch)
- **Infrastructure:** Docker & Docker Compose
- **Monitorizare:** Prometheus
- **Automatizare:** GitHub Actions (pentru verificarea build-ului)

```bash
docker-compose up --build