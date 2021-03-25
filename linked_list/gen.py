import random


ALL_MODES = ['i', 'i', 'i', 'dn', 'dan', 'dk', 'p', 'm']
NUM_COM = 100000
commands = ['i 100 100']
outputs = []
now_size = 1
data = [100]
for i in range(NUM_COM):
    mode = random.choice(ALL_MODES)
    if mode == 'i':
        now_size += 1
        num = random.randint(0, 123)
        pos = random.choice(range(len(commands)))
        data.insert(pos, num)
        commands.append(f'i {num} {pos}')
    elif mode == 'dn':
        num = random.randint(0, 123)
        commands.append(f'dn {num}')
        try:
            data.remove(num)
        except ValueError:
            outputs.append('delete error')
    elif mode == 'dan': 
        num = random.randint(0, 123)
        commands.append(f'dan {num}')
        data = [d for d in data if d != num]
        if num not in data:
            outputs.append('delete error')
    elif mode == 'dk':
        idx = random.choice(range(int(len(data) * 1.5)))
        commands.append(f'dk {idx}')
        if len(data) > idx:
            data.remove(data[idx])
        else:
            outputs.append('delete error')
    elif mode == 'p':
        front_k = random.randrange(1, len(data) // 2 + 1)
        tmp = map(str, data[:front_k])
        commands.append('p')
        outputs.append(' '.join(tmp))
    elif mode == 'm':
        commands.append('m')
        outputs.append(f'{sum(data) / len(data):.2f}')
with open('input.txt', 'w') as f:
    f.write('\n'.join(commands))

with open('output.txt', 'w') as f:
    f.write('\n'.join(outputs))