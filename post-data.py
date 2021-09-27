#!/usr/bin/env python3

import json
import urllib.request
import string

# Tunables
label_cardinality = 2
batch_size = 50
batch_count = 5000

vector_endpoint = 'http://localhost:8787'

label_values = [ 'value_%i' % i for i in range(label_cardinality)]

line_number = 0
for i in range(batch_count):
    batch = []
    for j in range(batch_size):
        message = "%07i (%06i) / %06i %s" % (line_number, j, i, "*" * 150)
        label = label_values[line_number % label_cardinality]
        batch.append(json.dumps({ 'message': message, 'label': label }))
        line_number += 1

    vector_data = bytes('\n'.join(batch), 'ascii')
    vector_rsp = urllib.request.urlopen(
        vector_endpoint, vector_data, timeout=20)
    print("Batch %i: response code %s" % (i, vector_rsp.status))
