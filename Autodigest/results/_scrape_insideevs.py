import sys, re

html = sys.stdin.read()

# try meta description name attribute
m = re.search(r'<meta[^>]+name=(["\'])description\1[^>]+content=\1([^"\']+)\1', html)
if m:
    print('DESC:', m.group(2)[:300])

# try og:description
m = re.search(r'<meta[^>]+property=(["\'])og:description\1[^>]+content=\1([^"\']+)\1', html)
if m:
    print('OG:', m.group(2)[:300])

# try excerpt class
m = re.search(r'class=(["\'])excerpt\1[^>]*>(.*?)<', html, re.DOTALL)
if m:
    t = re.sub(r'<[^>]+>', '', m.group(2)).strip()[:200]
    print('EXCERPT:', t)

# try article/div standalone text
m = re.search(r'class=(["\'])entry-summary\1[^>]*>(.*?)<', html, re.DOTALL)
if m:
    t = re.sub(r'<[^>]+>', '', m.group(2)).strip()[:200]
    print('SUMMARY:', t)