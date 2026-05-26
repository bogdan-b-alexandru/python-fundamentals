job_posting = {
    "company": "Flare",
    "title": "CyberSecurity",
    "skills": ["Python", "SQL", "Machine Learning"]
}

def analyze_job(job_posting):
    return job_posting['company'], job_posting['title'], len(job_posting['skills'])


name, role, skill = analyze_job(job_posting)
print(f"{name}, {role}, {skill}")