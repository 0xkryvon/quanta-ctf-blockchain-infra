# Cyber Summit Quanta CTF Blockchain Infra

This repository (forked from [TCP1P/TCP1P-CTF-Blockchain-Infra](https://github.com/TCP1P/TCP1P-CTF-Blockchain-Infra)) builds upon the original [paradigmxyz](https://github.com/paradigmxyz/paradigm-ctf-infrastructure/tree/master) infrastructure, adding a slick web interface and extra challenge setups. Think of it as your playground for exploring blockchain vulnerabilities in true CTF style.

### Launching Challenges
Each challenge runs via Docker Compose. For example, to run the Ethereum challenge:

```sh
cd ./challenge-eth
docker-compose up --build
```

If you want to lauch all challenges at once (recommended)
```sh
cd deployments/
./deploy-all.sh
```

Visit [http://127.0.0.1:48334/](http://127.0.0.1:48334/) in your browser. (Tip: The backend might take a few extra seconds to spin up.)

![Web Interface](image.png)

## Recommended Tools for Your Exploits

- **[Foundry](https://github.com/foundry-rs/foundry)** – A fast, flexible toolkit for Ethereum development.
- **[Foundpy](https://github.com/Wrth1/foundpy)** – Your Python sidekick for blockchain testing and automation.

## Official docker hub image

- https://hub.docker.com/r/dimasmaualana/eth