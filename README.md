# AggieConnect
Hellooooo This is my COMP 365 individual project at NC A&T. The idea is simple: you type one sentence about what you're into, and it recommends A&T campus events that fit.

I wanted to see if an AI model that matches by meaning does better than plain keyword search, which is basically how most campus sites work right now. So I tested both on the same events and the same test sentences.

What's in here
AggieConnect_Checkpoint2.ipynb is the main notebook. It runs everything.
build_events.py is the script I used to put the event data together. I collected the events from public A&T pages on October 4, 2026.
aggieconnect_events.csv has the 78 events. Every one has a link to the page it came from.
aggieconnect_test_profiles.csv has my 12 test sentences and which events I marked as good matches for each one. I labeled these before running anything.
requirements.txt lists the package versions I used.
How it works

I compared three methods:

Keyword matching. It just counts how many words your sentence and the event have in common. This is my baseline.
TF-IDF. Still keywords, but rare words count more than common ones.
MiniLM. This is the AI part. It uses a pretrained model called all-MiniLM-L6-v2 (revision 1110a243fdf4706b3f48f1d95db1a4f5529b4d41). I didn't train it, I just used it to compare what sentences mean instead of the exact words.

All three only get to see the event title, description and organization.

Running it yourself

You need Python 3.9 or newer. Download this repo, open a terminal in the folder, and run:

python3 -m pip install -r requirements.txt

Then open the notebook and hit Run All. The first time it'll download the model, so give it a minute. After that it runs in under a minute on my laptop (2021 MacBook Pro, M1 Pro, 16 GB). Nothing in it is random, so you should get the same numbers I did.

What I found

Average Precision@5 over the 12 test sentences:

Keyword matching: 0.367
TF-IDF: 0.450
MiniLM: 0.600

MiniLM did best, mostly when the student used different words than the event. Like if you say "farming," the keyword methods find nothing because the events say "food animal production" instead. MiniLM still found all 3 of those.

It's not perfect though. It recommended a robotics event for little kids to a computer science major, and it got nothing right for the fitness sentence. Also this is only 12 sentences that I labeled myself, so I'm treating it as an early result, not proof. The paper goes into all of that.
