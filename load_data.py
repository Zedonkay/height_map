import pickle

def load_model(file_path):
    with open(file_path, 'rb') as f:
        model = pickle.load(f)
    print("Model loaded successfully.")
    return model
    
def predict_z(model, x, y):
    z = model(x, y)
    return z
