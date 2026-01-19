# 💻 Installations-Anleitung für Students

## Willkommen zum Bilderkenner-Projekt! 🚀

Diese Anleitung hilft dir, **alles Notwendige** auf deinem Computer einzurichten, bevor wir mit dem Online-Unterricht starten.

**Zeitaufwand:** Ca. 30-45 Minuten
**Schwierigkeit:** Anfänger-freundlich
---

## ✅ Checkliste - Was du brauchst:

- [ ] Windows, macOS oder Linux Computer
- [ ] Stabile Internet-Verbindung
- [ ] Mind. 5 GB freier Speicherplatz
- [ ] Administrator-Rechte (für Installation)

---

## Schritt 1: Python installieren (15 Min)

### Windows

#### 1.1 Download Python

1. Gehe zu: https://www.python.org/downloads/
2. Klicke auf **"Download Python 3.11.x"** (neueste Version)
3. Warte bis Download fertig ist

#### 1.2 Python installieren

1. **Doppelklick** auf die heruntergeladene Datei (z.B. `python-3.11.x-amd64.exe`)
2. ⚠️ **WICHTIG:** Setze Häkchen bei **"Add Python to PATH"** (ganz unten!)
3. Klicke auf **"Install Now"**
4. Warte bis Installation fertig
5. Klicke **"Close"**

#### 1.3 Python testen

1. Öffne **Command Prompt** (CMD):
   - Windows-Taste drücken
   - Tippe: `cmd`
   - Enter drücken

2. Teste Python:
```cmd
python --version
```

**Erwartete Ausgabe:**
```
Python 3.11.x
```

✅ **Wenn du die Version siehst: Perfekt!**
❌ **Wenn Fehler:** Python wurde nicht zu PATH hinzugefügt → Neu installieren mit Häkchen!

### macOS

#### 1.1 Prüfe ob Python installiert ist

1. Öffne **Terminal**:
   - CMD + Space
   - Tippe: `terminal`
   - Enter

2. Prüfe Version:
```bash
python3 --version
```

#### 1.2 Python installieren (falls nötig)

**Option 1: Homebrew (empfohlen)**
```bash
# 1. Homebrew installieren (falls nicht vorhanden)
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# 2. Python installieren
brew install python@3.11
```

**Option 2: Von python.org**
1. https://www.python.org/downloads/macos/
2. Download und installieren wie bei Windows

### Linux (Ubuntu/Debian)

```bash
# Update package list
sudo apt update

# Install Python 3.11
sudo apt install python3.11 python3.11-venv python3-pip

# Verify
python3 --version
```

---

## Schritt 2: PyCharm installieren (10 Min)

### 2.1 Download PyCharm Community Edition (kostenlos!)

1. Gehe zu: https://www.jetbrains.com/pycharm/download/
2. Wähle dein **Betriebssystem** (Windows/macOS/Linux)
3. Klicke auf **"Download"** unter **"Community"** (NICHT Professional!)
4. Warte bis Download fertig

### 2.2 PyCharm installieren

**Windows:**
1. Doppelklick auf `.exe` Datei
2. Folge dem Installations-Assistenten
3. Empfohlene Optionen:
   - ✅ Create Desktop Shortcut
   - ✅ Add "bin" folder to PATH
   - ✅ .py file association
4. Installieren → Fertig → Restart (falls nötig)

**macOS:**
1. Öffne `.dmg` Datei
2. Ziehe PyCharm in den **Applications** Ordner
3. Öffne PyCharm aus Applications
4. Bei "App aus dem Internet": Öffnen erlauben

**Linux:**
1. Entpacke das `.tar.gz` Archiv
2. Terminal öffnen im entpackten Ordner
3. Ausführen:
```bash
cd bin
./pycharm.sh
```

### 2.3 PyCharm erste Einrichtung

1. **Starte PyCharm**
2. Bei erstem Start:
   - ✅ Accept Terms & Conditions
   - Theme wählen (hell/dunkel - egal)
   - ✅ Don't send usage statistics (optional)

---

## Schritt 3: Git installieren (10 Min)

### Windows

#### 3.1 Git für Windows downloaden

1. Gehe zu: https://git-scm.com/download/win
2. Download startet automatisch
3. Warte bis fertig

#### 3.2 Git installieren

1. Doppelklick auf `.exe` Datei
2. **Wichtige Einstellungen** während Installation:

   **Bei "Select Components":**
   - ✅ Git Bash Here
   - ✅ Git GUI Here

   **Bei "Choosing the default editor":**
   - Wähle: "Use Visual Studio Code" oder "Nano"

   **Bei "Adjusting PATH":**
   - ✅ **"Git from the command line and also from 3rd-party software"**

   **Rest:** Einfach "Next" klicken (Standardeinstellungen OK)

