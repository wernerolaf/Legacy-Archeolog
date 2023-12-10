# Legacy-Archeolog
System for analysing legacy systems

# Submodules

Submodules progress:
* collector: done;
* embed: done;
* index: done;

# Commands

Collecting repo data:
```bash
python src/collector.py /path/to/repo ./commits.json
```

Generating embeddings:
```bash
python src/embed.py ./commits.json ./descriptions.json ./embeddings.npy ./system_prompt.txt
```

Generating index:
```bash
python src/index.py ./embeddings.npy ./index.pickle 10000
```

Searching:
```bash
python main.py ./descriptions.json ./index.pickle 5
```
