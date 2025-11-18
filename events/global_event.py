from blinker import signal ,Namespace
#events = Namespace()
on_answer = signal("answer")
on_change_question = signal("new question")
on_end = signal("result")
on_restart = signal("restart")