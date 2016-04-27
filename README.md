JELO
======
## The *J*ournal of *E*conomic *L*iterature *O*rganizer

This is a fun exercise in trying to build a topic model for economics papers based on their abstracts. In a good world, all papers in [RePEC](http://econpapers.repec.org/) would include their JEL codes, and those codes would be the same codes used, e.g., by the classification in the NBER Working Paper Series ([e.g.](http://www.nber.org/papers/w22171)). Alas, this is not a good world.

Some of the "Top 5"<sup>1</sup> journals in economics include great information on categorization for recent papers, e.g. the [American Economic Review](http://econpapers.repec.org/article/aeaaecrev/v_3a106_3ay_3a2016_3ai_3a4_3ap_3a1144-81.htm). Others, not [so](http://www.journals.uchicago.edu/doi/10.1086/684718) [much](.

This project takes a dataset<sup>2</sup> of abstracts and uses `gensim` to

1. fit an LDA model for a number of topics matching the number of JEL codes
2. compare topics across NBER and RePEC categorizations and predict missing topics from the journals that don't have topics available

## Notes

1. Top 5 papers identified as in [this paper](http://eml.berkeley.edu//~sdellavi/wp/TopJournalsJELDec12LongV5.pdf) are the _American Economic Review_, _Econometrica_, _Journal of Political Economy_, _Quarterly Journal of Economics_, and the _Review of Economic Studies_.
2. The dataset comes from scraping RePEC using [this `golang` program](https://github.com/jisantuc/econ_scrapers).
