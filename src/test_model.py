import tiktoken
import config
import torch

enc = tiktoken.get_encoding(config.model_type)
encode = lambda s: enc.encode(s, allowed_special={"<|endoftext|>"})
decode = lambda l: enc.decode(l)

def testing(model, promt):
    promt = encode(promt)
    x = (torch.tensor(promt, dtype=torch.long, device=config.device)[None, ...])
    model.eval()
    with torch.no_grad():
        y = model.generate(x, 200)
        print(decode(y[0].tolist()))
        print('---------------')