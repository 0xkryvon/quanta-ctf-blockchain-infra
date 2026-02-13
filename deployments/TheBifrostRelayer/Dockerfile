FROM dimasmaualana/eth:latest

COPY deploy/ /home/ctf/

COPY contracts /tmp/contracts
COPY foundry.toml /tmp/foundry.toml

# Copy modified launcher with challenge name injection
COPY launcher.py /usr/lib/python/sandbox/launcher.py

RUN true \
    && cd /home/ctf \
    && pip install -r requirements.txt --break-system-packages \
    && cd /tmp \
    && forge build --out /home/ctf/compiled \
    && rm -rf /tmp/contracts \
    && true
