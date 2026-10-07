# 🎬 CineMatch — Movie Recommendation System using NLP
[![Live Demo](https://img.shields.io/badge/🚀%20Live%20Demo-View%20App-success?style=for-the-badge)](https://movie-recommendation-vishalbhatti.streamlit.app/)

CineMatch is a simple **content-based movie recommendation system** built as my first **Natural Language Processing (NLP)** project.

The application allows users to search for a movie and receive **10 similar movie recommendations** based on the textual information available in the dataset.

The recommendation system uses **TF-IDF Vectorization** and **Cosine Similarity** to calculate the similarity between movies.

The project also includes a simple and clean **Streamlit web interface** with a dark green theme.

---

## 🚀 Project Overview

The main goal of this project was to understand how **NLP techniques can be used to build a real-world recommendation system**.

The application follows this basic workflow:

```text
Movie Dataset
      ↓
Text Processing
      ↓
TF-IDF Vectorization
      ↓
Movie Feature Matrix
      ↓
Cosine Similarity
      ↓
Find Similar Movies
      ↓
Top 10 Recommendations
      ↓
Streamlit Web App
```

---

## ✨ Features

- 🔎 Search for movies
- 🎬 Get 10 similar movie recommendations
- 🧠 NLP-based recommendation system
- 📊 TF-IDF Vectorization
- 📐 Cosine Similarity
- ⭐ Movie ratings
- 🏷️ Movie genres
- 📈 Similarity scores
- 🎨 Dark green Streamlit UI
- 🔤 Flexible movie title searching
- ⚡ Fast recommendations using a precomputed TF-IDF matrix

---

## 🧠 How It Works

### 1. Movie Dataset

The project uses a movie dataset containing information about thousands of movies.

The textual information available in the dataset is used to represent each movie.

---

### 2. TF-IDF Vectorization

**TF-IDF (Term Frequency-Inverse Document Frequency)** is used to convert movie text information into numerical vectors.

TF-IDF helps determine which words are important for representing a movie.

The basic idea is:

```text
Movie Text
    ↓
TF-IDF
    ↓
Numerical Vector
```

Each movie is represented as a numerical vector that can be compared with other movies.

---

### 3. Cosine Similarity

After converting the movie information into vectors, **Cosine Similarity** is used to measure how similar two movies are.

A higher cosine similarity score means that the movies have more similar textual information.

```text
Movie A → Vector A
Movie B → Vector B

        ↓

Cosine Similarity

        ↓

Similarity Score
```

---

### 4. Movie Recommendation

When the user searches for a movie, the system:

1. Finds the movie in the dataset.
2. Gets its TF-IDF vector.
3. Compares it with all other movies.
4. Calculates cosine similarity.
5. Sorts movies based on similarity.
6. Returns the top 10 similar movies.

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Natural Language Processing
- TF-IDF
- Cosine Similarity
- Streamlit
- Pickle

---

## 📂 Project Structure

```text
Movie-Recommendation-System/
│
├── Dataset/
│
├── app.py
│
├── df.pickle
├── indices.pkl
├── tfidf.pkl
├── tfidf_matrix.pkl
│
├── requirements.txt
│
└── README.md
```

---

## 📊 Dataset

The project uses a movie dataset containing information about a large number of movies.

The recommendation system is based on the information available in this dataset.

### Dataset Limitation

The application can only recommend movies that are present in the underlying dataset.

If a movie is not available in the dataset, the application will display a **Movie Not Found** message.

Some possible limitations include:

- Some newer movies may not be available.
- Some movie titles may not be recognized.
- Some movies may have duplicate titles.
- Recommendation quality depends on the information available in the dataset.
- The system cannot recommend a movie that does not exist in the dataset.
- Movie posters and images are not included in the current version.

These are expected limitations of the current version of the project.

---

## 💻 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/movie-recommendation-system.git
```

Replace `YOUR-USERNAME` with your GitHub username.

---

### 2. Navigate to the Project Folder

```bash
cd movie-recommendation-system
```

---

### 3. Install Required Libraries

```bash
pip install -r requirements.txt
```

---

### 4. Run the Streamlit Application

```bash
python -m streamlit run app.py
```

The application will open in your browser.

You can also access it at:

```text
http://localhost:8501
```

---

## 🎬 Example Searches

You can search for movie titles that are available in the dataset.

Some examples include:

```text
Toy Story
Jumanji
Avatar
The Dark Knight
Superman
```

The search system also supports partial movie titles in many cases.

For example:

```text
Dark Knight
```

can find:

```text
The Dark Knight
```

---

## 📱 Streamlit Application

The application provides a simple user interface.

### Search

Users can enter a movie title in the search bar.

### Recommendation

After clicking the **Recommend** button, the application displays the top 10 similar movies.

Each recommendation contains:

- Movie title
- Genre
- Rating
- Similarity score

---

## 📈 Current Version

### Version 1.0

This is the first version of the project.

The main purpose of this version is to understand the fundamentals of building a recommendation system using NLP.

The project intentionally uses a simple approach:

```text
Text
 ↓
TF-IDF
 ↓
Cosine Similarity
 ↓
Movie Recommendations
```

---

## 🔮 Future Improvements

There are several improvements that can be added in future versions.

- [ ] Add movie posters
- [ ] Add movie descriptions
- [ ] Add movie release year
- [ ] Add genre filters
- [ ] Add movie autocomplete
- [ ] Improve fuzzy movie-title matching
- [ ] Add detailed movie information
- [ ] Improve recommendation accuracy
- [ ] Add a larger and more up-to-date dataset
- [ ] Add user-based recommendations
- [ ] Implement collaborative filtering
- [ ] Combine content-based and collaborative filtering
- [ ] Add user ratings
- [ ] Deploy the application online
- [ ] Improve the overall UI/UX

---

## 📚 What I Learned

This project helped me understand how NLP can be applied to a practical machine learning problem.

### NLP Concepts

- Text preprocessing
- Text representation
- TF-IDF
- Vectorization
- Cosine Similarity
- Similarity-based recommendation

### Python Concepts

- Pandas
- NumPy
- Functions
- Data manipulation
- Pickle
- Working with precomputed models
- Working with large datasets

### Application Development

- Streamlit
- Creating interactive web applications
- Connecting a machine learning/NLP model with a user interface
- Creating a simple user-friendly interface

---

## ⚠️ Limitations

This project is primarily a **learning and portfolio project**, so it has some limitations.

The recommendation system depends completely on the information available in the dataset.

If a movie is not present in the dataset, the application cannot recommend it.

Also, this is a **content-based recommendation system**, meaning it does not currently learn from individual user behavior.

The current system does not use:

- User watch history
- User ratings
- User preferences
- Other users' behavior
- Collaborative filtering

Therefore, two users searching for the same movie will receive the same recommendations.

---

---

## 📦 Large Files & Model Files

The original dataset and precomputed model files are **not included in this GitHub repository** because some of these files are too large for GitHub's standard file upload limits.

The following files are excluded from the repository:

```text
Dataset/
df.pickle
indices.pkl
tfidf.pkl
tfidf_matrix.pkl

## 🎯 Project Objective

The main objective of this project was to understand how Natural Language Processing can be used to solve a real-world problem.

Instead of starting with complex deep learning models, I focused on understanding the fundamentals:

```text
NLP
 ↓
Text Representation
 ↓
TF-IDF
 ↓
Cosine Similarity
 ↓
Content-Based Recommendation
 ↓
Streamlit Application
```

This project represents my first practical implementation of **NLP in a recommendation system**.

---

## 👨‍💻 About This Project

This is my **first NLP project**, created as part of my journey of learning:

- Data Science
- Machine Learning
- Natural Language Processing
- Artificial Intelligence
- Python

The goal of this project was not to build a production-level recommendation engine, but to understand the fundamental concepts and implement them in a complete end-to-end project.

---

## ⭐ Future Vision

I plan to continue improving this project by adding more advanced recommendation techniques, better datasets, movie posters, user preferences, and potentially collaborative filtering.

The current version is the foundation for a more advanced movie recommendation system.

---

## 📜 License

This project is created for **educational and portfolio purposes**.