3. **Finish** klicken

#### 3.3 Git testen

```cmd
git --version
```

**Erwartete Ausgabe:**
```
git version 2.x.x
```

### macOS

**Option 1: Mit Homebrew (empfohlen)**
```bash
brew install git
```

**Option 2: Xcode Command Line Tools**
```bash
xcode-select --install
```

**Testen:**
```bash
git --version
```

### Linux

```bash
# Ubuntu/Debian
sudo apt install git

# Fedora
sudo dnf install git

# Testen
git --version
```

### Git konfigurieren (ALLE Systeme)

⚠️ **Wichtig:** Ersetze mit DEINEN Daten!

```bash
# Dein Name (wird in Commits angezeigt)
git config --global user.name "Dein Name"

# Deine Email
git config --global user.email "deine.email@example.com"

# Prüfen
git config --global --list
```

---

## Schritt 4: Projekt vorbereiten (5 Min)

### 4.1 Arbeitsordner erstellen

**Windows (CMD):**
```cmd
# Navigiere zu deinem Benutzer-Ordner
cd %USERPROFILE%

# Erstelle Projekt-Ordner
mkdir bilderkenner-projekt
cd bilderkenner-projekt
```

**macOS/Linux (Terminal):**
```bash
# Navigiere zu Home
cd ~

# Erstelle Projekt-Ordner
mkdir bilderkenner-projekt
cd bilderkenner-projekt
```

### 4.2 PyCharm Projekt erstellen

1. **Öffne PyCharm**
2. Klicke **"New Project"**
3. **Location:** Wähle deinen `bilderkenner-projekt` Ordner
4. **Python Interpreter:**
   - ✅ "New environment using Virtualenv"
   - Location: `bilderkenner-projekt/venv`
   - Base interpreter: Python 3.11 (was du installiert hast)
5. Klicke **"Create"**

⏳ **Warte** bis PyCharm fertig ist (Status-Bar unten rechts)

### 4.3 Terminal in PyCharm öffnen

1. In PyCharm: **View → Tool Windows → Terminal**
2. Oder: **Alt + F12** (Shortcut)

Du solltest jetzt ein Terminal **INNERHALB** von PyCharm sehen!

---

## Schritt 5: Python Pakete installieren (5 Min)

### 5.1 requirements.txt erstellen

1. **In PyCharm:** Rechtsklick auf Projekt → **New → File**
2. Name: `requirements.txt`
3. **Enter** drücken

4. Kopiere folgenden Inhalt in die Datei:

```txt
torch==2.1.0
torchvision==0.16.0
fastapi==0.104.1
uvicorn==0.24.0
python-multipart==0.0.6
pillow==10.1.0
pytest==7.4.3
numpy==1.24.3
matplotlib==3.8.0
```

5. **Speichern:** Ctrl+S (Windows/Linux) oder Cmd+S (macOS)

### 5.2 Pakete installieren

**Im PyCharm Terminal (unten):**

```bash
pip install -r requirements.txt
```

⏳ **Das dauert 5-10 Minuten!** (Download + Installation)

**Was passiert:**
- PyTorch: Deep Learning Framework (~800 MB!)
- FastAPI: Web Framework für API
- PIL/Pillow: Bildverarbeitung
- pytest: Testing
- etc.

**Fortschritt:**
```
Collecting torch==2.1.0
  Downloading torch-2.1.0-cp311-cp311-win_amd64.whl (191 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━ 191/191 MB 5.2 MB/s
...
Successfully installed ...
```

✅ **Wenn am Ende "Successfully installed" steht: Perfekt!**

### 5.3 Installation testen

**Im Terminal:**

```bash
python -c "import torch; print('PyTorch:', torch.__version__)"
python -c "import fastapi; print('FastAPI: OK')"
python -c "from PIL import Image; print('Pillow: OK')"
```

**Erwartete Ausgabe:**
```
PyTorch: 2.1.0+cpu
FastAPI: OK
Pillow: OK
```

---

## Schritt 6: Git Repository initialisieren (5 Min)

### 6.1 Git initialisieren

**Im PyCharm Terminal:**

```bash
# Git Repository initialisieren
git init

# Prüfen
git status
```

**Ausgabe sollte sein:**
```
Initialized empty Git repository in .../bilderkenner-projekt/.git/
On branch main (oder master)
No commits yet
```

### 6.2 .gitignore erstellen

1. **In PyCharm:** Neue Datei erstellen: `.gitignore`
2. Kopiere folgenden Inhalt:

```gitignore
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
env/
venv/
*.egg-info/
dist/
build/

# PyCharm
.idea/

# Data & Models
*.pth
*.pkl
data/raw/
data/processed/
saved_models/*.pth

# OS
.DS_Store
Thumbs.db
*.swp
```

