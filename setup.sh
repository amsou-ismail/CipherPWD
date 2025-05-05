#!/bin/bash

# Nom de l'outil
TOOL_NAME="cipherpwd"
TOOL_FILE="./cipherpwd_pack"
INSTALL_LIB_PATH="/usr/local/lib/$TOOL_NAME"
BIN_PATH="/usr/local/bin/$TOOL_NAME"

echo "🔍 Vérification de Python..."
if ! command -v python3 &> /dev/null; then
    echo "❌ ERREUR : Python3 n'est pas installé. Installez-le et réessayez."
    exit 1
fi

echo "✅ Python3 détecté : $(python3 --version)"

echo "🔍 Vérification de la bibliothèque pycryptodome..."

# Vérifier si pycryptodome est installé via apt
if python3 -m pip show pycryptodome &> /dev/null; then
    echo "✔ pycryptodome est déjà installé."
else
    echo "❌ pycryptodome n'est pas installé."
    echo "Voulez-vous l'installer maintenant ? (y/n)"
    read -r response
    if [[ "$response" == "y" || "$response" == "Y" ]]; then
        echo "📦 Installation de pycryptodome..."
        sudo python3 -m pip install pycryptodome --break-system-packages 2> /dev/null
    else
        echo "🚫 Installation annulée. Veuillez installer pycryptodome avant d'installer l'outil.(sudo python3 -m pip install pycryptodome --break-system-packages)"
        exit 1
    fi
fi

echo "🚀 Installation de $TOOL_NAME..."

# Vérifier si le dossier source existe
if [[ ! -d "$TOOL_FILE" ]]; then
    echo "❌ ERREUR : Le dossier source '$TOOL_FILE' n'existe pas."
    exit 1
fi

# Créer le répertoire d'installation s'il n'existe pas
sudo mkdir -p "$INSTALL_LIB_PATH"

# Copier les fichiers Python
echo "📂 Copie des fichiers dans $INSTALL_LIB_PATH..."
sudo cp -r "$TOOL_FILE/"* "$INSTALL_LIB_PATH/"

# Vérifier si main.py existe après la copie
MAIN_FILE="$INSTALL_LIB_PATH/main.py"
if [[ ! -f "$MAIN_FILE" ]]; then
    echo "❌ ERREUR : Le fichier main.py n'existe pas dans $INSTALL_LIB_PATH."
    exit 1
fi

# Donner les permissions d'exécution
sudo chmod +x "$MAIN_FILE"
sudo chmod -R a+rX "$INSTALL_LIB_PATH"

# Supprimer un éventuel ancien lien symbolique
sudo rm -f "$BIN_PATH"

# Créer un script de lancement global
echo "⚙️ Création du script de lancement..."
echo -e "#!/bin/bash\npython3 \"$MAIN_FILE\" \"\$@\"" | sudo tee "$BIN_PATH" > /dev/null
sudo chmod +x "$BIN_PATH"

echo "✅ Installation terminée ! Utilisez '$TOOL_NAME' pour exécuter."
