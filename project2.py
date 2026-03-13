import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Data Load
df = pd.read_csv('youtuvedata.csv')

# --- Tip: Excessive spaces before & after column is removed ---
df.columns = df.columns.str.strip()

# 2. FEATURE ENGINEERING: Finding Engagement Score 
# Here the name of column is clear so there will be no error
df['Engagement_Score'] = (df['Likes_ thousand'] * 1000 + df['No of comments']) / (df['Views _million'] * 1000000)

# 3. DATA CATEGORIZATION: Dividing the video format
def categorize_length(mins):
    if mins >= 20:
        return "Long-form"
    else:
        return "Short-form"

df['Format'] = df['video_length_mins'].apply(categorize_length)

# 4. DATA FILTERING: Finding High Engagement channel
# Enabling filter to 0.0005 so that we can see the results
high_potential = df[(df['Format'] == 'Short-form') & (df['Engagement_Score'] > 0.0005)]

print("--- FULL DATASET ---")
print(df[['Channel', 'video_length_mins', 'Format', 'Engagement_Score']])

print("\n--- HIGH POTENTIAL CHANNELS ---")
if high_potential.empty:
    print("Sorry,as the filter doesn't match the engagement score")
else:
    print(high_potential[['Channel', 'Engagement_Score']])

# 5. Visualization: Generating the Report
sns.set_theme(style="whitegrid")
plt.figure(figsize=(12, 6))
sns.barplot(x='Channel', y='Engagement_Score', data=df, hue='Format', palette='magma')

plt.title('YouTube Content Intelligence Report (2026)', fontsize=16)
plt.xticks(rotation=45)
plt.ylabel('Engagement Score')

# Saving the output as a professional report image
plt.savefig('yt_engagement_report.png')
print("--- Success: Report generated as 'yt_engagement_report.png' ---")
plt.show()
# 6. AUTOMATED DATA INSIGHTS
print("\n--- STRATEGIC DATA INSIGHTS ---")

# Insight 1: Highest Engagement
top_channel = df.loc[df['Engagement_Score'].idxmax(), 'Channel']
print(f"1. Highest Audience Loyalty: {top_channel} has the best engagement-to-view ratio.")

# Insight 2: Format Performance
avg_short = df[df['Format'] == 'Short-form']['Engagement_Score'].mean()
avg_long = df[df['Format'] == 'Long-form']['Engagement_Score'].mean()

if avg_short > avg_long:
    print(f"2. Content Strategy: Short-form content is performing {((avg_short/avg_long)-1)*100:.1f}% better in engagement.")
else:
    print("2. Content Strategy: Long-form content provides better audience retention.")

# Insight 3: Engagement Benchmark
print(f"3. Market Benchmark: The average engagement score for this niche is {df['Engagement_Score'].mean():.5f}")