def get_project_recommendations(employee_skills, projects):
    recommendations = []
    for project in projects:
        if project["status"] != "open":
            continue
        match = len(set(employee_skills) & set(project["required_skills"]))
        recommendations.append({
            "project_name": project["name"],
            "match_score": match,
            "required_skills": project["required_skills"]
        })
    recommendations.sort(key=lambda x: x["match_score"], reverse=True)
    return recommendations
