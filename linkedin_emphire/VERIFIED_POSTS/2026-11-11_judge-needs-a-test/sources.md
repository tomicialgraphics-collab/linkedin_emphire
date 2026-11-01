# Sources and claims

## No numbers are asserted in the post. That is deliberate.

The post contains no statistic, because the only figures that would make it stronger are ones I have not published yet. Every line is a procedure the reader can run on their own data, plus one structural claim about how a model-judged score is produced.

## The one external reference

Zheng et al., "Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena" (2023), arXiv:2306.05685. It documents position bias, verbosity bias and self-enhancement bias, and reports that strong judges agree with human preference at a rate below human-human agreement. Only the existence and direction of position bias is relied on; no figure from the paper is quoted in the post.

## Claims in the post, and their basis

| Claim | Basis |
| --- | --- |
| A model-judged pass rate is agreement between two models | definitional: the judge is a model producing a verdict |
| Repeated runs of the same judge can move the verdict | sampling, unless temperature is zero and the harness is deterministic; even then the harness may resample |
| Swapping candidate order can change the verdict | documented position bias, see above |
| Judge version changes can silently alter historical results | operational: reports rarely store the model string |

## Not claimed

- No flip rate, no agreement figure, no pass rate. The post asks the reader to produce those, it does not supply them.
- No vendor or tool named, no product criticised.
- No claim that human raters are reliable. The post says the opposite.
