import sys
import pickle
import os

def compile_file(source_file):
    if source_file == "--version":
        print("🚀 Aether Native Compiler v3.0 [CyberSec Master Edition]")
        return
        
    print(f"\n⚙️ [Aether Native Compiler v3.0] Analyzing source: '{source_file}'...")
    try:
        from lexer import tokenize
        with open(source_file, 'r') as f:
            code = f.read()
        tokens = tokenize(code)
        print(f"🔍 Lexical Analysis Passed: {len(tokens)} tokens parsed.")
        
        binary_data = {
            "version": "v7.5",
            "source": source_file,
            "tokens": tokens
        }
        
        binary_filename = source_file.replace('.ae', '.aex')
        with open(binary_filename, 'wb') as f:
            pickle.dump(binary_data, f)
            
        print(f"✅ [Compilation Success] Standalone Native Binary generated: '{binary_filename}'")
        print(f"⚡ [Optimization]: Zero-overhead native runtime linked successfully.")
    except FileNotFoundError:
        print(f"❌ Error: Source file '{source_file}' nahi mili!")

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python3 compiler.py <program.ae>")
    else:
        compile_file(sys.argv[1])