3. **Speichern**

### 6.3 Erster Commit

```bash
# Alle Dateien hinzufügen
git add .

# Erster Commit
git commit -m "Initial project setup"

# Prüfen
git log
```

**Du solltest deinen ersten Commit sehen!**

---

## Schritt 7: Test-Setup (5 Min)

### 7.1 Einfache Test-Datei erstellen

1. Neue Python Datei: `test_setup.py`
2. Kopiere:

```python
"""
Test ob alles funktioniert
"""
import sys
import torch
import torchvision
import fastapi
from PIL import Image
import numpy as np


def test_python_version():
    """Test Python Version"""
    version = sys.version_info
    print(f"✓ Python {version.major}.{version.minor}.{version.micro}")
    assert version.major == 3
    assert version.minor >= 9


def test_pytorch():
    """Test PyTorch"""
    print(f"✓ PyTorch {torch.__version__}")
    # Einfacher Tensor Test
    x = torch.tensor([1.0, 2.0, 3.0])
    assert x.sum().item() == 6.0
    print("✓ PyTorch funktioniert!")


def test_torchvision():
    """Test torchvision"""
    print(f"✓ torchvision {torchvision.__version__}")
    # Test Transform
    from torchvision import transforms
    transform = transforms.ToTensor()
    print("✓ torchvision funktioniert!")


def test_pillow():
    """Test PIL/Pillow"""
    from PIL import __version__
    print(f"✓ Pillow {__version__}")
    # Erstelle dummy image
    img = Image.new('RGB', (100, 100), color='red')
    assert img.size == (100, 100)
    print("✓ Pillow funktioniert!")


def test_numpy():
    """Test NumPy"""
    print(f"✓ NumPy {np.__version__}")
    arr = np.array([1, 2, 3])
    assert arr.sum() == 6
    print("✓ NumPy funktioniert!")


def test_fastapi():
    """Test FastAPI"""
    print(f"✓ FastAPI {fastapi.__version__}")
    print("✓ FastAPI importiert!")


if __name__ == "__main__":
    print("=" * 50)
    print("SYSTEM CHECK - Teste Installation")
    print("=" * 50)

    try:
        test_python_version()
        test_pytorch()
        test_torchvision()
        test_pillow()
        test_numpy()
        test_fastapi()

        print("=" * 50)
        print("✅ ALLE TESTS BESTANDEN!")
        print("✅ Dein System ist bereit für den Unterricht!")
        print("=" * 50)
    except Exception as e:
        print("=" * 50)
        print(f"❌ FEHLER: {e}")
        print("=" * 50)
```

### 7.2 Test ausführen

**Im Terminal:**

```bash
python test_setup.py
```

**Erwartete Ausgabe:**
```
==================================================
SYSTEM CHECK - Teste Installation
==================================================
✓ Python 3.11.x
✓ PyTorch 2.1.0+cpu
✓ PyTorch funktioniert!
✓ torchvision 0.16.0+cpu
✓ torchvision funktioniert!
✓ Pillow 10.1.0
✓ Pillow funktioniert!
✓ NumPy 1.24.3
✓ NumPy funktioniert!
✓ FastAPI 0.104.1
✓ FastAPI importiert!
==================================================
✅ ALLE TESTS BESTANDEN!
✅ Dein System ist bereit für den Unterricht!
==================================================
```

✅ **Wenn alle Tests bestehen: Du bist fertig!**

---

## ❓ Troubleshooting - Häufige Probleme

### Problem 1: "python ist kein interner oder externer Befehl"

**Lösung:**
- Python wurde nicht zu PATH hinzugefügt
- **Windows:** Python NEU installieren mit "Add to PATH" Häkchen!
- **Alternative:** Nutze `py` statt `python`

### Problem 2: "pip: command not found"

**Windows:**
```cmd
python -m pip install --upgrade pip
```

**macOS/Linux:**
```bash
python3 -m pip install --upgrade pip
```

### Problem 3: PyTorch Installation schlägt fehl

**Grund:** Oft Speicherplatz oder Internet

**Lösung:**
```bash
# Nur CPU Version (kleiner)
pip install torch torchvision --index-url https://download.pytorch.org/whl/cpu
```

### Problem 4: "Permission denied"

**macOS/Linux:**
```bash
# Mit sudo (Administrator)
sudo pip install -r requirements.txt
```

**Besser:** Virtual Environment nutzen (sollte PyCharm automatisch machen)

### Problem 5: PyCharm findet Python nicht

1. **File → Settings** (Windows/Linux) oder **PyCharm → Preferences** (macOS)
2. **Project → Python Interpreter**
3. **Add Interpreter → Add Local Interpreter**
4. Wähle Python Installation (z.B. `C:\Python311\python.exe`)

### Problem 6: Git funktioniert nicht in PyCharm

