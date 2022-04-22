import pandas as pd
from pmaw import PushshiftAPI

api = PushshiftAPI()

not_finished=True
while not_finished:
    try:
        submissions = api.search_submissions(
            subreddit="AmItheAsshole",
            limit=100000,
            safe_exit=True,
            before=1650550522,
            cache_dir='../../data/raw'
        )
    except:
        print('Trying again...')
        continue
    not_finished=False

submission_df = pd.DataFrame(submissions)
submission_df.to_csv('../../data/raw/posts.csv', index=False)

