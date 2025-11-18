from events.global_event import on_answer , on_change_question

def log():
    on_answer.connect(not_lambda)
    on_change_question.connect(absolutely_not_lambda)

def not_lambda(s,answers):
    print(f"[log] {s,answers}")

def absolutely_not_lambda(s,question,answers):
    print(f"[log] {s,question,answers}")