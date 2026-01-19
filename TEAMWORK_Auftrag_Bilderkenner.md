# Teamwork-Session: Bilderkenner Backend

## 🎯 Mission

Ihr sollt als Team ein **Bilderkenner-Backend** entwickeln, das Bilder klassifizieren kann.

**Ziele:**
- ✅ Teamarbeit mit Git lernen
- ✅ Backend-Entwicklung mit Python
- ✅ CNN/Deep Learning praktisch umsetzen
- ✅ Professionelle Workflows etablieren

---

## 👥 Team-Struktur

Es gibt **4 Teams** mit jeweils unterschiedlichen Aufgaben. Jedes Team hat 3-4 Personen.

### Team 1: Data Pipeline Team 🗂️
**Verantwortlich für:** Daten laden, verarbeiten, augmentieren

### Team 2: Model Team 🧠
**Verantwortlich für:** CNN-Architektur, Training, Optimierung

### Team 3: API Team 🌐
**Verantwortlich für:** REST API, Endpoints, Request Handling

### Team 4: Testing & Deployment Team 🧪
**Verantwortlich für:** Tests, CI/CD, Dokumentation

---

## 📋 Projekt-Übersicht

### Was wird gebaut?

Ein Backend-System für Bilderkennung mit folgenden Features:
- Upload von Bildern über API
- Klassifikation in 10 Kategorien (CIFAR-10)
- Rückgabe von Vorhersage + Konfidenz
- Logging und Monitoring
- Tests und Dokumentation

### Tech Stack

```
Python 3.9+
├── PyTorch (Deep Learning)
├── FastAPI (REST API)
├── Pillow (Bildverarbeitung)
├── pytest (Testing)
└── Git (Versionskontrolle)
```

### Projekt-Struktur

```
bilderkenner-backend/
├── .git/
├── .gitignore
├── requirements.txt
├── README.md
│
├── data/                    # Team 1
│   ├── __init__.py
│   ├── dataset.py
│   ├── transforms.py
│   └── dataloader.py
│
├── models/                  # Team 2
│   ├── __init__.py
│   ├── cnn.py
│   ├── train.py
│   └── predict.py
│
├── api/                     # Team 3
│   ├── __init__.py
│   ├── main.py
│   ├── routes.py
│   └── schemas.py
│
├── tests/                   # Team 4
│   ├── test_data.py
│   ├── test_model.py
│   └── test_api.py
│
└── saved_models/
    └── .gitkeep
```

---

## 🚀 Setup & Git Workflow

### Initial Setup (Gemeinsam, 10 Min)

**Ein Team-Mitglied (Projekt-Lead) macht:**

```bash
# 1. Erstelle Projektordner
mkdir bilderkenner-backend
cd bilderkenner-backend

# 2. Git initialisieren
git init

# 3. Erstelle .gitignore
cat > .gitignore << EOF
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
env/
venv/
*.egg-info/

# PyCharm
.idea/

# Data & Models
*.pth
*.pkl
data/raw/
data/processed/

# OS
.DS_Store
Thumbs.db
EOF

# 4. Erstelle README
cat > README.md << EOF
# Bilderkenner Backend

KI-gestütztes Bilderkenner-Backend mit PyTorch und FastAPI.

## Team
- Team 1: Data Pipeline
- Team 2: Model Development
- Team 3: API Development
- Team 4: Testing & Deployment

## Installation
\`\`\`bash
pip install -r requirements.txt
\`\`\`

## Nutzung
\`\`\`bash
python api/main.py
\`\`\`
EOF

# 5. Erstelle requirements.txt
cat > requirements.txt << EOF
torch==2.1.0
torchvision==0.16.0
fastapi==0.104.1
uvicorn==0.24.0
python-multipart==0.0.6
pillow==10.1.0
pytest==7.4.3
numpy==1.24.3
EOF

# 6. Initial Commit
git add .
git commit -m "Initial project setup"

# 7. Erstelle Branches für Teams
git branch team1-data
git branch team2-model
git branch team3-api
git branch team4-testing

# 8. Optional: Remote Repository (GitHub)
# git remote add origin <REPOSITORY_URL>
# git push -u origin main
```

### Git Workflow für Teams

**Jedes Team arbeitet auf eigenem Branch:**

