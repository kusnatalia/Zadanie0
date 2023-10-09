
input_text = """3
Your care set up, do not pluck my care down.
My care is loss of care with old care done.
Your care is gain of care when new care is won.
2
care
is"""
lines = input_text.split('\n')
n = int(lines[0])
documents = lines[1:1 + n]
m = int(lines[1 + n])
queries = lines[2 + n:]
results = []
for query in queries:
    query_results = []
    for i, document in enumerate(documents):

        words = document.split()

        if query in words:

            frequency = words.count(query)
            query_results.append((i, frequency))


    query_results.sort(key=lambda x: (-x[1], x[0]))


    results.append(query_results)

for result in results:
    for document_index, frequency in result:
        print(document_index, end=' ')
    print()


