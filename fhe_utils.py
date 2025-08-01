def encrypt_vote(vote: str) -> str:
    return f"<enc>{vote}</enc>"

def decrypt_vote(enc_vote: str) -> str:
    return enc_vote.replace("<enc>", "").replace("</enc>", "")