```bash
# Team 1 Mitglied
git checkout team1-data
git pull origin team1-data  # Falls remote

# Arbeiten...
git add .
git commit -m "Add dataset loader"
git push origin team1-data
```

**Merging in main (nach Review):**

```bash
# Checkout main
git checkout main

# Merge Team Branch
git merge team1-data

# Push to main
git push origin main
```

---

## 📝 Team-spezifische Aufträge

---

## Team 1: Data Pipeline Team 🗂️

### Eure Aufgaben

1. ✅ Dataset laden (CIFAR-10)
2. ✅ Data Transformations (Augmentation)
3. ✅ DataLoader erstellen
4. ✅ Preprocessing Pipeline

### Auftrag 1.1: Dataset Loader (`data/dataset.py`)

```python
"""
Dataset Loader für CIFAR-10
"""
import torch
from torchvision import datasets, transforms
from torch.utils.data import DataLoader


class CIFAR10Dataset:
    """
    CIFAR-10 Dataset Handler

    Klassen:
    0: Flugzeug
    1: Auto
    2: Vogel
    3: Katze
    4: Hirsch
    5: Hund
    6: Frosch
    7: Pferd
    8: Schiff
    9: LKW
    """

    def __init__(self, data_dir='./data/cifar10'):
        self.data_dir = data_dir
        self.classes = ['Flugzeug', 'Auto', 'Vogel', 'Katze', 'Hirsch',
                       'Hund', 'Frosch', 'Pferd', 'Schiff', 'LKW']

    def get_train_dataset(self, transform=None):
        """
        Lädt Training Dataset

        TODO:
        1. Nutze torchvision.datasets.CIFAR10
        2. Parameter: root=self.data_dir, train=True, download=True
        3. Wende transform an (wenn gegeben)
        4. Returniere dataset
        """
        # DEIN CODE HIER
        pass

    def get_test_dataset(self, transform=None):
        """
        Lädt Test Dataset

        TODO:
        1. Nutze torchvision.datasets.CIFAR10
        2. Parameter: root=self.data_dir, train=False, download=True
        3. Wende transform an
        4. Returniere dataset
        """
        # DEIN CODE HIER
        pass

    def get_class_name(self, class_idx):
        """Gibt Klassennamen für Index zurück"""
        return self.classes[class_idx]


# BEISPIEL-NUTZUNG (zum Testen):
if __name__ == "__main__":
    dataset_handler = CIFAR10Dataset()
    train_data = dataset_handler.get_train_dataset()
    print(f"Training Samples: {len(train_data)}")
    print(f"Klassen: {dataset_handler.classes}")
```

### Auftrag 1.2: Transformations (`data/transforms.py`)

```python
"""
Data Transformations und Augmentation
"""
from torchvision import transforms


def get_train_transforms():
    """
    Transformations für Training mit Augmentation

    TODO:
    1. Erstelle transforms.Compose() mit:
       - RandomHorizontalFlip(p=0.5)
       - RandomCrop(32, padding=4)
       - ToTensor()
       - Normalize(mean=(0.5, 0.5, 0.5), std=(0.5, 0.5, 0.5))
    2. Returniere transform

    Warum Augmentation?
    - Mehr Trainingsdaten
    - Bessere Generalisierung
    - Robustheit gegen Variationen
    """
    # DEIN CODE HIER
    pass


def get_test_transforms():
    """
    Transformations für Testing (OHNE Augmentation)

    TODO:
    1. Erstelle transforms.Compose() mit:
       - ToTensor()
       - Normalize(mean=(0.5, 0.5, 0.5), std=(0.5, 0.5, 0.5))
    2. Returniere transform
    """
    # DEIN CODE HIER
    pass


# BEISPIEL
if __name__ == "__main__":
    train_t = get_train_transforms()
    test_t = get_test_transforms()
    print("Train Transforms:", train_t)
    print("Test Transforms:", test_t)
```

### Auftrag 1.3: DataLoader (`data/dataloader.py`)

