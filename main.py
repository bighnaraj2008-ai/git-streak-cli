import subprocess
from datetime import datetime, timedelta

def get_git_commits():
    try:
        cmd = ['git', 'log', '--pretty=format:%ad', '--date=short']
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        return result.stdout.splitlines()
    except subprocess.CalledProcessError:
        print("Error: This doesn't seem to be a Git repository.")
        return []

def main():
    print("🔥 Git Streak & Activity Analyzer 🔥\n")
    commit_dates = get_git_commits()
    
    if not commit_dates:
        print("No commits found in this repo yet. Make a commit to see the magic!")
        return

    date_counts = {}
    for date_str in commit_dates:
        date_counts[date_str] = date_counts.get(date_str, 0) + 1

    print("Activity for the past week:")
    today = datetime.now().date()
    
    for i in range(6, -1, -1):
        day = today - timedelta(days=i)
        day_str = day.strftime("%Y-%m-%d")
        count = date_counts.get(day_str, 0)
        
        blocks = "░" if count == 0 else "█" * min(count, 5)
        print(f"{day_str} | {blocks} ({count} commits)")

if __name__ == "__main__":
    main()
