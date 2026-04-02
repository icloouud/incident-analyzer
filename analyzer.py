import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def chunk_logs(logs, chunk_size=50):
    """Split logs into smaller chunks"""
    for i in range(0, len(logs), chunk_size):
        yield logs[i:i + chunk_size]

def analyze_chunk(log_chunk):
    prompt = f"""
You are an SRE assistant.

Analyze the following logs and:
1. Identify any anomalies or errors
2. Summarize what's happening
3. Highlight suspicious patterns

Logs:
{log_chunk}
"""

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2,
    )

    return response.choices[0].message.content


def final_summary(intermediate_summaries):
    prompt = f"""
You are an expert Site Reliability Engineer.

Given the following partial analyses, produce:
1. A concise incident summary
2. Likely root cause
3. Suggested next steps

Analyses:
{intermediate_summaries}
"""

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2,
    )

    return response.choices[0].message.content