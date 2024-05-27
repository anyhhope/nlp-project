from model import GPT, MyGPT, GPTConfig
import config

model = GPT.from_pretrained(config.model_type, dict(dropout=0.0))
cfg=GPTConfig(
    config.block_size,
    config.vocab_size,
    config.n_layer, 
    model.config.n_head,
    model.config.n_embd,
    config.dropout,
    config.bias
)
my_model = MyGPT(cfg, model)