from models.comment import Comment
from models.user import User


def filter_comments_by_author(comments: list[Comment], author: User) -> list[Comment]:
    ok_comments = []
    for comm in comments:
        if comm.author_id == author.id:
            ok_comments.append(comm)
    return ok_comments