```python
"""
DataLoader Setup
"""
import torch
from torch.utils.data import DataLoader
from .dataset import CIFAR10Dataset
from .transforms import get_train_transforms, get_test_transforms


def get_train_loader(batch_size=128, num_workers=2):
    """
    Erstellt Training DataLoader

    TODO:
    1. Hole train_transforms
    2. Erstelle CIFAR10Dataset instance
    3. Hole train_dataset mit transform
    4. Erstelle DataLoader:
       - dataset=train_dataset
       - batch_size=batch_size
       - shuffle=True (wichtig für Training!)
       - num_workers=num_workers
    5. Returniere loader

    Parameter:
        batch_size: Anzahl Samples pro Batch
        num_workers: Parallel Workers für Daten laden
    """
    # DEIN CODE HIER
    pass


def get_test_loader(batch_size=128, num_workers=2):
    """
    Erstellt Test DataLoader

    TODO:
    1. Hole test_transforms
    2. Erstelle CIFAR10Dataset instance
    3. Hole test_dataset mit transform
    4. Erstelle DataLoader:
       - dataset=test_dataset
       - batch_size=batch_size
       - shuffle=False (für konsistente Evaluation)
       - num_workers=num_workers
    5. Returniere loader
    """
    # DEIN CODE HIER
    pass


# TEST
if __name__ == "__main__":
    train_loader = get_train_loader(batch_size=4)

    # Teste einen Batch
    images, labels = next(iter(train_loader))
    print(f"Batch Shape: {images.shape}")  # Should be [4, 3, 32, 32]
    print(f"Labels: {labels}")
```

### Git Commits für Team 1

```bash
# Nach jedem Auftrag committen!

# Nach 1.1
git add data/dataset.py
git commit -m "Add CIFAR-10 dataset loader"

# Nach 1.2
git add data/transforms.py
git commit -m "Add data transformations and augmentation"

# Nach 1.3
git add data/dataloader.py
git commit -m "Add DataLoader setup"

# Push
git push origin team1-data
```

### Akzeptanzkriterien Team 1

- [ ] CIFAR-10 wird korrekt geladen
- [ ] Train/Test Split funktioniert
- [ ] Augmentation wird angewendet
- [ ] DataLoader liefert korrekte Batches
- [ ] Code ist dokumentiert
- [ ] Alle Commits haben sinnvolle Messages

---

## Team 2: Model Team 🧠

### Eure Aufgaben

1. ✅ CNN Architektur definieren
2. ✅ Training Loop implementieren
3. ✅ Model speichern/laden
4. ✅ Prediction Funktion

### Auftrag 2.1: CNN Architektur (`models/cnn.py`)

```python
"""
Convolutional Neural Network für CIFAR-10
"""
import torch
import torch.nn as nn
import torch.nn.functional as F


class SimpleCNN(nn.Module):
    """
    Einfaches CNN für Bildklassifikation

    Architektur:
    - 3 Convolutional Blocks (Conv → ReLU → MaxPool)
    - 2 Fully Connected Layers
    - Output: 10 Klassen
    """

    def __init__(self, num_classes=10):
        super(SimpleCNN, self).__init__()

        """
        TODO: Definiere Layer

        Convolutional Layers:
        1. self.conv1 = nn.Conv2d(3, 32, kernel_size=3, padding=1)
        2. self.conv2 = nn.Conv2d(32, 64, kernel_size=3, padding=1)
        3. self.conv3 = nn.Conv2d(64, 128, kernel_size=3, padding=1)

        Pooling:
        - self.pool = nn.MaxPool2d(2, 2)

        Fully Connected:
        - self.fc1 = nn.Linear(128 * 4 * 4, 512)
        - self.fc2 = nn.Linear(512, num_classes)

        Dropout (Regularisierung):
        - self.dropout = nn.Dropout(0.5)

        Warum diese Größen?
        - Input: 32x32x3 (CIFAR-10)
        - Nach Conv1 + Pool: 16x16x32
        - Nach Conv2 + Pool: 8x8x64
        - Nach Conv3 + Pool: 4x4x128
        - Flatten: 4*4*128 = 2048
        """
        # DEIN CODE HIER
        pass

    def forward(self, x):
        """
        Forward Pass

        TODO:
        1. Conv Block 1: conv1 → relu → pool
        2. Conv Block 2: conv2 → relu → pool
        3. Conv Block 3: conv3 → relu → pool
        4. Flatten: x.view(x.size(0), -1)
        5. FC1: fc1 → relu → dropout
        6. FC2: fc2 (Output)
        7. Return x

        Parameter:
            x: Input Tensor [batch_size, 3, 32, 32]

        Returns:
            Output Tensor [batch_size, 10]
        """
        # DEIN CODE HIER
        pass


# TEST
if __name__ == "__main__":
    model = SimpleCNN(num_classes=10)

    # Test mit random input
    test_input = torch.randn(4, 3, 32, 32)  # Batch von 4 Bildern
    output = model(test_input)

    print(f"Model Architecture:\n{model}")
    print(f"\nInput Shape: {test_input.shape}")
    print(f"Output Shape: {output.shape}")  # Should be [4, 10]
    print(f"Parameters: {sum(p.numel() for p in model.parameters()):,}")
```

