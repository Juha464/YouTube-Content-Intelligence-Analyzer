# YouTube-Content-Intelligence-Analyzer(2026)

This project is a Python-based data analysis tool designed to help content creators (specifically in the Kids' category) make data-driven decisions. It moves beyond "vanity metrics" like raw view counts to analyze true audience engagement and content format efficiency.

##  Project Objective
To identify high-potential content niches and formats by analyzing the relationship between video length, view counts, and audience engagement (Likes & Comments).

##  Technologies
- **Language:** Python 3.x
- **Libraries:** - `Pandas`: Data manipulation and cleaning.
  - `Matplotlib` & `Seaborn`: Data visualization and statistical plotting.

##  Key Features & Engineering
- **Automated Data Cleaning:** Implemented header stripping to handle inconsistent CSV formatting.
- **Feature Engineering:** Developed a custom `Engagement_Score` metric:
  - *Formula:* `(Likes + Comments) / Views`
- **Data Categorization:** Built a logic engine to classify videos into `Long-form` (>= 20 mins) and `Short-form` (< 20 mins).
- **Automated Insights:** The script automatically identifies the most loyal audience segments and compares format performance.

##  Strategic Insights Derived
- **Engagement > Views:** Identified that high-view channels often have lower relative engagement compared to niche-specific creators.
- **Format Efficiency:** Quantified the performance gap between short-form and long-form content to guide production strategy.
- **Market Benchmarking:** Established an average engagement baseline for the Kids' content category.

## 📂 How to Run
1. Clone the repository.
2. Ensure you have `youtuvedata.csv` in the root directory.
3. Install dependencies: `pip install pandas matplotlib seaborn`.
4. Run: `python project2.py`.
