def predict_dummy(model_path: str, input_text: str):
    try:
        with open(model_path, 'r') as f:
            _ = f.read()
    except Exception:
        return 'model not found'
    return f'predicted: {input_text[:50]}'
