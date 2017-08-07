import matplotlib.pyplot as plt
import json
import os
import pickle

from static_analysis import plot_stats

def load_file(fn):
    if os.path.exists("messages.pickle"):
        print("Found cached file: reading")
        return pickle.load(open("messages.pickle", "rb"))

    print("Reading and caching file")
    messages = json.load(open(fn, "r"))
    with open("messages.pickle", "wb") as f:
        pickle.dump(messages, f)

def analyze_file(fn):
    all_data = load_file(fn)
    messages = all_data['o0']['data']['message_thread']['messages']['nodes'] # hard coded from raw exploration
    field_keys = [
        "message_sender",
        "message",
        "timestamp_precise"
    ]

    field_values = [[message[field] for message in messages] for field in field_keys]
    message_data_lookup = dict(zip(field_keys, field_values))
    plot_stats(message_data_lookup)

if __name__ == "__main__":
    analyze_file("sample.json")