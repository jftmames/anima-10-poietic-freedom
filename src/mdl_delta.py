import zlib

def compressed_size(text: str) -> int:
    return len(zlib.compress(text.encode('utf-8', errors='ignore'), level=9))

def mdl_delta(pre_text: str, post_text: str) -> float:
    pre = compressed_size(pre_text); post = compressed_size(post_text)
    if pre == 0: return 0.0
    return (post - pre) / float(pre)
