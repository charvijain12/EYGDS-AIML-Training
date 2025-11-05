from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer('all-MiniLM-L6-v2')

def get_project_recommendations(employee_skills, projects):
    emp_text = " ".join(employee_skills)
    emp_emb = model.encode(emp_text, convert_to_tensor=True)
def find_missing_skills(employee_skills, project_skills):
    return list(set(project_skills) - set(employee_skills))

    results = []
    for p in projects:
        if p["status"] != "open":
            continue
        proj_text = " ".join(p["required_skills"])
        proj_emb = model.encode(proj_text, convert_to_tensor=True)
        similarity = float(util.cos_sim(emp_emb, proj_emb))
        results.append({
            "project_name": p["name"],
            "description": p["description"],
            "match_score": round(similarity * 100, 2)
        })
    results.sort(key=lambda x: x["match_score"], reverse=True)
    return results
