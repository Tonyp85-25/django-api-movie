def calculate_mean_review(reviews):
    """calculate the mean review for one movie"""
    mean = 0
    for review in reviews:
        mean += float(review.grade)
    return mean / len(reviews)
