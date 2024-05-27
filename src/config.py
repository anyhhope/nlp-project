import torch
types=['gpt2', 'gpt2-medium', 'gpt2-large', 'gpt2-xl']
model_type=types[0]  


block_size=1024
vocab_size=50257
n_layer=4  # Только 4 слоя
dropout=0.0
bias=True

train_size=0.9


batch_size = 32
train_block_size = 256
max_iters = 5
eval_interval = 10
learning_rate = 3e-4
eval_iters = 10

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
save_interval = 1000 # должно быть кратно eval_interval