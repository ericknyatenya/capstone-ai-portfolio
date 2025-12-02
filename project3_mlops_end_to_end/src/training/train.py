def train_dummy_model(data_path: str = None):
    """Placeholder training script that writes a small model artifact."""
    with open('model.txt', 'w') as f:
        f.write('dummy model')
    return 'model.txt'

if __name__ == '__main__':
    print(train_dummy_model())