### Auftrag 2.2: Training (`models/train.py`)

```python
"""
Model Training
"""
import torch
import torch.nn as nn
import torch.optim as optim
from tqdm import tqdm
import sys
sys.path.append('..')
from data.dataloader import get_train_loader, get_test_loader
from models.cnn import SimpleCNN


def train_model(epochs=10, batch_size=128, learning_rate=0.001, device='cpu'):
    """
    Trainiert das CNN Model

    TODO:
    1. Erstelle Model: model = SimpleCNN().to(device)
    2. Definiere Loss: criterion = nn.CrossEntropyLoss()
    3. Definiere Optimizer: optimizer = optim.Adam(model.parameters(), lr=learning_rate)
    4. Hole DataLoader: train_loader, test_loader
    5. Training Loop (siehe unten)
    6. Speichere Model

    Parameter:
        epochs: Anzahl Trainings-Durchläufe
        batch_size: Batch Größe
        learning_rate: Lernrate
        device: 'cuda' oder 'cpu'
    """

    # 1. Setup
    # DEIN CODE: Model, Loss, Optimizer, DataLoader

    # 2. Training Loop
    for epoch in range(epochs):
        model.train()  # Training Modus
        running_loss = 0.0
        correct = 0
        total = 0

        # Durch Batches iterieren
        for images, labels in tqdm(train_loader, desc=f'Epoch {epoch+1}/{epochs}'):
            """
            TODO:
            1. Verschiebe images, labels zu device
            2. Forward Pass: outputs = model(images)
            3. Berechne Loss: loss = criterion(outputs, labels)
            4. Zero Gradients: optimizer.zero_grad()
            5. Backward Pass: loss.backward()
            6. Update Weights: optimizer.step()
            7. Statistiken updaten
            """
            # DEIN CODE HIER
            pass

        # Epoch Statistiken
        train_accuracy = 100 * correct / total
        avg_loss = running_loss / len(train_loader)

        # Validation
        test_accuracy = evaluate_model(model, test_loader, device)

        print(f'Epoch [{epoch+1}/{epochs}]')
        print(f'  Train Loss: {avg_loss:.4f}, Train Acc: {train_accuracy:.2f}%')
        print(f'  Test Acc: {test_accuracy:.2f}%')

    # 3. Speichere Model
    torch.save({
        'model_state_dict': model.state_dict(),
        'optimizer_state_dict': optimizer.state_dict(),
        'epoch': epochs,
    }, '../saved_models/cifar10_cnn.pth')

    print("\n✓ Training abgeschlossen! Model gespeichert.")
    return model


def evaluate_model(model, test_loader, device):
    """
    Evaluiert Model auf Test Set

    TODO:
    1. model.eval()
    2. Deaktiviere Gradienten: with torch.no_grad()
    3. Iteriere durch test_loader
    4. Berechne Accuracy
    5. Return accuracy
    """
    # DEIN CODE HIER
    pass


# MAIN
if __name__ == "__main__":
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    print(f"Training auf: {device}")

    trained_model = train_model(
        epochs=10,
        batch_size=128,
        learning_rate=0.001,
        device=device
    )
```

### Auftrag 2.3: Prediction (`models/predict.py`)

