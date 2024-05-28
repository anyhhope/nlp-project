from init_model import my_model
import torch
import config
from test_model import encode, decode, testing


#!wget https://raw.githubusercontent.com/anyhhope/sample-df/main/combined_text_short.txt
with open('combined_text_short.txt', 'r', encoding='utf-8') as f:
    text = f.read()
data = torch.tensor(encode(text), dtype=torch.long)
n = int(config.train_size*len(data))
train_data = data[:n]
val_data = data[n:]

promt='London is the capital of USA'
testing(my_model, promt)

def get_batch(split):
    data = train_data if split == 'train' else val_data
    ix = torch.randint(len(data) - config.train_block_size, (config.batch_size,))
    x = torch.stack([data[i:i+config.train_block_size] for i in ix])
    y = torch.stack([data[i+1:i+config.train_block_size+1] for i in ix])
    x, y = x.to(config.device), y.to(config.device)
    return x, y 

@torch.no_grad()
def estimate_loss():
    out = {}
    my_model.eval()
    for split in ['train', 'val']:
        losses = torch.zeros(config.eval_iters)
        for k in range(config.eval_iters):
            X, Y = get_batch(split)
            logits, loss = my_model(X, Y)
            losses[k] = loss.item()
        out[split] = losses.mean()
    my_model.train()
    return out



optimizer = torch.optim.AdamW(my_model.parameters(), lr=config.learning_rate)
losses_train={}
losses_val={}
for iter in range(config.max_iters):
    if iter % config.eval_interval == 0 or iter == config.max_iters - 1:
        losses = estimate_loss()
        print(f"step {iter}: train loss {losses['train']:.4f}, val loss {losses['val']:.4f}")
        losses_train[iter]=losses['train']
        losses_val[iter]=losses['val']

        if iter % config.save_interval == 0:
            # Сохранение модели и оптимизатора
            checkpoint = {
                'model_state_dict': my_model.state_dict(),
                'optimizer_state_dict': optimizer.state_dict(),
                'iter': iter,
                'train_loss': losses['train'],
                'val_loss': losses['val']
            }
            torch.save(checkpoint, f"checkpoint_iter_{iter}.pt")

    xb, yb = get_batch('train')

    logits, loss = my_model(xb, yb)
    optimizer.zero_grad(set_to_none=True)
    loss.backward()
    optimizer.step()
    torch.cuda.empty_cache()

    del xb, yb, logits, loss