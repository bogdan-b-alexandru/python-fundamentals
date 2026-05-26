job_posting = {
    "title": "Data Scientist Intern",
    "company": "IBM",
    "location": "Montreal",
    "salary": "$68.3k",
    "skills": ["Python", "SQL", "Machine Learning"]
}

print(f"Company: {job_posting['company']}, Title: {job_posting['title']}")

job_posting["applied"] = False

for skill in job_posting["skills"]:
    print(skill)

