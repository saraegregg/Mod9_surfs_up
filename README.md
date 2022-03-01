# Module 9 Challenge

---
## Surfs Up
---

### Project Overview
W. Avy is an investor who is considering providing funds to open an ice cream parlor and surf shop on the island of Oahu. He has approved of the business plan but was concerned that the weather may not be such that the shop is profitable all year round, so he has asked you to complete some weather analyses on a dataset that he will provide.


### Challenge Objectives
Run a statistical analysis on the observed temperatures in Oahu for the months of June and December to detirmine if the business is sustainable throughout the year.


### Resources
**Data Sources**
-hawaii.sqlite

**Software**
- Jupyter Notebook 6.4.5
- Python 3.9.7


### Results

**June Summary Statistics**

![june_summary_stats.png](https://github.com/saraegregg/Mod9_surfs_up/blob/main/images/june_summary_stats.png)

**December Summary Statistics**
![dec_summary_stats.png](https://github.com/saraegregg/Mod9_surfs_up/blob/main/images/dec_summary_stats.png)

The analysis clearly shows that
- The average temperature in December on Oahu, 71.0°F, is slightly lower than the average temperature in June, 74.9°F.
    - Similar averages show that the temperature on the island of Oahu does not undergo big temperature changes during different seasons of the year.
- The standard deviation in observed temperatures for June is lower than that of December, 3.257 and 3.746 respectively.
    - This indicates there is less variation in tempature in June than there is in December.
- The average minimum temperatures are 64.0°F in June and 56.0°F in December.
    - The lower minimum temperatures in December may negatively impact surfing activity and ice cream consumption.


### Summary

It is clear that Oahu's weather in June is a little bit warmer and more stable relative to its weather in December. It would be helpful to expand the weather analysis we have done previous to this challege on precipitation to include a count of the number of days that precipitation fell in order to infer the number of days that would be ideal for surfing and going out for ice cream. Similarly, a count of the number of days that were below a certain temperature could provide an idea of which days would not encourage surfing or buying ice cream. With this data, the investors would have a clearer picture of how many profitable days per month the buisness could anticipate vs how many days might be too severely impacted by weather to generate a profit.

I would further recommend that the investor conducts some analysis on the assumptions around weather and the business model that we have been operating under up until now. I have heard that ice cream sales are highest per capita in the US state of Alaska, which is not known for high temperatures, and, anecdotaly, I have heard that enthusiastic surfers will wear appropriate wet suits to enjoy waves in low temperatures. A clearer picture of how weather will likely impact the target demographic for this business is my strong recommendation.