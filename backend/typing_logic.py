import time

def calculate_result(original, typed, start, end):
    time_taken = end - start
    minutes = time_taken / 60

    words = typed.split()
    wpm = len(words) / minutes if minutes > 0 else 0

    original_words = original.split()
    correct = 0
    for i in range(min(len(original_words), len(words))):
        if original_words[i] == words[i]:
            correct += 1

    accuracy = (correct / len(original_words)) * 100

    return round(wpm, 2), round(accuracy, 2), round(time_taken, 2)
