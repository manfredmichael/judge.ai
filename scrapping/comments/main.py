import pandas as pd
from pmaw import PushshiftAPI

api = PushshiftAPI()

subs_df = pd.read_csv('../../data/raw/posts.csv', low_memory=False) 
sub_ids = list(subs_df.loc[:, 'id']) 

not_finished=True
while not_finished:
    try:
        comment_ids = api.search_submission_comment_ids(
            ids=sub_ids,
            safe_exit=True,
            before=1650550522,
            cache_dir='../../data/raw',
        ) 
        comment_ids = list(comment_ids)
    except Exception as e:
        print('Trying again: get submission')
    	print(e)
        continue
    not_finished=False

not_finished=True
while not_finished:
    try:
        comments = api.search_comments(
            ids=comment_ids,
            safe_exit=True,
            before=1650550522,
            cache_dir='../../data/raw',
        )
    except Exception as e:
        print('Trying again: search comments')
    	print(e)
        continue
    not_finished=False


comments_df = pd.DataFrame(comments)
comments_df.to_csv('./data/wallstreetbets_comments.csv', header=True, index=False, columns=list(comments_df.axes[1]))

