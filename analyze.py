import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("job_listings.csv")

categories = {
    "Tech": ["developer", "programmer", "software", "data scientist", "database", "systems"],
    "Engineering": ["engineer", "architect"],
    "Medical": ["surgeon", "nurse", "psychiatrist", "ophthalmologist", "neurosurgeon", "medical", "physiological"],
    "Science": ["scientist", "ecologist", "meteorologist", "chemist", "physicist"],
    "Finance": ["trader", "banker", "broker", "underwriter", "accountant"],
    "Media": ["journalist", "editor", "producer", "photographer", "writer", "designer"],
    "Legal": ["barrister", "legal", "conveyancer"],
    "Education": ["teacher", "lecturer", "librarian"],
}

def categorize(title):
    title_lower = title.lower()
    for category, keywords in categories.items():
        for keyword in keywords:
            if keyword in title_lower:
                return category
    return "Other"

df["category"] = df["title"].apply(categorize)
counts = df["category"].value_counts()
print(counts)
counts.plot(kind="bar")
plt.title("Job Listings by Category")
plt.xlabel("Category")
plt.ylabel("Number of Jobs")
plt.tight_layout()
plt.savefig("job_categories.png")
print("Chart saved to job_categories.png")