```python
"""
Prediction und Inference
"""
import torch
from PIL import Image
from torchvision import transforms
from models.cnn import SimpleCNN


class ImageClassifier:
    """
    Wrapper für trained model - verwendet für API
    """

    def __init__(self, model_path='../saved_models/cifar10_cnn.pth', device='cpu'):
        """
        TODO:
        1. Lade Model: self.model = SimpleCNN()
        2. Lade Weights: checkpoint = torch.load(model_path)
        3. self.model.load_state_dict(checkpoint['model_state_dict'])
        4. self.model.to(device)
        5. self.model.eval()
        """
        self.device = device
        self.classes = ['Flugzeug', 'Auto', 'Vogel', 'Katze', 'Hirsch',
                       'Hund', 'Frosch', 'Pferd', 'Schiff', 'LKW']

        # DEIN CODE: Model laden
        pass

    def preprocess_image(self, image):
        """
        Bereitet Bild für Prediction vor

        TODO:
        1. Definiere Transform:
           - Resize(32, 32)
           - ToTensor()
           - Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
        2. Wende auf image an
        3. Füge Batch Dimension hinzu: .unsqueeze(0)
        4. Return tensor

        Parameter:
            image: PIL Image
        """
        # DEIN CODE HIER
        pass

    def predict(self, image):
        """
        Klassifiziert Bild

        TODO:
        1. Preprocess: tensor = self.preprocess_image(image)
        2. Verschiebe zu device
        3. Forward Pass: output = self.model(tensor)
        4. Softmax für Wahrscheinlichkeiten: probs = F.softmax(output, dim=1)
        5. Hole Top-Klasse: confidence, predicted = torch.max(probs, 1)
        6. Return predicted class und confidence

        Parameter:
            image: PIL Image oder path

        Returns:
            dict: {
                'class': 'Katze',
                'class_id': 3,
                'confidence': 0.95
            }
        """
        # DEIN CODE HIER
        pass


# TEST
if __name__ == "__main__":
    # Lade ein Test-Bild (muss existieren!)
    # test_image = Image.open('test.jpg')

    classifier = ImageClassifier(device='cpu')
    # result = classifier.predict(test_image)
    # print(result)
```

### Git Commits für Team 2

```bash
git add models/cnn.py
git commit -m "Add SimpleCNN architecture"

git add models/train.py
git commit -m "Implement training loop"

git add models/predict.py
git commit -m "Add prediction and inference"

git push origin team2-model
```

### Akzeptanzkriterien Team 2

- [ ] CNN kompiliert ohne Fehler
- [ ] Forward Pass funktioniert
- [ ] Training läuft durch
- [ ] Model wird gespeichert
- [ ] Prediction funktioniert
- [ ] Accuracy > 60% auf Test Set

---

## Team 3: API Team 🌐

### Eure Aufgaben

1. ✅ FastAPI Setup
2. ✅ Upload Endpoint
3. ✅ Prediction Endpoint
4. ✅ Response Schemas

### Auftrag 3.1: Main API (`api/main.py`)

```python
"""
FastAPI Hauptdatei
"""
from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
from PIL import Image
import io
import sys
sys.path.append('..')
from models.predict import ImageClassifier


# Erstelle FastAPI App
app = FastAPI(
    title="Bilderkenner API",
    description="KI-gestützte Bildklassifikation mit CNN",
    version="1.0.0"
)

# Initialisiere Classifier (global)
classifier = None


@app.on_event("startup")
async def startup_event():
    """
    Läuft beim Server-Start

    TODO:
    1. Initialisiere ImageClassifier
    2. Speichere in global classifier
    3. Print "Model geladen"
    """
    global classifier
    # DEIN CODE HIER
    pass


@app.get("/")
async def root():
    """
    Health Check Endpoint

    TODO:
    Return: {"status": "online", "message": "Bilderkenner API läuft"}
    """
    # DEIN CODE HIER
    pass


@app.get("/classes")
async def get_classes():
    """
    Gibt alle verfügbaren Klassen zurück

    TODO:
    Return: {"classes": classifier.classes}
    """
    # DEIN CODE HIER
    pass


@app.post("/predict")
async def predict_image(file: UploadFile = File(...)):
    """
    Hauptendpoint: Bild Upload und Klassifikation

    TODO:
    1. Prüfe File-Type (muss Bild sein)
    2. Lade Bild: contents = await file.read()
    3. Öffne mit PIL: image = Image.open(io.BytesIO(contents))
    4. Konvertiere zu RGB: image = image.convert('RGB')
    5. Predict: result = classifier.predict(image)
    6. Return result

    Fehlerbehandlung:
    - try/except für Fehler
    - HTTPException(status_code=400) bei Fehler

    Parameter:
        file: Hochgeladene Bilddatei

    Returns:
        JSON: {
            "class": "Katze",
            "class_id": 3,
            "confidence": 0.95,
            "filename": "cat.jpg"
        }
    """
    # DEIN CODE HIER
    pass


# Server starten
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

### Auftrag 3.2: Request Testing

Erstelle eine Test-Datei für manuelle API-Tests:

**`api/test_requests.py`:**

```python
"""
Manuelle API Tests mit requests
"""
import requests


