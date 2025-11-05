from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def get_project_recommendations(emp_skills, projects):
    emp_text = " ".join(emp_skills)
    project_texts = [" ".join(p["skills"]) for p in projects]

    vectorizer = CountVectorizer().fit([emp_text] + project_texts)
    vectors = vectorizer.transform([emp_text] + project_texts)

    similarities = cosine_similarity(vectors[0:1], vectors[1:]).flatten()
    recommendations = sorted(
        zip(projects, similarities), key=lambda x: x[1], reverse=True
    )

    result = []
    for project, score in recommendations:
        result.append({
            "project": project["name"],
            "match_score": round(float(score) * 100, 2)
        })
    return {"recommendations": result}