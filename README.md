# Movie Recommender – Python · Streamlit · TF‑IDF

A content‑based movie recommendation web‑app built with **Streamlit** and The Movie Database (TMDb) data.  
It suggests similar titles by computing **TF‑IDF** vectors over each film’s *genre & tag* text and measuring cosine similarity.

## Features
- **Search by title** – get the 10 most similar films.
- **Filter by genre, rating, popularity** (interactive sidebar widgets).
- **Poster & metadata fetch** via TMDb API.
- Easily switch to any similarity metric (e.g., BM25, embeddings).


## 1 · Clone the repo
git clone https://github.com/<your‑user>/movie‑recommender‑tfidf.git
cd movie‑recommender‑tfidf

## 2 · Create & activate a virtual environment (optional but recommended)
python -m venv .venv
## On Windows:
.venv\Scripts\activate
## On macOS / Linux:
source .venv/bin/activate

## 3 · Install dependencies
pip install -r requirements.txt


## requirements

'streamlit',
'pandas',
'numpy'->mathematical calculations,
'scikit-learn'-> for model Import,
'requests'->For API request.

## Output
<img width="1366" height="720" alt="Screenshot 2025-07-15 111747" src="https://github.com/user-attachments/assets/d966d11f-205c-4e81-bddb-ba458c80d66a" />
<img width="1366" height="768" alt="Screenshot 2025-07-15 111820" src="https://github.com/user-attachments/assets/9675c05a-6f3a-476e-af93-bacf3c195ace" />
<img width="1363" height="626" alt="Screenshot 2025-07-15 111921" src="https://github.com/user-attachments/assets/129eaf5d-a1af-498b-aa66-08c4256be9df" />
<img width="1362" height="629" alt="Screenshot 2025-07-15 111958" src="https://github.com/user-attachments/assets/443384e5-9c49-4e4f-ba35-61e2136e90f9" />
<img width="1365" height="629" alt="Screenshot 2025-07-15 112025" src="https://github.com/user-attachments/assets/d093bf52-1041-4129-81ce-944822da63c6" />
