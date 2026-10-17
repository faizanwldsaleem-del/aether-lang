import enum

class TokenType(enum.Enum):
    OMEGA = "OMEGA"
    SECTION = "SECTION"
    IDENTIFIER = "IDENTIFIER"
    SYMBOL = "SYMBOL"
    KEYWORD = "KEYWORD"
    NUMBER = "NUMBER"
    EOF = "EOF"

def tokenize(code):
    tokens = []
    i = 0
    n = len(code)
    
    keywords = [
        'val', 't_rewind', 'if', 'db_query', 'api_fetch', 'crypto_hash', 'file_write', 
        'file_read', 'sys_info', 'env_var', 'json_parse', 'regex_match', 'base64_enc', 
        'time_bench', 'rand_gen', 'log_emit', 'zip_pack', 'net_ping', 'str_transform', 
        'math_calc', 'process_spawn', 'thread_pool', 'cache_set', 'socket_listen', 
        'cron_sched', 'jwt_verify', 'csv_parse', 'gc_trigger', 'assert_check', 
        'ai', 'mesh_sync', 'mem_shield', 'Ω_pulse', '§_entropy',
        'hack_scan', 'packet_sniff', 'exploit_dispatch', 'vuln_audit', 'dns_enum'
    ]
    
    while i < n:
        char = code[i]
        if char.isspace():
            i += 1
            continue
            
        matched_kw = False
        for kw in keywords:
            if code.startswith(kw, i):
                kw_len = len(kw)
                if i + kw_len >= n or not (code[i+kw_len].isalnum() or code[i+kw_len] == '_'):
                    tokens.append((TokenType.KEYWORD, kw))
                    i += kw_len
                    matched_kw = True
                    break
        if matched_kw:
            continue
            
        if char == 'Ω':
            tokens.append((TokenType.OMEGA, 'Ω'))
            i += 1
            continue
        if char == '§':
            tokens.append((TokenType.SECTION, '§'))
            i += 1
            continue
        if code.startswith('⟾∞', i):
            tokens.append((TokenType.SYMBOL, '⟾∞'))
            i += len('⟾∞')
            continue
        if code.startswith('⟾', i):
            tokens.append((TokenType.SYMBOL, '⟾'))
            i += 1
            continue
        if code.startswith('⇶', i):
            tokens.append((TokenType.SYMBOL, '⇶'))
            i += 1
            continue
        if char in '{}[];()=+>':
            tokens.append((TokenType.SYMBOL, char))
            i += 1
            continue
        if char.isdigit():
            num = []
            while i < n and code[i].isdigit():
                num.append(code[i])
                i += 1
            tokens.append((TokenType.NUMBER, "".join(num)))
            continue
        if char.isalpha() or char == '_':
            ident = []
            while i < n and (code[i].isalnum() or code[i] == '_'):
                ident.append(code[i])
                i += 1
            word = "".join(ident)
            if word in keywords:
                tokens.append((TokenType.KEYWORD, word))
            else:
                tokens.append((TokenType.IDENTIFIER, word))
            continue
        i += 1
    tokens.append((TokenType.EOF, 'EOF'))
    return tokens
