import sys
import platform
import subprocess
import importlib
from importlib.metadata import version, PackageNotFoundError

print("🔍 Python Setup Check\n")

# --- System / Python ---
print(f"Python-Version: {sys.version.split()[0]}")
print(f"Interpreter-Pfad: {sys.executable}")
print(f"Betriebssystem: {platform.system()} {platform.release()}")
print(f"Architektur: {platform.machine()}")

# --- Pip ---
try:
    pip_version = subprocess.check_output([sys.executable, "-m", "pip", "--version"], text=True)
    print(f"Pip: {pip_version.strip()}")
except Exception as e:
    print("❌ Pip nicht gefunden:", e)

# --- Paketliste mit Kurzinfos ---
paket_infos = {
    "numpy": "N-dimensionale Arrays, lineare Algebra, Vektorisierung",
    "pandas": "Tabellen/Series, CSV/Excel/SQL, Datenanalyse",
    "scipy": "Wissenschaftl. Rechnen, Statistik, Optimierung",
    "scikit-learn": "Klassisches ML: Modelle, Pipelines, Metriken",
    "polars": "Schnelles DataFrame-Tool (Rust-Backend)",
    "pyarrow": "Apache Arrow, Parquet/Feather I/O",
    "matplotlib": "Grundlagen-Plotting",
    "seaborn": "Statistische Plots auf Matplotlib",
    "plotly": "Interaktive Charts (Web/Notebook)",
    "ipykernel": "Kernel für Jupyter/VS Code Notebooks",
    "jupyterlab": "Jupyter-IDE",
    "tqdm": "Fortschrittsbalken",
    "pytest": "Unit-Tests",
    "black": "Code-Formatierung",
    "flake8": "Linting",
    "mypy": "Static Typing Checks",
    "pydantic": "Validierung & Settings per Typen",
    "requests": "Einfache HTTP-Requests (Sync)",
    "httpx": "HTTP-Client modern, auch async",
    "beautifulsoup4": "HTML/XML-Parsing",
    "lxml": "Schnelles XML/HTML Parsing",
    "selenium": "Browser-Automation & Tests",
    "fastapi": "Schnelles Web-API-Framework (async)",
    "uvicorn": "ASGI-Server für FastAPI/Starlette",
    "sqlalchemy": "ORM & SQL Toolkit",
    "psycopg2-binary": "PostgreSQL-Client",
    "pymysql": "MySQL/MariaDB-Client",
    "openpyxl": "Excel .xlsx lesen/schreiben",
    "xlrd": "Ältere Excel-Formate lesen (xls)",
    "pillow": "Bildverarbeitung (PIL fork)",
    "opencv-python": "Computer Vision",
    "faker": "Testdaten generieren (Namen, Adressen, etc.)",
    "tensorflow": "Deep Learning Framework von Google (neuronale Netze)",
    "torch": "Deep Learning Framework PyTorch (flexibel, forschungsnah)",
    "emnist": "EMNIST"
}

pakete = list(paket_infos.keys())
installiert, fehlend = [], []

print("\n📦 Pakete werden geprüft ...")
for pkg in pakete:
    try:
        ver = version(pkg)
        installiert.append((pkg, ver, paket_infos[pkg]))
    except PackageNotFoundError:
        fehlend.append((pkg, paket_infos[pkg]))
    except Exception:
        try:
            m = importlib.import_module(pkg)
            ver = getattr(m, "__version__", "?")
            installiert.append((pkg, ver, paket_infos[pkg]))
        except Exception:
            fehlend.append((pkg, paket_infos[pkg]))

# --- Ausgabe getrennt ---
print("\n✔️ Installierte Pakete:")
if installiert:
    for pkg, ver, info in installiert:
        print(f"  {pkg} v{ver} – {info}")
else:
    print("  (keine gefunden)")

print("\n❌ Fehlende Pakete:")
if fehlend:
    for pkg, info in fehlend:
        print(f"  {pkg} – {info}")
    print("\n🔧 Installationsvorschlag (alle fehlenden auf einmal):")
    print("python -m pip install -U " + " ".join([p[0] for p in fehlend]))
else:
    print("  🎉 Alle wichtigen Pakete sind installiert!")

print("\n✅ Setup-Check abgeschlossen")