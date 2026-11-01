The position-swap test is not my invention and it is not new. It is documented in the MT-Bench work from 2023, which measured how often a strong judge changes its answer when the two candidates are swapped in the prompt:

https://arxiv.org/abs/2306.05685

The reason I still write about it is that the fix stayed in the paper. Most eval harnesses in production today will happily give you a leaderboard with no agreement figure beside it and no record of which judge version produced it.
