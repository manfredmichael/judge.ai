import pandas as pd
from pmaw import PushshiftAPI

api = PushshiftAPI()

submissions = api.search_submissions(subreddit="AmItheAsshole",
        limit=200_000)

submission_df = pd.DataFrame(submissions)
submission_df.to_csv('../../data/raw/posts.csv', index=False)