1. **Settings → Version Control → Git**
2. **Path to Git executable:** Klicke "..."
3. Wähle Git:
   - Windows: `C:\Program Files\Git\bin\git.exe`
   - macOS: `/usr/local/bin/git`
   - Linux: `/usr/bin/git`

### Problem 7: Import Errors trotz Installation

**Lösung:** Stelle sicher, dass du im richtigen Environment bist

**Im Terminal:**
```bash
# Sollte (venv) am Anfang zeigen
(venv) C:\...\bilderkenner-projekt>

# Falls nicht:
# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

---

## 📸 Screenshots - Wie soll es aussehen?

### ✅ Korrektes PyCharm Setup:

```
PyCharm
├── Project: bilderkenner-projekt
│   ├── venv/ (Virtual Environment - grau)
│   ├── requirements.txt
│   ├── test_setup.py
│   └── .gitignore
│
└── Terminal (unten):
    (venv) C:\Users\...\bilderkenner-projekt>
```

### ✅ Korrektes Git Setup:

```bash
git status
# Output:
On branch main
nothing to commit, working tree clean
```

### ✅ Korrekte Python Installation:

```bash
python --version
# Output: Python 3.11.x

pip list
# Output: Liste mit torch, fastapi, etc.
```

---

## 🎯 Final Checklist

Gehe diese Liste durch, bevor der Unterricht startet:

### Software installiert:
- [ ] Python 3.11+ (`python --version` funktioniert)
- [ ] PyCharm Community Edition (öffnet sich)
- [ ] Git (`git --version` funktioniert)

### PyCharm Setup:
- [ ] Projekt erstellt: `bilderkenner-projekt`
- [ ] Virtual Environment aktiv (zeigt `(venv)`)
- [ ] Terminal in PyCharm funktioniert

### Pakete installiert:
- [ ] `requirements.txt` existiert
- [ ] Alle Pakete installiert (`pip list` zeigt torch, etc.)
- [ ] `test_setup.py` läuft durch (alle ✓)

### Git Setup:
- [ ] Repository initialisiert (`git status` funktioniert)
- [ ] `.gitignore` existiert
- [ ] Erster Commit gemacht (`git log` zeigt Commit)

### Bereit für Unterricht:
- [ ] Internet-Verbindung stabil
- [ ] Mikrofon & Kamera (für Online-Unterricht)
- [ ] Bildschirm groß genug (empf. 2 Monitore oder großer Screen)
- [ ] Notizen-App bereit (OneNote, Notion, etc.)

---

## 📞 Support & Hilfe

### Vor dem Unterricht:

**Bei Problemen:**
1. Lies Troubleshooting-Section oben
2. Google den Fehler (oft gibt es Lösungen)
3. Screenshot machen von Fehlermeldung
4. Im Unterricht fragen

### Hilfreiche Links:

- **Python Docs:** https://docs.python.org/3/
- **PyCharm Guide:** https://www.jetbrains.com/help/pycharm/
- **Git Basics:** https://git-scm.com/book/en/v2/Getting-Started-First-Time-Git-Setup
- **PyTorch:** https://pytorch.org/get-started/locally/

### Im Unterricht:

- ✅ Fragen stellen ist erwünscht!
- ✅ Screen-Sharing bei Problemen
- ✅ Chat nutzen für technische Fragen
- ✅ Andere Students helfen sich gegenseitig

---

## 🎉 Geschafft!

**Wenn du bis hier gekommen bist und alle Checkboxen ✅ sind:**

🎊 **HERZLICHEN GLÜCKWUNSCH!** 🎊

Du bist **vollständig vorbereitet** für den Online-Unterricht!

### Was kommt als Nächstes?

1. **Warte auf Unterrichtsbeginn**
2. **Halte diese Anleitung griffbereit**
3. **Öffne PyCharm**
4. **Sei bereit zu lernen!** 🚀

### Tipps für den Unterricht:

💡 **Vor dem Unterricht:**
- [ ] Laptop vollständig geladen
- [ ] PyCharm schon geöffnet
- [ ] `test_setup.py` einmal laufen lassen
- [ ] Internet-Verbindung testen

💡 **Während dem Unterricht:**
- [ ] Aktiv mitmachen
- [ ] Fragen stellen
- [ ] Code selbst tippen (nicht nur copy-paste)
- [ ] Mit Team kommunizieren

💡 **Nach dem Unterricht:**
- [ ] Code committen: `git add .` → `git commit -m "..."`
- [ ] Notizen durchgehen
- [ ] Projekt weiterentwickeln

---

**Viel Erfolg! Wir sehen uns im Unterricht! 🚀**

---

*Bei Fragen zur Installation: Bitte Screenshot von Fehlermeldung machen und im Unterricht zeigen!*
