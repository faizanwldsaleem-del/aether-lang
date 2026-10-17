# Aether Language Parser & Executor - Dynamic Data Pipeline Engine
import multiprocessing
import time
from lexer import tokenize, TokenType

def pipeline_worker_node(node_name, incoming_data, queue, worker_id):
    # Har node data ko process karega aur ek naya transformed data aage bhejega
    print(f"     [Pipeline Stage {worker_id}] Node '{node_name}' processing input: '{incoming_data}'...")
    time.sleep(1.0) # Heavy computation simulation
    
    # Data transformation / mutation (Pipeline effect)
    processed_output = f"{incoming_data} -> [{node_name}_Processed]"
    print(f"     [Stage Complete] '{node_name}' produced output: '{processed_output}'")
    
    # Result ko shared queue mein daalna taaki agla node utha sake
    queue.put((worker_id, processed_output))

class AetherParser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def parse(self):
        print("\n=== [Aether Engine] Deploying Dynamic Data Pipeline... ===")
        current_data = "None"
        nodes_pipeline = []
        node_counter = 1
        
        while self.pos < len(self.tokens):
            token_type, token_val = self.tokens[self.pos]
            
            # Omega Block
            if token_type == TokenType.OMEGA:
                self.pos += 2
                if self.pos < len(self.tokens):
                    block_name = self.tokens[self.pos][1]
                    print(f"🔒 Pipeline Cluster Initialized: [{block_name}]")
            
            # Section Stream & Payload Detection
            elif token_type == TokenType.SECTION:
                self.pos += 1
                if self.pos < len(self.tokens):
                    stream_name = self.tokens[self.pos][1]
                    print(f"📡 Pipeline Stream Active: '{stream_name}'")
                
                # Check for Payload
                if self.pos + 1 < len(self.tokens) and self.tokens[self.pos + 1][1] == '(':
                    self.pos += 2
                    if self.pos < len(self.tokens):
                        current_data = self.tokens[self.pos][1]
                        print(f"📦 Initial Pipeline Seed Data: '{current_data}'")
                    if self.pos + 1 < len(self.tokens) and self.tokens[self.pos + 1][1] == ')':
                        self.pos += 1
                
            # Collect Nodes for Pipeline
            elif token_val in ['⟾', '⇶']:
                self.pos += 1
                if self.pos < len(self.tokens) and self.tokens[self.pos][1] == '[':
                    self.pos += 1
                    if self.pos < len(self.tokens):
                        node_name = self.tokens[self.pos][1]
                        nodes_pipeline.append((node_name, node_counter))
                        node_counter += 1
                        
            self.pos += 1
            
        # Executing Pipeline Stages Sequentially/Concurrently with Data Mutation
        if nodes_pipeline:
            print(f"   ⚡ EXECUTING PIPELINE: Passing data through {len(nodes_pipeline)} sequential stages...")
            
            ctx = multiprocessing.get_context('spawn')
            queue = ctx.Queue()
            
            active_data = current_data
            
            for node_name, wid in nodes_pipeline:
                p = ctx.Process(target=pipeline_worker_node, args=(node_name, active_data, queue, wid))
                p.start()
                p.join() # Ek stage complete hone ke baad hi agli stage chalegi (True Pipeline Flow)
                
                # Queue se naya processed data nikalna
                if not queue.empty():
                    _, active_data = queue.get()
            
            print(f"\n✨ [Pipeline Success] Final Transformed Data Output: '{active_data}'")

def run_aether_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            code = f.read()
            
        tokens = tokenize(code)
        engine = AetherParser(tokens)
        engine.parse()
        
    except FileNotFoundError:
        print(f"❌ Error: File '{filename}' nahi mili!")

if __name__ == '__main__':
    run_aether_file("program.ae")
