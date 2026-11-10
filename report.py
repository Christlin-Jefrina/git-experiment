from pathlib import Path
prompt = """
Summarize the CI/CD execution.
Identify errors and recommend actions.
"""
try:
    result = Path("result.txt").read_text().strip()
    status = "SUCCESS" if "Job completed" in result else "FAILED"
except FileNotFoundError:
    result = "Output file missing"
    status = "FAILED"
report = f"""
AUTOMATION REPORT
Prompt: {prompt.strip()}
Status: {status}
Result: {result}
Action: {"No action required" if status == "SUCCESS" else "Check job output and fix errors"}
"""
Path("report.txt").write_text(report)
print(report)
