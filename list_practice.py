jobs = ["Data scientist", "Intern", "ML Engineer", "Dev", "AI Researcher"]

long_titles = [job for job in jobs if len(job) > 5]
print(long_titles)
upper_titles = [job.upper() for job in jobs]
print(upper_titles)