def test_health_check():
    """Test / endpoint"""
    response = requests.get("http://localhost:8000/")
    print("Health Check:", response.json())


def test_get_classes():
    """Test /classes endpoint"""
    response = requests.get("http://localhost:8000/classes")
    print("Classes:", response.json())


def test_predict(image_path):
    """
    Test /predict endpoint

    TODO:
    1. Öffne Bild-Datei im binary mode
    2. POST Request zu http://localhost:8000/predict
    3. files={'file': open(image_path, 'rb')}
    4. Print Response
    """
    # DEIN CODE HIER
    pass


if __name__ == "__main__":
    print("Testing API...")

    test_health_check()
    test_get_classes()

    # TODO: Ersetze mit echtem Bildpfad
    # test_predict('test_image.jpg')
```

### Auftrag 3.3: Dokumentation

**`api/README.md`:**

```markdown
# API Dokumentation

## Endpoints

### GET /
Health Check

**Response:**
\`\`\`json
{
  "status": "online",
  "message": "Bilderkenner API läuft"
}
\`\`\`

### GET /classes
Liste aller Klassen

**Response:**
\`\`\`json
{
  "classes": ["Flugzeug", "Auto", "Vogel", ...]
}
\`\`\`

### POST /predict
Bild klassifizieren

**Request:**
- Form Data: `file` (image file)

**Response:**
\`\`\`json
{
  "class": "Katze",
  "class_id": 3,
  "confidence": 0.95,
  "filename": "cat.jpg"
}
\`\`\`

## Nutzung

### Server starten
\`\`\`bash
python api/main.py
\`\`\`

Server läuft auf: http://localhost:8000

### Swagger Docs
http://localhost:8000/docs

### cURL Beispiel
\`\`\`bash
curl -X POST "http://localhost:8000/predict" \\
  -H "accept: application/json" \\
  -H "Content-Type: multipart/form-data" \\
  -F "file=@test.jpg"
\`\`\`
```

### Git Commits für Team 3

```bash
git add api/main.py
git commit -m "Add FastAPI endpoints"

git add api/test_requests.py
git commit -m "Add API testing script"

git add api/README.md
git commit -m "Add API documentation"

git push origin team3-api
```

### Akzeptanzkriterien Team 3

- [ ] Server startet ohne Fehler
- [ ] Alle Endpoints erreichbar
- [ ] File Upload funktioniert
- [ ] Prediction gibt korrektes JSON zurück
- [ ] Fehlerbehandlung implementiert
- [ ] Dokumentation vollständig

---

## Team 4: Testing & Deployment Team 🧪

### Eure Aufgaben

1. ✅ Unit Tests schreiben
2. ✅ Integration Tests
3. ✅ CI/CD Setup (optional)
4. ✅ Projekt-Dokumentation

### Auftrag 4.1: Unit Tests (`tests/test_data.py`)

```python
"""
Tests für Data Pipeline
"""
import pytest
import sys
sys.path.append('..')
from data.dataset import CIFAR10Dataset
from data.transforms import get_train_transforms, get_test_transforms
from data.dataloader import get_train_loader, get_test_loader


def test_dataset_loading():
    """
    Test: CIFAR-10 wird geladen

    TODO:
    1. Erstelle CIFAR10Dataset()
    2. Hole train_dataset
    3. Assert len(train_dataset) == 50000
    4. Assert len(test_dataset) == 10000
    """
    # DEIN CODE HIER
    pass


def test_transforms():
    """
    Test: Transforms funktionieren

    TODO:
    1. Hole train_transforms
    2. Assert ist nicht None
    3. Teste auf einem dummy Bild
    """
    # DEIN CODE HIER
    pass


def test_dataloader():
    """
    Test: DataLoader liefert korrekte Batches

    TODO:
    1. Erstelle train_loader mit batch_size=4
    2. Hole einen Batch
    3. Assert images.shape == [4, 3, 32, 32]
    4. Assert labels.shape == [4]
    """
    # DEIN CODE HIER
    pass


def test_class_names():
    """Test: Klassennamen sind korrekt"""
    dataset = CIFAR10Dataset()
    assert len(dataset.classes) == 10
    assert 'Katze' in dataset.classes
    assert 'Hund' in dataset.classes
```

