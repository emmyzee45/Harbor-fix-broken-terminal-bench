There is an Apache-style access log at /app/access.log in your working directory. Read
through it and produce a short summary of the traffic: how many requests were made, how
many distinct clients were involved, and which path was requested most often.

Write your summary to /app/report.json as a single JSON object with exactly these keys:

- "total_requests": integer — the total number of request lines in the log
- "unique_ips": integer — the number of distinct client IP addresses in the log
- "top_path": string — the request path (e.g. "/index.html") that appears most often

Success criteria:

1. /app/report.json exists and contains a single valid JSON object.
2. "total_requests" equals the total number of request lines in /app/access.log.
3. "unique_ips" equals the number of distinct client IP addresses in /app/access.log.
4. "top_path" is the request path that appears most frequently in /app/access.log.