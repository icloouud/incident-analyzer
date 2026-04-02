import json
from analyzer import chunk_logs, analyze_chunk, final_summary

def load_logs(file_path):
    with open(file_path, "r") as f:
        return json.load(f)

def main():
    logs = load_logs("sample_logs.json")

    print("🔍 Analyzing logs...\n")

    summaries = []

    for chunk in chunk_logs(logs):
        result = analyze_chunk(chunk)
        summaries.append(result)

    print("🧠 Generating final report...\n")

    final = final_summary("\n".join(summaries))

    print("===== INCIDENT REPORT =====\n")
    print(final)


if __name__ == "__main__":
    main()