import re

def process_new_id(new_id):
    # 1단계
    new_id = new_id.lower()
    # 2단계
    new_id = re.sub(r'[^a-z0-9-_.]', '', new_id)
    # 3단계
    new_id = re.sub(r'\.+', '.', new_id)
    # 4단계
    new_id = new_id.strip('.')
    # 5단계
    if new_id == '':
        new_id = 'a'
    # 6단계(4단계도 실행)
    if len(new_id) >= 16:
        new_id = new_id[:15]
        new_id = new_id.rstrip('.')
    # 7단계
    while len(new_id) < 3:
        new_id += new_id[-1]
    return new_id

new_id = input("Enter new ID: ")
print("Processed new ID:", process_new_id(new_id))