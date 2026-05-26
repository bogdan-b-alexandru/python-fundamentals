job_posting = {
    "title": "Data Scientist Intern",
    "company": "IBM",
    "location": "Montreal",
    "salary": "$68.3k",
    "skills": ["Python", "SQL", "Machine Learning"]
}

def get_skill(job_posting, index):
    try:
        return job_posting["skills"][index]
    except IndexError:
        return "Skill not found"    


print(get_skill(job_posting, 1))
print(get_skill(job_posting, 99))