### Auftrag 4.2: Model Tests (`tests/test_model.py`)

```python
"""
Tests für Model
"""
import pytest
import torch
import sys
sys.path.append('..')
from models.cnn import SimpleCNN


def test_model_creation():
    """
    Test: Model kann erstellt werden

    TODO:
    1. model = SimpleCNN()
    2. Assert model ist nicht None
    3. Assert hat Parameter
    """
    # DEIN CODE HIER
    pass


def test_forward_pass():
    """
    Test: Forward Pass funktioniert

    TODO:
    1. Erstelle model
    2. Dummy input: torch.randn(1, 3, 32, 32)
    3. output = model(input)
    4. Assert output.shape == [1, 10]
    """
    # DEIN CODE HIER
    pass


def test_output_range():
    """
    Test: Output ist valide

    TODO:
    1. Forward pass
    2. Apply softmax
    3. Assert sum(probabilities) ≈ 1.0
    4. Assert all probabilities between 0 and 1
    """
    # DEIN CODE HIER
    pass
```

### Auftrag 4.3: API Tests (`tests/test_api.py`)

```python
"""
Tests für API
"""
import pytest
from fastapi.testclient import TestClient
import sys
sys.path.append('..')
from api.main import app

client = TestClient(app)


def test_root_endpoint():
    """
    Test: / endpoint

    TODO:
    1. response = client.get("/")
    2. Assert status_code == 200
    3. Assert response.json() hat 'status'
    """
    # DEIN CODE HIER
    pass


def test_classes_endpoint():
    """
    Test: /classes endpoint

    TODO:
    1. response = client.get("/classes")
    2. Assert status_code == 200
    3. Assert 'classes' in response.json()
    4. Assert len(classes) == 10
    """
    # DEIN CODE HIER
    pass


def test_predict_endpoint():
    """
    Test: /predict endpoint (mit mock image)

    TODO:
    1. Erstelle dummy image (PIL)
    2. Save to BytesIO
    3. POST zu /predict
    4. Assert response hat 'class', 'confidence'
    """
    # DEIN CODE HIER (optional, complex)
    pass
```

### Auftrag 4.4: Projekt README (`README.md`)

Erweitert das Haupt-README:

```markdown
# Bilderkenner Backend

KI-gestütztes Bilderkenner-Backend mit PyTorch und FastAPI.

## 📋 Features
- ✅ CIFAR-10 Bildklassifikation
- ✅ REST API mit FastAPI
- ✅ 10 Klassen: Flugzeug, Auto, Vogel, Katze, Hirsch, Hund, Frosch, Pferd, Schiff, LKW
- ✅ Confidence Scores
- ✅ Umfangreiche Tests

## 🚀 Installation

### Voraussetzungen
- Python 3.9+
- pip

### Setup
\`\`\`bash
# Repository klonen
git clone <URL>
cd bilderkenner-backend

# Dependencies installieren
pip install -r requirements.txt

# Model trainieren (optional)
python models/train.py

# Server starten
python api/main.py
\`\`\`

## 📖 Nutzung

### API Endpoints

**Health Check**
\`\`\`bash
curl http://localhost:8000/
\`\`\`

**Klassen abrufen**
\`\`\`bash
curl http://localhost:8000/classes
\`\`\`

**Bild klassifizieren**
\`\`\`bash
curl -X POST "http://localhost:8000/predict" \\
  -F "file=@test.jpg"
\`\`\`

### Swagger Dokumentation
http://localhost:8000/docs

## 🧪 Tests

\`\`\`bash
# Alle Tests
pytest

# Specific test file
pytest tests/test_data.py
pytest tests/test_model.py
pytest tests/test_api.py

# Mit Coverage
pytest --cov=.
\`\`\`

## 👥 Team

### Team 1: Data Pipeline
- [Namen]
- **Verantwortlich:** Dataset, Transformations, DataLoader

### Team 2: Model Development
- [Namen]
- **Verantwortlich:** CNN, Training, Prediction

### Team 3: API Development
- [Namen]
- **Verantwortlich:** FastAPI, Endpoints, Documentation

### Team 4: Testing & Deployment
- [Namen]
- **Verantwortlich:** Tests, CI/CD, Projekt-Docs

## 📊 Model Performance

- **Architektur:** SimpleCNN (3 Conv Layers)
- **Dataset:** CIFAR-10
- **Training Samples:** 50,000
- **Test Samples:** 10,000
- **Test Accuracy:** XX.X%

## 🔧 Technologie-Stack

- **Framework:** PyTorch 2.1
- **API:** FastAPI
- **Testing:** pytest
- **Version Control:** Git

## 📝 Lizenz
MIT

## 🤝 Beitragen
Siehe [CONTRIBUTING.md](CONTRIBUTING.md)
```

