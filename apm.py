import sys
import os
import json
import urllib.request

APM_REGISTRY = {
    "ai-vision": {"version": "1.0.0", "desc": "Neural network and computer vision modules for Aether"},
    "fast-db": {"version": "2.1.0", "desc": "Ultra-fast distributed relational database connectors"},
    "quantum-crypto": {"version": "1.2.5", "desc": "Post-quantum cryptographic encryption wrappers"},
    "cloud-mesh": {"version": "3.0.1", "desc": "Zero-config peer-to-peer cloud node clustering"}
}

def apm_main():
    print("\n📦 [APM - Aether Package Manager v1.0]")
    if len(sys.argv) < 2:
        print("Usage: apm <install/search/list> <package_name>")
        return
    
    command = sys.argv[1]
    
    if command == "list":
        print("📋 Available Official Aether Packages in Registry:")
        for pkg, info in APM_REGISTRY.items():
            print(f"   • {pkg} (v{info['version']}) - {info['desc']}")
            
    elif command == "search":
        if len(sys.argv) < 3:
            print("❌ Error: Search query specify karein!")
            return
        query = sys.argv[2]
        print(f"🔍 Searching registry for '{query}'...")
        found = [p for p in APM_REGISTRY if query in p]
        if found:
            for p in found:
                print(f"   ✅ Found: {p} -> {APM_REGISTRY[p]['desc']}")
        else:
            print("❌ No matching packages found.")
            
    elif command == "install":
        if len(sys.argv) < 3:
            print("❌ Error: Install karne ke liye package ka naam dein (e.g., apm install fast-db)")
            return
        pkg_name = sys.argv[2]
        if pkg_name in APM_REGISTRY:
            print(f"⬇️ Downloading package '{pkg_name}' (v{APM_REGISTRY[pkg_name]['version']}) from Aether Cloud...")
            import time
            time.sleep(0.5)
            # Create local modules directory if not exists
            os.makedirs("aether_modules", exist_ok=True)
            with open(f"aether_modules/{pkg_name}.ae", "w") as f:
                f.write(f"# Aether Module: {pkg_name}\n# Description: {APM_REGISTRY[pkg_name]['desc']}\n")
            print(f"✨ [Success] Package '{pkg_name}' successfully installed to './aether_modules/'!")
        else:
            print(f"❌ Error: Package '{pkg_name}' registry mein mojood nahi hai. 'apm list' check karein.")
    else:
        print(f"❌ Unknown command: '{command}'. Use list, search, or install.")

if __name__ == '__main__':
    apm_main()
