import streamlit as st
import pandas as pd
import pickle
import numpy as np
from sklearn.metrics.pairwise import linear_kernel

# ---------------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------------
st.set_page_config(
    page_title="CineMatch | Movie Recommender",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ---------------------------------------------------------
# CUSTOM CSS — RICH GREEN THEME
# ---------------------------------------------------------
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

    .stApp {
        background:
            radial-gradient(circle at 10% 0%, rgba(34, 197, 94, 0.14), transparent 28%),
            radial-gradient(circle at 90% 10%, rgba(16, 185, 129, 0.10), transparent 25%),
            #07130d;
        color: #f0fdf4;
        font-family: 'Inter', sans-serif;
    }

    [data-testid="stHeader"] {
        background: rgba(7, 19, 13, 0.85);
    }

    .block-container {
        max-width: 1150px;
        padding-top: 2.5rem;
        padding-bottom: 4rem;
    }

    /* Hero */
    .hero {
        text-align: center;
        padding: 35px 20px 25px;
    }

    .brand {
        color: #4ade80;
        font-size: 15px;
        font-weight: 800;
        letter-spacing: 4px;
        text-transform: uppercase;
        margin-bottom: 12px;
    }

    .hero h1 {
        font-size: clamp(38px, 6vw, 68px);
        line-height: 1.05;
        margin: 0;
        font-weight: 800;
        letter-spacing: -2px;
        color: #f0fdf4;
    }

    .hero h1 span {
        color: #22c55e;
    }

    .hero p {
        color: #86a892;
        font-size: 17px;
        margin: 16px auto 0;
        max-width: 650px;
        line-height: 1.6;
    }

    /* Search */
    .search-label {
        color: #bbf7d0;
        font-weight: 700;
        font-size: 14px;
        margin: 5px 0 8px;
    }

    div[data-testid="stTextInput"] input {
        background: #0c2116 !important;
        color: #ecfdf5 !important;
        border: 1px solid #1f6f3d !important;
        border-radius: 14px !important;
        height: 54px !important;
        font-size: 16px !important;
        padding-left: 18px !important;
        box-shadow: 0 0 0 0 rgba(34,197,94,0);
    }

    div[data-testid="stTextInput"] input:focus {
        border-color: #22c55e !important;
        box-shadow: 0 0 0 2px rgba(34,197,94,0.15) !important;
    }

    div[data-testid="stTextInput"] input::placeholder {
        color: #6f927b !important;
    }

    /* Button */
    .stButton > button {
        width: 100%;
        height: 54px;
        border: 0;
        border-radius: 14px;
        background: linear-gradient(135deg, #22c55e, #16a34a);
        color: #031108;
        font-size: 16px;
        font-weight: 800;
        transition: all 0.2s ease;
        box-shadow: 0 8px 25px rgba(34, 197, 94, 0.15);
    }

    .stButton > button:hover {
        background: linear-gradient(135deg, #4ade80, #22c55e);
        transform: translateY(-1px);
        box-shadow: 0 12px 30px rgba(34, 197, 94, 0.24);
    }

    /* Section heading */
    .section-title {
        display: flex;
        align-items: center;
        gap: 12px;
        margin: 40px 0 20px;
    }

    .section-title h2 {
        margin: 0;
        color: #dcfce7;
        font-size: 24px;
        font-weight: 800;
    }

    .section-title .line {
        height: 1px;
        flex: 1;
        background: linear-gradient(90deg, #1f6f3d, transparent);
    }

    /* Movie cards */
    .movie-card {
        min-height: 150px;
        background: linear-gradient(145deg, #0d2417, #091a10);
        border: 1px solid #174d2b;
        border-radius: 18px;
        padding: 20px;
        margin-bottom: 18px;
        position: relative;
        overflow: hidden;
        transition: all 0.2s ease;
    }

    .movie-card:hover {
        border-color: #2eb85c;
        transform: translateY(-2px);
        box-shadow: 0 12px 30px rgba(0,0,0,0.25);
    }

    .movie-card::before {
        content: "";
        position: absolute;
        left: 0;
        top: 0;
        bottom: 0;
        width: 4px;
        background: linear-gradient(#22c55e, #15803d);
    }

    .rank {
        color: #4ade80;
        font-size: 12px;
        font-weight: 800;
        letter-spacing: 1px;
        margin-bottom: 8px;
    }

    .movie-title {
        color: #f0fdf4;
        font-size: 19px;
        font-weight: 800;
        margin-bottom: 10px;
        line-height: 1.3;
    }

    .movie-meta {
        display: flex;
        gap: 8px;
        flex-wrap: wrap;
        margin-bottom: 12px;
    }

    .tag {
        display: inline-block;
        background: #12351f;
        color: #86efac;
        border: 1px solid #1b6335;
        padding: 4px 9px;
        border-radius: 999px;
        font-size: 11px;
        font-weight: 700;
    }

    .score {
        color: #86efac;
        font-size: 12px;
        font-weight: 700;
        margin-top: 3px;
    }

    /* Welcome box */
    .welcome {
        text-align: center;
        margin: 35px auto;
        padding: 38px 20px;
        max-width: 700px;
        border: 1px dashed #215f38;
        border-radius: 20px;
        background: rgba(12, 33, 22, 0.55);
    }

    .welcome-icon {
        font-size: 42px;
        margin-bottom: 10px;
    }

    .welcome h3 {
        color: #dcfce7;
        margin: 0 0 8px;
    }

    .welcome p {
        color: #71947d;
        margin: 0;
    }

    /* Footer */
    .footer {
        text-align: center;
        color: #52715d;
        font-size: 12px;
        margin-top: 55px;
        padding-top: 20px;
        border-top: 1px solid #12351f;
    }

    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)


# ---------------------------------------------------------
# LOAD MODEL FILES
# ---------------------------------------------------------
@st.cache_resource
def load_model():
    with open("df.pickle", "rb") as f:
        df = pickle.load(f)

    with open("indices.pkl", "rb") as f:
        indices = pickle.load(f)

    with open("tfidf.pkl", "rb") as f:
        tfidf = pickle.load(f)

    with open("tfidf_matrix.pkl", "rb") as f:
        tfidf_matrix = pickle.load(f)

    return df, indices, tfidf, tfidf_matrix


df, indices, tfidf, tfidf_matrix = load_model()


# ---------------------------------------------------------
# RECOMMENDATION FUNCTION
# ---------------------------------------------------------
def recommend_movies(movie_title, n=10):
    """Return the top n movies using cosine similarity."""

    query = movie_title.strip().lower()

    # -----------------------------------------------------
    # CREATE A CLEAN LIST OF MOVIE TITLES
    # -----------------------------------------------------
    all_titles = [str(title) for title in indices.index]

    # -----------------------------------------------------
    # 1. EXACT MATCH
    # -----------------------------------------------------
    exact_matches = [
        title for title in all_titles
        if title.strip().lower() == query
    ]

    if exact_matches:
        matched_title = exact_matches[0]

    else:
        # -------------------------------------------------
        # 2. PARTIAL MATCH
        # -------------------------------------------------
        partial_matches = [
            title for title in all_titles
            if query in title.lower()
        ]

        if partial_matches:
            # Choose the shortest matching title
            matched_title = min(
                partial_matches,
                key=len
            )

        else:
            # -------------------------------------------------
            # 3. WORD-BASED MATCH
            # -------------------------------------------------
            query_words = set(query.split())

            best_title = None
            best_score = 0

            for title in all_titles:

                title_words = set(
                    title.lower().split()
                )

                if not query_words:
                    continue

                common_words = query_words.intersection(
                    title_words
                )

                score = len(common_words) / len(query_words)

                if score > best_score:
                    best_score = score
                    best_title = title

            if best_title is not None and best_score >= 0.5:
                matched_title = best_title
            else:
                return None, []

    # -----------------------------------------------------
    # GET MOVIE INDEX
    # -----------------------------------------------------
    movie_indices = indices[
        indices.index.astype(str) == matched_title
    ]

    # If duplicate title exists, take the first index
    if isinstance(movie_indices, pd.Series):
        movie_index = movie_indices.iloc[0]
    else:
        movie_index = movie_indices

    movie_index = int(movie_index)

    # -----------------------------------------------------
    # CALCULATE COSINE SIMILARITY
    # -----------------------------------------------------
    similarity_scores = linear_kernel(
        tfidf_matrix[movie_index],
        tfidf_matrix
    ).flatten()

    # -----------------------------------------------------
    # GET TOP MOVIES
    # -----------------------------------------------------
    candidate_count = min(
        n + 20,
        len(similarity_scores)
    )

    candidate_indices = np.argpartition(
        -similarity_scores,
        candidate_count - 1
    )[:candidate_count]

    candidate_indices = candidate_indices[
        np.argsort(
            -similarity_scores[candidate_indices]
        )
    ]

    recommendations = []

    for idx in candidate_indices:

        # Don't recommend the movie itself
        if int(idx) == movie_index:
            continue

        row = df.iloc[int(idx)]

        recommendations.append({
            "title": row["original_title"],
            "genres": row["genres"],
            "rating": row["vote_average"],
            "similarity": float(
                similarity_scores[int(idx)]
            )
        })

        if len(recommendations) == n:
            break

    return matched_title, recommendations


# ---------------------------------------------------------
# HERO
# ---------------------------------------------------------
st.markdown("""
<div class="hero">
    <div class="brand">CINEMATCH · NLP PROJECT</div>
    <h1>Find your next <span>favorite</span> movie.</h1>
    <p>
        Search for a movie and discover 10 similar films powered by
        TF-IDF and cosine similarity.
    </p>
</div>
""", unsafe_allow_html=True)


# ---------------------------------------------------------
# SEARCH AREA
# ---------------------------------------------------------
with st.form("movie_search", clear_on_submit=False):
    col1, col2 = st.columns([5, 1.25], gap="small")

    with col1:
        st.markdown('<div class="search-label">SEARCH MOVIE</div>', unsafe_allow_html=True)
        movie_input = st.text_input(
            "Movie",
            placeholder="Try: The Dark Knight, Toy Story, Avatar...",
            label_visibility="collapsed"
        )

    with col2:
        st.markdown("<div style='height: 28px'></div>", unsafe_allow_html=True)
        search_clicked = st.form_submit_button(
            "Recommend",
            use_container_width=True
        )

# Form submission works with both the button and the Enter key.
should_search = search_clicked


# ---------------------------------------------------------
# RESULTS
# ---------------------------------------------------------
if should_search:

    if not movie_input.strip():
        st.warning("Please enter a movie title first.")
    else:
        matched_title, recommendations = recommend_movies(movie_input, 10)

        if matched_title is None:
            st.error(
                "Movie not found. Please enter a title from the dataset "
                "or try a different spelling."
            )
            st.caption(
                "Tip: try **Toy Story**, **Jumanji**, **Avatar**, or "
                "**The Dark Knight**."
            )

        else:
            st.markdown(
                f"""
                <div class="section-title">
                    <h2>Because you watched {matched_title}</h2>
                    <div class="line"></div>
                </div>
                """,
                unsafe_allow_html=True
            )

            left, right = st.columns(2, gap="medium")

            for i, movie in enumerate(recommendations):
                card = f"""
                <div class="movie-card">
                    <div class="rank">#{i + 1} RECOMMENDATION</div>
                    <div class="movie-title">{movie["title"]}</div>
                    <div class="movie-meta">
                        <span class="tag">{movie["genres"] if movie["genres"] else "Movie"}</span>
                        <span class="tag">⭐ {movie["rating"]:.1f}</span>
                    </div>
                    <div class="score">
                        Match score · {movie["similarity"] * 100:.1f}%
                    </div>
                </div>
                """

                with left if i % 2 == 0 else right:
                    st.markdown(card, unsafe_allow_html=True)


# ---------------------------------------------------------
# INITIAL STATE
# ---------------------------------------------------------
else:
    st.markdown("""
    <div class="welcome">
        <div class="welcome-icon">🍿</div>
        <h3>What are you in the mood for?</h3>
        <p>
            Enter a movie above and CineMatch will find 10 movies
            with similar content using your NLP recommendation model.
        </p>
    </div>
    """, unsafe_allow_html=True)


# ---------------------------------------------------------
# FOOTER
# ---------------------------------------------------------
st.markdown("""
<div class="footer">
    Built with Python · Streamlit · NLP · TF-IDF · Cosine Similarity
</div>
""", unsafe_allow_html=True)