### Git Commits für Team 4

```bash
git add tests/
git commit -m "Add comprehensive test suite"

git add README.md
git commit -m "Update project documentation"

git add .github/workflows/  # Falls CI/CD
git commit -m "Add CI/CD pipeline"

git push origin team4-testing
```

### Akzeptanzkriterien Team 4

- [ ] Alle Tests sind geschrieben
- [ ] Tests laufen durch (pytest)
- [ ] Code Coverage > 70%
- [ ] README ist vollständig
- [ ] API Dokumentation vorhanden
- [ ] Optional: CI/CD funktioniert

---

## 🎯 Finale Integration

### Merge Reihenfolge

```bash
# 1. Team 1 (Data) wird zuerst gemerged
git checkout main
git merge team1-data

# 2. Team 2 (Model) benötigt Data
git merge team2-model

# 3. Team 3 (API) benötigt Model
git merge team3-api

# 4. Team 4 (Tests) testet alles
git merge team4-testing

# 5. Final Push
git push origin main
```

### Finale Demo

**Ablauf:**
1. Server starten
2. Swagger UI öffnen (http://localhost:8000/docs)
3. Test-Bild hochladen
4. Ergebnis präsentieren

**Erfolgs-Demo:**
```bash
# Terminal 1: Server
python api/main.py

# Terminal 2: Request
curl -X POST "http://localhost:8000/predict" \
  -F "file=@cat.jpg"

# Erwartet:
{
  "class": "Katze",
  "class_id": 3,
  "confidence": 0.92,
  "filename": "cat.jpg"
}
```

---

## ⏱️ Zeitplan (3 Stunden)

### Phase 1: Setup (30 Min)
- [ ] Git Repository erstellen
- [ ] Branches erstellen
- [ ] Teams formieren
- [ ] PyCharm einrichten

### Phase 2: Development (90 Min)
- [ ] Jedes Team arbeitet an Aufträgen
- [ ] Regelmäßige Commits
- [ ] Code Reviews innerhalb Team

### Phase 3: Integration (45 Min)
- [ ] Merges durchführen
- [ ] Konflikte auflösen
- [ ] Tests laufen lassen

### Phase 4: Demo (15 Min)
- [ ] Live-Präsentation
- [ ] Q&A
- [ ] Feedback

---

## 📚 Hilfreiche Git Commands

```bash
# Status checken
git status

# Änderungen sehen
git diff

# Committen
git add .
git commit -m "Beschreibung"

# Pushen
git push origin <branch-name>

# Pullen
git pull origin <branch-name>

# Branch wechseln
git checkout <branch-name>

# Merge
git merge <branch-name>

# Konflikte sehen
git status
# Datei editieren, dann:
git add <file>
git commit

# Log sehen
git log --oneline --graph
```

---

## 🎓 Lernziele

Nach dieser Session könnt ihr:
- ✅ Im Team mit Git arbeiten
- ✅ Branches erstellen und mergen
- ✅ Konflikte lösen
- ✅ PyTorch CNNs entwickeln
- ✅ REST APIs mit FastAPI bauen
- ✅ Tests schreiben mit pytest
- ✅ Professionelle Projekt-Struktur erstellen

---

## 🆘 Support & Fragen

Bei Problemen:
1. Team fragen
2. Andere Teams fragen
3. Dokumentation checken
4. Trainer fragen

**Häufige Fehler:**
- Git Merge Konflikte → Dateien manuell editieren
- Import Errors → `sys.path.append('..')` nutzen
- CUDA Errors → Nutze `device='cpu'`
- Module not found → `pip install -r requirements.txt`

---

**Viel Erfolg! 🚀**

*Denkt daran: Kommunikation ist key! Sprecht miteinander, macht Code Reviews, und habt Spaß am Programmieren!*
