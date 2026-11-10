from datetime import datetime
from pathlib import Path
message = f"Job completed at {datetime.now()}"
Path("result.txt").write_text(message + "\n")
print(message)
