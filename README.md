## Movie Recommender – Python · Streamlit · TF‑IDF

A content‑based movie recommendation web‑app built with **Streamlit** and The Movie Database (TMDb) data.  
It suggests similar titles by computing **TF‑IDF** vectors over each film’s *genre & tag* text and measuring cosine similarity.

## Features
- **Search by title** – get the 10 most similar films.
- **Filter by genre, rating, popularity** (interactive sidebar widgets).
- **Poster & metadata fetch** via TMDb API.
- Easily switch to any similarity metric (e.g., BM25, embeddings).


# 1 · Clone the repo
git clone https://github.com/<your‑user>/movie‑recommender‑tfidf.git
cd movie‑recommender‑tfidf

# 2 · Create & activate a virtual environment (optional but recommended)
python -m venv .venv
# On Windows:
.venv\Scripts\activate
# On macOS / Linux:
source .venv/bin/activate

# 3 · Install dependencies
pip install -r requirements.txt


# requirements

'streamlit'
'pandas'
'numpy'->mathematical calculations
'scikit-learn'-> for model Import
'requests'->For API request

# Output

<img width="1365" height="629" alt="Screenshot 2025-07-15 112025" src="https://github.com/user-attachments/assets/770359e6-4989-4efb-9e2b-0b849aa5de44" />
<img width="1362" height="629" alt="Screenshot 2025-07-15 111958" src="https://github.com/user-attachments/assets/e147f1f6-2925-43b6-a5f2-26c7e717f5bf" />
<img width="1363" height="626" alt="Screenshot 2025-07-15 111921" src="https://github.com/user-attachments/assets/dbd01cfc-8208-4c76-8024-83599b6a1587" />
<img width="1366" height="768" alt="Screenshot 2025-07-15 111820" src="https://github.com/user-attachments/assets/2a3c85e0-bd50-4c8e-8f10-928b22e17bd2" />
<img width="1366" height="720" alt="Screenshot 2025-07-15 111747" src="https://github.com/user-attachments/assets/b65a0657-d13b-478e-a2b9-c32b71973302" />



