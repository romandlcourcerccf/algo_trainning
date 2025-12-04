from exam_scores_tracker import ScoresTracker


def test_record():
    st = ScoresTracker()

    temes = [1, 3, 5, 10, 20, 50]
    scores = [4, 5, 5, 4, 3, 5]

    for i in range(len(temes)):
        st.record(temes[i], scores[i])

    assert st._scores == scores
    assert st._times == temes


def test_total_score():
    st = ScoresTracker()

    temes = [1, 3, 5, 10, 20, 50]
    scores = [4, 5, 5, 4, 3, 5]

    for i in range(len(temes)):
        st.record(temes[i], scores[i])

    assert st.totalScore(3, 5) == 10

    assert st.totalScore(3, 7) == 10

    assert st.totalScore(2, 7) == 10
