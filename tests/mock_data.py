json_test_string = ' {"guid": "1234","content": {"type": "text/html","title": "Challenge 1","entities": [ "1.2.3.4", "wannacry", "malware.com"], "href":{"link":{"parent":"https://www.google.com"}}},"score": 74,"time": 1574879179}'

test_fields = ["guid", "content.entities[0]", "content.entities[99]", "score", "score.sign", "content.href.link.parent"]

expected_result = {'guid': '1234', 'content.entities[0]': '1.2.3.4', 'score': 74, 'content.href.link.parent': 'https://www.google.com'}
