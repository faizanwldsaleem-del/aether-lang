#!/bin/bash
echo "🚀 [Aether Engine Installer] Installing Aether Engine globally..."

# Create binary launcher wrappers
sudo cat << 'INNER' > /usr/local/bin/aetherc
#!/bin/bash
python3 ~/aether_lang/compiler.py "$@"
INNER

sudo cat << 'INNER' > /usr/local/bin/avm
#!/bin/bash
python3 ~/aether_lang/avm.py "$@"
INNER

sudo chmod +x /usr/local/bin/aetherc /usr/local/bin/avm

echo "✅ [Installation Complete] You can now run 'aetherc' and 'avm' from anywhere on your system!"
