# Load model
import pickle
from scipy.sparse import load_npz

with open('models/implicit_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Load label encoders
with open('models/user_le.pkl', 'rb') as f:
    user_le = pickle.load(f)

with open('models/item_le.pkl', 'rb') as f:
    item_le = pickle.load(f)

# Load train matrix
train_matrix_csr = load_npz('models/train_matrix.npz')

def recommend(user_id):
    user_id_le = user_le.transform([user_id])[0]
    recommendations = model.recommend(user_id_le, train_matrix_csr[user_id_le], N=10)
    
    item_ids, scores = recommendations

    # Convert item_ids to their actual labels
    item_labels = item_le.inverse_transform(item_ids)

    # Prepare the result in the desired format
    result = {"user_id": user_id, "recommendations": []}
    for item, score in zip(item_labels, scores):
        result["recommendations"].append({"item_id": item, "score": str(score)})

    return result

if __name__ == '__main__':
    print(recommend("7670b27dcd2805736b5efb8e2ef06917"))
