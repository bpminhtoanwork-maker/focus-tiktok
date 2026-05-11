import json
import subprocess

# Danh sách 10 chủ đề Startup & Tech
TOPICS = [
    "Startup Tips", "AI Tools 2026", "Coding Life", 
    "Marketing Strategy", "Fintech News", "Productivity Hacks", 
    "Blockchain Technology", "New Tech Gadgets", "UIUX Design", "E-commerce"
]

def get_ids(query):
    print(f"Đang tìm kiếm: {query}")
    # Lấy 20 video để lọc ra 10 cái tốt nhất
    cmd = [
        'yt-dlp', 
        f"ytsearch20:tiktok {query}", 
        '--get-id', 
        '--flat-playlist',
        '--sleep-requests', '1' # Nghỉ 1 giây giữa các yêu cầu để tránh bị chặn
    ]
    try:
        output = subprocess.check_output(cmd).decode('utf-8')
        ids = [i for i in output.strip().split('\n') if len(i) > 5]
        return ids[:10] # Giữ lại 10 video mỗi chủ đề
    except Exception as e:
        print(f"Lỗi khi quét {query}: {e}")
        return []

data = {}
for t in TOPICS:
    ids = get_ids(t)
    if ids:
        data[t] = ids

# Ghi dữ liệu ra file data.json
with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Hoàn thành: data.json đã sẵn sàng!")